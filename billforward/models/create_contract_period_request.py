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

class CreateContractPeriodRequest(object):
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
        'organization_id': 'str',
        'contract_period': 'int',
        'subscription_periods': 'int',
        'quote_id': 'str',
        'purchase_order': 'str'
    }

    attribute_map = {
        'organization_id': 'organizationID',
        'contract_period': 'contractPeriod',
        'subscription_periods': 'subscriptionPeriods',
        'quote_id': 'quoteID',
        'purchase_order': 'purchaseOrder'
    }

    def __init__(self, organization_id=None, contract_period=None, subscription_periods=None, quote_id=None, purchase_order=None):  # noqa: E501
        """CreateContractPeriodRequest - a model defined in Swagger"""  # noqa: E501
        self._organization_id = None
        self._contract_period = None
        self._subscription_periods = None
        self._quote_id = None
        self._purchase_order = None
        self.discriminator = None
        if organization_id is not None:
            self.organization_id = organization_id
        if contract_period is not None:
            self.contract_period = contract_period
        if subscription_periods is not None:
            self.subscription_periods = subscription_periods
        if quote_id is not None:
            self.quote_id = quote_id
        if purchase_order is not None:
            self.purchase_order = purchase_order

    @property
    def organization_id(self):
        """Gets the organization_id of this CreateContractPeriodRequest.  # noqa: E501


        :return: The organization_id of this CreateContractPeriodRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this CreateContractPeriodRequest.


        :param organization_id: The organization_id of this CreateContractPeriodRequest.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def contract_period(self):
        """Gets the contract_period of this CreateContractPeriodRequest.  # noqa: E501


        :return: The contract_period of this CreateContractPeriodRequest.  # noqa: E501
        :rtype: int
        """
        return self._contract_period

    @contract_period.setter
    def contract_period(self, contract_period):
        """Sets the contract_period of this CreateContractPeriodRequest.


        :param contract_period: The contract_period of this CreateContractPeriodRequest.  # noqa: E501
        :type: int
        """

        self._contract_period = contract_period

    @property
    def subscription_periods(self):
        """Gets the subscription_periods of this CreateContractPeriodRequest.  # noqa: E501


        :return: The subscription_periods of this CreateContractPeriodRequest.  # noqa: E501
        :rtype: int
        """
        return self._subscription_periods

    @subscription_periods.setter
    def subscription_periods(self, subscription_periods):
        """Sets the subscription_periods of this CreateContractPeriodRequest.


        :param subscription_periods: The subscription_periods of this CreateContractPeriodRequest.  # noqa: E501
        :type: int
        """

        self._subscription_periods = subscription_periods

    @property
    def quote_id(self):
        """Gets the quote_id of this CreateContractPeriodRequest.  # noqa: E501


        :return: The quote_id of this CreateContractPeriodRequest.  # noqa: E501
        :rtype: str
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        """Sets the quote_id of this CreateContractPeriodRequest.


        :param quote_id: The quote_id of this CreateContractPeriodRequest.  # noqa: E501
        :type: str
        """

        self._quote_id = quote_id

    @property
    def purchase_order(self):
        """Gets the purchase_order of this CreateContractPeriodRequest.  # noqa: E501


        :return: The purchase_order of this CreateContractPeriodRequest.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order

    @purchase_order.setter
    def purchase_order(self, purchase_order):
        """Sets the purchase_order of this CreateContractPeriodRequest.


        :param purchase_order: The purchase_order of this CreateContractPeriodRequest.  # noqa: E501
        :type: str
        """

        self._purchase_order = purchase_order

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
        if issubclass(CreateContractPeriodRequest, dict):
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
        if not isinstance(other, CreateContractPeriodRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
