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

class CouponCharge(SubscriptionCharge):
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
        'public_pricing_component_name': 'str',
        'pricing_component_name': 'str',
        'pricing_component_value': 'int',
        'coupon_definition_id': 'str',
        'coupon_instance_id': 'str',
        'coupon_modifier_id': 'str',
        'originating_charge_id': 'str',
        'coupon_code': 'str',
        'coupon_type': 'str',
        'pricing_component_credit_id': 'str'
    }
    if hasattr(SubscriptionCharge, "swagger_types"):
        swagger_types.update(SubscriptionCharge.swagger_types)

    attribute_map = {
        'pricing_component_id': 'pricingComponentID',
        'public_pricing_component_name': 'publicPricingComponentName',
        'pricing_component_name': 'pricingComponentName',
        'pricing_component_value': 'pricingComponentValue',
        'coupon_definition_id': 'couponDefinitionID',
        'coupon_instance_id': 'couponInstanceID',
        'coupon_modifier_id': 'couponModifierID',
        'originating_charge_id': 'originatingChargeID',
        'coupon_code': 'couponCode',
        'coupon_type': 'couponType',
        'pricing_component_credit_id': 'pricingComponentCreditID'
    }
    if hasattr(SubscriptionCharge, "attribute_map"):
        attribute_map.update(SubscriptionCharge.attribute_map)

    def __init__(self, pricing_component_id=None, public_pricing_component_name=None, pricing_component_name=None, pricing_component_value=None, coupon_definition_id=None, coupon_instance_id=None, coupon_modifier_id=None, originating_charge_id=None, coupon_code=None, coupon_type=None, pricing_component_credit_id=None, *args, **kwargs):  # noqa: E501
        """CouponCharge - a model defined in Swagger"""  # noqa: E501
        self._pricing_component_id = None
        self._public_pricing_component_name = None
        self._pricing_component_name = None
        self._pricing_component_value = None
        self._coupon_definition_id = None
        self._coupon_instance_id = None
        self._coupon_modifier_id = None
        self._originating_charge_id = None
        self._coupon_code = None
        self._coupon_type = None
        self._pricing_component_credit_id = None
        self.discriminator = None
        if pricing_component_id is not None:
            self.pricing_component_id = pricing_component_id
        if public_pricing_component_name is not None:
            self.public_pricing_component_name = public_pricing_component_name
        if pricing_component_name is not None:
            self.pricing_component_name = pricing_component_name
        if pricing_component_value is not None:
            self.pricing_component_value = pricing_component_value
        if coupon_definition_id is not None:
            self.coupon_definition_id = coupon_definition_id
        if coupon_instance_id is not None:
            self.coupon_instance_id = coupon_instance_id
        if coupon_modifier_id is not None:
            self.coupon_modifier_id = coupon_modifier_id
        if originating_charge_id is not None:
            self.originating_charge_id = originating_charge_id
        if coupon_code is not None:
            self.coupon_code = coupon_code
        if coupon_type is not None:
            self.coupon_type = coupon_type
        if pricing_component_credit_id is not None:
            self.pricing_component_credit_id = pricing_component_credit_id
        SubscriptionCharge.__init__(self, *args, **kwargs)

    @property
    def pricing_component_id(self):
        """Gets the pricing_component_id of this CouponCharge.  # noqa: E501


        :return: The pricing_component_id of this CouponCharge.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component_id

    @pricing_component_id.setter
    def pricing_component_id(self, pricing_component_id):
        """Sets the pricing_component_id of this CouponCharge.


        :param pricing_component_id: The pricing_component_id of this CouponCharge.  # noqa: E501
        :type: str
        """

        self._pricing_component_id = pricing_component_id

    @property
    def public_pricing_component_name(self):
        """Gets the public_pricing_component_name of this CouponCharge.  # noqa: E501


        :return: The public_pricing_component_name of this CouponCharge.  # noqa: E501
        :rtype: str
        """
        return self._public_pricing_component_name

    @public_pricing_component_name.setter
    def public_pricing_component_name(self, public_pricing_component_name):
        """Sets the public_pricing_component_name of this CouponCharge.


        :param public_pricing_component_name: The public_pricing_component_name of this CouponCharge.  # noqa: E501
        :type: str
        """

        self._public_pricing_component_name = public_pricing_component_name

    @property
    def pricing_component_name(self):
        """Gets the pricing_component_name of this CouponCharge.  # noqa: E501


        :return: The pricing_component_name of this CouponCharge.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component_name

    @pricing_component_name.setter
    def pricing_component_name(self, pricing_component_name):
        """Sets the pricing_component_name of this CouponCharge.


        :param pricing_component_name: The pricing_component_name of this CouponCharge.  # noqa: E501
        :type: str
        """

        self._pricing_component_name = pricing_component_name

    @property
    def pricing_component_value(self):
        """Gets the pricing_component_value of this CouponCharge.  # noqa: E501


        :return: The pricing_component_value of this CouponCharge.  # noqa: E501
        :rtype: int
        """
        return self._pricing_component_value

    @pricing_component_value.setter
    def pricing_component_value(self, pricing_component_value):
        """Sets the pricing_component_value of this CouponCharge.


        :param pricing_component_value: The pricing_component_value of this CouponCharge.  # noqa: E501
        :type: int
        """

        self._pricing_component_value = pricing_component_value

    @property
    def coupon_definition_id(self):
        """Gets the coupon_definition_id of this CouponCharge.  # noqa: E501


        :return: The coupon_definition_id of this CouponCharge.  # noqa: E501
        :rtype: str
        """
        return self._coupon_definition_id

    @coupon_definition_id.setter
    def coupon_definition_id(self, coupon_definition_id):
        """Sets the coupon_definition_id of this CouponCharge.


        :param coupon_definition_id: The coupon_definition_id of this CouponCharge.  # noqa: E501
        :type: str
        """

        self._coupon_definition_id = coupon_definition_id

    @property
    def coupon_instance_id(self):
        """Gets the coupon_instance_id of this CouponCharge.  # noqa: E501


        :return: The coupon_instance_id of this CouponCharge.  # noqa: E501
        :rtype: str
        """
        return self._coupon_instance_id

    @coupon_instance_id.setter
    def coupon_instance_id(self, coupon_instance_id):
        """Sets the coupon_instance_id of this CouponCharge.


        :param coupon_instance_id: The coupon_instance_id of this CouponCharge.  # noqa: E501
        :type: str
        """

        self._coupon_instance_id = coupon_instance_id

    @property
    def coupon_modifier_id(self):
        """Gets the coupon_modifier_id of this CouponCharge.  # noqa: E501


        :return: The coupon_modifier_id of this CouponCharge.  # noqa: E501
        :rtype: str
        """
        return self._coupon_modifier_id

    @coupon_modifier_id.setter
    def coupon_modifier_id(self, coupon_modifier_id):
        """Sets the coupon_modifier_id of this CouponCharge.


        :param coupon_modifier_id: The coupon_modifier_id of this CouponCharge.  # noqa: E501
        :type: str
        """

        self._coupon_modifier_id = coupon_modifier_id

    @property
    def originating_charge_id(self):
        """Gets the originating_charge_id of this CouponCharge.  # noqa: E501


        :return: The originating_charge_id of this CouponCharge.  # noqa: E501
        :rtype: str
        """
        return self._originating_charge_id

    @originating_charge_id.setter
    def originating_charge_id(self, originating_charge_id):
        """Sets the originating_charge_id of this CouponCharge.


        :param originating_charge_id: The originating_charge_id of this CouponCharge.  # noqa: E501
        :type: str
        """

        self._originating_charge_id = originating_charge_id

    @property
    def coupon_code(self):
        """Gets the coupon_code of this CouponCharge.  # noqa: E501


        :return: The coupon_code of this CouponCharge.  # noqa: E501
        :rtype: str
        """
        return self._coupon_code

    @coupon_code.setter
    def coupon_code(self, coupon_code):
        """Sets the coupon_code of this CouponCharge.


        :param coupon_code: The coupon_code of this CouponCharge.  # noqa: E501
        :type: str
        """

        self._coupon_code = coupon_code

    @property
    def coupon_type(self):
        """Gets the coupon_type of this CouponCharge.  # noqa: E501


        :return: The coupon_type of this CouponCharge.  # noqa: E501
        :rtype: str
        """
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, coupon_type):
        """Sets the coupon_type of this CouponCharge.


        :param coupon_type: The coupon_type of this CouponCharge.  # noqa: E501
        :type: str
        """
        allowed_values = ["Coupon", "PricingComponentUnitCredit"]  # noqa: E501
        if coupon_type not in allowed_values:
            raise ValueError(
                "Invalid value for `coupon_type` ({0}), must be one of {1}"  # noqa: E501
                .format(coupon_type, allowed_values)
            )

        self._coupon_type = coupon_type

    @property
    def pricing_component_credit_id(self):
        """Gets the pricing_component_credit_id of this CouponCharge.  # noqa: E501


        :return: The pricing_component_credit_id of this CouponCharge.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component_credit_id

    @pricing_component_credit_id.setter
    def pricing_component_credit_id(self, pricing_component_credit_id):
        """Sets the pricing_component_credit_id of this CouponCharge.


        :param pricing_component_credit_id: The pricing_component_credit_id of this CouponCharge.  # noqa: E501
        :type: str
        """

        self._pricing_component_credit_id = pricing_component_credit_id

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
        if issubclass(CouponCharge, dict):
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
        if not isinstance(other, CouponCharge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
