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

class CouponDiscount(object):
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
        'pricing_component': 'str',
        'pricing_component_name': 'str',
        'pricing_component_id': 'str',
        'unit_of_measure_name': 'str',
        'unit_of_measure_id': 'str',
        'units_free': 'int',
        'percentage_discount': 'float',
        'cash_discount': 'float',
        'tax_code': 'str',
        'organization_id': 'str'
    }

    attribute_map = {
        'created': 'created',
        'changed_by': 'changedBy',
        'updated': 'updated',
        'id': 'id',
        'pricing_component': 'pricingComponent',
        'pricing_component_name': 'pricingComponentName',
        'pricing_component_id': 'pricingComponentID',
        'unit_of_measure_name': 'unitOfMeasureName',
        'unit_of_measure_id': 'unitOfMeasureID',
        'units_free': 'unitsFree',
        'percentage_discount': 'percentageDiscount',
        'cash_discount': 'cashDiscount',
        'tax_code': 'taxCode',
        'organization_id': 'organizationID'
    }

    def __init__(self, created=None, changed_by=None, updated=None, id=None, pricing_component=None, pricing_component_name=None, pricing_component_id=None, unit_of_measure_name=None, unit_of_measure_id=None, units_free=None, percentage_discount=None, cash_discount=None, tax_code=None, organization_id=None):  # noqa: E501
        """CouponDiscount - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._changed_by = None
        self._updated = None
        self._id = None
        self._pricing_component = None
        self._pricing_component_name = None
        self._pricing_component_id = None
        self._unit_of_measure_name = None
        self._unit_of_measure_id = None
        self._units_free = None
        self._percentage_discount = None
        self._cash_discount = None
        self._tax_code = None
        self._organization_id = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if changed_by is not None:
            self.changed_by = changed_by
        if updated is not None:
            self.updated = updated
        if id is not None:
            self.id = id
        if pricing_component is not None:
            self.pricing_component = pricing_component
        if pricing_component_name is not None:
            self.pricing_component_name = pricing_component_name
        if pricing_component_id is not None:
            self.pricing_component_id = pricing_component_id
        if unit_of_measure_name is not None:
            self.unit_of_measure_name = unit_of_measure_name
        if unit_of_measure_id is not None:
            self.unit_of_measure_id = unit_of_measure_id
        if units_free is not None:
            self.units_free = units_free
        if percentage_discount is not None:
            self.percentage_discount = percentage_discount
        if cash_discount is not None:
            self.cash_discount = cash_discount
        if tax_code is not None:
            self.tax_code = tax_code
        if organization_id is not None:
            self.organization_id = organization_id

    @property
    def created(self):
        """Gets the created of this CouponDiscount.  # noqa: E501


        :return: The created of this CouponDiscount.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CouponDiscount.


        :param created: The created of this CouponDiscount.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """Gets the changed_by of this CouponDiscount.  # noqa: E501


        :return: The changed_by of this CouponDiscount.  # noqa: E501
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """Sets the changed_by of this CouponDiscount.


        :param changed_by: The changed_by of this CouponDiscount.  # noqa: E501
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """Gets the updated of this CouponDiscount.  # noqa: E501


        :return: The updated of this CouponDiscount.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this CouponDiscount.


        :param updated: The updated of this CouponDiscount.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """Gets the id of this CouponDiscount.  # noqa: E501


        :return: The id of this CouponDiscount.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CouponDiscount.


        :param id: The id of this CouponDiscount.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def pricing_component(self):
        """Gets the pricing_component of this CouponDiscount.  # noqa: E501


        :return: The pricing_component of this CouponDiscount.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component

    @pricing_component.setter
    def pricing_component(self, pricing_component):
        """Sets the pricing_component of this CouponDiscount.


        :param pricing_component: The pricing_component of this CouponDiscount.  # noqa: E501
        :type: str
        """

        self._pricing_component = pricing_component

    @property
    def pricing_component_name(self):
        """Gets the pricing_component_name of this CouponDiscount.  # noqa: E501


        :return: The pricing_component_name of this CouponDiscount.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component_name

    @pricing_component_name.setter
    def pricing_component_name(self, pricing_component_name):
        """Sets the pricing_component_name of this CouponDiscount.


        :param pricing_component_name: The pricing_component_name of this CouponDiscount.  # noqa: E501
        :type: str
        """

        self._pricing_component_name = pricing_component_name

    @property
    def pricing_component_id(self):
        """Gets the pricing_component_id of this CouponDiscount.  # noqa: E501


        :return: The pricing_component_id of this CouponDiscount.  # noqa: E501
        :rtype: str
        """
        return self._pricing_component_id

    @pricing_component_id.setter
    def pricing_component_id(self, pricing_component_id):
        """Sets the pricing_component_id of this CouponDiscount.


        :param pricing_component_id: The pricing_component_id of this CouponDiscount.  # noqa: E501
        :type: str
        """

        self._pricing_component_id = pricing_component_id

    @property
    def unit_of_measure_name(self):
        """Gets the unit_of_measure_name of this CouponDiscount.  # noqa: E501


        :return: The unit_of_measure_name of this CouponDiscount.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measure_name

    @unit_of_measure_name.setter
    def unit_of_measure_name(self, unit_of_measure_name):
        """Sets the unit_of_measure_name of this CouponDiscount.


        :param unit_of_measure_name: The unit_of_measure_name of this CouponDiscount.  # noqa: E501
        :type: str
        """

        self._unit_of_measure_name = unit_of_measure_name

    @property
    def unit_of_measure_id(self):
        """Gets the unit_of_measure_id of this CouponDiscount.  # noqa: E501


        :return: The unit_of_measure_id of this CouponDiscount.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measure_id

    @unit_of_measure_id.setter
    def unit_of_measure_id(self, unit_of_measure_id):
        """Sets the unit_of_measure_id of this CouponDiscount.


        :param unit_of_measure_id: The unit_of_measure_id of this CouponDiscount.  # noqa: E501
        :type: str
        """

        self._unit_of_measure_id = unit_of_measure_id

    @property
    def units_free(self):
        """Gets the units_free of this CouponDiscount.  # noqa: E501


        :return: The units_free of this CouponDiscount.  # noqa: E501
        :rtype: int
        """
        return self._units_free

    @units_free.setter
    def units_free(self, units_free):
        """Sets the units_free of this CouponDiscount.


        :param units_free: The units_free of this CouponDiscount.  # noqa: E501
        :type: int
        """

        self._units_free = units_free

    @property
    def percentage_discount(self):
        """Gets the percentage_discount of this CouponDiscount.  # noqa: E501


        :return: The percentage_discount of this CouponDiscount.  # noqa: E501
        :rtype: float
        """
        return self._percentage_discount

    @percentage_discount.setter
    def percentage_discount(self, percentage_discount):
        """Sets the percentage_discount of this CouponDiscount.


        :param percentage_discount: The percentage_discount of this CouponDiscount.  # noqa: E501
        :type: float
        """

        self._percentage_discount = percentage_discount

    @property
    def cash_discount(self):
        """Gets the cash_discount of this CouponDiscount.  # noqa: E501


        :return: The cash_discount of this CouponDiscount.  # noqa: E501
        :rtype: float
        """
        return self._cash_discount

    @cash_discount.setter
    def cash_discount(self, cash_discount):
        """Sets the cash_discount of this CouponDiscount.


        :param cash_discount: The cash_discount of this CouponDiscount.  # noqa: E501
        :type: float
        """

        self._cash_discount = cash_discount

    @property
    def tax_code(self):
        """Gets the tax_code of this CouponDiscount.  # noqa: E501


        :return: The tax_code of this CouponDiscount.  # noqa: E501
        :rtype: str
        """
        return self._tax_code

    @tax_code.setter
    def tax_code(self, tax_code):
        """Sets the tax_code of this CouponDiscount.


        :param tax_code: The tax_code of this CouponDiscount.  # noqa: E501
        :type: str
        """

        self._tax_code = tax_code

    @property
    def organization_id(self):
        """Gets the organization_id of this CouponDiscount.  # noqa: E501


        :return: The organization_id of this CouponDiscount.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this CouponDiscount.


        :param organization_id: The organization_id of this CouponDiscount.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

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
        if issubclass(CouponDiscount, dict):
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
        if not isinstance(other, CouponDiscount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
