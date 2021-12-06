# coding: utf-8

"""
    Billforward API

    This is documentation for the Billforward API. You can find out more at billforward.io.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: team@billforward.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserTimezone(object):
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
        'display_name': 'str',
        'id': 'str',
        'dstsavings': 'int',
        'raw_offset': 'int'
    }

    attribute_map = {
        'display_name': 'displayName',
        'id': 'id',
        'dstsavings': 'dstsavings',
        'raw_offset': 'rawOffset'
    }

    def __init__(self, display_name=None, id=None, dstsavings=None, raw_offset=None):  # noqa: E501
        """UserTimezone - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._id = None
        self._dstsavings = None
        self._raw_offset = None
        self.discriminator = None
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if dstsavings is not None:
            self.dstsavings = dstsavings
        if raw_offset is not None:
            self.raw_offset = raw_offset

    @property
    def display_name(self):
        """Gets the display_name of this UserTimezone.  # noqa: E501


        :return: The display_name of this UserTimezone.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UserTimezone.


        :param display_name: The display_name of this UserTimezone.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this UserTimezone.  # noqa: E501


        :return: The id of this UserTimezone.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserTimezone.


        :param id: The id of this UserTimezone.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def dstsavings(self):
        """Gets the dstsavings of this UserTimezone.  # noqa: E501


        :return: The dstsavings of this UserTimezone.  # noqa: E501
        :rtype: int
        """
        return self._dstsavings

    @dstsavings.setter
    def dstsavings(self, dstsavings):
        """Sets the dstsavings of this UserTimezone.


        :param dstsavings: The dstsavings of this UserTimezone.  # noqa: E501
        :type: int
        """

        self._dstsavings = dstsavings

    @property
    def raw_offset(self):
        """Gets the raw_offset of this UserTimezone.  # noqa: E501


        :return: The raw_offset of this UserTimezone.  # noqa: E501
        :rtype: int
        """
        return self._raw_offset

    @raw_offset.setter
    def raw_offset(self, raw_offset):
        """Sets the raw_offset of this UserTimezone.


        :param raw_offset: The raw_offset of this UserTimezone.  # noqa: E501
        :type: int
        """

        self._raw_offset = raw_offset

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
        if issubclass(UserTimezone, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserTimezone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other