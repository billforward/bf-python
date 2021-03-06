# coding: utf-8

"""
    BillForward REST API


    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class BFError(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, error_type=None, error_message=None, error_code=None, error_parameters=None):
        """
        BFError - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'error_type': 'str',
            'error_message': 'str',
            'error_code': 'int',
            'error_parameters': 'list[str]'
        }

        self.attribute_map = {
            'error_type': 'errorType',
            'error_message': 'errorMessage',
            'error_code': 'errorCode',
            'error_parameters': 'errorParameters'
        }

        self._error_type = error_type
        self._error_message = error_message
        self._error_code = error_code
        self._error_parameters = error_parameters

    @property
    def error_type(self):
        """
        Gets the error_type of this BFError.
        {\"description\":\"Enum categorizing the nature of the error.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :return: The error_type of this BFError.
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """
        Sets the error_type of this BFError.
        {\"description\":\"Enum categorizing the nature of the error.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :param error_type: The error_type of this BFError.
        :type: str
        """
        allowed_values = ["BFError", "ServerError", "ValidationError", "UnserializationException", "Oauth", "PermissionsError", "PreconditionFailed", "NotImplemented", "InvocationError", "NoSuchEntity", "InconsistentState", "StripeOperationFailure", "BraintreeOperationFailure", "BraintreeValidationError", "SagePayOperationFailure", "TokenizationAuthCaptureFailure", "TokenizationPreAuthFailure", "CouponException", "CouponUniqueCodesRequestException", "CouponUniqueCodesResponseException", "RemoveCouponException", "AddCouponCodeToSubscriptionRequestException", "GatewayAuthenticationError", "GatewayAuthorizationError", "GatewayResourceNotFoundError", "GatewayProtocolVersionError", "GatewayInternalError", "GatewayDownTemporarilyError", "GatewayUnexpectedError", "GatewayUnhandledError", "GatewaySDKUnhandledError"]
        if error_type not in allowed_values:
            raise ValueError(
                "Invalid value for `error_type` ({0}), must be one of {1}"
                .format(error_type, allowed_values)
            )

        self._error_type = error_type

    @property
    def error_message(self):
        """
        Gets the error_message of this BFError.
        {\"description\":\"Human-readable description of the reason for the error.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :return: The error_message of this BFError.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this BFError.
        {\"description\":\"Human-readable description of the reason for the error.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :param error_message: The error_message of this BFError.
        :type: str
        """

        self._error_message = error_message

    @property
    def error_code(self):
        """
        Gets the error_code of this BFError.
        {\"description\":\"Code describing the nature of the error. Currently unused; prefer `errorType`.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :return: The error_code of this BFError.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this BFError.
        {\"description\":\"Code describing the nature of the error. Currently unused; prefer `errorType`.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :param error_code: The error_code of this BFError.
        :type: int
        """

        self._error_code = error_code

    @property
    def error_parameters(self):
        """
        Gets the error_parameters of this BFError.
        {\"description\":\"List of erroneous parameters found in your input (if applicable).\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :return: The error_parameters of this BFError.
        :rtype: list[str]
        """
        return self._error_parameters

    @error_parameters.setter
    def error_parameters(self, error_parameters):
        """
        Sets the error_parameters of this BFError.
        {\"description\":\"List of erroneous parameters found in your input (if applicable).\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :param error_parameters: The error_parameters of this BFError.
        :type: list[str]
        """

        self._error_parameters = error_parameters

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
