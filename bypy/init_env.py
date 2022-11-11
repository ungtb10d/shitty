#!/usr/bin/env python
# vim:fileencoding=utf-8
# License: GPLv3 Copyright: 2020, Kovid Goyal <kovid at ungtb10d.net>

import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from contextlib import suppress

from bypy.constants import (
    LIBDIR, PREFIX, PYTHON, SRC as shitty_DIR, ismacos, worker_env
)
from bypy.utils import run_shell, walk


def read_src_file(name):
    with open(os.path.join(shitty_DIR, 'shitty', name), 'rb') as f:
        return f.read().decode('utf-8')


def initialize_constants():
    shitty_constants = {}
    src = read_src_file('constants.py')
    nv = re.search(r'Version\((\d+), (\d+), (\d+)\)', src)
    shitty_constants['version'] = '%s.%s.%s' % (nv.group(1), nv.group(2), nv.group(3))
    shitty_constants['appname'] = re.search(
            r'appname: str\s+=\s+(u{0,1})[\'"]([^\'"]+)[\'"]', src
    ).group(2)
    return shitty_constants


def run(*args, **extra_env):
    env = os.environ.copy()
    env.update(worker_env)
    env.update(extra_env)
    env['SW'] = PREFIX
    env['LD_LIBRARY_PATH'] = LIBDIR
    if ismacos:
        env['PKGCONFIG_EXE'] = os.path.join(PREFIX, 'bin', 'pkg-config')
    cwd = env.pop('cwd', shitty_DIR)
    print(' '.join(map(shlex.quote, args)), flush=True)
    return subprocess.call(list(args), env=env, cwd=cwd)


SETUP_CMD = [PYTHON, 'setup.py', '--build-universal-binary']


def build_frozen_launcher(extra_include_dirs):
    inc_dirs = [f'--extra-include-dirs={x}' for x in extra_include_dirs]
    cmd = SETUP_CMD + ['--prefix', build_frozen_launcher.prefix] + inc_dirs + ['build-frozen-launcher']
    if run(*cmd, cwd=build_frozen_launcher.writeable_src_dir) != 0:
        print('Building of frozen shitty launcher failed', file=sys.stderr)
        os.chdir(shitty_DIR)
        run_shell()
        raise SystemExit('Building of shitty launcher failed')
    return build_frozen_launcher.writeable_src_dir


def run_tests(shitty_exe):
    with tempfile.TemporaryDirectory() as tdir:
        env = {
            'shitty_CONFIG_DIRECTORY': os.path.join(tdir, 'conf'),
            'shitty_CACHE_DIRECTORY': os.path.join(tdir, 'cache')
        }
        [os.mkdir(x) for x in env.values()]
        cmd = [shitty_exe, '+runpy', 'from shitty_tests.main import run_tests; run_tests()']
        print(*map(shlex.quote, cmd), flush=True)
        if subprocess.call(cmd, env=env) != 0:
            print('Checking of shitty build failed', file=sys.stderr)
            os.chdir(os.path.dirname(shitty_exe))
            run_shell()
            raise SystemExit('Checking of shitty build failed')


def sanitize_source_folder(path: str) -> None:
    for q in walk(path):
        if os.path.splitext(q)[1] not in ('.py', '.glsl', '.ttf', '.otf'):
            os.unlink(q)


def build_c_extensions(ext_dir, args):
    writeable_src_dir = os.path.join(ext_dir, 'src')
    build_frozen_launcher.writeable_src_dir = writeable_src_dir
    shutil.copytree(
        shitty_DIR, writeable_src_dir, symlinks=True,
        ignore=shutil.ignore_patterns('b', 'build', 'dist', '*_commands.json', '*.o', '*.so', '*.dylib', '*.pyd'))

    with suppress(FileNotFoundError):
        os.unlink(os.path.join(writeable_src_dir, 'shitty', 'launcher', 'shitty'))

    cmd = SETUP_CMD + ['macos-freeze' if ismacos else 'linux-freeze']
    if args.dont_strip:
        cmd.append('--debug')
    dest = shitty_constants['appname'] + ('.app' if ismacos else '')
    dest = build_frozen_launcher.prefix = os.path.join(ext_dir, dest)
    cmd += ['--prefix', dest, '--full']
    if run(*cmd, cwd=writeable_src_dir) != 0:
        print('Building of shitty package failed', file=sys.stderr)
        os.chdir(writeable_src_dir)
        run_shell()
        raise SystemExit('Building of shitty package failed')
    return ext_dir


if __name__ == 'program':
    shitty_constants = initialize_constants()
