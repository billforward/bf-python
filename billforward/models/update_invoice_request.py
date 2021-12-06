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

class UpdateInvoiceRequest(object):
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
        'id': 'str',
        'version_id': 'str',
        'state': 'str',
        'name': 'str',
        'description': 'str',
        'purchase_order': 'str',
        'payment_terms': 'int',
        'payment_amount': 'float',
        'due': 'datetime'
    }

    attribute_map = {
        'organization_id': 'organizationID',
        'id': 'id',
        'version_id': 'versionID',
        'state': 'state',
        'name': 'name',
        'description': 'description',
        'purchase_order': 'purchaseOrder',
        'payment_terms': 'paymentTerms',
        'payment_amount': 'paymentAmount',
        'due': 'due'
    }

    def __init__(self, organization_id=None, id=None, version_id=None, state=None, name=None, description=None, purchase_order=None, payment_terms=None, payment_amount=None, due=None):  # noqa: E501
        """UpdateInvoiceRequest - a model defined in Swagger"""  # noqa: E501
        self._organization_id = None
        self._id = None
        self._version_id = None
        self._state = None
        self._name = None
        self._description = None
        self._purchase_order = None
        self._payment_terms = None
        self._payment_amount = None
        self._due = None
        self.discriminator = None
        if organization_id is not None:
            self.organization_id = organization_id
        if id is not None:
            self.id = id
        if version_id is not None:
            self.version_id = version_id
        if state is not None:
            self.state = state
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if purchase_order is not None:
            self.purchase_order = purchase_order
        if payment_terms is not None:
            self.payment_terms = payment_terms
        if payment_amount is not None:
            self.payment_amount = payment_amount
        if due is not None:
            self.due = due

    @property
    def organization_id(self):
        """Gets the organization_id of this UpdateInvoiceRequest.  # noqa: E501


        :return: The organization_id of this UpdateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this UpdateInvoiceRequest.


        :param organization_id: The organization_id of this UpdateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def id(self):
        """Gets the id of this UpdateInvoiceRequest.  # noqa: E501


        :return: The id of this UpdateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateInvoiceRequest.


        :param id: The id of this UpdateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def version_id(self):
        """Gets the version_id of this UpdateInvoiceRequest.  # noqa: E501


        :return: The version_id of this UpdateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this UpdateInvoiceRequest.


        :param version_id: The version_id of this UpdateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def state(self):
        """Gets the state of this UpdateInvoiceRequest.  # noqa: E501


        :return: The state of this UpdateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UpdateInvoiceRequest.


        :param state: The state of this UpdateInvoiceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unpaid", "Pending"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def name(self):
        """Gets the name of this UpdateInvoiceRequest.  # noqa: E501


        :return: The name of this UpdateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateInvoiceRequest.


        :param name: The name of this UpdateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateInvoiceRequest.  # noqa: E501


        :return: The description of this UpdateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateInvoiceRequest.


        :param description: The description of this UpdateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def purchase_order(self):
        """Gets the purchase_order of this UpdateInvoiceRequest.  # noqa: E501


        :return: The purchase_order of this UpdateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order

    @purchase_order.setter
    def purchase_order(self, purchase_order):
        """Sets the purchase_order of this UpdateInvoiceRequest.


        :param purchase_order: The purchase_order of this UpdateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._purchase_order = purchase_order

    @property
    def payment_terms(self):
        """Gets the payment_terms of this UpdateInvoiceRequest.  # noqa: E501


        :return: The payment_terms of this UpdateInvoiceRequest.  # noqa: E501
        :rtype: int
        """
        return self._payment_terms

    @payment_terms.setter
    def payment_terms(self, payment_terms):
        """Sets the payment_terms of this UpdateInvoiceRequest.


        :param payment_terms: The payment_terms of this UpdateInvoiceRequest.  # noqa: E501
        :type: int
        """

        self._payment_terms = payment_terms

    @property
    def payment_amount(self):
        """Gets the payment_amount of this UpdateInvoiceRequest.  # noqa: E501


        :return: The payment_amount of this UpdateInvoiceRequest.  # noqa: E501
        :rtype: float
        """
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, payment_amount):
        """Sets the payment_amount of this UpdateInvoiceRequest.


        :param payment_amount: The payment_amount of this UpdateInvoiceRequest.  # noqa: E501
        :type: float
        """

        self._payment_amount = payment_amount

    @property
    def due(self):
        """Gets the due of this UpdateInvoiceRequest.  # noqa: E501


        :return: The due of this UpdateInvoiceRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._due

    @due.setter
    def due(self, due):
        """Sets the due of this UpdateInvoiceRequest.


        :param due: The due of this UpdateInvoiceRequest.  # noqa: E501
        :type: datetime
        """

        self._due = due

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
        if issubclass(UpdateInvoiceRequest, dict):
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
        if not isinstance(other, UpdateInvoiceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
