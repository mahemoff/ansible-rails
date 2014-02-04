# -*- coding: utf-8 -*-

import os
import os.path
import sys

import unittest
from mock import Mock

from ansible.module_utils.basic import AnsibleModule

import imp
imp.load_source('rake', os.path.join(os.path.dirname(__file__), os.path.pardir, 'library','rake'))

from rake import BaseModule, RakeModule

class FakeAnsibleModule(object):
  check_mode = False
  params = {}

class TestBundle(unittest.TestCase):
  def test_get_bundle_path(self):
    module = FakeAnsibleModule()
    module.params = { 'path': '/path/to/app' }
    module.get_bin_path = Mock(return_value='/bin/bandler')

    rake = BaseModule(module)
    rake.get_bundle_path()

    module.get_bin_path.assert_called_with('bundle', True, [])

  def test_diff(self):
    module = FakeAnsibleModule()
    rake = BaseModule(module)

    assert rake.diff('test/fixtures/current_db', 'test/fixtures/next_db') == False

    assert rake.diff('test/fixtures/changed_db', 'test/fixtures/next_db') == True


if __name__ == '__main__':
  unittest.main()