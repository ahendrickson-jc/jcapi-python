# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The previous version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Radiusserverput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'network_source_ip': 'str',
        'name': 'str',
        'tag_names': 'list[str]'
    }

    attribute_map = {
        'id': '_id',
        'network_source_ip': 'networkSourceIp',
        'name': 'name',
        'tag_names': 'tagNames'
    }

    def __init__(self, id=None, network_source_ip=None, name=None, tag_names=None):
        """
        Radiusserverput - a model defined in Swagger
        """

        self._id = None
        self._network_source_ip = None
        self._name = None
        self._tag_names = None

        if id is not None:
          self.id = id
        if network_source_ip is not None:
          self.network_source_ip = network_source_ip
        if name is not None:
          self.name = name
        if tag_names is not None:
          self.tag_names = tag_names

    @property
    def id(self):
        """
        Gets the id of this Radiusserverput.

        :return: The id of this Radiusserverput.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Radiusserverput.

        :param id: The id of this Radiusserverput.
        :type: str
        """

        self._id = id

    @property
    def network_source_ip(self):
        """
        Gets the network_source_ip of this Radiusserverput.

        :return: The network_source_ip of this Radiusserverput.
        :rtype: str
        """
        return self._network_source_ip

    @network_source_ip.setter
    def network_source_ip(self, network_source_ip):
        """
        Sets the network_source_ip of this Radiusserverput.

        :param network_source_ip: The network_source_ip of this Radiusserverput.
        :type: str
        """

        self._network_source_ip = network_source_ip

    @property
    def name(self):
        """
        Gets the name of this Radiusserverput.

        :return: The name of this Radiusserverput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Radiusserverput.

        :param name: The name of this Radiusserverput.
        :type: str
        """

        self._name = name

    @property
    def tag_names(self):
        """
        Gets the tag_names of this Radiusserverput.

        :return: The tag_names of this Radiusserverput.
        :rtype: list[str]
        """
        return self._tag_names

    @tag_names.setter
    def tag_names(self, tag_names):
        """
        Sets the tag_names of this Radiusserverput.

        :param tag_names: The tag_names of this Radiusserverput.
        :type: list[str]
        """

        self._tag_names = tag_names

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Radiusserverput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
