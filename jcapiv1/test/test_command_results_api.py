# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import jcapiv1
from jcapiv1.api.command_results_api import CommandResultsApi  # noqa: E501
from jcapiv1.rest import ApiException


class TestCommandResultsApi(unittest.TestCase):
    """CommandResultsApi unit test stubs"""

    def setUp(self):
        self.api = jcapiv1.api.command_results_api.CommandResultsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_command_results_delete(self):
        """Test case for command_results_delete

        Delete a Command result  # noqa: E501
        """
        pass

    def test_command_results_get(self):
        """Test case for command_results_get

        List an individual Command result  # noqa: E501
        """
        pass

    def test_command_results_list(self):
        """Test case for command_results_list

        List all Command Results  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
