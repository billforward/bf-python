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

class AddChargesToAccountAPIRequest(object):
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
        'name': 'str',
        'purchase_order': 'str',
        'description': 'str',
        'currency': 'CreditNoteCurrency',
        'invoicing_type': 'str',
        'payment_terms': 'int',
        'remaining_credit_behaviour': 'str',
        'invoice_state': 'str',
        'charges': 'list[NestedChargeRequest]',
        'adhoc_charges': 'list[NestedAdhocChargeRequest]',
        'dry_run': 'bool'
    }

    attribute_map = {
        'organization_id': 'organizationID',
        'name': 'name',
        'purchase_order': 'purchaseOrder',
        'description': 'description',
        'currency': 'currency',
        'invoicing_type': 'invoicingType',
        'payment_terms': 'paymentTerms',
        'remaining_credit_behaviour': 'remainingCreditBehaviour',
        'invoice_state': 'invoiceState',
        'charges': 'charges',
        'adhoc_charges': 'adhocCharges',
        'dry_run': 'dryRun'
    }

    def __init__(self, organization_id=None, name=None, purchase_order=None, description=None, currency=None, invoicing_type=None, payment_terms=None, remaining_credit_behaviour=None, invoice_state=None, charges=None, adhoc_charges=None, dry_run=None):  # noqa: E501
        """AddChargesToAccountAPIRequest - a model defined in Swagger"""  # noqa: E501
        self._organization_id = None
        self._name = None
        self._purchase_order = None
        self._description = None
        self._currency = None
        self._invoicing_type = None
        self._payment_terms = None
        self._remaining_credit_behaviour = None
        self._invoice_state = None
        self._charges = None
        self._adhoc_charges = None
        self._dry_run = None
        self.discriminator = None
        if organization_id is not None:
            self.organization_id = organization_id
        if name is not None:
            self.name = name
        if purchase_order is not None:
            self.purchase_order = purchase_order
        if description is not None:
            self.description = description
        if currency is not None:
            self.currency = currency
        if invoicing_type is not None:
            self.invoicing_type = invoicing_type
        if payment_terms is not None:
            self.payment_terms = payment_terms
        self.remaining_credit_behaviour = remaining_credit_behaviour
        if invoice_state is not None:
            self.invoice_state = invoice_state
        if charges is not None:
            self.charges = charges
        if adhoc_charges is not None:
            self.adhoc_charges = adhoc_charges
        if dry_run is not None:
            self.dry_run = dry_run

    @property
    def organization_id(self):
        """Gets the organization_id of this AddChargesToAccountAPIRequest.  # noqa: E501


        :return: The organization_id of this AddChargesToAccountAPIRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this AddChargesToAccountAPIRequest.


        :param organization_id: The organization_id of this AddChargesToAccountAPIRequest.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def name(self):
        """Gets the name of this AddChargesToAccountAPIRequest.  # noqa: E501


        :return: The name of this AddChargesToAccountAPIRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddChargesToAccountAPIRequest.


        :param name: The name of this AddChargesToAccountAPIRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def purchase_order(self):
        """Gets the purchase_order of this AddChargesToAccountAPIRequest.  # noqa: E501


        :return: The purchase_order of this AddChargesToAccountAPIRequest.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order

    @purchase_order.setter
    def purchase_order(self, purchase_order):
        """Sets the purchase_order of this AddChargesToAccountAPIRequest.


        :param purchase_order: The purchase_order of this AddChargesToAccountAPIRequest.  # noqa: E501
        :type: str
        """

        self._purchase_order = purchase_order

    @property
    def description(self):
        """Gets the description of this AddChargesToAccountAPIRequest.  # noqa: E501


        :return: The description of this AddChargesToAccountAPIRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddChargesToAccountAPIRequest.


        :param description: The description of this AddChargesToAccountAPIRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def currency(self):
        """Gets the currency of this AddChargesToAccountAPIRequest.  # noqa: E501


        :return: The currency of this AddChargesToAccountAPIRequest.  # noqa: E501
        :rtype: CreditNoteCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AddChargesToAccountAPIRequest.


        :param currency: The currency of this AddChargesToAccountAPIRequest.  # noqa: E501
        :type: CreditNoteCurrency
        """

        self._currency = currency

    @property
    def invoicing_type(self):
        """Gets the invoicing_type of this AddChargesToAccountAPIRequest.  # noqa: E501


        :return: The invoicing_type of this AddChargesToAccountAPIRequest.  # noqa: E501
        :rtype: str
        """
        return self._invoicing_type

    @invoicing_type.setter
    def invoicing_type(self, invoicing_type):
        """Sets the invoicing_type of this AddChargesToAccountAPIRequest.


        :param invoicing_type: The invoicing_type of this AddChargesToAccountAPIRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Immediate", "Aggregated"]  # noqa: E501
        if invoicing_type not in allowed_values:
            raise ValueError(
                "Invalid value for `invoicing_type` ({0}), must be one of {1}"  # noqa: E501
                .format(invoicing_type, allowed_values)
            )

        self._invoicing_type = invoicing_type

    @property
    def payment_terms(self):
        """Gets the payment_terms of this AddChargesToAccountAPIRequest.  # noqa: E501


        :return: The payment_terms of this AddChargesToAccountAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._payment_terms

    @payment_terms.setter
    def payment_terms(self, payment_terms):
        """Sets the payment_terms of this AddChargesToAccountAPIRequest.


        :param payment_terms: The payment_terms of this AddChargesToAccountAPIRequest.  # noqa: E501
        :type: int
        """

        self._payment_terms = payment_terms

    @property
    def remaining_credit_behaviour(self):
        """Gets the remaining_credit_behaviour of this AddChargesToAccountAPIRequest.  # noqa: E501


        :return: The remaining_credit_behaviour of this AddChargesToAccountAPIRequest.  # noqa: E501
        :rtype: str
        """
        return self._remaining_credit_behaviour

    @remaining_credit_behaviour.setter
    def remaining_credit_behaviour(self, remaining_credit_behaviour):
        """Sets the remaining_credit_behaviour of this AddChargesToAccountAPIRequest.


        :param remaining_credit_behaviour: The remaining_credit_behaviour of this AddChargesToAccountAPIRequest.  # noqa: E501
        :type: str
        """
        if remaining_credit_behaviour is None:
            raise ValueError("Invalid value for `remaining_credit_behaviour`, must not be `None`")  # noqa: E501
        allowed_values = ["Rollover", "Discard"]  # noqa: E501
        if remaining_credit_behaviour not in allowed_values:
            raise ValueError(
                "Invalid value for `remaining_credit_behaviour` ({0}), must be one of {1}"  # noqa: E501
                .format(remaining_credit_behaviour, allowed_values)
            )

        self._remaining_credit_behaviour = remaining_credit_behaviour

    @property
    def invoice_state(self):
        """Gets the invoice_state of this AddChargesToAccountAPIRequest.  # noqa: E501


        :return: The invoice_state of this AddChargesToAccountAPIRequest.  # noqa: E501
        :rtype: str
        """
        return self._invoice_state

    @invoice_state.setter
    def invoice_state(self, invoice_state):
        """Sets the invoice_state of this AddChargesToAccountAPIRequest.


        :param invoice_state: The invoice_state of this AddChargesToAccountAPIRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unpaid", "Pending"]  # noqa: E501
        if invoice_state not in allowed_values:
            raise ValueError(
                "Invalid value for `invoice_state` ({0}), must be one of {1}"  # noqa: E501
                .format(invoice_state, allowed_values)
            )

        self._invoice_state = invoice_state

    @property
    def charges(self):
        """Gets the charges of this AddChargesToAccountAPIRequest.  # noqa: E501


        :return: The charges of this AddChargesToAccountAPIRequest.  # noqa: E501
        :rtype: list[NestedChargeRequest]
        """
        return self._charges

    @charges.setter
    def charges(self, charges):
        """Sets the charges of this AddChargesToAccountAPIRequest.


        :param charges: The charges of this AddChargesToAccountAPIRequest.  # noqa: E501
        :type: list[NestedChargeRequest]
        """

        self._charges = charges

    @property
    def adhoc_charges(self):
        """Gets the adhoc_charges of this AddChargesToAccountAPIRequest.  # noqa: E501


        :return: The adhoc_charges of this AddChargesToAccountAPIRequest.  # noqa: E501
        :rtype: list[NestedAdhocChargeRequest]
        """
        return self._adhoc_charges

    @adhoc_charges.setter
    def adhoc_charges(self, adhoc_charges):
        """Sets the adhoc_charges of this AddChargesToAccountAPIRequest.


        :param adhoc_charges: The adhoc_charges of this AddChargesToAccountAPIRequest.  # noqa: E501
        :type: list[NestedAdhocChargeRequest]
        """

        self._adhoc_charges = adhoc_charges

    @property
    def dry_run(self):
        """Gets the dry_run of this AddChargesToAccountAPIRequest.  # noqa: E501


        :return: The dry_run of this AddChargesToAccountAPIRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this AddChargesToAccountAPIRequest.


        :param dry_run: The dry_run of this AddChargesToAccountAPIRequest.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

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
        if issubclass(AddChargesToAccountAPIRequest, dict):
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
        if not isinstance(other, AddChargesToAccountAPIRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other