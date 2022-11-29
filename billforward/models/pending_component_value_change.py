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

class PendingComponentValueChange(object):
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
        'value': 'int',
        'at': 'datetime',
        'discard_url': 'str',
        'discard_http_verb': 'str'
    }

    attribute_map = {
        'value': 'value',
        'at': 'at',
        'discard_url': 'discardUrl',
        'discard_http_verb': 'discardHttpVerb'
    }

    def __init__(self, value=None, at=None, discard_url=None, discard_http_verb=None):  # noqa: E501
        """PendingComponentValueChange - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._at = None
        self._discard_url = None
        self._discard_http_verb = None
        self.discriminator = None
        if value is not None:
            self.value = value
        if at is not None:
            self.at = at
        if discard_url is not None:
            self.discard_url = discard_url
        if discard_http_verb is not None:
            self.discard_http_verb = discard_http_verb

    @property
    def value(self):
        """Gets the value of this PendingComponentValueChange.  # noqa: E501


        :return: The value of this PendingComponentValueChange.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PendingComponentValueChange.


        :param value: The value of this PendingComponentValueChange.  # noqa: E501
        :type: int
        """

        self._value = value

    @property
    def at(self):
        """Gets the at of this PendingComponentValueChange.  # noqa: E501


        :return: The at of this PendingComponentValueChange.  # noqa: E501
        :rtype: datetime
        """
        return self._at

    @at.setter
    def at(self, at):
        """Sets the at of this PendingComponentValueChange.


        :param at: The at of this PendingComponentValueChange.  # noqa: E501
        :type: datetime
        """

        self._at = at

    @property
    def discard_url(self):
        """Gets the discard_url of this PendingComponentValueChange.  # noqa: E501


        :return: The discard_url of this PendingComponentValueChange.  # noqa: E501
        :rtype: str
        """
        return self._discard_url

    @discard_url.setter
    def discard_url(self, discard_url):
        """Sets the discard_url of this PendingComponentValueChange.


        :param discard_url: The discard_url of this PendingComponentValueChange.  # noqa: E501
        :type: str
        """

        self._discard_url = discard_url

    @property
    def discard_http_verb(self):
        """Gets the discard_http_verb of this PendingComponentValueChange.  # noqa: E501


        :return: The discard_http_verb of this PendingComponentValueChange.  # noqa: E501
        :rtype: str
        """
        return self._discard_http_verb

    @discard_http_verb.setter
    def discard_http_verb(self, discard_http_verb):
        """Sets the discard_http_verb of this PendingComponentValueChange.


        :param discard_http_verb: The discard_http_verb of this PendingComponentValueChange.  # noqa: E501
        :type: str
        """

        self._discard_http_verb = discard_http_verb

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
        if issubclass(PendingComponentValueChange, dict):
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
        if not isinstance(other, PendingComponentValueChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
