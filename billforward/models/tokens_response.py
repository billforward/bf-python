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

class TokensResponse(object):
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
        'private_token': 'OAuthToken',
        'public_token': 'OAuthToken'
    }

    attribute_map = {
        'private_token': 'privateToken',
        'public_token': 'publicToken'
    }

    def __init__(self, private_token=None, public_token=None):  # noqa: E501
        """TokensResponse - a model defined in Swagger"""  # noqa: E501
        self._private_token = None
        self._public_token = None
        self.discriminator = None
        if private_token is not None:
            self.private_token = private_token
        if public_token is not None:
            self.public_token = public_token

    @property
    def private_token(self):
        """Gets the private_token of this TokensResponse.  # noqa: E501


        :return: The private_token of this TokensResponse.  # noqa: E501
        :rtype: OAuthToken
        """
        return self._private_token

    @private_token.setter
    def private_token(self, private_token):
        """Sets the private_token of this TokensResponse.


        :param private_token: The private_token of this TokensResponse.  # noqa: E501
        :type: OAuthToken
        """

        self._private_token = private_token

    @property
    def public_token(self):
        """Gets the public_token of this TokensResponse.  # noqa: E501


        :return: The public_token of this TokensResponse.  # noqa: E501
        :rtype: OAuthToken
        """
        return self._public_token

    @public_token.setter
    def public_token(self, public_token):
        """Sets the public_token of this TokensResponse.


        :param public_token: The public_token of this TokensResponse.  # noqa: E501
        :type: OAuthToken
        """

        self._public_token = public_token

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
        if issubclass(TokensResponse, dict):
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
        if not isinstance(other, TokensResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
