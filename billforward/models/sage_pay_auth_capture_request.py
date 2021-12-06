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

class SagePayAuthCaptureRequest(AuthCaptureRequest):
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
        'card_token': 'str',
        'card_type': 'str',
        'expiry_date': 'str',
        'last4_digits': 'str'
    }
    if hasattr(AuthCaptureRequest, "swagger_types"):
        swagger_types.update(AuthCaptureRequest.swagger_types)

    attribute_map = {
        'card_token': 'cardToken',
        'card_type': 'cardType',
        'expiry_date': 'expiryDate',
        'last4_digits': 'last4Digits'
    }
    if hasattr(AuthCaptureRequest, "attribute_map"):
        attribute_map.update(AuthCaptureRequest.attribute_map)

    def __init__(self, card_token=None, card_type=None, expiry_date=None, last4_digits=None, *args, **kwargs):  # noqa: E501
        """SagePayAuthCaptureRequest - a model defined in Swagger"""  # noqa: E501
        self._card_token = None
        self._card_type = None
        self._expiry_date = None
        self._last4_digits = None
        self.discriminator = None
        self.card_token = card_token
        if card_type is not None:
            self.card_type = card_type
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if last4_digits is not None:
            self.last4_digits = last4_digits
        AuthCaptureRequest.__init__(self, *args, **kwargs)

    @property
    def card_token(self):
        """Gets the card_token of this SagePayAuthCaptureRequest.  # noqa: E501


        :return: The card_token of this SagePayAuthCaptureRequest.  # noqa: E501
        :rtype: str
        """
        return self._card_token

    @card_token.setter
    def card_token(self, card_token):
        """Sets the card_token of this SagePayAuthCaptureRequest.


        :param card_token: The card_token of this SagePayAuthCaptureRequest.  # noqa: E501
        :type: str
        """
        if card_token is None:
            raise ValueError("Invalid value for `card_token`, must not be `None`")  # noqa: E501

        self._card_token = card_token

    @property
    def card_type(self):
        """Gets the card_type of this SagePayAuthCaptureRequest.  # noqa: E501


        :return: The card_type of this SagePayAuthCaptureRequest.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this SagePayAuthCaptureRequest.


        :param card_type: The card_type of this SagePayAuthCaptureRequest.  # noqa: E501
        :type: str
        """

        self._card_type = card_type

    @property
    def expiry_date(self):
        """Gets the expiry_date of this SagePayAuthCaptureRequest.  # noqa: E501


        :return: The expiry_date of this SagePayAuthCaptureRequest.  # noqa: E501
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this SagePayAuthCaptureRequest.


        :param expiry_date: The expiry_date of this SagePayAuthCaptureRequest.  # noqa: E501
        :type: str
        """

        self._expiry_date = expiry_date

    @property
    def last4_digits(self):
        """Gets the last4_digits of this SagePayAuthCaptureRequest.  # noqa: E501


        :return: The last4_digits of this SagePayAuthCaptureRequest.  # noqa: E501
        :rtype: str
        """
        return self._last4_digits

    @last4_digits.setter
    def last4_digits(self, last4_digits):
        """Sets the last4_digits of this SagePayAuthCaptureRequest.


        :param last4_digits: The last4_digits of this SagePayAuthCaptureRequest.  # noqa: E501
        :type: str
        """

        self._last4_digits = last4_digits

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
        if issubclass(SagePayAuthCaptureRequest, dict):
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
        if not isinstance(other, SagePayAuthCaptureRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other