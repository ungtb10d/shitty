#!/usr/bin/env python
# vim:fileencoding=utf-8
# License: GPLv3 Copyright: 2020, Kovid Goyal <kovid at ungtb10d.net>

from typing import TYPE_CHECKING, Optional

from .base import (
    MATCH_WINDOW_OPTION, ArgsType, Boss, MatchError, PayloadGetType,
    PayloadType, RCOptions, RemoteCommand, ResponseType, Window
)

if TYPE_CHECKING:
    from shitty.cli_stub import shittenRCOptions as CLIOptions


class shitten(RemoteCommand):

    '''
    shitten+: The name of the shitten to run
    args: Arguments to pass to the shitten as a list
    match: The window to run the shitten over
    '''

    short_desc = 'Run a shitten'
    desc = (
        'Run a shitten over the specified window (active window by default).'
        ' The :italic:`shitten_name` can be either the name of a builtin shitten'
        ' or the path to a python file containing a custom shitten. If a relative path'
        ' is used it is searched for in the shitty config directory. If the shitten is a'
        ' no_ui shitten and its handle response method returns a string or boolean, this'
        ' is printed out to stdout.'
    )
    options_spec = MATCH_WINDOW_OPTION
    argspec = 'shitten_name'

    def message_to_shitty(self, global_opts: RCOptions, opts: 'CLIOptions', args: ArgsType) -> PayloadType:
        if len(args) < 1:
            self.fatal('Must specify shitten name')
        return {'match': opts.match, 'args': list(args)[1:], 'shitten': args[0]}

    def response_from_shitty(self, boss: Boss, window: Optional[Window], payload_get: PayloadGetType) -> ResponseType:
        windows = [window or boss.active_window]
        match = payload_get('match')
        if match:
            windows = list(boss.match_windows(match))
            if not windows:
                raise MatchError(match)
        retval = None
        for window in windows:
            if window:
                retval = boss._run_shitten(payload_get('shitten'), args=tuple(payload_get('args') or ()), window=window)
                break
        if isinstance(retval, (str, bool)):
            return retval


shitten = shitten()
