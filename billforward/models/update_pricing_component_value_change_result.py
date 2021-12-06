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

class UpdatePricingComponentValueChangeResult(object):
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
        'pricing_component_id': 'str',
        'pricing_component_name': 'str',
        'pricing_component_public_name': 'str',
        'new_value': 'int',
        'old_value': 'int',
        'type': 'str',
        'subscription_id': 'str',
        'amount': 'float',
        'charge_type': 'str',
        'charge': 'SubscriptionCharge',
        'amendment': 'Amendment',
        'state': 'str'
    }

    attribute_map = {
        'pricing_component_id': 'pricingComponentID',
        'pricing_component_name': 'pricingComponentName',
        'pricing_component_public_name': 'pricingComponentPublicName',
        'new_value': 'newValue',
        'old_value': 'oldValue',
        'type': 'type',
        'subscription_id': 'subscriptionID',
        'amount': 'amount',
        'charge_type': 'chargeType',
        'charge': 'charge',
        'amendment': 'amendment',
        'state': 'state'
    }

    def __init__(self, pricing_component_id=None, pricing_component_name=None, pricing_component_public_name=None, new_value=None, old_value=None, type=None, subscription_id=None, amount=None, charge_type=None, charge=None, amendment=None, state=None):  # noqa: E501
        """UpdatePricingComponentValueChangeResult - a model defined in Swagger"""  # noqa: E501
        self._pricing_component_id = None
        self._pricing_component_name = None
        self._pricing_component_public_name = None
        self._new_value = None
        self._old_value = None
        self._type = None
        self._subscription_id = None
        self._amount = None
        self._charge_type = None
        self._charge = None
        self._amendment = None
        self._state = None
        self.discriminator = None
        if pricing_component_id is not None:
            self.pricing_component_id = pricing_component_id
        if pricing_component_name is not None:
            self.pricing_component_name = pricing_component_name
        if pricing_component_public_name is not None:
            self.pricing_component_public_name = pricing_component_public_name
        if new_value is not None:
            self.new_value = new_value
        if old_value is not None:
            self.old_value = old_value
        if type is not None:
            self.type = type
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if amount is not None:
            self.amount = amount
        if charge_type is not None:
            self.charge_type = charge_type
        if charge is not None:
            self.charge = charge
        if amendment is not None:
            self.amendment = amendment
        if state is not None:
            self.state = state

    @property
    def pricing_component_id(self):
        """Gets the pricing_component_id of this UpdatePricingComponentValueChangeResult.  # noqa: E501


        :return: The pricing_component_id of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component_id

    @pricing_component_id.setter
    def pricing_component_id(self, pricing_component_id):
        """Sets the pricing_component_id of this UpdatePricingComponentValueChangeResult.


        :param pricing_component_id: The pricing_component_id of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :type: str
        """

        self._pricing_component_id = pricing_component_id

    @property
    def pricing_component_name(self):
        """Gets the pricing_component_name of this UpdatePricingComponentValueChangeResult.  # noqa: E501


        :return: The pricing_component_name of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component_name

    @pricing_component_name.setter
    def pricing_component_name(self, pricing_component_name):
        """Sets the pricing_component_name of this UpdatePricingComponentValueChangeResult.


        :param pricing_component_name: The pricing_component_name of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :type: str
        """

        self._pricing_component_name = pricing_component_name

    @property
    def pricing_component_public_name(self):
        """Gets the pricing_component_public_name of this UpdatePricingComponentValueChangeResult.  # noqa: E501


        :return: The pricing_component_public_name of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component_public_name

    @pricing_component_public_name.setter
    def pricing_component_public_name(self, pricing_component_public_name):
        """Sets the pricing_component_public_name of this UpdatePricingComponentValueChangeResult.


        :param pricing_component_public_name: The pricing_component_public_name of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :type: str
        """

        self._pricing_component_public_name = pricing_component_public_name

    @property
    def new_value(self):
        """Gets the new_value of this UpdatePricingComponentValueChangeResult.  # noqa: E501


        :return: The new_value of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :rtype: int
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this UpdatePricingComponentValueChangeResult.


        :param new_value: The new_value of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :type: int
        """

        self._new_value = new_value

    @property
    def old_value(self):
        """Gets the old_value of this UpdatePricingComponentValueChangeResult.  # noqa: E501


        :return: The old_value of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :rtype: int
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """Sets the old_value of this UpdatePricingComponentValueChangeResult.


        :param old_value: The old_value of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :type: int
        """

        self._old_value = old_value

    @property
    def type(self):
        """Gets the type of this UpdatePricingComponentValueChangeResult.  # noqa: E501


        :return: The type of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdatePricingComponentValueChangeResult.


        :param type: The type of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["Upgrade", "Downgrade", "NoChange"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def subscription_id(self):
        """Gets the subscription_id of this UpdatePricingComponentValueChangeResult.  # noqa: E501


        :return: The subscription_id of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this UpdatePricingComponentValueChangeResult.


        :param subscription_id: The subscription_id of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def amount(self):
        """Gets the amount of this UpdatePricingComponentValueChangeResult.  # noqa: E501


        :return: The amount of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this UpdatePricingComponentValueChangeResult.


        :param amount: The amount of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def charge_type(self):
        """Gets the charge_type of this UpdatePricingComponentValueChangeResult.  # noqa: E501


        :return: The charge_type of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this UpdatePricingComponentValueChangeResult.


        :param charge_type: The charge_type of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["Credit", "Debit"]  # noqa: E501
        if charge_type not in allowed_values:
            raise ValueError(
                "Invalid value for `charge_type` ({0}), must be one of {1}"  # noqa: E501
                .format(charge_type, allowed_values)
            )

        self._charge_type = charge_type

    @property
    def charge(self):
        """Gets the charge of this UpdatePricingComponentValueChangeResult.  # noqa: E501


        :return: The charge of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :rtype: SubscriptionCharge
        """
        return self._charge

    @charge.setter
    def charge(self, charge):
        """Sets the charge of this UpdatePricingComponentValueChangeResult.


        :param charge: The charge of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :type: SubscriptionCharge
        """

        self._charge = charge

    @property
    def amendment(self):
        """Gets the amendment of this UpdatePricingComponentValueChangeResult.  # noqa: E501


        :return: The amendment of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :rtype: Amendment
        """
        return self._amendment

    @amendment.setter
    def amendment(self, amendment):
        """Sets the amendment of this UpdatePricingComponentValueChangeResult.


        :param amendment: The amendment of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :type: Amendment
        """

        self._amendment = amendment

    @property
    def state(self):
        """Gets the state of this UpdatePricingComponentValueChangeResult.  # noqa: E501


        :return: The state of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UpdatePricingComponentValueChangeResult.


        :param state: The state of this UpdatePricingComponentValueChangeResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["Failed", "Succeeded", "Pending"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if issubclass(UpdatePricingComponentValueChangeResult, dict):
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
        if not isinstance(other, UpdatePricingComponentValueChangeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other