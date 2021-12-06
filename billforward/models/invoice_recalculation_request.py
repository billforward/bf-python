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

class InvoiceRecalculationRequest(object):
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
        'recalculation_behaviour': 'str',
        'new_state': 'str',
        'only_invoice_associated_charges': 'bool',
        'recalculate_parent': 'bool',
        'apply_coupons': 'bool',
        'dry_run': 'bool',
        'organization_id': 'str',
        'invoice_id': 'str'
    }

    attribute_map = {
        'created': 'created',
        'recalculation_behaviour': 'recalculationBehaviour',
        'new_state': 'newState',
        'only_invoice_associated_charges': 'onlyInvoiceAssociatedCharges',
        'recalculate_parent': 'recalculateParent',
        'apply_coupons': 'applyCoupons',
        'dry_run': 'dryRun',
        'organization_id': 'organizationID',
        'invoice_id': 'invoiceID'
    }

    def __init__(self, created=None, recalculation_behaviour=None, new_state=None, only_invoice_associated_charges=None, recalculate_parent=None, apply_coupons=None, dry_run=None, organization_id=None, invoice_id=None):  # noqa: E501
        """InvoiceRecalculationRequest - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._recalculation_behaviour = None
        self._new_state = None
        self._only_invoice_associated_charges = None
        self._recalculate_parent = None
        self._apply_coupons = None
        self._dry_run = None
        self._organization_id = None
        self._invoice_id = None
        self.discriminator = None
        if created is not None:
            self.created = created
        self.recalculation_behaviour = recalculation_behaviour
        self.new_state = new_state
        self.only_invoice_associated_charges = only_invoice_associated_charges
        self.recalculate_parent = recalculate_parent
        self.apply_coupons = apply_coupons
        self.dry_run = dry_run
        if organization_id is not None:
            self.organization_id = organization_id
        if invoice_id is not None:
            self.invoice_id = invoice_id

    @property
    def created(self):
        """Gets the created of this InvoiceRecalculationRequest.  # noqa: E501


        :return: The created of this InvoiceRecalculationRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this InvoiceRecalculationRequest.


        :param created: The created of this InvoiceRecalculationRequest.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def recalculation_behaviour(self):
        """Gets the recalculation_behaviour of this InvoiceRecalculationRequest.  # noqa: E501


        :return: The recalculation_behaviour of this InvoiceRecalculationRequest.  # noqa: E501
        :rtype: str
        """
        return self._recalculation_behaviour

    @recalculation_behaviour.setter
    def recalculation_behaviour(self, recalculation_behaviour):
        """Sets the recalculation_behaviour of this InvoiceRecalculationRequest.


        :param recalculation_behaviour: The recalculation_behaviour of this InvoiceRecalculationRequest.  # noqa: E501
        :type: str
        """
        if recalculation_behaviour is None:
            raise ValueError("Invalid value for `recalculation_behaviour`, must not be `None`")  # noqa: E501
        allowed_values = ["RecalculateAsLatestSubscriptionVersion", "RecalculateAsCurrentSubscriptionVersion"]  # noqa: E501
        if recalculation_behaviour not in allowed_values:
            raise ValueError(
                "Invalid value for `recalculation_behaviour` ({0}), must be one of {1}"  # noqa: E501
                .format(recalculation_behaviour, allowed_values)
            )

        self._recalculation_behaviour = recalculation_behaviour

    @property
    def new_state(self):
        """Gets the new_state of this InvoiceRecalculationRequest.  # noqa: E501


        :return: The new_state of this InvoiceRecalculationRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_state

    @new_state.setter
    def new_state(self, new_state):
        """Sets the new_state of this InvoiceRecalculationRequest.


        :param new_state: The new_state of this InvoiceRecalculationRequest.  # noqa: E501
        :type: str
        """
        if new_state is None:
            raise ValueError("Invalid value for `new_state`, must not be `None`")  # noqa: E501
        allowed_values = ["Paid", "Unpaid", "Pending", "Voided"]  # noqa: E501
        if new_state not in allowed_values:
            raise ValueError(
                "Invalid value for `new_state` ({0}), must be one of {1}"  # noqa: E501
                .format(new_state, allowed_values)
            )

        self._new_state = new_state

    @property
    def only_invoice_associated_charges(self):
        """Gets the only_invoice_associated_charges of this InvoiceRecalculationRequest.  # noqa: E501


        :return: The only_invoice_associated_charges of this InvoiceRecalculationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._only_invoice_associated_charges

    @only_invoice_associated_charges.setter
    def only_invoice_associated_charges(self, only_invoice_associated_charges):
        """Sets the only_invoice_associated_charges of this InvoiceRecalculationRequest.


        :param only_invoice_associated_charges: The only_invoice_associated_charges of this InvoiceRecalculationRequest.  # noqa: E501
        :type: bool
        """
        if only_invoice_associated_charges is None:
            raise ValueError("Invalid value for `only_invoice_associated_charges`, must not be `None`")  # noqa: E501

        self._only_invoice_associated_charges = only_invoice_associated_charges

    @property
    def recalculate_parent(self):
        """Gets the recalculate_parent of this InvoiceRecalculationRequest.  # noqa: E501


        :return: The recalculate_parent of this InvoiceRecalculationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._recalculate_parent

    @recalculate_parent.setter
    def recalculate_parent(self, recalculate_parent):
        """Sets the recalculate_parent of this InvoiceRecalculationRequest.


        :param recalculate_parent: The recalculate_parent of this InvoiceRecalculationRequest.  # noqa: E501
        :type: bool
        """
        if recalculate_parent is None:
            raise ValueError("Invalid value for `recalculate_parent`, must not be `None`")  # noqa: E501

        self._recalculate_parent = recalculate_parent

    @property
    def apply_coupons(self):
        """Gets the apply_coupons of this InvoiceRecalculationRequest.  # noqa: E501


        :return: The apply_coupons of this InvoiceRecalculationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._apply_coupons

    @apply_coupons.setter
    def apply_coupons(self, apply_coupons):
        """Sets the apply_coupons of this InvoiceRecalculationRequest.


        :param apply_coupons: The apply_coupons of this InvoiceRecalculationRequest.  # noqa: E501
        :type: bool
        """
        if apply_coupons is None:
            raise ValueError("Invalid value for `apply_coupons`, must not be `None`")  # noqa: E501

        self._apply_coupons = apply_coupons

    @property
    def dry_run(self):
        """Gets the dry_run of this InvoiceRecalculationRequest.  # noqa: E501


        :return: The dry_run of this InvoiceRecalculationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this InvoiceRecalculationRequest.


        :param dry_run: The dry_run of this InvoiceRecalculationRequest.  # noqa: E501
        :type: bool
        """
        if dry_run is None:
            raise ValueError("Invalid value for `dry_run`, must not be `None`")  # noqa: E501

        self._dry_run = dry_run

    @property
    def organization_id(self):
        """Gets the organization_id of this InvoiceRecalculationRequest.  # noqa: E501


        :return: The organization_id of this InvoiceRecalculationRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this InvoiceRecalculationRequest.


        :param organization_id: The organization_id of this InvoiceRecalculationRequest.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this InvoiceRecalculationRequest.  # noqa: E501


        :return: The invoice_id of this InvoiceRecalculationRequest.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this InvoiceRecalculationRequest.


        :param invoice_id: The invoice_id of this InvoiceRecalculationRequest.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

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
        if issubclass(InvoiceRecalculationRequest, dict):
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
        if not isinstance(other, InvoiceRecalculationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
