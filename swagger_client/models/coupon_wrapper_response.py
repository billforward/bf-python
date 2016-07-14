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


class CouponWrapperResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, coupon_code=None, discount=None, discount_excluding_tax=None, calculation=None, pricing_component_name=None, pricing_component_id=None):
        """
        CouponWrapperResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'coupon_code': 'str',
            'discount': 'float',
            'discount_excluding_tax': 'float',
            'calculation': 'str',
            'pricing_component_name': 'str',
            'pricing_component_id': 'str'
        }

        self.attribute_map = {
            'coupon_code': 'couponCode',
            'discount': 'discount',
            'discount_excluding_tax': 'discountExcludingTax',
            'calculation': 'calculation',
            'pricing_component_name': 'pricingComponentName',
            'pricing_component_id': 'pricingComponentID'
        }

        self._coupon_code = coupon_code
        self._discount = discount
        self._discount_excluding_tax = discount_excluding_tax
        self._calculation = calculation
        self._pricing_component_name = pricing_component_name
        self._pricing_component_id = pricing_component_id

    @property
    def coupon_code(self):
        """
        Gets the coupon_code of this CouponWrapperResponse.
        {\"description\":\"Code of the coupon applied.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The coupon_code of this CouponWrapperResponse.
        :rtype: str
        """
        return self._coupon_code

    @coupon_code.setter
    def coupon_code(self, coupon_code):
        """
        Sets the coupon_code of this CouponWrapperResponse.
        {\"description\":\"Code of the coupon applied.\",\"verbs\":[\"POST\",\"GET\"]}

        :param coupon_code: The coupon_code of this CouponWrapperResponse.
        :type: str
        """

        self._coupon_code = coupon_code

    @property
    def discount(self):
        """
        Gets the discount of this CouponWrapperResponse.
        {\"description\":\"Discount &mdash; including tax &mdash; contributed to the cost of the pricing component, due to application of coupon.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The discount of this CouponWrapperResponse.
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """
        Sets the discount of this CouponWrapperResponse.
        {\"description\":\"Discount &mdash; including tax &mdash; contributed to the cost of the pricing component, due to application of coupon.\",\"verbs\":[\"POST\",\"GET\"]}

        :param discount: The discount of this CouponWrapperResponse.
        :type: float
        """

        self._discount = discount

    @property
    def discount_excluding_tax(self):
        """
        Gets the discount_excluding_tax of this CouponWrapperResponse.
        {\"description\":\"Discount &mdash; excluding tax &mdash; contributed to the cost of the pricing component, due to application of coupon.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The discount_excluding_tax of this CouponWrapperResponse.
        :rtype: float
        """
        return self._discount_excluding_tax

    @discount_excluding_tax.setter
    def discount_excluding_tax(self, discount_excluding_tax):
        """
        Sets the discount_excluding_tax of this CouponWrapperResponse.
        {\"description\":\"Discount &mdash; excluding tax &mdash; contributed to the cost of the pricing component, due to application of coupon.\",\"verbs\":[\"POST\",\"GET\"]}

        :param discount_excluding_tax: The discount_excluding_tax of this CouponWrapperResponse.
        :type: float
        """

        self._discount_excluding_tax = discount_excluding_tax

    @property
    def calculation(self):
        """
        Gets the calculation of this CouponWrapperResponse.
        {\"description\":\"Friendly text describing the calculation performed in applying the coupon.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The calculation of this CouponWrapperResponse.
        :rtype: str
        """
        return self._calculation

    @calculation.setter
    def calculation(self, calculation):
        """
        Sets the calculation of this CouponWrapperResponse.
        {\"description\":\"Friendly text describing the calculation performed in applying the coupon.\",\"verbs\":[\"POST\",\"GET\"]}

        :param calculation: The calculation of this CouponWrapperResponse.
        :type: str
        """

        self._calculation = calculation

    @property
    def pricing_component_name(self):
        """
        Gets the pricing_component_name of this CouponWrapperResponse.
        {\"description\":\"Name of the pricing component to whom the coupon was applied.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The pricing_component_name of this CouponWrapperResponse.
        :rtype: str
        """
        return self._pricing_component_name

    @pricing_component_name.setter
    def pricing_component_name(self, pricing_component_name):
        """
        Sets the pricing_component_name of this CouponWrapperResponse.
        {\"description\":\"Name of the pricing component to whom the coupon was applied.\",\"verbs\":[\"POST\",\"GET\"]}

        :param pricing_component_name: The pricing_component_name of this CouponWrapperResponse.
        :type: str
        """

        self._pricing_component_name = pricing_component_name

    @property
    def pricing_component_id(self):
        """
        Gets the pricing_component_id of this CouponWrapperResponse.
        {\"description\":\"ID of the pricing component to whom the coupon was applied.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The pricing_component_id of this CouponWrapperResponse.
        :rtype: str
        """
        return self._pricing_component_id

    @pricing_component_id.setter
    def pricing_component_id(self, pricing_component_id):
        """
        Sets the pricing_component_id of this CouponWrapperResponse.
        {\"description\":\"ID of the pricing component to whom the coupon was applied.\",\"verbs\":[\"POST\",\"GET\"]}

        :param pricing_component_id: The pricing_component_id of this CouponWrapperResponse.
        :type: str
        """

        self._pricing_component_id = pricing_component_id

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
