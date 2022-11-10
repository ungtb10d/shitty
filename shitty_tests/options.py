#!/usr/bin/env python3
# License: GPL v3 Copyright: 2018, Kovid Goyal <kovid at ungtb10d.net>


from . import BaseTest
from shitty.utils import log_error
from shitty.options.utils import DELETE_ENV_VAR
from shitty.fast_data_types import Color


class TestConfParsing(BaseTest):

    def setUp(self):
        super().setUp()
        self.error_messages = []
        log_error.redirect = self.error_messages.append

    def tearDown(self):
        del log_error.redirect
        super().tearDown()

    def test_conf_parsing(self):
        from shitty.config import load_config, defaults
        from shitty.constants import is_macos
        from shitty.options.utils import to_modifiers
        from shitty.fonts import FontModification, ModificationType, ModificationValue, ModificationUnit
        bad_lines = []

        def p(*lines, bad_line_num=0):
            del bad_lines[:]
            del self.error_messages[:]
            ans = load_config(overrides=lines, accumulate_bad_lines=bad_lines)
            if bad_line_num:
                self.ae(len(bad_lines), bad_line_num)
            else:
                self.assertFalse(bad_lines)
            return ans

        def keys_for_func(opts, name):
            for key, defn in opts.keymap.items():
                for action in opts.alias_map.resolve_aliases(defn):
                    if action.func == name:
                        yield key

        opts = p('font_size 11.37', 'clear_all_shortcuts y', 'color23 red')
        self.ae(opts.font_size, 11.37)
        self.ae(opts.mouse_hide_wait, 0 if is_macos else 3)
        self.ae(opts.color23, Color(255, 0, 0))
        self.assertFalse(opts.keymap)
        opts = p('clear_all_shortcuts y', 'map f1 next_window')
        self.ae(len(opts.keymap), 1)
        opts = p('clear_all_mouse_actions y', 'mouse_map left click ungrabbed mouse_click_url_or_select')
        self.ae(len(opts.mousemap), 1)
        opts = p('strip_trailing_spaces always')
        self.ae(opts.strip_trailing_spaces, 'always')
        self.assertFalse(bad_lines)
        opts = p('pointer_shape_when_grabbed XXX', bad_line_num=1)
        self.ae(opts.pointer_shape_when_grabbed, defaults.pointer_shape_when_grabbed)
        opts = p('modify_font underline_position -2', 'modify_font underline_thickness 150%', 'modify_font size Test -1px')
        self.ae(opts.modify_font, {
            'underline_position': FontModification(ModificationType.underline_position, ModificationValue(-2., ModificationUnit.pt)),
            'underline_thickness': FontModification(ModificationType.underline_thickness, ModificationValue(150, ModificationUnit.percent)),
            'size:Test': FontModification(ModificationType.size, ModificationValue(-1., ModificationUnit.pixel), 'Test'),
        })

        # test the aliasing options
        opts = p('env A=1', 'env B=x$A', 'env C=', 'env D', 'clear_all_shortcuts y', 'kitten_alias a b --moo', 'map f1 shitten a arg')
        self.ae(opts.env, {'A': '1', 'B': 'x1', 'C': '', 'D': DELETE_ENV_VAR})

        def ac(which=0):
            ka = tuple(opts.keymap.values())[0]
            acs = opts.alias_map.resolve_aliases(ka)
            return acs[which]

        ka = ac()
        self.ae(ka.func, 'shitten')
        self.ae(ka.args, ('b', '--moo', 'arg'))

        opts = p('clear_all_shortcuts y', 'kitten_alias hints hints --hi', 'map f1 shitten hints XXX')
        ka = ac()
        self.ae(ka.func, 'shitten')
        self.ae(ka.args, ('hints', '--hi', 'XXX'))

        opts = p('clear_all_shortcuts y', 'action_alias la launch --moo', 'map f1 la XXX')
        ka = ac()
        self.ae(ka.func, 'launch')
        self.ae(ka.args, ('--moo', 'XXX'))

        opts = p('clear_all_shortcuts y', 'action_alias one launch --moo', 'action_alias two one recursive', 'map f1 two XXX')
        ka = ac()
        self.ae(ka.func, 'launch')
        self.ae(ka.args, ('--moo', 'recursive', 'XXX'))

        opts = p('clear_all_shortcuts y', 'action_alias launch two 1', 'action_alias two launch 2', 'map f1 launch 3')
        ka = ac()
        self.ae(ka.func, 'launch')
        self.ae(ka.args, ('2', '1', '3'))

        opts = p('clear_all_shortcuts y', 'action_alias launch launch --moo', 'map f1 launch XXX')
        ka = ac()
        self.ae(ka.func, 'launch')
        self.ae(ka.args, ('--moo', 'XXX'))

        opts = p('clear_all_shortcuts y', 'action_alias cfs change_font_size current', 'map f1 cfs +2')
        ka = ac()
        self.ae(ka.func, 'change_font_size')
        self.ae(ka.args, (False, '+', 2.0))

        opts = p('clear_all_shortcuts y', 'action_alias la launch --moo', 'map f1 combine : new_window : la ')
        self.ae((ac().func, ac(1).func), ('new_window', 'launch'))

        opts = p('clear_all_shortcuts y', 'action_alias cc combine : new_window : launch --moo', 'map f1 cc XXX')
        self.ae((ac().func, ac(1).func), ('new_window', 'launch'))
        self.ae(ac(1).args, ('--moo', 'XXX'))

        opts = p('kitty_mod alt')
        self.ae(opts.kitty_mod, to_modifiers('alt'))
        self.ae(next(keys_for_func(opts, 'next_layout')).mods, opts.kitty_mod)

        # deprecation handling
        opts = p('clear_all_shortcuts y', 'send_text all f1 hello')
        self.ae(len(opts.keymap), 1)
        opts = p('macos_hide_titlebar y' if is_macos else 'x11_hide_window_decorations y')
        self.assertTrue(opts.hide_window_decorations)
        self.ae(len(self.error_messages), 1)
