#!/usr/bin/env python
# License: GPLv3 Copyright: 2022, Kovid Goyal <kovid at ungtb10d.net>


import json
import os
import select
import signal
import subprocess
import tempfile
import time

from shitty.constants import kitty_exe
from shitty.fast_data_types import (
    CLD_EXITED, CLD_KILLED, CLD_STOPPED, get_options, has_sigqueue, install_signal_handlers,
    read_signals, sigqueue
)

from . import BaseTest


class Prewarm(BaseTest):

    maxDiff = None

    def test_prewarming(self):
        from shitty.prewarm import fork_prewarm_process

        cwd = tempfile.gettempdir()
        env = {'TEST_ENV_PASS': 'xyz'}
        cols = 317
        stdin_data = 'from_stdin'
        pty = self.create_pty(cols=cols)
        ttyname = os.ttyname(pty.slave_fd)
        opts = get_options()
        opts.config_overrides = 'font_family prewarm',
        os.environ['SHOULD_NOT_BE_PRESENT'] = '1'
        p = fork_prewarm_process(opts, use_exec=True)
        del os.environ['SHOULD_NOT_BE_PRESENT']
        if p is None:
            return
        p.take_from_worker_fd(create_file=True)
        child = p(pty.slave_fd, [kitty_exe(), '+runpy', """\
import os, json; from shitty.utils import *; from shitty.fast_data_types import get_options; print(json.dumps({
        'cterm': os.ctermid(),
        'ttyname': os.ttyname(sys.stdout.fileno()),
        'cols': read_screen_size().cols,
        'cwd': os.getcwd(),
        'env': os.environ.copy(),
        'pid': os.getpid(),
        'font_family': get_options().font_family,
        'stdin': sys.stdin.read(),
        }, indent=2), "ALL_OUTPUT_PRESENT", sep="")"""], cwd=cwd, env=env, stdin_data=stdin_data, timeout=15.0)
        self.assertFalse(pty.screen_contents().strip())
        p.mark_child_as_ready(child.child_id)
        pty.wait_till(lambda: 'ALL_OUTPUT_PRESENT' in pty.screen_contents())
        data = json.JSONDecoder().raw_decode(pty.screen_contents())[0]
        self.ae(data['cols'], cols)
        self.assertTrue(data['cterm'])
        self.ae(data['ttyname'], ttyname)
        self.ae(os.path.realpath(data['cwd']), os.path.realpath(cwd))
        self.ae(data['env']['TEST_ENV_PASS'], env['TEST_ENV_PASS'])
        self.assertNotIn('SHOULD_NOT_BE_PRESENT', data['env'])
        self.ae(data['font_family'], 'prewarm')
        self.ae(int(p.from_worker.readline()), data['pid'])

    def test_signal_handling(self):
        from shitty.prewarm import restore_python_signal_handlers, wait_for_child_death
        expecting_code = 0
        expecting_signal = signal.SIGCHLD
        expecting_value = 0
        found_signal = False

        def handle_signals(signals):
            nonlocal found_signal
            for siginfo in signals:
                if siginfo.si_signo != expecting_signal.value:
                    continue
                if expecting_code is not None:
                    self.ae(siginfo.si_code, expecting_code)
                self.ae(siginfo.sival_int, expecting_value)
                if expecting_code in (CLD_EXITED, CLD_KILLED):
                    p.wait(1)
                    p.stdin.close()
                found_signal = True

        def assert_signal():
            nonlocal found_signal
            found_signal = False
            st = time.monotonic()
            while time.monotonic() - st < 30:
                for (fd, event) in poll.poll(10):
                    if fd == signal_read_fd:
                        signals = []
                        read_signals(signal_read_fd, signals.append)
                        handle_signals(signals)
                if found_signal:
                    break
            self.assertTrue(found_signal, f'Failed to get signal: {expecting_signal!r}')

        def t(signal, q, expecting_sig=signal.SIGCHLD):
            nonlocal expecting_code, found_signal, expecting_signal
            expecting_code = q
            expecting_signal = expecting_sig
            if signal is not None:
                p.send_signal(signal)
            assert_signal()

        poll = select.poll()

        def run():
            return subprocess.Popen([kitty_exe(), '+runpy', 'import sys; sys.stdin.read()'], stderr=subprocess.DEVNULL, stdin=subprocess.PIPE)
        p = run()
        orig_mask = signal.pthread_sigmask(signal.SIG_BLOCK, ())
        signal_read_fd = install_signal_handlers(signal.SIGCHLD, signal.SIGUSR1)[0]
        try:
            poll.register(signal_read_fd, select.POLLIN)
            t(signal.SIGINT, CLD_KILLED)
            p = run()
            p.stdin.close()
            t(None, CLD_EXITED)
            expecting_code = None
            expecting_signal = signal.SIGUSR1
            os.kill(os.getpid(), signal.SIGUSR1)
            assert_signal()
            expecting_value = 17 if has_sigqueue else 0
            sigqueue(os.getpid(), signal.SIGUSR1.value, expecting_value)
            assert_signal()

            expecting_code = None
            expecting_value = 0
            p = run()
            p.send_signal(signal.SIGSTOP)
            s = wait_for_child_death(p.pid, options=os.WUNTRACED, timeout=5)
            self.assertTrue(os.WIFSTOPPED(s))
            t(None, CLD_STOPPED)
            p.send_signal(signal.SIGCONT)
            s = wait_for_child_death(p.pid, options=os.WCONTINUED, timeout=5)
            self.assertTrue(os.WIFCONTINUED(s))
            # macOS does not send SIGCHLD when child is continued
            # https://stackoverflow.com/questions/48487935/sigchld-is-sent-on-sigcont-on-linux-but-not-on-macos
            p.stdin.close()
            p.wait(3)
            for fd, event in poll.poll(0):
                read_signals(signal_read_fd, lambda si: None)
        finally:
            restore_python_signal_handlers()
            signal.pthread_sigmask(signal.SIG_SETMASK, orig_mask)
