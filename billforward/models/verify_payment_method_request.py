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

class VerifyPaymentMethodRequest(object):
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
        'created': 'datetime',
        'amounts': 'list[int]',
        'organization_id': 'str'
    }

    attribute_map = {
        'created': 'created',
        'amounts': 'amounts',
        'organization_id': 'organizationID'
    }

    def __init__(self, created=None, amounts=None, organization_id=None):  # noqa: E501
        """VerifyPaymentMethodRequest - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._amounts = None
        self._organization_id = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if amounts is not None:
            self.amounts = amounts
        if organization_id is not None:
            self.organization_id = organization_id

    @property
    def created(self):
        """Gets the created of this VerifyPaymentMethodRequest.  # noqa: E501


        :return: The created of this VerifyPaymentMethodRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this VerifyPaymentMethodRequest.


        :param created: The created of this VerifyPaymentMethodRequest.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def amounts(self):
        """Gets the amounts of this VerifyPaymentMethodRequest.  # noqa: E501


        :return: The amounts of this VerifyPaymentMethodRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._amounts

    @amounts.setter
    def amounts(self, amounts):
        """Sets the amounts of this VerifyPaymentMethodRequest.


        :param amounts: The amounts of this VerifyPaymentMethodRequest.  # noqa: E501
        :type: list[int]
        """

        self._amounts = amounts

    @property
    def organization_id(self):
        """Gets the organization_id of this VerifyPaymentMethodRequest.  # noqa: E501


        :return: The organization_id of this VerifyPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this VerifyPaymentMethodRequest.


        :param organization_id: The organization_id of this VerifyPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

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
        if issubclass(VerifyPaymentMethodRequest, dict):
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
        if not isinstance(other, VerifyPaymentMethodRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other