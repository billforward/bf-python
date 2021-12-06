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

class CalculatorResult(object):
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
        'value': 'float',
        'commission_structure': 'CommissionStructure'
    }

    attribute_map = {
        'value': 'value',
        'commission_structure': 'commissionStructure'
    }

    def __init__(self, value=None, commission_structure=None):  # noqa: E501
        """CalculatorResult - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._commission_structure = None
        self.discriminator = None
        if value is not None:
            self.value = value
        if commission_structure is not None:
            self.commission_structure = commission_structure

    @property
    def value(self):
        """Gets the value of this CalculatorResult.  # noqa: E501


        :return: The value of this CalculatorResult.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CalculatorResult.


        :param value: The value of this CalculatorResult.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def commission_structure(self):
        """Gets the commission_structure of this CalculatorResult.  # noqa: E501


        :return: The commission_structure of this CalculatorResult.  # noqa: E501
        :rtype: CommissionStructure
        """
        return self._commission_structure

    @commission_structure.setter
    def commission_structure(self, commission_structure):
        """Sets the commission_structure of this CalculatorResult.


        :param commission_structure: The commission_structure of this CalculatorResult.  # noqa: E501
        :type: CommissionStructure
        """

        self._commission_structure = commission_structure

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
        if issubclass(CalculatorResult, dict):
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
        if not isinstance(other, CalculatorResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
