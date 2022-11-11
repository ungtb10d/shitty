#!/usr/bin/env python
# vim:fileencoding=utf-8
# License: GPLv3 Copyright: 2021, Kovid Goyal <kovid at ungtb10d.net>


import os
import unittest

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
        from shittens.unicode_input import unicode_names
        from shittens.choose import subseq_matcher
        from shittens.diff import diff_speedup
        del fdt, unicode_names, subseq_matcher, diff_speedup

    def test_loading_shaders(self) -> None:
        from shitty.utils import load_shaders
        for name in 'cell border bgimage tint blit graphics'.split():
            load_shaders(name)

    def test_glfw_modules(self) -> None:
        from shitty.constants import is_macos, glfw_path
        linux_backends = ['x11']
        if not self.is_ci:
            linux_backends.append('wayland')
        modules = ['cocoa'] if is_macos else linux_backends
        for name in modules:
            path = glfw_path(name)
            self.assertTrue(os.path.isfile(path))
            self.assertTrue(os.access(path, os.X_OK))

    def test_all_shitten_names(self) -> None:
        from shittens.runner import all_shitten_names
        names = all_shitten_names()
        self.assertIn('diff', names)
        self.assertIn('hints', names)
        self.assertGreater(len(names), 8)

    def test_filesystem_locations(self) -> None:
        from shitty.constants import terminfo_dir, logo_png_file
        self.assertTrue(os.path.isdir(terminfo_dir), f'Terminfo dir: {terminfo_dir}')
        self.assertTrue(os.path.exists(logo_png_file), f'Logo file: {logo_png_file}')


def main() -> None:
    tests = unittest.defaultTestLoader.loadTestsFromTestCase(TestBuild)
    r = unittest.TextTestRunner(verbosity=4)
    result = r.run(tests)
    if result.errors or result.failures:
        raise SystemExit(1)
