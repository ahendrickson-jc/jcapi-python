# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import jcapiv2
from jcapiv2.api.samba_domains_api import SambaDomainsApi  # noqa: E501
from jcapiv2.rest import ApiException


class TestSambaDomainsApi(unittest.TestCase):
    """SambaDomainsApi unit test stubs"""

    def setUp(self):
        self.api = jcapiv2.api.samba_domains_api.SambaDomainsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ldapservers_samba_domains_delete(self):
        """Test case for ldapservers_samba_domains_delete

        Delete Samba Domain  # noqa: E501
        """
        pass

    def test_ldapservers_samba_domains_get(self):
        """Test case for ldapservers_samba_domains_get

        Get Samba Domain  # noqa: E501
        """
        pass

    def test_ldapservers_samba_domains_list(self):
        """Test case for ldapservers_samba_domains_list

        List Samba Domains  # noqa: E501
        """
        pass

    def test_ldapservers_samba_domains_post(self):
        """Test case for ldapservers_samba_domains_post

        Create Samba Domain  # noqa: E501
        """
        pass

    def test_ldapservers_samba_domains_put(self):
        """Test case for ldapservers_samba_domains_put

        Update Samba Domain  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
