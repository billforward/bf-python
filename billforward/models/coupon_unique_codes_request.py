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


class CouponUniqueCodesRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, changed_by=None, organization_id=None, quantity=None):
        """
        CouponUniqueCodesRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'changed_by': 'str',
            'organization_id': 'str',
            'quantity': 'int'
        }

        self.attribute_map = {
            'created': 'created',
            'changed_by': 'changedBy',
            'organization_id': 'organizationID',
            'quantity': 'quantity'
        }

        self._created = created
        self._changed_by = changed_by
        self._organization_id = organization_id
        self._quantity = quantity

    @property
    def created(self):
        """
        Gets the created of this CouponUniqueCodesRequest.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this CouponUniqueCodesRequest.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this CouponUniqueCodesRequest.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this CouponUniqueCodesRequest.
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """
        Gets the changed_by of this CouponUniqueCodesRequest.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :return: The changed_by of this CouponUniqueCodesRequest.
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """
        Sets the changed_by of this CouponUniqueCodesRequest.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :param changed_by: The changed_by of this CouponUniqueCodesRequest.
        :type: str
        """

        self._changed_by = changed_by

    @property
    def organization_id(self):
        """
        Gets the organization_id of this CouponUniqueCodesRequest.
        { \"description\" : \"\", \"verbs\":[\"POST\"] }

        :return: The organization_id of this CouponUniqueCodesRequest.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this CouponUniqueCodesRequest.
        { \"description\" : \"\", \"verbs\":[\"POST\"] }

        :param organization_id: The organization_id of this CouponUniqueCodesRequest.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def quantity(self):
        """
        Gets the quantity of this CouponUniqueCodesRequest.
        { \"description\" : \"The number of unique codes that will be returned.\", \"verbs\":[\"POST\"] }

        :return: The quantity of this CouponUniqueCodesRequest.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this CouponUniqueCodesRequest.
        { \"description\" : \"The number of unique codes that will be returned.\", \"verbs\":[\"POST\"] }

        :param quantity: The quantity of this CouponUniqueCodesRequest.
        :type: int
        """

        self._quantity = quantity

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
