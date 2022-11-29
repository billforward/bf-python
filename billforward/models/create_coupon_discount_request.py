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

class CreateCouponDiscountRequest(object):
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
        'pricing_component': 'str',
        'unit_of_measure': 'str',
        'units_free': 'int',
        'percentage_discount': 'float',
        'cash_discount': 'float',
        'tax_code': 'str'
    }

    attribute_map = {
        'organization_id': 'organizationID',
        'pricing_component': 'pricingComponent',
        'unit_of_measure': 'unitOfMeasure',
        'units_free': 'unitsFree',
        'percentage_discount': 'percentageDiscount',
        'cash_discount': 'cashDiscount',
        'tax_code': 'taxCode'
    }

    def __init__(self, organization_id=None, pricing_component=None, unit_of_measure=None, units_free=None, percentage_discount=None, cash_discount=None, tax_code=None):  # noqa: E501
        """CreateCouponDiscountRequest - a model defined in Swagger"""  # noqa: E501
        self._organization_id = None
        self._pricing_component = None
        self._unit_of_measure = None
        self._units_free = None
        self._percentage_discount = None
        self._cash_discount = None
        self._tax_code = None
        self.discriminator = None
        if organization_id is not None:
            self.organization_id = organization_id
        if pricing_component is not None:
            self.pricing_component = pricing_component
        if unit_of_measure is not None:
            self.unit_of_measure = unit_of_measure
        if units_free is not None:
            self.units_free = units_free
        if percentage_discount is not None:
            self.percentage_discount = percentage_discount
        if cash_discount is not None:
            self.cash_discount = cash_discount
        if tax_code is not None:
            self.tax_code = tax_code

    @property
    def organization_id(self):
        """Gets the organization_id of this CreateCouponDiscountRequest.  # noqa: E501


        :return: The organization_id of this CreateCouponDiscountRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this CreateCouponDiscountRequest.


        :param organization_id: The organization_id of this CreateCouponDiscountRequest.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def pricing_component(self):
        """Gets the pricing_component of this CreateCouponDiscountRequest.  # noqa: E501


        :return: The pricing_component of this CreateCouponDiscountRequest.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component

    @pricing_component.setter
    def pricing_component(self, pricing_component):
        """Sets the pricing_component of this CreateCouponDiscountRequest.


        :param pricing_component: The pricing_component of this CreateCouponDiscountRequest.  # noqa: E501
        :type: str
        """

        self._pricing_component = pricing_component

    @property
    def unit_of_measure(self):
        """Gets the unit_of_measure of this CreateCouponDiscountRequest.  # noqa: E501


        :return: The unit_of_measure of this CreateCouponDiscountRequest.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """Sets the unit_of_measure of this CreateCouponDiscountRequest.


        :param unit_of_measure: The unit_of_measure of this CreateCouponDiscountRequest.  # noqa: E501
        :type: str
        """

        self._unit_of_measure = unit_of_measure

    @property
    def units_free(self):
        """Gets the units_free of this CreateCouponDiscountRequest.  # noqa: E501


        :return: The units_free of this CreateCouponDiscountRequest.  # noqa: E501
        :rtype: int
        """
        return self._units_free

    @units_free.setter
    def units_free(self, units_free):
        """Sets the units_free of this CreateCouponDiscountRequest.


        :param units_free: The units_free of this CreateCouponDiscountRequest.  # noqa: E501
        :type: int
        """

        self._units_free = units_free

    @property
    def percentage_discount(self):
        """Gets the percentage_discount of this CreateCouponDiscountRequest.  # noqa: E501


        :return: The percentage_discount of this CreateCouponDiscountRequest.  # noqa: E501
        :rtype: float
        """
        return self._percentage_discount

    @percentage_discount.setter
    def percentage_discount(self, percentage_discount):
        """Sets the percentage_discount of this CreateCouponDiscountRequest.


        :param percentage_discount: The percentage_discount of this CreateCouponDiscountRequest.  # noqa: E501
        :type: float
        """

        self._percentage_discount = percentage_discount

    @property
    def cash_discount(self):
        """Gets the cash_discount of this CreateCouponDiscountRequest.  # noqa: E501


        :return: The cash_discount of this CreateCouponDiscountRequest.  # noqa: E501
        :rtype: float
        """
        return self._cash_discount

    @cash_discount.setter
    def cash_discount(self, cash_discount):
        """Sets the cash_discount of this CreateCouponDiscountRequest.


        :param cash_discount: The cash_discount of this CreateCouponDiscountRequest.  # noqa: E501
        :type: float
        """

        self._cash_discount = cash_discount

    @property
    def tax_code(self):
        """Gets the tax_code of this CreateCouponDiscountRequest.  # noqa: E501


        :return: The tax_code of this CreateCouponDiscountRequest.  # noqa: E501
        :rtype: str
        """
        return self._tax_code

    @tax_code.setter
    def tax_code(self, tax_code):
        """Sets the tax_code of this CreateCouponDiscountRequest.


        :param tax_code: The tax_code of this CreateCouponDiscountRequest.  # noqa: E501
        :type: str
        """

        self._tax_code = tax_code

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
        if issubclass(CreateCouponDiscountRequest, dict):
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
        if not isinstance(other, CreateCouponDiscountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
