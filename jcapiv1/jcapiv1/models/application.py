# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from jcapiv1.models.application_config import ApplicationConfig  # noqa: F401,E501


class Application(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'active': 'bool',
        'name': 'str',
        'display_name': 'str',
        'display_label': 'str',
        'organization': 'str',
        'sso_url': 'str',
        'learn_more': 'str',
        'config': 'ApplicationConfig'
    }

    attribute_map = {
        'id': '_id',
        'active': 'active',
        'name': 'name',
        'display_name': 'displayName',
        'display_label': 'displayLabel',
        'organization': 'organization',
        'sso_url': 'ssoUrl',
        'learn_more': 'learnMore',
        'config': 'config'
    }

    def __init__(self, id=None, active=None, name=None, display_name=None, display_label=None, organization=None, sso_url=None, learn_more=None, config=None):  # noqa: E501
        """Application - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._active = None
        self._name = None
        self._display_name = None
        self._display_label = None
        self._organization = None
        self._sso_url = None
        self._learn_more = None
        self._config = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if active is not None:
            self.active = active
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if display_label is not None:
            self.display_label = display_label
        if organization is not None:
            self.organization = organization
        if sso_url is not None:
            self.sso_url = sso_url
        if learn_more is not None:
            self.learn_more = learn_more
        if config is not None:
            self.config = config

    @property
    def id(self):
        """Gets the id of this Application.  # noqa: E501


        :return: The id of this Application.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Application.


        :param id: The id of this Application.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def active(self):
        """Gets the active of this Application.  # noqa: E501


        :return: The active of this Application.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Application.


        :param active: The active of this Application.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def name(self):
        """Gets the name of this Application.  # noqa: E501


        :return: The name of this Application.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Application.


        :param name: The name of this Application.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this Application.  # noqa: E501


        :return: The display_name of this Application.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Application.


        :param display_name: The display_name of this Application.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def display_label(self):
        """Gets the display_label of this Application.  # noqa: E501


        :return: The display_label of this Application.  # noqa: E501
        :rtype: str
        """
        return self._display_label

    @display_label.setter
    def display_label(self, display_label):
        """Sets the display_label of this Application.


        :param display_label: The display_label of this Application.  # noqa: E501
        :type: str
        """

        self._display_label = display_label

    @property
    def organization(self):
        """Gets the organization of this Application.  # noqa: E501


        :return: The organization of this Application.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Application.


        :param organization: The organization of this Application.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def sso_url(self):
        """Gets the sso_url of this Application.  # noqa: E501


        :return: The sso_url of this Application.  # noqa: E501
        :rtype: str
        """
        return self._sso_url

    @sso_url.setter
    def sso_url(self, sso_url):
        """Sets the sso_url of this Application.


        :param sso_url: The sso_url of this Application.  # noqa: E501
        :type: str
        """

        self._sso_url = sso_url

    @property
    def learn_more(self):
        """Gets the learn_more of this Application.  # noqa: E501


        :return: The learn_more of this Application.  # noqa: E501
        :rtype: str
        """
        return self._learn_more

    @learn_more.setter
    def learn_more(self, learn_more):
        """Sets the learn_more of this Application.


        :param learn_more: The learn_more of this Application.  # noqa: E501
        :type: str
        """

        self._learn_more = learn_more

    @property
    def config(self):
        """Gets the config of this Application.  # noqa: E501


        :return: The config of this Application.  # noqa: E501
        :rtype: ApplicationConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Application.


        :param config: The config of this Application.  # noqa: E501
        :type: ApplicationConfig
        """

        self._config = config

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Application):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
