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

class CardConnectGatewayRequest(object):
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
        'username': 'str',
        'password': 'str',
        'site': 'str',
        'mid': 'str'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'site': 'site',
        'mid': 'mid'
    }

    def __init__(self, username=None, password=None, site=None, mid=None):  # noqa: E501
        """CardConnectGatewayRequest - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._password = None
        self._site = None
        self._mid = None
        self.discriminator = None
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if site is not None:
            self.site = site
        if mid is not None:
            self.mid = mid

    @property
    def username(self):
        """Gets the username of this CardConnectGatewayRequest.  # noqa: E501


        :return: The username of this CardConnectGatewayRequest.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CardConnectGatewayRequest.


        :param username: The username of this CardConnectGatewayRequest.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this CardConnectGatewayRequest.  # noqa: E501


        :return: The password of this CardConnectGatewayRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CardConnectGatewayRequest.


        :param password: The password of this CardConnectGatewayRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def site(self):
        """Gets the site of this CardConnectGatewayRequest.  # noqa: E501


        :return: The site of this CardConnectGatewayRequest.  # noqa: E501
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this CardConnectGatewayRequest.


        :param site: The site of this CardConnectGatewayRequest.  # noqa: E501
        :type: str
        """

        self._site = site

    @property
    def mid(self):
        """Gets the mid of this CardConnectGatewayRequest.  # noqa: E501


        :return: The mid of this CardConnectGatewayRequest.  # noqa: E501
        :rtype: str
        """
        return self._mid

    @mid.setter
    def mid(self, mid):
        """Sets the mid of this CardConnectGatewayRequest.


        :param mid: The mid of this CardConnectGatewayRequest.  # noqa: E501
        :type: str
        """

        self._mid = mid

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
        if issubclass(CardConnectGatewayRequest, dict):
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
        if not isinstance(other, CardConnectGatewayRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other