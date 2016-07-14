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


class EventData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, previous_attributes=None, object=None):
        """
        EventData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'previous_attributes': 'dict(str, object)',
            'object': 'StripeObject'
        }

        self.attribute_map = {
            'previous_attributes': 'previousAttributes',
            'object': 'object'
        }

        self._previous_attributes = previous_attributes
        self._object = object

    @property
    def previous_attributes(self):
        """
        Gets the previous_attributes of this EventData.


        :return: The previous_attributes of this EventData.
        :rtype: dict(str, object)
        """
        return self._previous_attributes

    @previous_attributes.setter
    def previous_attributes(self, previous_attributes):
        """
        Sets the previous_attributes of this EventData.


        :param previous_attributes: The previous_attributes of this EventData.
        :type: dict(str, object)
        """

        self._previous_attributes = previous_attributes

    @property
    def object(self):
        """
        Gets the object of this EventData.


        :return: The object of this EventData.
        :rtype: StripeObject
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this EventData.


        :param object: The object of this EventData.
        :type: StripeObject
        """

        self._object = object

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
