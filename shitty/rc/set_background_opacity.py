#!/usr/bin/env python
# License: GPLv3 Copyright: 2020, ungtb10d <kovid at ungtb10d.net>


from typing import TYPE_CHECKING, Optional

from .base import (
    MATCH_TAB_OPTION, MATCH_WINDOW_OPTION, ArgsType, Boss, OpacityError,
    PayloadGetType, PayloadType, RCOptions, RemoteCommand, ResponseType,
    Window
)

if TYPE_CHECKING:
    from shitty.cli_stub import SetBackgroundOpacityRCOptions as CLIOptions


class SetBackgroundOpacity(RemoteCommand):

    '''
    opacity+/float: A number between 0.1 and 1
    match_window/str: Window to change opacity in
    match_tab/str: Tab to change opacity in
    all/bool: Boolean indicating operate on all windows
    '''

    short_desc = 'Set the background opacity'
    desc = (
        'Set the background opacity for the specified windows. This will only work if you have turned on'
        ' :opt:`dynamic_background_opacity` in :file:`shitty.conf`. The background opacity affects all shitty windows in a'
        ' single OS window. For example::\n\n'
        '    shitty @ set-background-opacity 0.5'
    )
    options_spec = '''\
--all -a
type=bool-set
By default, background opacity are only changed for the currently active window. This option will
cause background opacity to be changed in all windows.

''' + '\n\n' + MATCH_WINDOW_OPTION + '\n\n' + MATCH_TAB_OPTION.replace('--match -m', '--match-tab -t')
    argspec = 'OPACITY'
    args_count = 1

    def message_to_shitty(self, global_opts: RCOptions, opts: 'CLIOptions', args: ArgsType) -> PayloadType:
        opacity = max(0.1, min(float(args[0]), 1.0))
        return {
                'opacity': opacity, 'match_window': opts.match,
                'all': opts.all, 'match_tab': opts.match_tab
        }

    def response_from_shitty(self, boss: Boss, window: Optional[Window], payload_get: PayloadGetType) -> ResponseType:
        from shitty.fast_data_types import get_options
        if not get_options().dynamic_background_opacity:
            raise OpacityError('You must turn on the dynamic_background_opacity option in shitty.conf to be able to set background opacity')
        windows = self.windows_for_payload(boss, window, payload_get)
        for os_window_id in {w.os_window_id for w in windows if w}:
            boss._set_os_window_background_opacity(os_window_id, payload_get('opacity'))
        return None


set_background_opacity = SetBackgroundOpacity()
