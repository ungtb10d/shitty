#!./shitty/launcher/shitty +launch
# License: GPL v3 Copyright: 2016, Kovid Goyal <kovid at ungtb10d.net>

import importlib
import os
import shutil
import warnings
from contextlib import contextmanager
from tempfile import TemporaryDirectory
from typing import Iterator


@contextmanager
def env_vars(**kw: str) -> Iterator[None]:
    originals = {k: os.environ.get(k) for k in kw}
    os.environ.update(kw)
    try:
        yield
    finally:
        for k, v in originals.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


def main() -> None:
    warnings.simplefilter('error')
    current_home = os.path.expanduser('~') + os.sep
    paths = os.environ.get('PATH', '/usr/local/sbin:/usr/local/bin:/usr/bin').split(os.pathsep)
    path = os.pathsep.join(x for x in paths if not x.startswith(current_home))
    launcher_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shitty', 'launcher')
    path = f'{launcher_dir}{os.pathsep}{path}'
    PYTHON_FOR_TYPE_CHECK = shutil.which('python') or shutil.which('python3') or ''
    with TemporaryDirectory() as tdir, env_vars(
        PYTHONWARNINGS='error', HOME=tdir, USERPROFILE=tdir, PATH=path,
        XDG_CONFIG_HOME=os.path.join(tdir, '.config'),
        XDG_CONFIG_DIRS=os.path.join(tdir, '.config'),
        XDG_DATA_DIRS=os.path.join(tdir, '.local', 'xdg'),
        XDG_CACHE_HOME=os.path.join(tdir, '.cache'),
        PYTHON_FOR_TYPE_CHECK=PYTHON_FOR_TYPE_CHECK,
    ):
        m = importlib.import_module('kitty_tests.main')
        getattr(m, 'run_tests')()


if __name__ == '__main__':
    main()
