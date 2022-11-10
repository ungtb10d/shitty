import subprocess

from shitty.fast_data_types import num_users

from . import BaseTest


class UTMPTest(BaseTest):

    def test_num_users(self):
        # who is the control
        try:
            expected = subprocess.check_output(['who']).decode('utf-8').count('\n')
        except FileNotFoundError:
            self.skipTest('No who executable cannot verify num_users')
        self.ae(num_users(), expected)
