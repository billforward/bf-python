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

class PublicConfigurationResponse(object):
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
        'square_app_id': 'str',
        'square_o_auth_url': 'str',
        'stripe_client_id': 'str'
    }

    attribute_map = {
        'square_app_id': 'squareAppID',
        'square_o_auth_url': 'squareOAuthUrl',
        'stripe_client_id': 'stripeClientId'
    }

    def __init__(self, square_app_id=None, square_o_auth_url=None, stripe_client_id=None):  # noqa: E501
        """PublicConfigurationResponse - a model defined in Swagger"""  # noqa: E501
        self._square_app_id = None
        self._square_o_auth_url = None
        self._stripe_client_id = None
        self.discriminator = None
        if square_app_id is not None:
            self.square_app_id = square_app_id
        if square_o_auth_url is not None:
            self.square_o_auth_url = square_o_auth_url
        if stripe_client_id is not None:
            self.stripe_client_id = stripe_client_id

    @property
    def square_app_id(self):
        """Gets the square_app_id of this PublicConfigurationResponse.  # noqa: E501


        :return: The square_app_id of this PublicConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._square_app_id

    @square_app_id.setter
    def square_app_id(self, square_app_id):
        """Sets the square_app_id of this PublicConfigurationResponse.


        :param square_app_id: The square_app_id of this PublicConfigurationResponse.  # noqa: E501
        :type: str
        """

        self._square_app_id = square_app_id

    @property
    def square_o_auth_url(self):
        """Gets the square_o_auth_url of this PublicConfigurationResponse.  # noqa: E501


        :return: The square_o_auth_url of this PublicConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._square_o_auth_url

    @square_o_auth_url.setter
    def square_o_auth_url(self, square_o_auth_url):
        """Sets the square_o_auth_url of this PublicConfigurationResponse.


        :param square_o_auth_url: The square_o_auth_url of this PublicConfigurationResponse.  # noqa: E501
        :type: str
        """

        self._square_o_auth_url = square_o_auth_url

    @property
    def stripe_client_id(self):
        """Gets the stripe_client_id of this PublicConfigurationResponse.  # noqa: E501


        :return: The stripe_client_id of this PublicConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._stripe_client_id

    @stripe_client_id.setter
    def stripe_client_id(self, stripe_client_id):
        """Sets the stripe_client_id of this PublicConfigurationResponse.


        :param stripe_client_id: The stripe_client_id of this PublicConfigurationResponse.  # noqa: E501
        :type: str
        """

        self._stripe_client_id = stripe_client_id

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
        if issubclass(PublicConfigurationResponse, dict):
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
        if not isinstance(other, PublicConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
