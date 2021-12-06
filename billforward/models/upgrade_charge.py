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
from billforward.models.subscription_charge import SubscriptionCharge  # noqa: F401,E501

class UpgradeCharge(SubscriptionCharge):
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
        'pricing_component_value_change': 'PricingComponentValueChange',
        'pricing_component_name': 'str',
        'public_pricing_component_name': 'str',
        'pricing_component_id': 'str'
    }
    if hasattr(SubscriptionCharge, "swagger_types"):
        swagger_types.update(SubscriptionCharge.swagger_types)

    attribute_map = {
        'pricing_component_value_change': 'pricingComponentValueChange',
        'pricing_component_name': 'pricingComponentName',
        'public_pricing_component_name': 'publicPricingComponentName',
        'pricing_component_id': 'pricingComponentID'
    }
    if hasattr(SubscriptionCharge, "attribute_map"):
        attribute_map.update(SubscriptionCharge.attribute_map)

    def __init__(self, pricing_component_value_change=None, pricing_component_name=None, public_pricing_component_name=None, pricing_component_id=None, *args, **kwargs):  # noqa: E501
        """UpgradeCharge - a model defined in Swagger"""  # noqa: E501
        self._pricing_component_value_change = None
        self._pricing_component_name = None
        self._public_pricing_component_name = None
        self._pricing_component_id = None
        self.discriminator = None
        if pricing_component_value_change is not None:
            self.pricing_component_value_change = pricing_component_value_change
        if pricing_component_name is not None:
            self.pricing_component_name = pricing_component_name
        if public_pricing_component_name is not None:
            self.public_pricing_component_name = public_pricing_component_name
        if pricing_component_id is not None:
            self.pricing_component_id = pricing_component_id
        SubscriptionCharge.__init__(self, *args, **kwargs)

    @property
    def pricing_component_value_change(self):
        """Gets the pricing_component_value_change of this UpgradeCharge.  # noqa: E501


        :return: The pricing_component_value_change of this UpgradeCharge.  # noqa: E501
        :rtype: PricingComponentValueChange
        """
        return self._pricing_component_value_change

    @pricing_component_value_change.setter
    def pricing_component_value_change(self, pricing_component_value_change):
        """Sets the pricing_component_value_change of this UpgradeCharge.


        :param pricing_component_value_change: The pricing_component_value_change of this UpgradeCharge.  # noqa: E501
        :type: PricingComponentValueChange
        """

        self._pricing_component_value_change = pricing_component_value_change

    @property
    def pricing_component_name(self):
        """Gets the pricing_component_name of this UpgradeCharge.  # noqa: E501


        :return: The pricing_component_name of this UpgradeCharge.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component_name

    @pricing_component_name.setter
    def pricing_component_name(self, pricing_component_name):
        """Sets the pricing_component_name of this UpgradeCharge.


        :param pricing_component_name: The pricing_component_name of this UpgradeCharge.  # noqa: E501
        :type: str
        """

        self._pricing_component_name = pricing_component_name

    @property
    def public_pricing_component_name(self):
        """Gets the public_pricing_component_name of this UpgradeCharge.  # noqa: E501


        :return: The public_pricing_component_name of this UpgradeCharge.  # noqa: E501
        :rtype: str
        """
        return self._public_pricing_component_name

    @public_pricing_component_name.setter
    def public_pricing_component_name(self, public_pricing_component_name):
        """Sets the public_pricing_component_name of this UpgradeCharge.


        :param public_pricing_component_name: The public_pricing_component_name of this UpgradeCharge.  # noqa: E501
        :type: str
        """

        self._public_pricing_component_name = public_pricing_component_name

    @property
    def pricing_component_id(self):
        """Gets the pricing_component_id of this UpgradeCharge.  # noqa: E501


        :return: The pricing_component_id of this UpgradeCharge.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component_id

    @pricing_component_id.setter
    def pricing_component_id(self, pricing_component_id):
        """Sets the pricing_component_id of this UpgradeCharge.


        :param pricing_component_id: The pricing_component_id of this UpgradeCharge.  # noqa: E501
        :type: str
        """

        self._pricing_component_id = pricing_component_id

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
        if issubclass(UpgradeCharge, dict):
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
        if not isinstance(other, UpgradeCharge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other