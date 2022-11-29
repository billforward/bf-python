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

class PaymentRefundResponse(object):
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
        'payment': 'Payment',
        'refunds': 'list[Refund]',
        'invoices': 'list[Invoice]',
        'organization_id': 'str',
        'requested_amount': 'float',
        'refunded_amount': 'float',
        'amount_left_to_refund': 'float'
    }

    attribute_map = {
        'created': 'created',
        'payment': 'payment',
        'refunds': 'refunds',
        'invoices': 'invoices',
        'organization_id': 'organizationID',
        'requested_amount': 'requestedAmount',
        'refunded_amount': 'refundedAmount',
        'amount_left_to_refund': 'amountLeftToRefund'
    }

    def __init__(self, created=None, payment=None, refunds=None, invoices=None, organization_id=None, requested_amount=None, refunded_amount=None, amount_left_to_refund=None):  # noqa: E501
        """PaymentRefundResponse - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._payment = None
        self._refunds = None
        self._invoices = None
        self._organization_id = None
        self._requested_amount = None
        self._refunded_amount = None
        self._amount_left_to_refund = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if payment is not None:
            self.payment = payment
        if refunds is not None:
            self.refunds = refunds
        if invoices is not None:
            self.invoices = invoices
        if organization_id is not None:
            self.organization_id = organization_id
        if requested_amount is not None:
            self.requested_amount = requested_amount
        if refunded_amount is not None:
            self.refunded_amount = refunded_amount
        if amount_left_to_refund is not None:
            self.amount_left_to_refund = amount_left_to_refund

    @property
    def created(self):
        """Gets the created of this PaymentRefundResponse.  # noqa: E501


        :return: The created of this PaymentRefundResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PaymentRefundResponse.


        :param created: The created of this PaymentRefundResponse.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def payment(self):
        """Gets the payment of this PaymentRefundResponse.  # noqa: E501


        :return: The payment of this PaymentRefundResponse.  # noqa: E501
        :rtype: Payment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this PaymentRefundResponse.


        :param payment: The payment of this PaymentRefundResponse.  # noqa: E501
        :type: Payment
        """

        self._payment = payment

    @property
    def refunds(self):
        """Gets the refunds of this PaymentRefundResponse.  # noqa: E501


        :return: The refunds of this PaymentRefundResponse.  # noqa: E501
        :rtype: list[Refund]
        """
        return self._refunds

    @refunds.setter
    def refunds(self, refunds):
        """Sets the refunds of this PaymentRefundResponse.


        :param refunds: The refunds of this PaymentRefundResponse.  # noqa: E501
        :type: list[Refund]
        """

        self._refunds = refunds

    @property
    def invoices(self):
        """Gets the invoices of this PaymentRefundResponse.  # noqa: E501


        :return: The invoices of this PaymentRefundResponse.  # noqa: E501
        :rtype: list[Invoice]
        """
        return self._invoices

    @invoices.setter
    def invoices(self, invoices):
        """Sets the invoices of this PaymentRefundResponse.


        :param invoices: The invoices of this PaymentRefundResponse.  # noqa: E501
        :type: list[Invoice]
        """

        self._invoices = invoices

    @property
    def organization_id(self):
        """Gets the organization_id of this PaymentRefundResponse.  # noqa: E501


        :return: The organization_id of this PaymentRefundResponse.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this PaymentRefundResponse.


        :param organization_id: The organization_id of this PaymentRefundResponse.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def requested_amount(self):
        """Gets the requested_amount of this PaymentRefundResponse.  # noqa: E501


        :return: The requested_amount of this PaymentRefundResponse.  # noqa: E501
        :rtype: float
        """
        return self._requested_amount

    @requested_amount.setter
    def requested_amount(self, requested_amount):
        """Sets the requested_amount of this PaymentRefundResponse.


        :param requested_amount: The requested_amount of this PaymentRefundResponse.  # noqa: E501
        :type: float
        """

        self._requested_amount = requested_amount

    @property
    def refunded_amount(self):
        """Gets the refunded_amount of this PaymentRefundResponse.  # noqa: E501


        :return: The refunded_amount of this PaymentRefundResponse.  # noqa: E501
        :rtype: float
        """
        return self._refunded_amount

    @refunded_amount.setter
    def refunded_amount(self, refunded_amount):
        """Sets the refunded_amount of this PaymentRefundResponse.


        :param refunded_amount: The refunded_amount of this PaymentRefundResponse.  # noqa: E501
        :type: float
        """

        self._refunded_amount = refunded_amount

    @property
    def amount_left_to_refund(self):
        """Gets the amount_left_to_refund of this PaymentRefundResponse.  # noqa: E501


        :return: The amount_left_to_refund of this PaymentRefundResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount_left_to_refund

    @amount_left_to_refund.setter
    def amount_left_to_refund(self, amount_left_to_refund):
        """Sets the amount_left_to_refund of this PaymentRefundResponse.


        :param amount_left_to_refund: The amount_left_to_refund of this PaymentRefundResponse.  # noqa: E501
        :type: float
        """

        self._amount_left_to_refund = amount_left_to_refund

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
        if issubclass(PaymentRefundResponse, dict):
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
        if not isinstance(other, PaymentRefundResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
