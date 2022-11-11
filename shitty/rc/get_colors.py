#!/usr/bin/env python
# vim:fileencoding=utf-8
# License: GPLv3 Copyright: 2020, Kovid Goyal <kovid at ungtb10d.net>

from typing import TYPE_CHECKING, Optional

from shitty.rgb import Color, color_as_sharp, color_from_int
from shitty.utils import natsort_ints

from .base import (
    MATCH_WINDOW_OPTION, ArgsType, Boss, PayloadGetType, PayloadType,
    RCOptions, RemoteCommand, ResponseType, Window
)

if TYPE_CHECKING:
    from shitty.cli_stub import GetColorsRCOptions as CLIOptions


class GetColors(RemoteCommand):

    '''
    match: The window to get the colors for
    configured: Boolean indicating whether to get configured or current colors
    '''

    short_desc = 'Get terminal colors'
    desc = (
        'Get the terminal colors for the specified window (defaults to active window). '
        'Colors will be output to stdout in the same syntax as used for shitty.conf'
    )
    options_spec = '''\
--configured -c
type=bool-set
Instead of outputting the colors for the specified window, output the currently
configured colors.

''' + '\n\n' + MATCH_WINDOW_OPTION

    def message_to_shitty(self, global_opts: RCOptions, opts: 'CLIOptions', args: ArgsType) -> PayloadType:
        return {'configured': opts.configured, 'match': opts.match}

    def response_from_shitty(self, boss: Boss, window: Optional[Window], payload_get: PayloadGetType) -> ResponseType:
        from shitty.fast_data_types import get_options
        opts = get_options()
        ans = {k: getattr(opts, k) for k in opts if isinstance(getattr(opts, k), Color)}
        if not payload_get('configured'):
            windows = self.windows_for_match_payload(boss, window, payload_get)
            ans.update({k: color_from_int(v) for k, v in windows[0].current_colors.items()})
        all_keys = natsort_ints(ans)
        maxlen = max(map(len, all_keys))
        return '\n'.join(('{:%ds} {}' % maxlen).format(key, color_as_sharp(ans[key])) for key in all_keys)
# }}}


get_colors = GetColors()
