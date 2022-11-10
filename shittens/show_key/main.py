#!/usr/bin/env python
# License: GPLv3 Copyright: 2021, Kovid Goyal <kovid at ungtb10d.net>


import os
import sys
from typing import List

from shitty.cli import parse_args
from shitty.cli_stub import ShowKeyCLIOptions
from shittens.tui.operations import raw_mode, styled

ctrl_keys = '@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_'


def print_key(raw: bytearray) -> None:
    unix = ''
    for ch in raw:
        if ch < len(ctrl_keys):
            unix += f'^{ctrl_keys[ch]}'
        elif ch == 127:
            unix += '^?'
        else:
            unix += chr(ch)
    print(unix + '\t\t', end='')
    for ch in raw:
        x = chr(ch).encode('utf-8')
        print(styled(repr(x)[2:-1], fg='yellow'), end='')
    print(end='\r\n', flush=True)


def read_keys() -> None:
    fd = sys.stdin.fileno()
    while True:
        try:
            raw = bytearray(os.read(fd, 64))
        except OSError as err:
            print(err, file=sys.stderr, flush=True)
            break
        if not raw:
            break
        print_key(raw)
        if len(raw) == 1 and raw[0] == 4:
            break


def legacy_main() -> None:
    print('Press any keys - Ctrl+D will terminate this program', end='\r\n', flush=True)
    print(styled('UNIX', italic=True, fg='green'), styled('send_text', italic=True, fg='green'), sep='\t\t', end='\r\n')

    with raw_mode():
        read_keys()


OPTIONS = r'''
--key-mode -m
default=normal
type=choices
choices=normal,application,shitty,unchanged
The keyboard mode to use when showing keys. :code:`normal` mode is with DECCKM
reset and :code:`application` mode is with DECCKM set. :code:`shitty` is the full
shitty extended keyboard protocol.
'''.format
help_text = 'Show the codes generated by the terminal for key presses in various keyboard modes'
usage = ''


def main(args: List[str]) -> None:
    cli_opts, items = parse_args(args[1:], OPTIONS, '', help_text, 'shitty +shitten show_key', result_class=ShowKeyCLIOptions)
    if cli_opts.key_mode == 'shitty':
        from .shitty_mode import main as shitty_main
        return shitty_main()
    if cli_opts.key_mode != 'unchanged':
        print(end='\x1b[?1' + ('l' if cli_opts.key_mode == 'normal' else 'h'), flush=True)
    try:
        return legacy_main()
    finally:
        if cli_opts.key_mode != 'unchanged':
            print(end='\x1b[?1l', flush=True)


if __name__ == '__main__':
    main(sys.argv)
elif __name__ == '__doc__':
    cd = sys.cli_docs  # type: ignore
    cd['usage'] = usage
    cd['options'] = OPTIONS
    cd['help_text'] = help_text
