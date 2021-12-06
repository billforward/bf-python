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
from billforward.models.auth_capture_request import AuthCaptureRequest  # noqa: F401,E501

class CardConnectAuthCaptureRequest(AuthCaptureRequest):
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
        'tokenized_card_number': 'str',
        'expiry': 'str'
    }
    if hasattr(AuthCaptureRequest, "swagger_types"):
        swagger_types.update(AuthCaptureRequest.swagger_types)

    attribute_map = {
        'tokenized_card_number': 'tokenizedCardNumber',
        'expiry': 'expiry'
    }
    if hasattr(AuthCaptureRequest, "attribute_map"):
        attribute_map.update(AuthCaptureRequest.attribute_map)

    def __init__(self, tokenized_card_number=None, expiry=None, *args, **kwargs):  # noqa: E501
        """CardConnectAuthCaptureRequest - a model defined in Swagger"""  # noqa: E501
        self._tokenized_card_number = None
        self._expiry = None
        self.discriminator = None
        if tokenized_card_number is not None:
            self.tokenized_card_number = tokenized_card_number
        if expiry is not None:
            self.expiry = expiry
        AuthCaptureRequest.__init__(self, *args, **kwargs)

    @property
    def tokenized_card_number(self):
        """Gets the tokenized_card_number of this CardConnectAuthCaptureRequest.  # noqa: E501


        :return: The tokenized_card_number of this CardConnectAuthCaptureRequest.  # noqa: E501
        :rtype: str
        """
        return self._tokenized_card_number

    @tokenized_card_number.setter
    def tokenized_card_number(self, tokenized_card_number):
        """Sets the tokenized_card_number of this CardConnectAuthCaptureRequest.


        :param tokenized_card_number: The tokenized_card_number of this CardConnectAuthCaptureRequest.  # noqa: E501
        :type: str
        """

        self._tokenized_card_number = tokenized_card_number

    @property
    def expiry(self):
        """Gets the expiry of this CardConnectAuthCaptureRequest.  # noqa: E501


        :return: The expiry of this CardConnectAuthCaptureRequest.  # noqa: E501
        :rtype: str
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this CardConnectAuthCaptureRequest.


        :param expiry: The expiry of this CardConnectAuthCaptureRequest.  # noqa: E501
        :type: str
        """

        self._expiry = expiry

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
        if issubclass(CardConnectAuthCaptureRequest, dict):
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
        if not isinstance(other, CardConnectAuthCaptureRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other