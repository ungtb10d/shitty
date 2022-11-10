#!/usr/bin/env python
# License: GPLv3 Copyright: 2020, Kovid Goyal <kovid at ungtb10d.net>


class CMD:
    pass


def generate_stub() -> None:
    from shittens.tui.operations import as_type_stub
    from shitty.conf.utils import save_type_stub
    text = as_type_stub()
    save_type_stub(text, __file__)
