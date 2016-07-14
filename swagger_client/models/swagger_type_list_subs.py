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


class SwaggerTypeListSubs(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, credit_subscription_request=None, add_payment_method_request=None):
        """
        SwaggerTypeListSubs - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'credit_subscription_request': 'CreditSubscriptionRequest',
            'add_payment_method_request': 'AddPaymentMethodRequest'
        }

        self.attribute_map = {
            'credit_subscription_request': 'creditSubscriptionRequest',
            'add_payment_method_request': 'addPaymentMethodRequest'
        }

        self._credit_subscription_request = credit_subscription_request
        self._add_payment_method_request = add_payment_method_request

    @property
    def credit_subscription_request(self):
        """
        Gets the credit_subscription_request of this SwaggerTypeListSubs.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The credit_subscription_request of this SwaggerTypeListSubs.
        :rtype: CreditSubscriptionRequest
        """
        return self._credit_subscription_request

    @credit_subscription_request.setter
    def credit_subscription_request(self, credit_subscription_request):
        """
        Sets the credit_subscription_request of this SwaggerTypeListSubs.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param credit_subscription_request: The credit_subscription_request of this SwaggerTypeListSubs.
        :type: CreditSubscriptionRequest
        """

        self._credit_subscription_request = credit_subscription_request

    @property
    def add_payment_method_request(self):
        """
        Gets the add_payment_method_request of this SwaggerTypeListSubs.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The add_payment_method_request of this SwaggerTypeListSubs.
        :rtype: AddPaymentMethodRequest
        """
        return self._add_payment_method_request

    @add_payment_method_request.setter
    def add_payment_method_request(self, add_payment_method_request):
        """
        Sets the add_payment_method_request of this SwaggerTypeListSubs.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param add_payment_method_request: The add_payment_method_request of this SwaggerTypeListSubs.
        :type: AddPaymentMethodRequest
        """

        self._add_payment_method_request = add_payment_method_request

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