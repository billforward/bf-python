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

class PricingComponentValueResponse(object):
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
        'state': 'str',
        'existing_value': 'int',
        'new_value': 'int',
        'type': 'str',
        'pricing_component_id': 'str',
        'pricing_component_name': 'str',
        'pricing_component_public_name': 'str',
        'organization_id': 'str',
        'invoice_id': 'str',
        'subscription_id': 'str',
        'cost': 'float',
        'credit': 'float',
        'discount': 'float',
        'currency': 'CreditNoteCurrency',
        'new_value_active': 'datetime',
        'charge_id': 'str',
        'amendment_id': 'str',
        'coupon_charge_id': 'str'
    }

    attribute_map = {
        'created': 'created',
        'state': 'state',
        'existing_value': 'existingValue',
        'new_value': 'newValue',
        'type': 'type',
        'pricing_component_id': 'pricingComponentID',
        'pricing_component_name': 'pricingComponentName',
        'pricing_component_public_name': 'pricingComponentPublicName',
        'organization_id': 'organizationID',
        'invoice_id': 'invoiceID',
        'subscription_id': 'subscriptionID',
        'cost': 'cost',
        'credit': 'credit',
        'discount': 'discount',
        'currency': 'currency',
        'new_value_active': 'newValueActive',
        'charge_id': 'chargeID',
        'amendment_id': 'amendmentID',
        'coupon_charge_id': 'couponChargeID'
    }

    def __init__(self, created=None, state=None, existing_value=None, new_value=None, type=None, pricing_component_id=None, pricing_component_name=None, pricing_component_public_name=None, organization_id=None, invoice_id=None, subscription_id=None, cost=None, credit=None, discount=None, currency=None, new_value_active=None, charge_id=None, amendment_id=None, coupon_charge_id=None):  # noqa: E501
        """PricingComponentValueResponse - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._state = None
        self._existing_value = None
        self._new_value = None
        self._type = None
        self._pricing_component_id = None
        self._pricing_component_name = None
        self._pricing_component_public_name = None
        self._organization_id = None
        self._invoice_id = None
        self._subscription_id = None
        self._cost = None
        self._credit = None
        self._discount = None
        self._currency = None
        self._new_value_active = None
        self._charge_id = None
        self._amendment_id = None
        self._coupon_charge_id = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if state is not None:
            self.state = state
        if existing_value is not None:
            self.existing_value = existing_value
        if new_value is not None:
            self.new_value = new_value
        if type is not None:
            self.type = type
        if pricing_component_id is not None:
            self.pricing_component_id = pricing_component_id
        if pricing_component_name is not None:
            self.pricing_component_name = pricing_component_name
        if pricing_component_public_name is not None:
            self.pricing_component_public_name = pricing_component_public_name
        if organization_id is not None:
            self.organization_id = organization_id
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if cost is not None:
            self.cost = cost
        if credit is not None:
            self.credit = credit
        if discount is not None:
            self.discount = discount
        if currency is not None:
            self.currency = currency
        if new_value_active is not None:
            self.new_value_active = new_value_active
        if charge_id is not None:
            self.charge_id = charge_id
        if amendment_id is not None:
            self.amendment_id = amendment_id
        if coupon_charge_id is not None:
            self.coupon_charge_id = coupon_charge_id

    @property
    def created(self):
        """Gets the created of this PricingComponentValueResponse.  # noqa: E501


        :return: The created of this PricingComponentValueResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PricingComponentValueResponse.


        :param created: The created of this PricingComponentValueResponse.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def state(self):
        """Gets the state of this PricingComponentValueResponse.  # noqa: E501


        :return: The state of this PricingComponentValueResponse.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PricingComponentValueResponse.


        :param state: The state of this PricingComponentValueResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Success", "Failed"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def existing_value(self):
        """Gets the existing_value of this PricingComponentValueResponse.  # noqa: E501


        :return: The existing_value of this PricingComponentValueResponse.  # noqa: E501
        :rtype: int
        """
        return self._existing_value

    @existing_value.setter
    def existing_value(self, existing_value):
        """Sets the existing_value of this PricingComponentValueResponse.


        :param existing_value: The existing_value of this PricingComponentValueResponse.  # noqa: E501
        :type: int
        """

        self._existing_value = existing_value

    @property
    def new_value(self):
        """Gets the new_value of this PricingComponentValueResponse.  # noqa: E501


        :return: The new_value of this PricingComponentValueResponse.  # noqa: E501
        :rtype: int
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this PricingComponentValueResponse.


        :param new_value: The new_value of this PricingComponentValueResponse.  # noqa: E501
        :type: int
        """

        self._new_value = new_value

    @property
    def type(self):
        """Gets the type of this PricingComponentValueResponse.  # noqa: E501


        :return: The type of this PricingComponentValueResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PricingComponentValueResponse.


        :param type: The type of this PricingComponentValueResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Initial", "Upgrade", "Downgrade"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def pricing_component_id(self):
        """Gets the pricing_component_id of this PricingComponentValueResponse.  # noqa: E501


        :return: The pricing_component_id of this PricingComponentValueResponse.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component_id

    @pricing_component_id.setter
    def pricing_component_id(self, pricing_component_id):
        """Sets the pricing_component_id of this PricingComponentValueResponse.


        :param pricing_component_id: The pricing_component_id of this PricingComponentValueResponse.  # noqa: E501
        :type: str
        """

        self._pricing_component_id = pricing_component_id

    @property
    def pricing_component_name(self):
        """Gets the pricing_component_name of this PricingComponentValueResponse.  # noqa: E501


        :return: The pricing_component_name of this PricingComponentValueResponse.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component_name

    @pricing_component_name.setter
    def pricing_component_name(self, pricing_component_name):
        """Sets the pricing_component_name of this PricingComponentValueResponse.


        :param pricing_component_name: The pricing_component_name of this PricingComponentValueResponse.  # noqa: E501
        :type: str
        """

        self._pricing_component_name = pricing_component_name

    @property
    def pricing_component_public_name(self):
        """Gets the pricing_component_public_name of this PricingComponentValueResponse.  # noqa: E501


        :return: The pricing_component_public_name of this PricingComponentValueResponse.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component_public_name

    @pricing_component_public_name.setter
    def pricing_component_public_name(self, pricing_component_public_name):
        """Sets the pricing_component_public_name of this PricingComponentValueResponse.


        :param pricing_component_public_name: The pricing_component_public_name of this PricingComponentValueResponse.  # noqa: E501
        :type: str
        """

        self._pricing_component_public_name = pricing_component_public_name

    @property
    def organization_id(self):
        """Gets the organization_id of this PricingComponentValueResponse.  # noqa: E501


        :return: The organization_id of this PricingComponentValueResponse.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this PricingComponentValueResponse.


        :param organization_id: The organization_id of this PricingComponentValueResponse.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this PricingComponentValueResponse.  # noqa: E501


        :return: The invoice_id of this PricingComponentValueResponse.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this PricingComponentValueResponse.


        :param invoice_id: The invoice_id of this PricingComponentValueResponse.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this PricingComponentValueResponse.  # noqa: E501


        :return: The subscription_id of this PricingComponentValueResponse.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this PricingComponentValueResponse.


        :param subscription_id: The subscription_id of this PricingComponentValueResponse.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def cost(self):
        """Gets the cost of this PricingComponentValueResponse.  # noqa: E501


        :return: The cost of this PricingComponentValueResponse.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this PricingComponentValueResponse.


        :param cost: The cost of this PricingComponentValueResponse.  # noqa: E501
        :type: float
        """

        self._cost = cost

    @property
    def credit(self):
        """Gets the credit of this PricingComponentValueResponse.  # noqa: E501


        :return: The credit of this PricingComponentValueResponse.  # noqa: E501
        :rtype: float
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        """Sets the credit of this PricingComponentValueResponse.


        :param credit: The credit of this PricingComponentValueResponse.  # noqa: E501
        :type: float
        """

        self._credit = credit

    @property
    def discount(self):
        """Gets the discount of this PricingComponentValueResponse.  # noqa: E501


        :return: The discount of this PricingComponentValueResponse.  # noqa: E501
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this PricingComponentValueResponse.


        :param discount: The discount of this PricingComponentValueResponse.  # noqa: E501
        :type: float
        """

        self._discount = discount

    @property
    def currency(self):
        """Gets the currency of this PricingComponentValueResponse.  # noqa: E501


        :return: The currency of this PricingComponentValueResponse.  # noqa: E501
        :rtype: CreditNoteCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PricingComponentValueResponse.


        :param currency: The currency of this PricingComponentValueResponse.  # noqa: E501
        :type: CreditNoteCurrency
        """

        self._currency = currency

    @property
    def new_value_active(self):
        """Gets the new_value_active of this PricingComponentValueResponse.  # noqa: E501


        :return: The new_value_active of this PricingComponentValueResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._new_value_active

    @new_value_active.setter
    def new_value_active(self, new_value_active):
        """Sets the new_value_active of this PricingComponentValueResponse.


        :param new_value_active: The new_value_active of this PricingComponentValueResponse.  # noqa: E501
        :type: datetime
        """

        self._new_value_active = new_value_active

    @property
    def charge_id(self):
        """Gets the charge_id of this PricingComponentValueResponse.  # noqa: E501


        :return: The charge_id of this PricingComponentValueResponse.  # noqa: E501
        :rtype: str
        """
        return self._charge_id

    @charge_id.setter
    def charge_id(self, charge_id):
        """Sets the charge_id of this PricingComponentValueResponse.


        :param charge_id: The charge_id of this PricingComponentValueResponse.  # noqa: E501
        :type: str
        """

        self._charge_id = charge_id

    @property
    def amendment_id(self):
        """Gets the amendment_id of this PricingComponentValueResponse.  # noqa: E501


        :return: The amendment_id of this PricingComponentValueResponse.  # noqa: E501
        :rtype: str
        """
        return self._amendment_id

    @amendment_id.setter
    def amendment_id(self, amendment_id):
        """Sets the amendment_id of this PricingComponentValueResponse.


        :param amendment_id: The amendment_id of this PricingComponentValueResponse.  # noqa: E501
        :type: str
        """

        self._amendment_id = amendment_id

    @property
    def coupon_charge_id(self):
        """Gets the coupon_charge_id of this PricingComponentValueResponse.  # noqa: E501


        :return: The coupon_charge_id of this PricingComponentValueResponse.  # noqa: E501
        :rtype: str
        """
        return self._coupon_charge_id

    @coupon_charge_id.setter
    def coupon_charge_id(self, coupon_charge_id):
        """Sets the coupon_charge_id of this PricingComponentValueResponse.


        :param coupon_charge_id: The coupon_charge_id of this PricingComponentValueResponse.  # noqa: E501
        :type: str
        """

        self._coupon_charge_id = coupon_charge_id

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
        if issubclass(PricingComponentValueResponse, dict):
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
        if not isinstance(other, PricingComponentValueResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
