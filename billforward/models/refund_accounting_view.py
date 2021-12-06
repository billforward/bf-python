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

class RefundAccountingView(object):
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
        'id': 'str',
        'actual_refunded_value': 'float',
        'refund_completed': 'datetime',
        'currency': 'CreditNoteCurrency',
        'account_id': 'str',
        'reason': 'str',
        'nominal_value': 'float',
        'actual_value': 'float',
        'nominal_refunded_value': 'float',
        'refund_type': 'str',
        'refund_nature': 'str',
        'payment_method_id': 'str',
        'invoice_payment_id': 'str',
        'original_payment_id': 'str',
        'refund_payment_id': 'str',
        'invoice_id': 'str',
        'receipt_id': 'str',
        'original_receipt_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'actual_refunded_value': 'actualRefundedValue',
        'refund_completed': 'refundCompleted',
        'currency': 'currency',
        'account_id': 'accountID',
        'reason': 'reason',
        'nominal_value': 'nominalValue',
        'actual_value': 'actualValue',
        'nominal_refunded_value': 'nominalRefundedValue',
        'refund_type': 'refundType',
        'refund_nature': 'refundNature',
        'payment_method_id': 'paymentMethodID',
        'invoice_payment_id': 'invoicePaymentID',
        'original_payment_id': 'originalPaymentID',
        'refund_payment_id': 'refundPaymentID',
        'invoice_id': 'invoiceID',
        'receipt_id': 'receiptID',
        'original_receipt_id': 'originalReceiptID'
    }

    def __init__(self, id=None, actual_refunded_value=None, refund_completed=None, currency=None, account_id=None, reason=None, nominal_value=None, actual_value=None, nominal_refunded_value=None, refund_type=None, refund_nature=None, payment_method_id=None, invoice_payment_id=None, original_payment_id=None, refund_payment_id=None, invoice_id=None, receipt_id=None, original_receipt_id=None):  # noqa: E501
        """RefundAccountingView - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._actual_refunded_value = None
        self._refund_completed = None
        self._currency = None
        self._account_id = None
        self._reason = None
        self._nominal_value = None
        self._actual_value = None
        self._nominal_refunded_value = None
        self._refund_type = None
        self._refund_nature = None
        self._payment_method_id = None
        self._invoice_payment_id = None
        self._original_payment_id = None
        self._refund_payment_id = None
        self._invoice_id = None
        self._receipt_id = None
        self._original_receipt_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if actual_refunded_value is not None:
            self.actual_refunded_value = actual_refunded_value
        if refund_completed is not None:
            self.refund_completed = refund_completed
        if currency is not None:
            self.currency = currency
        if account_id is not None:
            self.account_id = account_id
        if reason is not None:
            self.reason = reason
        if nominal_value is not None:
            self.nominal_value = nominal_value
        if actual_value is not None:
            self.actual_value = actual_value
        if nominal_refunded_value is not None:
            self.nominal_refunded_value = nominal_refunded_value
        if refund_type is not None:
            self.refund_type = refund_type
        if refund_nature is not None:
            self.refund_nature = refund_nature
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if invoice_payment_id is not None:
            self.invoice_payment_id = invoice_payment_id
        if original_payment_id is not None:
            self.original_payment_id = original_payment_id
        if refund_payment_id is not None:
            self.refund_payment_id = refund_payment_id
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if receipt_id is not None:
            self.receipt_id = receipt_id
        if original_receipt_id is not None:
            self.original_receipt_id = original_receipt_id

    @property
    def id(self):
        """Gets the id of this RefundAccountingView.  # noqa: E501


        :return: The id of this RefundAccountingView.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RefundAccountingView.


        :param id: The id of this RefundAccountingView.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def actual_refunded_value(self):
        """Gets the actual_refunded_value of this RefundAccountingView.  # noqa: E501


        :return: The actual_refunded_value of this RefundAccountingView.  # noqa: E501
        :rtype: float
        """
        return self._actual_refunded_value

    @actual_refunded_value.setter
    def actual_refunded_value(self, actual_refunded_value):
        """Sets the actual_refunded_value of this RefundAccountingView.


        :param actual_refunded_value: The actual_refunded_value of this RefundAccountingView.  # noqa: E501
        :type: float
        """

        self._actual_refunded_value = actual_refunded_value

    @property
    def refund_completed(self):
        """Gets the refund_completed of this RefundAccountingView.  # noqa: E501


        :return: The refund_completed of this RefundAccountingView.  # noqa: E501
        :rtype: datetime
        """
        return self._refund_completed

    @refund_completed.setter
    def refund_completed(self, refund_completed):
        """Sets the refund_completed of this RefundAccountingView.


        :param refund_completed: The refund_completed of this RefundAccountingView.  # noqa: E501
        :type: datetime
        """

        self._refund_completed = refund_completed

    @property
    def currency(self):
        """Gets the currency of this RefundAccountingView.  # noqa: E501


        :return: The currency of this RefundAccountingView.  # noqa: E501
        :rtype: CreditNoteCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this RefundAccountingView.


        :param currency: The currency of this RefundAccountingView.  # noqa: E501
        :type: CreditNoteCurrency
        """

        self._currency = currency

    @property
    def account_id(self):
        """Gets the account_id of this RefundAccountingView.  # noqa: E501


        :return: The account_id of this RefundAccountingView.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this RefundAccountingView.


        :param account_id: The account_id of this RefundAccountingView.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def reason(self):
        """Gets the reason of this RefundAccountingView.  # noqa: E501


        :return: The reason of this RefundAccountingView.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this RefundAccountingView.


        :param reason: The reason of this RefundAccountingView.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def nominal_value(self):
        """Gets the nominal_value of this RefundAccountingView.  # noqa: E501


        :return: The nominal_value of this RefundAccountingView.  # noqa: E501
        :rtype: float
        """
        return self._nominal_value

    @nominal_value.setter
    def nominal_value(self, nominal_value):
        """Sets the nominal_value of this RefundAccountingView.


        :param nominal_value: The nominal_value of this RefundAccountingView.  # noqa: E501
        :type: float
        """

        self._nominal_value = nominal_value

    @property
    def actual_value(self):
        """Gets the actual_value of this RefundAccountingView.  # noqa: E501


        :return: The actual_value of this RefundAccountingView.  # noqa: E501
        :rtype: float
        """
        return self._actual_value

    @actual_value.setter
    def actual_value(self, actual_value):
        """Sets the actual_value of this RefundAccountingView.


        :param actual_value: The actual_value of this RefundAccountingView.  # noqa: E501
        :type: float
        """

        self._actual_value = actual_value

    @property
    def nominal_refunded_value(self):
        """Gets the nominal_refunded_value of this RefundAccountingView.  # noqa: E501


        :return: The nominal_refunded_value of this RefundAccountingView.  # noqa: E501
        :rtype: float
        """
        return self._nominal_refunded_value

    @nominal_refunded_value.setter
    def nominal_refunded_value(self, nominal_refunded_value):
        """Sets the nominal_refunded_value of this RefundAccountingView.


        :param nominal_refunded_value: The nominal_refunded_value of this RefundAccountingView.  # noqa: E501
        :type: float
        """

        self._nominal_refunded_value = nominal_refunded_value

    @property
    def refund_type(self):
        """Gets the refund_type of this RefundAccountingView.  # noqa: E501


        :return: The refund_type of this RefundAccountingView.  # noqa: E501
        :rtype: str
        """
        return self._refund_type

    @refund_type.setter
    def refund_type(self, refund_type):
        """Sets the refund_type of this RefundAccountingView.


        :param refund_type: The refund_type of this RefundAccountingView.  # noqa: E501
        :type: str
        """
        allowed_values = ["InvoicePayment", "Payment"]  # noqa: E501
        if refund_type not in allowed_values:
            raise ValueError(
                "Invalid value for `refund_type` ({0}), must be one of {1}"  # noqa: E501
                .format(refund_type, allowed_values)
            )

        self._refund_type = refund_type

    @property
    def refund_nature(self):
        """Gets the refund_nature of this RefundAccountingView.  # noqa: E501


        :return: The refund_nature of this RefundAccountingView.  # noqa: E501
        :rtype: str
        """
        return self._refund_nature

    @refund_nature.setter
    def refund_nature(self, refund_nature):
        """Sets the refund_nature of this RefundAccountingView.


        :param refund_nature: The refund_nature of this RefundAccountingView.  # noqa: E501
        :type: str
        """
        allowed_values = ["Refund", "Void"]  # noqa: E501
        if refund_nature not in allowed_values:
            raise ValueError(
                "Invalid value for `refund_nature` ({0}), must be one of {1}"  # noqa: E501
                .format(refund_nature, allowed_values)
            )

        self._refund_nature = refund_nature

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this RefundAccountingView.  # noqa: E501


        :return: The payment_method_id of this RefundAccountingView.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this RefundAccountingView.


        :param payment_method_id: The payment_method_id of this RefundAccountingView.  # noqa: E501
        :type: str
        """

        self._payment_method_id = payment_method_id

    @property
    def invoice_payment_id(self):
        """Gets the invoice_payment_id of this RefundAccountingView.  # noqa: E501


        :return: The invoice_payment_id of this RefundAccountingView.  # noqa: E501
        :rtype: str
        """
        return self._invoice_payment_id

    @invoice_payment_id.setter
    def invoice_payment_id(self, invoice_payment_id):
        """Sets the invoice_payment_id of this RefundAccountingView.


        :param invoice_payment_id: The invoice_payment_id of this RefundAccountingView.  # noqa: E501
        :type: str
        """

        self._invoice_payment_id = invoice_payment_id

    @property
    def original_payment_id(self):
        """Gets the original_payment_id of this RefundAccountingView.  # noqa: E501


        :return: The original_payment_id of this RefundAccountingView.  # noqa: E501
        :rtype: str
        """
        return self._original_payment_id

    @original_payment_id.setter
    def original_payment_id(self, original_payment_id):
        """Sets the original_payment_id of this RefundAccountingView.


        :param original_payment_id: The original_payment_id of this RefundAccountingView.  # noqa: E501
        :type: str
        """

        self._original_payment_id = original_payment_id

    @property
    def refund_payment_id(self):
        """Gets the refund_payment_id of this RefundAccountingView.  # noqa: E501


        :return: The refund_payment_id of this RefundAccountingView.  # noqa: E501
        :rtype: str
        """
        return self._refund_payment_id

    @refund_payment_id.setter
    def refund_payment_id(self, refund_payment_id):
        """Sets the refund_payment_id of this RefundAccountingView.


        :param refund_payment_id: The refund_payment_id of this RefundAccountingView.  # noqa: E501
        :type: str
        """

        self._refund_payment_id = refund_payment_id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this RefundAccountingView.  # noqa: E501


        :return: The invoice_id of this RefundAccountingView.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this RefundAccountingView.


        :param invoice_id: The invoice_id of this RefundAccountingView.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def receipt_id(self):
        """Gets the receipt_id of this RefundAccountingView.  # noqa: E501


        :return: The receipt_id of this RefundAccountingView.  # noqa: E501
        :rtype: str
        """
        return self._receipt_id

    @receipt_id.setter
    def receipt_id(self, receipt_id):
        """Sets the receipt_id of this RefundAccountingView.


        :param receipt_id: The receipt_id of this RefundAccountingView.  # noqa: E501
        :type: str
        """

        self._receipt_id = receipt_id

    @property
    def original_receipt_id(self):
        """Gets the original_receipt_id of this RefundAccountingView.  # noqa: E501


        :return: The original_receipt_id of this RefundAccountingView.  # noqa: E501
        :rtype: str
        """
        return self._original_receipt_id

    @original_receipt_id.setter
    def original_receipt_id(self, original_receipt_id):
        """Sets the original_receipt_id of this RefundAccountingView.


        :param original_receipt_id: The original_receipt_id of this RefundAccountingView.  # noqa: E501
        :type: str
        """

        self._original_receipt_id = original_receipt_id

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
        if issubclass(RefundAccountingView, dict):
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
        if not isinstance(other, RefundAccountingView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other