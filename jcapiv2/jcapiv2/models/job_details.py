# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JobDetails(object):
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
        'admin_id': 'str',
        'work_units_count': 'int',
        'name': 'str',
        'status': 'str',
        'meta': 'object',
        'updated_at': 'str',
        'persisted_fields': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'admin_id': 'adminId',
        'work_units_count': 'workUnitsCount',
        'name': 'name',
        'status': 'status',
        'meta': 'meta',
        'updated_at': 'updatedAt',
        'persisted_fields': 'persistedFields'
    }

    def __init__(self, id=None, admin_id=None, work_units_count=None, name=None, status=None, meta=None, updated_at=None, persisted_fields=None):  # noqa: E501
        """JobDetails - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._admin_id = None
        self._work_units_count = None
        self._name = None
        self._status = None
        self._meta = None
        self._updated_at = None
        self._persisted_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if admin_id is not None:
            self.admin_id = admin_id
        if work_units_count is not None:
            self.work_units_count = work_units_count
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if meta is not None:
            self.meta = meta
        if updated_at is not None:
            self.updated_at = updated_at
        if persisted_fields is not None:
            self.persisted_fields = persisted_fields

    @property
    def id(self):
        """Gets the id of this JobDetails.  # noqa: E501


        :return: The id of this JobDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobDetails.


        :param id: The id of this JobDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def admin_id(self):
        """Gets the admin_id of this JobDetails.  # noqa: E501


        :return: The admin_id of this JobDetails.  # noqa: E501
        :rtype: str
        """
        return self._admin_id

    @admin_id.setter
    def admin_id(self, admin_id):
        """Sets the admin_id of this JobDetails.


        :param admin_id: The admin_id of this JobDetails.  # noqa: E501
        :type: str
        """

        self._admin_id = admin_id

    @property
    def work_units_count(self):
        """Gets the work_units_count of this JobDetails.  # noqa: E501


        :return: The work_units_count of this JobDetails.  # noqa: E501
        :rtype: int
        """
        return self._work_units_count

    @work_units_count.setter
    def work_units_count(self, work_units_count):
        """Sets the work_units_count of this JobDetails.


        :param work_units_count: The work_units_count of this JobDetails.  # noqa: E501
        :type: int
        """

        self._work_units_count = work_units_count

    @property
    def name(self):
        """Gets the name of this JobDetails.  # noqa: E501


        :return: The name of this JobDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobDetails.


        :param name: The name of this JobDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this JobDetails.  # noqa: E501


        :return: The status of this JobDetails.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobDetails.


        :param status: The status of this JobDetails.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def meta(self):
        """Gets the meta of this JobDetails.  # noqa: E501


        :return: The meta of this JobDetails.  # noqa: E501
        :rtype: object
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this JobDetails.


        :param meta: The meta of this JobDetails.  # noqa: E501
        :type: object
        """

        self._meta = meta

    @property
    def updated_at(self):
        """Gets the updated_at of this JobDetails.  # noqa: E501


        :return: The updated_at of this JobDetails.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this JobDetails.


        :param updated_at: The updated_at of this JobDetails.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def persisted_fields(self):
        """Gets the persisted_fields of this JobDetails.  # noqa: E501


        :return: The persisted_fields of this JobDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._persisted_fields

    @persisted_fields.setter
    def persisted_fields(self, persisted_fields):
        """Sets the persisted_fields of this JobDetails.


        :param persisted_fields: The persisted_fields of this JobDetails.  # noqa: E501
        :type: list[str]
        """

        self._persisted_fields = persisted_fields

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
        if not isinstance(other, JobDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
