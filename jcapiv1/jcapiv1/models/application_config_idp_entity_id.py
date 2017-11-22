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


class ApplicationConfigIdpEntityId(object):
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
        'label': 'str',
        'read_only': 'bool',
        'tooltip': 'ApplicationConfigIdpEntityIdTooltip',
        'type': 'str',
        'value': 'str',
        'visible': 'bool',
        'required': 'bool',
        'position': 'int'
    }

    attribute_map = {
        'label': 'label',
        'read_only': 'readOnly',
        'tooltip': 'tooltip',
        'type': 'type',
        'value': 'value',
        'visible': 'visible',
        'required': 'required',
        'position': 'position'
    }

    def __init__(self, label=None, read_only=None, tooltip=None, type=None, value=None, visible=None, required=None, position=None):
        """
        ApplicationConfigIdpEntityId - a model defined in Swagger
        """

        self._label = None
        self._read_only = None
        self._tooltip = None
        self._type = None
        self._value = None
        self._visible = None
        self._required = None
        self._position = None

        if label is not None:
          self.label = label
        if read_only is not None:
          self.read_only = read_only
        if tooltip is not None:
          self.tooltip = tooltip
        if type is not None:
          self.type = type
        if value is not None:
          self.value = value
        if visible is not None:
          self.visible = visible
        if required is not None:
          self.required = required
        if position is not None:
          self.position = position

    @property
    def label(self):
        """
        Gets the label of this ApplicationConfigIdpEntityId.

        :return: The label of this ApplicationConfigIdpEntityId.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this ApplicationConfigIdpEntityId.

        :param label: The label of this ApplicationConfigIdpEntityId.
        :type: str
        """

        self._label = label

    @property
    def read_only(self):
        """
        Gets the read_only of this ApplicationConfigIdpEntityId.

        :return: The read_only of this ApplicationConfigIdpEntityId.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this ApplicationConfigIdpEntityId.

        :param read_only: The read_only of this ApplicationConfigIdpEntityId.
        :type: bool
        """

        self._read_only = read_only

    @property
    def tooltip(self):
        """
        Gets the tooltip of this ApplicationConfigIdpEntityId.

        :return: The tooltip of this ApplicationConfigIdpEntityId.
        :rtype: ApplicationConfigIdpEntityIdTooltip
        """
        return self._tooltip

    @tooltip.setter
    def tooltip(self, tooltip):
        """
        Sets the tooltip of this ApplicationConfigIdpEntityId.

        :param tooltip: The tooltip of this ApplicationConfigIdpEntityId.
        :type: ApplicationConfigIdpEntityIdTooltip
        """

        self._tooltip = tooltip

    @property
    def type(self):
        """
        Gets the type of this ApplicationConfigIdpEntityId.

        :return: The type of this ApplicationConfigIdpEntityId.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ApplicationConfigIdpEntityId.

        :param type: The type of this ApplicationConfigIdpEntityId.
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """
        Gets the value of this ApplicationConfigIdpEntityId.

        :return: The value of this ApplicationConfigIdpEntityId.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ApplicationConfigIdpEntityId.

        :param value: The value of this ApplicationConfigIdpEntityId.
        :type: str
        """

        self._value = value

    @property
    def visible(self):
        """
        Gets the visible of this ApplicationConfigIdpEntityId.

        :return: The visible of this ApplicationConfigIdpEntityId.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """
        Sets the visible of this ApplicationConfigIdpEntityId.

        :param visible: The visible of this ApplicationConfigIdpEntityId.
        :type: bool
        """

        self._visible = visible

    @property
    def required(self):
        """
        Gets the required of this ApplicationConfigIdpEntityId.

        :return: The required of this ApplicationConfigIdpEntityId.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this ApplicationConfigIdpEntityId.

        :param required: The required of this ApplicationConfigIdpEntityId.
        :type: bool
        """

        self._required = required

    @property
    def position(self):
        """
        Gets the position of this ApplicationConfigIdpEntityId.

        :return: The position of this ApplicationConfigIdpEntityId.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this ApplicationConfigIdpEntityId.

        :param position: The position of this ApplicationConfigIdpEntityId.
        :type: int
        """

        self._position = position

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
        if not isinstance(other, ApplicationConfigIdpEntityId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
