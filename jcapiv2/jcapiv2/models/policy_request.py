# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The next version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings. The most recent version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PolicyRequest(object):
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
        'name': 'str',
        'values': 'list[PolicyValue]',
        'template': 'PolicyRequestTemplate'
    }

    attribute_map = {
        'name': 'name',
        'values': 'values',
        'template': 'template'
    }

    def __init__(self, name=None, values=None, template=None):
        """
        PolicyRequest - a model defined in Swagger
        """

        self._name = None
        self._values = None
        self._template = None

        self.name = name
        if values is not None:
          self.values = values
        if template is not None:
          self.template = template

    @property
    def name(self):
        """
        Gets the name of this PolicyRequest.
        The description for this specific Policy.

        :return: The name of this PolicyRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PolicyRequest.
        The description for this specific Policy.

        :param name: The name of this PolicyRequest.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def values(self):
        """
        Gets the values of this PolicyRequest.

        :return: The values of this PolicyRequest.
        :rtype: list[PolicyValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this PolicyRequest.

        :param values: The values of this PolicyRequest.
        :type: list[PolicyValue]
        """

        self._values = values

    @property
    def template(self):
        """
        Gets the template of this PolicyRequest.

        :return: The template of this PolicyRequest.
        :rtype: PolicyRequestTemplate
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this PolicyRequest.

        :param template: The template of this PolicyRequest.
        :type: PolicyRequestTemplate
        """

        self._template = template

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
        if not isinstance(other, PolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
