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

class CouponWrapperResponse(object):
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
        'changed_by': 'str',
        'updated': 'datetime',
        'id': 'str',
        'organization_id': 'str',
        'coupon_code': 'str',
        'discount': 'float',
        'discount_excluding_tax': 'float',
        'calculation': 'str',
        'pricing_component_name': 'str',
        'pricing_component_id': 'str'
    }

    attribute_map = {
        'created': 'created',
        'changed_by': 'changedBy',
        'updated': 'updated',
        'id': 'id',
        'organization_id': 'organizationID',
        'coupon_code': 'couponCode',
        'discount': 'discount',
        'discount_excluding_tax': 'discountExcludingTax',
        'calculation': 'calculation',
        'pricing_component_name': 'pricingComponentName',
        'pricing_component_id': 'pricingComponentID'
    }

    def __init__(self, created=None, changed_by=None, updated=None, id=None, organization_id=None, coupon_code=None, discount=None, discount_excluding_tax=None, calculation=None, pricing_component_name=None, pricing_component_id=None):  # noqa: E501
        """CouponWrapperResponse - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._changed_by = None
        self._updated = None
        self._id = None
        self._organization_id = None
        self._coupon_code = None
        self._discount = None
        self._discount_excluding_tax = None
        self._calculation = None
        self._pricing_component_name = None
        self._pricing_component_id = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if changed_by is not None:
            self.changed_by = changed_by
        if updated is not None:
            self.updated = updated
        if id is not None:
            self.id = id
        if organization_id is not None:
            self.organization_id = organization_id
        if coupon_code is not None:
            self.coupon_code = coupon_code
        if discount is not None:
            self.discount = discount
        if discount_excluding_tax is not None:
            self.discount_excluding_tax = discount_excluding_tax
        if calculation is not None:
            self.calculation = calculation
        if pricing_component_name is not None:
            self.pricing_component_name = pricing_component_name
        if pricing_component_id is not None:
            self.pricing_component_id = pricing_component_id

    @property
    def created(self):
        """Gets the created of this CouponWrapperResponse.  # noqa: E501


        :return: The created of this CouponWrapperResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CouponWrapperResponse.


        :param created: The created of this CouponWrapperResponse.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """Gets the changed_by of this CouponWrapperResponse.  # noqa: E501


        :return: The changed_by of this CouponWrapperResponse.  # noqa: E501
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """Sets the changed_by of this CouponWrapperResponse.


        :param changed_by: The changed_by of this CouponWrapperResponse.  # noqa: E501
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """Gets the updated of this CouponWrapperResponse.  # noqa: E501


        :return: The updated of this CouponWrapperResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this CouponWrapperResponse.


        :param updated: The updated of this CouponWrapperResponse.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """Gets the id of this CouponWrapperResponse.  # noqa: E501


        :return: The id of this CouponWrapperResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CouponWrapperResponse.


        :param id: The id of this CouponWrapperResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def organization_id(self):
        """Gets the organization_id of this CouponWrapperResponse.  # noqa: E501


        :return: The organization_id of this CouponWrapperResponse.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this CouponWrapperResponse.


        :param organization_id: The organization_id of this CouponWrapperResponse.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def coupon_code(self):
        """Gets the coupon_code of this CouponWrapperResponse.  # noqa: E501


        :return: The coupon_code of this CouponWrapperResponse.  # noqa: E501
        :rtype: str
        """
        return self._coupon_code

    @coupon_code.setter
    def coupon_code(self, coupon_code):
        """Sets the coupon_code of this CouponWrapperResponse.


        :param coupon_code: The coupon_code of this CouponWrapperResponse.  # noqa: E501
        :type: str
        """

        self._coupon_code = coupon_code

    @property
    def discount(self):
        """Gets the discount of this CouponWrapperResponse.  # noqa: E501


        :return: The discount of this CouponWrapperResponse.  # noqa: E501
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this CouponWrapperResponse.


        :param discount: The discount of this CouponWrapperResponse.  # noqa: E501
        :type: float
        """

        self._discount = discount

    @property
    def discount_excluding_tax(self):
        """Gets the discount_excluding_tax of this CouponWrapperResponse.  # noqa: E501


        :return: The discount_excluding_tax of this CouponWrapperResponse.  # noqa: E501
        :rtype: float
        """
        return self._discount_excluding_tax

    @discount_excluding_tax.setter
    def discount_excluding_tax(self, discount_excluding_tax):
        """Sets the discount_excluding_tax of this CouponWrapperResponse.


        :param discount_excluding_tax: The discount_excluding_tax of this CouponWrapperResponse.  # noqa: E501
        :type: float
        """

        self._discount_excluding_tax = discount_excluding_tax

    @property
    def calculation(self):
        """Gets the calculation of this CouponWrapperResponse.  # noqa: E501


        :return: The calculation of this CouponWrapperResponse.  # noqa: E501
        :rtype: str
        """
        return self._calculation

    @calculation.setter
    def calculation(self, calculation):
        """Sets the calculation of this CouponWrapperResponse.


        :param calculation: The calculation of this CouponWrapperResponse.  # noqa: E501
        :type: str
        """

        self._calculation = calculation

    @property
    def pricing_component_name(self):
        """Gets the pricing_component_name of this CouponWrapperResponse.  # noqa: E501


        :return: The pricing_component_name of this CouponWrapperResponse.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component_name

    @pricing_component_name.setter
    def pricing_component_name(self, pricing_component_name):
        """Sets the pricing_component_name of this CouponWrapperResponse.


        :param pricing_component_name: The pricing_component_name of this CouponWrapperResponse.  # noqa: E501
        :type: str
        """

        self._pricing_component_name = pricing_component_name

    @property
    def pricing_component_id(self):
        """Gets the pricing_component_id of this CouponWrapperResponse.  # noqa: E501


        :return: The pricing_component_id of this CouponWrapperResponse.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component_id

    @pricing_component_id.setter
    def pricing_component_id(self, pricing_component_id):
        """Sets the pricing_component_id of this CouponWrapperResponse.


        :param pricing_component_id: The pricing_component_id of this CouponWrapperResponse.  # noqa: E501
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
        if issubclass(CouponWrapperResponse, dict):
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
        if not isinstance(other, CouponWrapperResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
