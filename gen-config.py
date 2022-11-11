#!/usr/bin/env python
# vim:fileencoding=utf-8
# License: GPLv3 Copyright: 2021, Kovid Goyal <kovid at ungtb10d.net>


from shitty.conf.generate import write_output


def main() -> None:
    from shitty.options.definition import definition
    write_output('shitty', definition)
    from shittens.diff.options.definition import definition as kd
    write_output('shittens.diff', kd)


if __name__ == '__main__':
    main()
