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
from jcapiv2.api.user_group_members__membership_api import UserGroupMembersMembershipApi  # noqa: E501
from jcapiv2.rest import ApiException


class TestUserGroupMembersMembershipApi(unittest.TestCase):
    """UserGroupMembersMembershipApi unit test stubs"""

    def setUp(self):
        self.api = jcapiv2.api.user_group_members__membership_api.UserGroupMembersMembershipApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_graph_user_group_member_of(self):
        """Test case for graph_user_group_member_of

        List the User Group's parents  # noqa: E501
        """
        pass

    def test_graph_user_group_members_list(self):
        """Test case for graph_user_group_members_list

        List the members of a User Group  # noqa: E501
        """
        pass

    def test_graph_user_group_members_post(self):
        """Test case for graph_user_group_members_post

        Manage the members of a User Group  # noqa: E501
        """
        pass

    def test_graph_user_group_membership(self):
        """Test case for graph_user_group_membership

        List the User Group's membership  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
