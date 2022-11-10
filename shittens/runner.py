#!/usr/bin/env python3
# License: GPL v3 Copyright: 2018, ungtb10d <kovid at ungtb10d.net>


import importlib
import os
import sys
from contextlib import contextmanager
from functools import partial
from typing import TYPE_CHECKING, Any, Dict, FrozenSet, Generator, List, cast

from shitty.constants import list_shitty_resources
from shitty.types import run_once
from shitty.utils import resolve_abs_or_config_path

aliases = {'url_hints': 'hints'}
if TYPE_CHECKING:
    from shitty.conf.types import Definition
else:
    Definition = object


def resolved_shitten(k: str) -> str:
    ans = aliases.get(k, k)
    head, tail = os.path.split(ans)
    tail = tail.replace('-', '_')
    return os.path.join(head, tail)


def path_to_custom_shitten(config_dir: str, shitten: str) -> str:
    path = resolve_abs_or_config_path(shitten, conf_dir=config_dir)
    return os.path.abspath(path)


@contextmanager
def preserve_sys_path() -> Generator[None, None, None]:
    orig = sys.path[:]
    try:
        yield
    finally:
        if sys.path != orig:
            del sys.path[:]
            sys.path.extend(orig)


def import_shitten_main_module(config_dir: str, shitten: str) -> Dict[str, Any]:
    if shitten.endswith('.py'):
        with preserve_sys_path():
            path = path_to_custom_shitten(config_dir, shitten)
            if os.path.dirname(path):
                sys.path.insert(0, os.path.dirname(path))
            with open(path) as f:
                src = f.read()
            code = compile(src, path, 'exec')
            g = {'__name__': 'shitten'}
            exec(code, g)
            hr = g.get('handle_result', lambda *a, **kw: None)
        return {'start': g['main'], 'end': hr}

    shitten = resolved_shitten(shitten)
    m = importlib.import_module(f'shittens.{shitten}.main')
    return {'start': getattr(m, 'main'), 'end': getattr(m, 'handle_result', lambda *a, **k: None)}


def create_shitten_handler(shitten: str, orig_args: List[str]) -> Any:
    from shitty.constants import config_dir
    shitten = resolved_shitten(shitten)
    m = import_shitten_main_module(config_dir, shitten)
    ans = partial(m['end'], [shitten] + orig_args)
    setattr(ans, 'type_of_input', getattr(m['end'], 'type_of_input', None))
    setattr(ans, 'no_ui', getattr(m['end'], 'no_ui', False))
    setattr(ans, 'has_ready_notification', getattr(m['end'], 'has_ready_notification', False))
    return ans


def set_debug(shitten: str) -> None:
    import builtins

    from shittens.tui.loop import debug
    setattr(builtins, 'debug', debug)


def launch(args: List[str]) -> None:
    config_dir, shitten = args[:2]
    shitten = resolved_shitten(shitten)
    del args[:2]
    args = [shitten] + args
    os.environ['shitty_CONFIG_DIRECTORY'] = config_dir
    set_debug(shitten)
    m = import_shitten_main_module(config_dir, shitten)
    try:
        result = m['start'](args)
    finally:
        sys.stdin = sys.__stdin__
    if result is not None:
        import json
        import base64
        data = base64.b85encode(json.dumps(result).encode('utf-8'))
        sys.stdout.buffer.write(b'\x1bP@shitty-shitten-result|')
        sys.stdout.buffer.write(data)
        sys.stdout.buffer.write(b'\x1b\\')
    sys.stderr.flush()
    sys.stdout.flush()


def run_shitten(shitten: str, run_name: str = '__main__') -> None:
    import runpy
    original_shitten_name = shitten
    shitten = resolved_shitten(shitten)
    set_debug(shitten)
    if shitten in all_shitten_names():
        runpy.run_module(f'shittens.{shitten}.main', run_name=run_name)
        return
    # Look for a custom shitten
    if not shitten.endswith('.py'):
        shitten += '.py'
    from shitty.constants import config_dir
    path = path_to_custom_shitten(config_dir, shitten)
    if not os.path.exists(path):
        print('Available builtin shittens:', file=sys.stderr)
        for shitten in all_shitten_names():
            print(shitten, file=sys.stderr)
        raise SystemExit(f'No shitten named {original_shitten_name}')
    m = runpy.run_path(path, init_globals={'sys': sys, 'os': os}, run_name='__run_shitten__')
    from shitty.fast_data_types import set_options
    try:
        m['main'](sys.argv)
    finally:
        set_options(None)


@run_once
def all_shitten_names() -> FrozenSet[str]:
    ans = []
    for name in list_shitty_resources('shittens'):
        if '__' not in name and '.' not in name and name != 'tui':
            ans.append(name)
    return frozenset(ans)


def list_shittens() -> None:
    print('You must specify the name of a shitten to run')
    print('Choose from:')
    print()
    for shitten in all_shitten_names():
        print(shitten)


def get_shitten_cli_docs(shitten: str) -> Any:
    setattr(sys, 'cli_docs', {})
    run_shitten(shitten, run_name='__doc__')
    ans = getattr(sys, 'cli_docs')
    delattr(sys, 'cli_docs')
    if 'help_text' in ans and 'usage' in ans and 'options' in ans:
        return ans


def get_shitten_completer(shitten: str) -> Any:
    run_shitten(shitten, run_name='__completer__')
    ans = getattr(sys, 'shitten_completer', None)
    if ans is not None:
        delattr(sys, 'shitten_completer')
    return ans


def get_shitten_conf_docs(shitten: str) -> Definition:
    setattr(sys, 'options_definition', None)
    run_shitten(shitten, run_name='__conf__')
    ans = getattr(sys, 'options_definition')
    delattr(sys, 'options_definition')
    return cast(Definition, ans)


def main() -> None:
    try:
        args = sys.argv[1:]
        launch(args)
    except Exception:
        print('Unhandled exception running shitten:')
        import traceback
        traceback.print_exc()
        input('Press Enter to quit')
