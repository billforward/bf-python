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


class UnitDiscount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, unit_value=None, tier_id=None, unaltered_value=None, discount_value=None):
        """
        UnitDiscount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'unit_value': 'int',
            'tier_id': 'str',
            'unaltered_value': 'float',
            'discount_value': 'float'
        }

        self.attribute_map = {
            'unit_value': 'unitValue',
            'tier_id': 'tierID',
            'unaltered_value': 'unalteredValue',
            'discount_value': 'discountValue'
        }

        self._unit_value = unit_value
        self._tier_id = tier_id
        self._unaltered_value = unaltered_value
        self._discount_value = discount_value

    @property
    def unit_value(self):
        """
        Gets the unit_value of this UnitDiscount.


        :return: The unit_value of this UnitDiscount.
        :rtype: int
        """
        return self._unit_value

    @unit_value.setter
    def unit_value(self, unit_value):
        """
        Sets the unit_value of this UnitDiscount.


        :param unit_value: The unit_value of this UnitDiscount.
        :type: int
        """

        self._unit_value = unit_value

    @property
    def tier_id(self):
        """
        Gets the tier_id of this UnitDiscount.


        :return: The tier_id of this UnitDiscount.
        :rtype: str
        """
        return self._tier_id

    @tier_id.setter
    def tier_id(self, tier_id):
        """
        Sets the tier_id of this UnitDiscount.


        :param tier_id: The tier_id of this UnitDiscount.
        :type: str
        """

        self._tier_id = tier_id

    @property
    def unaltered_value(self):
        """
        Gets the unaltered_value of this UnitDiscount.


        :return: The unaltered_value of this UnitDiscount.
        :rtype: float
        """
        return self._unaltered_value

    @unaltered_value.setter
    def unaltered_value(self, unaltered_value):
        """
        Sets the unaltered_value of this UnitDiscount.


        :param unaltered_value: The unaltered_value of this UnitDiscount.
        :type: float
        """

        self._unaltered_value = unaltered_value

    @property
    def discount_value(self):
        """
        Gets the discount_value of this UnitDiscount.


        :return: The discount_value of this UnitDiscount.
        :rtype: float
        """
        return self._discount_value

    @discount_value.setter
    def discount_value(self, discount_value):
        """
        Sets the discount_value of this UnitDiscount.


        :param discount_value: The discount_value of this UnitDiscount.
        :type: float
        """

        self._discount_value = discount_value

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
