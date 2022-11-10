#!/usr/bin/env python
# License: GPLv3 Copyright: 2020, ungtb10d <kovid at ungtb10d.net>


from typing import TYPE_CHECKING, Optional

from .base import (
    MATCH_WINDOW_OPTION, ArgsType, Boss, PayloadGetType, PayloadType,
    RCOptions, RemoteCommand, ResponseType, Window
)

if TYPE_CHECKING:
    from shitty.cli_stub import RemoveMarkerRCOptions as CLIOptions


class RemoveMarker(RemoteCommand):

    '''
    match/str: Which window to remove the marker from
    self/bool: Boolean indicating whether to detach the window the command is run in
    '''

    short_desc = 'Remove the currently set marker, if any.'
    options_spec = MATCH_WINDOW_OPTION + '''\n
--self
type=bool-set
Apply marker to the window this command is run in, rather than the active window.
'''
    argspec = ''

    def message_to_shitty(self, global_opts: RCOptions, opts: 'CLIOptions', args: ArgsType) -> PayloadType:
        return {'match': opts.match, 'self': opts.self}

    def response_from_shitty(self, boss: Boss, window: Optional[Window], payload_get: PayloadGetType) -> ResponseType:
        for window in self.windows_for_match_payload(boss, window, payload_get):
            if window:
                window.remove_marker()
        return None


remove_marker = RemoveMarker()
