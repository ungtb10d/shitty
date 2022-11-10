#!/usr/bin/env python
# License: GPLv3 Copyright: 2021, ungtb10d <kovid at ungtb10d.net>


import os
import stat
import sys
import unittest
from functools import partial

from . import BaseTest


class TestBuild(BaseTest):

    def test_exe(self) -> None:
        from shitty.constants import shitty_exe
        exe = shitty_exe()
        self.assertTrue(os.access(exe, os.X_OK))
        self.assertTrue(os.path.isfile(exe))
        self.assertIn('shitty', os.path.basename(exe))

    def test_loading_extensions(self) -> None:
        import shitty.fast_data_types as fdt
        from shittens.choose import subseq_matcher
        from shittens.diff import diff_speedup
        from shittens.transfer import rsync
        from shittens.unicode_input import unicode_names
        del fdt, unicode_names, subseq_matcher, diff_speedup, rsync

    def test_loading_shaders(self) -> None:
        from shitty.utils import load_shaders
        for name in 'cell border bgimage tint blit graphics'.split():
            load_shaders(name)

    def test_glfw_modules(self) -> None:
        from shitty.constants import glfw_path, is_macos
        linux_backends = ['x11']
        if not self.is_ci:
            linux_backends.append('wayland')
        modules = ['cocoa'] if is_macos else linux_backends
        for name in modules:
            path = glfw_path(name)
            self.assertTrue(os.path.isfile(path), f'{path} is not a file')
            self.assertTrue(os.access(path, os.X_OK), f'{path} is not executable')

    def test_all_shitten_names(self) -> None:
        from shittens.runner import all_shitten_names
        names = all_shitten_names()
        self.assertIn('diff', names)
        self.assertIn('hints', names)
        self.assertGreater(len(names), 8)

    def test_filesystem_locations(self) -> None:
        from shitty.constants import (
            local_docs, logo_png_file, shell_integration_dir, terminfo_dir
        )
        zsh = os.path.join(shell_integration_dir, 'zsh')
        self.assertTrue(os.path.isdir(terminfo_dir), f'Terminfo dir: {terminfo_dir}')
        self.assertTrue(os.path.exists(logo_png_file), f'Logo file: {logo_png_file}')
        self.assertTrue(os.path.exists(zsh), f'Shell integration: {zsh}')

        def is_executable(x):
            mode = os.stat(x).st_mode
            q = stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
            return mode & q == q

        for x in ('shitty', 'askpass.py'):
            x = os.path.join(shell_integration_dir, 'ssh', x)
            self.assertTrue(is_executable(x), f'{x} is not executable')
        if getattr(sys, 'frozen', False):
            self.assertTrue(os.path.isdir(local_docs()), f'Local docs: {local_docs()}')

    def test_ca_certificates(self):
        import ssl
        if not getattr(sys, 'frozen', False):
            self.skipTest('CA certificates are only tested on frozen builds')
        c = ssl.create_default_context()
        self.assertGreater(c.cert_store_stats()['x509_ca'], 2)

    def test_pygments(self):
        if not getattr(sys, 'frozen', False):
            self.skipTest('Pygments is only tested on frozen builds')
        import pygments
        del pygments

    def test_docs_url(self):
        from shitty.constants import website_url
        from shitty.utils import docs_url

        def run_tests(p, base, suffix='.html'):
            def t(x, e):
                self.ae(p(x), base + e)
            t('', 'index.html' if suffix == '.html' else '')
            t('conf', f'conf{suffix}')
            t('shittens/ssh#frag', f'shittens/ssh{suffix}#frag')
            t('#ref=confloc', f'conf{suffix}#confloc')
            t('#ref=conf-shitty-fonts', f'conf{suffix}#conf-shitty-fonts')
            t('#ref=conf-shitten-ssh-xxx', f'shittens/ssh{suffix}#conf-shitten-ssh-xxx')
            t('#ref=at_close_tab', f'remote-control{suffix}#at-close-tab')
            t('#ref=at-close-tab', f'remote-control{suffix}#at-close-tab')
            t('#ref=action-copy', f'actions{suffix}#copy')
            t('#ref=doc-/marks', f'marks{suffix}')

        run_tests(partial(docs_url, local_docs_root='/docs'), 'file:///docs/')
        w = website_url()
        run_tests(partial(docs_url, local_docs_root=None), w, '/')
        self.ae(docs_url('#ref=issues-123'), 'https://github.com/ungtb10d/shitty/issues/123')

    def test_launcher_ensures_stdio(self):
        from shitty.constants import shitty_exe
        import subprocess
        exe = shitty_exe()
        cp = subprocess.run([exe, '+runpy', f'''\
import os, sys
if sys.stdin:
    os.close(sys.stdin.fileno())
if sys.stdout:
    os.close(sys.stdout.fileno())
if sys.stderr:
    os.close(sys.stderr.fileno())
os.execlp({exe!r}, 'shitty', '+runpy', 'import sys; raise SystemExit(1 if sys.stdout is None or sys.stdin is None or sys.stderr is None else 0)')
'''])
        self.assertEqual(cp.returncode, 0)


def main() -> None:
    tests = unittest.defaultTestLoader.loadTestsFromTestCase(TestBuild)
    r = unittest.TextTestRunner(verbosity=4)
    result = r.run(tests)
    if result.errors or result.failures:
        raise SystemExit(1)
