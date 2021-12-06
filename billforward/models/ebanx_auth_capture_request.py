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

class EBANXAuthCaptureRequest(AuthCaptureRequest):
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
        'token': 'str',
        'expiry': 'str',
        'eft_code': 'str',
        'payment_type_code': 'str',
        'masked_card_number': 'str'
    }
    if hasattr(AuthCaptureRequest, "swagger_types"):
        swagger_types.update(AuthCaptureRequest.swagger_types)

    attribute_map = {
        'token': 'token',
        'expiry': 'expiry',
        'eft_code': 'eftCode',
        'payment_type_code': 'paymentTypeCode',
        'masked_card_number': 'maskedCardNumber'
    }
    if hasattr(AuthCaptureRequest, "attribute_map"):
        attribute_map.update(AuthCaptureRequest.attribute_map)

    def __init__(self, token=None, expiry=None, eft_code=None, payment_type_code=None, masked_card_number=None, *args, **kwargs):  # noqa: E501
        """EBANXAuthCaptureRequest - a model defined in Swagger"""  # noqa: E501
        self._token = None
        self._expiry = None
        self._eft_code = None
        self._payment_type_code = None
        self._masked_card_number = None
        self.discriminator = None
        if token is not None:
            self.token = token
        if expiry is not None:
            self.expiry = expiry
        if eft_code is not None:
            self.eft_code = eft_code
        if payment_type_code is not None:
            self.payment_type_code = payment_type_code
        if masked_card_number is not None:
            self.masked_card_number = masked_card_number
        AuthCaptureRequest.__init__(self, *args, **kwargs)

    @property
    def token(self):
        """Gets the token of this EBANXAuthCaptureRequest.  # noqa: E501


        :return: The token of this EBANXAuthCaptureRequest.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this EBANXAuthCaptureRequest.


        :param token: The token of this EBANXAuthCaptureRequest.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def expiry(self):
        """Gets the expiry of this EBANXAuthCaptureRequest.  # noqa: E501


        :return: The expiry of this EBANXAuthCaptureRequest.  # noqa: E501
        :rtype: str
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this EBANXAuthCaptureRequest.


        :param expiry: The expiry of this EBANXAuthCaptureRequest.  # noqa: E501
        :type: str
        """

        self._expiry = expiry

    @property
    def eft_code(self):
        """Gets the eft_code of this EBANXAuthCaptureRequest.  # noqa: E501


        :return: The eft_code of this EBANXAuthCaptureRequest.  # noqa: E501
        :rtype: str
        """
        return self._eft_code

    @eft_code.setter
    def eft_code(self, eft_code):
        """Sets the eft_code of this EBANXAuthCaptureRequest.


        :param eft_code: The eft_code of this EBANXAuthCaptureRequest.  # noqa: E501
        :type: str
        """

        self._eft_code = eft_code

    @property
    def payment_type_code(self):
        """Gets the payment_type_code of this EBANXAuthCaptureRequest.  # noqa: E501


        :return: The payment_type_code of this EBANXAuthCaptureRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_type_code

    @payment_type_code.setter
    def payment_type_code(self, payment_type_code):
        """Sets the payment_type_code of this EBANXAuthCaptureRequest.


        :param payment_type_code: The payment_type_code of this EBANXAuthCaptureRequest.  # noqa: E501
        :type: str
        """

        self._payment_type_code = payment_type_code

    @property
    def masked_card_number(self):
        """Gets the masked_card_number of this EBANXAuthCaptureRequest.  # noqa: E501


        :return: The masked_card_number of this EBANXAuthCaptureRequest.  # noqa: E501
        :rtype: str
        """
        return self._masked_card_number

    @masked_card_number.setter
    def masked_card_number(self, masked_card_number):
        """Sets the masked_card_number of this EBANXAuthCaptureRequest.


        :param masked_card_number: The masked_card_number of this EBANXAuthCaptureRequest.  # noqa: E501
        :type: str
        """

        self._masked_card_number = masked_card_number

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
        if issubclass(EBANXAuthCaptureRequest, dict):
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
        if not isinstance(other, EBANXAuthCaptureRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other