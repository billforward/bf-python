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

class EBANXGatewayRequest(object):
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
        'integration_key': 'str',
        'public_integration_key': 'str',
        'production': 'bool'
    }

    attribute_map = {
        'integration_key': 'integrationKey',
        'public_integration_key': 'publicIntegrationKey',
        'production': 'production'
    }

    def __init__(self, integration_key=None, public_integration_key=None, production=None):  # noqa: E501
        """EBANXGatewayRequest - a model defined in Swagger"""  # noqa: E501
        self._integration_key = None
        self._public_integration_key = None
        self._production = None
        self.discriminator = None
        if integration_key is not None:
            self.integration_key = integration_key
        if public_integration_key is not None:
            self.public_integration_key = public_integration_key
        if production is not None:
            self.production = production

    @property
    def integration_key(self):
        """Gets the integration_key of this EBANXGatewayRequest.  # noqa: E501


        :return: The integration_key of this EBANXGatewayRequest.  # noqa: E501
        :rtype: str
        """
        return self._integration_key

    @integration_key.setter
    def integration_key(self, integration_key):
        """Sets the integration_key of this EBANXGatewayRequest.


        :param integration_key: The integration_key of this EBANXGatewayRequest.  # noqa: E501
        :type: str
        """

        self._integration_key = integration_key

    @property
    def public_integration_key(self):
        """Gets the public_integration_key of this EBANXGatewayRequest.  # noqa: E501


        :return: The public_integration_key of this EBANXGatewayRequest.  # noqa: E501
        :rtype: str
        """
        return self._public_integration_key

    @public_integration_key.setter
    def public_integration_key(self, public_integration_key):
        """Sets the public_integration_key of this EBANXGatewayRequest.


        :param public_integration_key: The public_integration_key of this EBANXGatewayRequest.  # noqa: E501
        :type: str
        """

        self._public_integration_key = public_integration_key

    @property
    def production(self):
        """Gets the production of this EBANXGatewayRequest.  # noqa: E501


        :return: The production of this EBANXGatewayRequest.  # noqa: E501
        :rtype: bool
        """
        return self._production

    @production.setter
    def production(self, production):
        """Sets the production of this EBANXGatewayRequest.


        :param production: The production of this EBANXGatewayRequest.  # noqa: E501
        :type: bool
        """

        self._production = production

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
        if issubclass(EBANXGatewayRequest, dict):
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
        if not isinstance(other, EBANXGatewayRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other