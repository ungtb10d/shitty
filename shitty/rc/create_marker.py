#!/usr/bin/env python
# License: GPLv3 Copyright: 2020, ungtb10d <kovid at ungtb10d.net>

from typing import TYPE_CHECKING, Optional

from shitty.options.utils import parse_marker_spec

from .base import (
    MATCH_WINDOW_OPTION, ArgsType, Boss, PayloadGetType,
    PayloadType, RCOptions, RemoteCommand, ResponseType, Window
)

if TYPE_CHECKING:
    from shitty.cli_stub import CreateMarkerRCOptions as CLIOptions


class CreateMarker(RemoteCommand):

    '''
    match/str: Which window to create the marker in
    self/bool: Boolean indicating whether to create marker in the window the command is run in
    marker_spec/list.str: A list or arguments that define the marker specification, for example: ['text', '1', 'ERROR']
    '''

    short_desc = 'Create a marker that highlights specified text'
    desc = (
        'Create a marker which can highlight text in the specified window. For example:'
        ' :code:`create_marker text 1 ERROR`. For full details see: :doc:`marks`'
    )
    options_spec = MATCH_WINDOW_OPTION + '''\n
--self
type=bool-set
Apply marker to the window this command is run in, rather than the active window.
'''
    argspec = 'MARKER SPECIFICATION'

    def message_to_shitty(self, global_opts: RCOptions, opts: 'CLIOptions', args: ArgsType) -> PayloadType:
        if len(args) < 2:
            self.fatal('Invalid marker specification: {}'.format(' '.join(args)))
        try:
            parse_marker_spec(args[0], args[1:])
        except Exception as err:
            self.fatal(f"Failed to parse marker specification {' '.join(args)} with error: {err}")
        return {'match': opts.match, 'self': opts.self, 'marker_spec': args}

    def response_from_shitty(self, boss: Boss, window: Optional[Window], payload_get: PayloadGetType) -> ResponseType:
        args = payload_get('marker_spec')
        for window in self.windows_for_match_payload(boss, window, payload_get):
            if window:
                window.set_marker(args)
        return None


create_marker = CreateMarker()
