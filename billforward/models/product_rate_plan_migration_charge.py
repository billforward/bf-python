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

class ProductRatePlanMigrationCharge(SubscriptionCharge):
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
        'pricing_behaviour': 'str',
        'same_period': 'bool',
        'original_product_rate_plan_id': 'str',
        'original_public_product_rate_plan_name': 'str',
        'original_product_rate_plan_name': 'str',
        'new_product_rate_plan_id': 'str',
        'new_public_product_rate_plan_name': 'str',
        'new_product_rate_plan_name': 'str',
        'new_product_id': 'str',
        'new_public_product_name': 'str',
        'new_product_name': 'str',
        'pricing_component_values': 'list[PricingComponentMigrationValue]'
    }
    if hasattr(SubscriptionCharge, "swagger_types"):
        swagger_types.update(SubscriptionCharge.swagger_types)

    attribute_map = {
        'pricing_behaviour': 'pricingBehaviour',
        'same_period': 'samePeriod',
        'original_product_rate_plan_id': 'originalProductRatePlanID',
        'original_public_product_rate_plan_name': 'originalPublicProductRatePlanName',
        'original_product_rate_plan_name': 'originalProductRatePlanName',
        'new_product_rate_plan_id': 'newProductRatePlanID',
        'new_public_product_rate_plan_name': 'newPublicProductRatePlanName',
        'new_product_rate_plan_name': 'newProductRatePlanName',
        'new_product_id': 'newProductID',
        'new_public_product_name': 'newPublicProductName',
        'new_product_name': 'newProductName',
        'pricing_component_values': 'pricingComponentValues'
    }
    if hasattr(SubscriptionCharge, "attribute_map"):
        attribute_map.update(SubscriptionCharge.attribute_map)

    def __init__(self, pricing_behaviour=None, same_period=None, original_product_rate_plan_id=None, original_public_product_rate_plan_name=None, original_product_rate_plan_name=None, new_product_rate_plan_id=None, new_public_product_rate_plan_name=None, new_product_rate_plan_name=None, new_product_id=None, new_public_product_name=None, new_product_name=None, pricing_component_values=None, *args, **kwargs):  # noqa: E501
        """ProductRatePlanMigrationCharge - a model defined in Swagger"""  # noqa: E501
        self._pricing_behaviour = None
        self._same_period = None
        self._original_product_rate_plan_id = None
        self._original_public_product_rate_plan_name = None
        self._original_product_rate_plan_name = None
        self._new_product_rate_plan_id = None
        self._new_public_product_rate_plan_name = None
        self._new_product_rate_plan_name = None
        self._new_product_id = None
        self._new_public_product_name = None
        self._new_product_name = None
        self._pricing_component_values = None
        self.discriminator = None
        self.pricing_behaviour = pricing_behaviour
        if same_period is not None:
            self.same_period = same_period
        if original_product_rate_plan_id is not None:
            self.original_product_rate_plan_id = original_product_rate_plan_id
        if original_public_product_rate_plan_name is not None:
            self.original_public_product_rate_plan_name = original_public_product_rate_plan_name
        if original_product_rate_plan_name is not None:
            self.original_product_rate_plan_name = original_product_rate_plan_name
        if new_product_rate_plan_id is not None:
            self.new_product_rate_plan_id = new_product_rate_plan_id
        if new_public_product_rate_plan_name is not None:
            self.new_public_product_rate_plan_name = new_public_product_rate_plan_name
        if new_product_rate_plan_name is not None:
            self.new_product_rate_plan_name = new_product_rate_plan_name
        if new_product_id is not None:
            self.new_product_id = new_product_id
        if new_public_product_name is not None:
            self.new_public_product_name = new_public_product_name
        if new_product_name is not None:
            self.new_product_name = new_product_name
        if pricing_component_values is not None:
            self.pricing_component_values = pricing_component_values
        SubscriptionCharge.__init__(self, *args, **kwargs)

    @property
    def pricing_behaviour(self):
        """Gets the pricing_behaviour of this ProductRatePlanMigrationCharge.  # noqa: E501


        :return: The pricing_behaviour of this ProductRatePlanMigrationCharge.  # noqa: E501
        :rtype: str
        """
        return self._pricing_behaviour

    @pricing_behaviour.setter
    def pricing_behaviour(self, pricing_behaviour):
        """Sets the pricing_behaviour of this ProductRatePlanMigrationCharge.


        :param pricing_behaviour: The pricing_behaviour of this ProductRatePlanMigrationCharge.  # noqa: E501
        :type: str
        """
        if pricing_behaviour is None:
            raise ValueError("Invalid value for `pricing_behaviour`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "Full", "Difference", "DifferenceProRated", "ProRated"]  # noqa: E501
        if pricing_behaviour not in allowed_values:
            raise ValueError(
                "Invalid value for `pricing_behaviour` ({0}), must be one of {1}"  # noqa: E501
                .format(pricing_behaviour, allowed_values)
            )

        self._pricing_behaviour = pricing_behaviour

    @property
    def same_period(self):
        """Gets the same_period of this ProductRatePlanMigrationCharge.  # noqa: E501


        :return: The same_period of this ProductRatePlanMigrationCharge.  # noqa: E501
        :rtype: bool
        """
        return self._same_period

    @same_period.setter
    def same_period(self, same_period):
        """Sets the same_period of this ProductRatePlanMigrationCharge.


        :param same_period: The same_period of this ProductRatePlanMigrationCharge.  # noqa: E501
        :type: bool
        """

        self._same_period = same_period

    @property
    def original_product_rate_plan_id(self):
        """Gets the original_product_rate_plan_id of this ProductRatePlanMigrationCharge.  # noqa: E501


        :return: The original_product_rate_plan_id of this ProductRatePlanMigrationCharge.  # noqa: E501
        :rtype: str
        """
        return self._original_product_rate_plan_id

    @original_product_rate_plan_id.setter
    def original_product_rate_plan_id(self, original_product_rate_plan_id):
        """Sets the original_product_rate_plan_id of this ProductRatePlanMigrationCharge.


        :param original_product_rate_plan_id: The original_product_rate_plan_id of this ProductRatePlanMigrationCharge.  # noqa: E501
        :type: str
        """

        self._original_product_rate_plan_id = original_product_rate_plan_id

    @property
    def original_public_product_rate_plan_name(self):
        """Gets the original_public_product_rate_plan_name of this ProductRatePlanMigrationCharge.  # noqa: E501


        :return: The original_public_product_rate_plan_name of this ProductRatePlanMigrationCharge.  # noqa: E501
        :rtype: str
        """
        return self._original_public_product_rate_plan_name

    @original_public_product_rate_plan_name.setter
    def original_public_product_rate_plan_name(self, original_public_product_rate_plan_name):
        """Sets the original_public_product_rate_plan_name of this ProductRatePlanMigrationCharge.


        :param original_public_product_rate_plan_name: The original_public_product_rate_plan_name of this ProductRatePlanMigrationCharge.  # noqa: E501
        :type: str
        """

        self._original_public_product_rate_plan_name = original_public_product_rate_plan_name

    @property
    def original_product_rate_plan_name(self):
        """Gets the original_product_rate_plan_name of this ProductRatePlanMigrationCharge.  # noqa: E501


        :return: The original_product_rate_plan_name of this ProductRatePlanMigrationCharge.  # noqa: E501
        :rtype: str
        """
        return self._original_product_rate_plan_name

    @original_product_rate_plan_name.setter
    def original_product_rate_plan_name(self, original_product_rate_plan_name):
        """Sets the original_product_rate_plan_name of this ProductRatePlanMigrationCharge.


        :param original_product_rate_plan_name: The original_product_rate_plan_name of this ProductRatePlanMigrationCharge.  # noqa: E501
        :type: str
        """

        self._original_product_rate_plan_name = original_product_rate_plan_name

    @property
    def new_product_rate_plan_id(self):
        """Gets the new_product_rate_plan_id of this ProductRatePlanMigrationCharge.  # noqa: E501


        :return: The new_product_rate_plan_id of this ProductRatePlanMigrationCharge.  # noqa: E501
        :rtype: str
        """
        return self._new_product_rate_plan_id

    @new_product_rate_plan_id.setter
    def new_product_rate_plan_id(self, new_product_rate_plan_id):
        """Sets the new_product_rate_plan_id of this ProductRatePlanMigrationCharge.


        :param new_product_rate_plan_id: The new_product_rate_plan_id of this ProductRatePlanMigrationCharge.  # noqa: E501
        :type: str
        """

        self._new_product_rate_plan_id = new_product_rate_plan_id

    @property
    def new_public_product_rate_plan_name(self):
        """Gets the new_public_product_rate_plan_name of this ProductRatePlanMigrationCharge.  # noqa: E501


        :return: The new_public_product_rate_plan_name of this ProductRatePlanMigrationCharge.  # noqa: E501
        :rtype: str
        """
        return self._new_public_product_rate_plan_name

    @new_public_product_rate_plan_name.setter
    def new_public_product_rate_plan_name(self, new_public_product_rate_plan_name):
        """Sets the new_public_product_rate_plan_name of this ProductRatePlanMigrationCharge.


        :param new_public_product_rate_plan_name: The new_public_product_rate_plan_name of this ProductRatePlanMigrationCharge.  # noqa: E501
        :type: str
        """

        self._new_public_product_rate_plan_name = new_public_product_rate_plan_name

    @property
    def new_product_rate_plan_name(self):
        """Gets the new_product_rate_plan_name of this ProductRatePlanMigrationCharge.  # noqa: E501


        :return: The new_product_rate_plan_name of this ProductRatePlanMigrationCharge.  # noqa: E501
        :rtype: str
        """
        return self._new_product_rate_plan_name

    @new_product_rate_plan_name.setter
    def new_product_rate_plan_name(self, new_product_rate_plan_name):
        """Sets the new_product_rate_plan_name of this ProductRatePlanMigrationCharge.


        :param new_product_rate_plan_name: The new_product_rate_plan_name of this ProductRatePlanMigrationCharge.  # noqa: E501
        :type: str
        """

        self._new_product_rate_plan_name = new_product_rate_plan_name

    @property
    def new_product_id(self):
        """Gets the new_product_id of this ProductRatePlanMigrationCharge.  # noqa: E501


        :return: The new_product_id of this ProductRatePlanMigrationCharge.  # noqa: E501
        :rtype: str
        """
        return self._new_product_id

    @new_product_id.setter
    def new_product_id(self, new_product_id):
        """Sets the new_product_id of this ProductRatePlanMigrationCharge.


        :param new_product_id: The new_product_id of this ProductRatePlanMigrationCharge.  # noqa: E501
        :type: str
        """

        self._new_product_id = new_product_id

    @property
    def new_public_product_name(self):
        """Gets the new_public_product_name of this ProductRatePlanMigrationCharge.  # noqa: E501


        :return: The new_public_product_name of this ProductRatePlanMigrationCharge.  # noqa: E501
        :rtype: str
        """
        return self._new_public_product_name

    @new_public_product_name.setter
    def new_public_product_name(self, new_public_product_name):
        """Sets the new_public_product_name of this ProductRatePlanMigrationCharge.


        :param new_public_product_name: The new_public_product_name of this ProductRatePlanMigrationCharge.  # noqa: E501
        :type: str
        """

        self._new_public_product_name = new_public_product_name

    @property
    def new_product_name(self):
        """Gets the new_product_name of this ProductRatePlanMigrationCharge.  # noqa: E501


        :return: The new_product_name of this ProductRatePlanMigrationCharge.  # noqa: E501
        :rtype: str
        """
        return self._new_product_name

    @new_product_name.setter
    def new_product_name(self, new_product_name):
        """Sets the new_product_name of this ProductRatePlanMigrationCharge.


        :param new_product_name: The new_product_name of this ProductRatePlanMigrationCharge.  # noqa: E501
        :type: str
        """

        self._new_product_name = new_product_name

    @property
    def pricing_component_values(self):
        """Gets the pricing_component_values of this ProductRatePlanMigrationCharge.  # noqa: E501


        :return: The pricing_component_values of this ProductRatePlanMigrationCharge.  # noqa: E501
        :rtype: list[PricingComponentMigrationValue]
        """
        return self._pricing_component_values

    @pricing_component_values.setter
    def pricing_component_values(self, pricing_component_values):
        """Sets the pricing_component_values of this ProductRatePlanMigrationCharge.


        :param pricing_component_values: The pricing_component_values of this ProductRatePlanMigrationCharge.  # noqa: E501
        :type: list[PricingComponentMigrationValue]
        """

        self._pricing_component_values = pricing_component_values

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
        if issubclass(ProductRatePlanMigrationCharge, dict):
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
        if not isinstance(other, ProductRatePlanMigrationCharge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
