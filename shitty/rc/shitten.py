#!/usr/bin/env python
# License: GPLv3 Copyright: 2020, Kovid Goyal <kovid at ungtb10d.net>

from typing import TYPE_CHECKING, Optional

from .base import (
    MATCH_WINDOW_OPTION, ArgsType, Boss, PayloadGetType, PayloadType, RCOptions,
    RemoteCommand, ResponseType, Window
)

if TYPE_CHECKING:
    from shitty.cli_stub import shittenRCOptions as CLIOptions


class shitten(RemoteCommand):

    '''
    shitten+/str: The name of the shitten to run
    args/list.str: Arguments to pass to the shitten as a list
    match/str: The window to run the shitten over
    '''

    short_desc = 'Run a shitten'
    desc = (
        'Run a shitten over the specified windows (active window by default).'
        ' The :italic:`shitten_name` can be either the name of a builtin shitten'
        ' or the path to a Python file containing a custom shitten. If a relative path'
        ' is used it is searched for in the :ref:`shitty config directory <confloc>`. If the shitten is a'
        ' :italic:`no_ui` shitten and its handle response method returns a string or boolean, this'
        ' is printed out to stdout.'
    )
    options_spec = MATCH_WINDOW_OPTION
    argspec = 'shitten_name'

    def message_to_shitty(self, global_opts: RCOptions, opts: 'CLIOptions', args: ArgsType) -> PayloadType:
        if len(args) < 1:
            self.fatal('Must specify shitten name')
        return {'match': opts.match, 'args': list(args)[1:], 'shitten': args[0]}

    def response_from_shitty(self, boss: Boss, window: Optional[Window], payload_get: PayloadGetType) -> ResponseType:
        retval = None
        for window in self.windows_for_match_payload(boss, window, payload_get):
            if window:
                retval = boss.run_shitten_with_metadata(payload_get('shitten'), args=tuple(payload_get('args') or ()), window=window)
                break
        if isinstance(retval, (str, bool)):
            return retval
        return None


shitten = shitten()
