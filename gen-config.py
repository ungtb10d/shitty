#!./shitty/launcher/shitty +launch
# License: GPLv3 Copyright: 2021, Kovid Goyal <kovid at ungtb10d.net>


import re
from typing import List

from shitty.conf.generate import write_output


def patch_color_list(path: str, colors: List[str], name: str, spc: str = '    ') -> None:
    with open(path, 'r+') as f:
        raw = f.read()
        nraw = re.sub(
            fr'(# {name}_COLORS_START).+?(\s+# {name}_COLORS_END)',
            r'\1' + f'\n{spc}' + f'\n{spc}'.join(map(lambda x: f'{x!r},', sorted(colors))) + r'\2',
            raw, flags=re.DOTALL | re.MULTILINE)
        if nraw != raw:
            f.seek(0)
            f.truncate()
            f.write(nraw)


def main() -> None:
    from shitty.options.definition import definition
    write_output('shitty', definition)
    nullable_colors = []
    all_colors = []
    for opt in definition.iter_all_options():
        if callable(opt.parser_func):
            if opt.parser_func.__name__ in ('to_color_or_none', 'cursor_text_color'):
                nullable_colors.append(opt.name)
                all_colors.append(opt.name)
            elif opt.parser_func.__name__ in ('to_color', 'titlebar_color', 'macos_titlebar_color'):
                all_colors.append(opt.name)
    patch_color_list('shitty/rc/set_colors.py', nullable_colors, 'NULLABLE')
    patch_color_list('shittens/themes/collection.py', all_colors, 'ALL', ' ' * 8)

    from shittens.diff.options.definition import definition as kd
    write_output('shittens.diff', kd)
    from shittens.ssh.options.definition import definition as sd
    write_output('shittens.ssh', sd)


if __name__ == '__main__':
    main()
