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

class ApiQuote(object):
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
        'subtotal': 'float',
        'subtotal_excluding_tax': 'float',
        'total': 'float',
        'total_excluding_tax': 'float',
        'tax': 'float',
        'discount': 'float',
        'discount_excluding_tax': 'float',
        'currency': 'CreditNoteCurrency',
        'product_name': 'str',
        'public_product_name': 'str',
        'product_rate_plan_name': 'str',
        'public_product_rate_plan_name': 'str',
        'product_id': 'str',
        'product_rate_plan_id': 'str',
        'subscription_id': 'str',
        'account_id': 'str',
        'quantities': 'list[APIQuoteResponseQuantity]',
        'discounts': 'list[CouponWrapperResponse]',
        'quote_for': 'str',
        'period_start': 'datetime',
        'period_end': 'datetime',
        'total_periods': 'float',
        'proration_enabled': 'bool',
        'uplift': 'float',
        'coupon_codes': 'list[str]',
        'organization_id': 'str',
        'same_product_period': 'bool',
        'purchase_order': 'str'
    }

    attribute_map = {
        'created': 'created',
        'changed_by': 'changedBy',
        'updated': 'updated',
        'id': 'id',
        'subtotal': 'subtotal',
        'subtotal_excluding_tax': 'subtotalExcludingTax',
        'total': 'total',
        'total_excluding_tax': 'totalExcludingTax',
        'tax': 'tax',
        'discount': 'discount',
        'discount_excluding_tax': 'discountExcludingTax',
        'currency': 'currency',
        'product_name': 'productName',
        'public_product_name': 'publicProductName',
        'product_rate_plan_name': 'productRatePlanName',
        'public_product_rate_plan_name': 'publicProductRatePlanName',
        'product_id': 'productID',
        'product_rate_plan_id': 'productRatePlanID',
        'subscription_id': 'subscriptionID',
        'account_id': 'accountID',
        'quantities': 'quantities',
        'discounts': 'discounts',
        'quote_for': 'quoteFor',
        'period_start': 'periodStart',
        'period_end': 'periodEnd',
        'total_periods': 'totalPeriods',
        'proration_enabled': 'prorationEnabled',
        'uplift': 'uplift',
        'coupon_codes': 'couponCodes',
        'organization_id': 'organizationID',
        'same_product_period': 'sameProductPeriod',
        'purchase_order': 'purchaseOrder'
    }

    def __init__(self, created=None, changed_by=None, updated=None, id=None, subtotal=None, subtotal_excluding_tax=None, total=None, total_excluding_tax=None, tax=None, discount=None, discount_excluding_tax=None, currency=None, product_name=None, public_product_name=None, product_rate_plan_name=None, public_product_rate_plan_name=None, product_id=None, product_rate_plan_id=None, subscription_id=None, account_id=None, quantities=None, discounts=None, quote_for=None, period_start=None, period_end=None, total_periods=None, proration_enabled=None, uplift=None, coupon_codes=None, organization_id=None, same_product_period=None, purchase_order=None):  # noqa: E501
        """ApiQuote - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._changed_by = None
        self._updated = None
        self._id = None
        self._subtotal = None
        self._subtotal_excluding_tax = None
        self._total = None
        self._total_excluding_tax = None
        self._tax = None
        self._discount = None
        self._discount_excluding_tax = None
        self._currency = None
        self._product_name = None
        self._public_product_name = None
        self._product_rate_plan_name = None
        self._public_product_rate_plan_name = None
        self._product_id = None
        self._product_rate_plan_id = None
        self._subscription_id = None
        self._account_id = None
        self._quantities = None
        self._discounts = None
        self._quote_for = None
        self._period_start = None
        self._period_end = None
        self._total_periods = None
        self._proration_enabled = None
        self._uplift = None
        self._coupon_codes = None
        self._organization_id = None
        self._same_product_period = None
        self._purchase_order = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if changed_by is not None:
            self.changed_by = changed_by
        if updated is not None:
            self.updated = updated
        if id is not None:
            self.id = id
        if subtotal is not None:
            self.subtotal = subtotal
        if subtotal_excluding_tax is not None:
            self.subtotal_excluding_tax = subtotal_excluding_tax
        if total is not None:
            self.total = total
        if total_excluding_tax is not None:
            self.total_excluding_tax = total_excluding_tax
        if tax is not None:
            self.tax = tax
        if discount is not None:
            self.discount = discount
        if discount_excluding_tax is not None:
            self.discount_excluding_tax = discount_excluding_tax
        if currency is not None:
            self.currency = currency
        if product_name is not None:
            self.product_name = product_name
        if public_product_name is not None:
            self.public_product_name = public_product_name
        if product_rate_plan_name is not None:
            self.product_rate_plan_name = product_rate_plan_name
        if public_product_rate_plan_name is not None:
            self.public_product_rate_plan_name = public_product_rate_plan_name
        if product_id is not None:
            self.product_id = product_id
        if product_rate_plan_id is not None:
            self.product_rate_plan_id = product_rate_plan_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if account_id is not None:
            self.account_id = account_id
        if quantities is not None:
            self.quantities = quantities
        if discounts is not None:
            self.discounts = discounts
        if quote_for is not None:
            self.quote_for = quote_for
        self.period_start = period_start
        self.period_end = period_end
        if total_periods is not None:
            self.total_periods = total_periods
        if proration_enabled is not None:
            self.proration_enabled = proration_enabled
        if uplift is not None:
            self.uplift = uplift
        if coupon_codes is not None:
            self.coupon_codes = coupon_codes
        if organization_id is not None:
            self.organization_id = organization_id
        if same_product_period is not None:
            self.same_product_period = same_product_period
        if purchase_order is not None:
            self.purchase_order = purchase_order

    @property
    def created(self):
        """Gets the created of this ApiQuote.  # noqa: E501


        :return: The created of this ApiQuote.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ApiQuote.


        :param created: The created of this ApiQuote.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """Gets the changed_by of this ApiQuote.  # noqa: E501


        :return: The changed_by of this ApiQuote.  # noqa: E501
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """Sets the changed_by of this ApiQuote.


        :param changed_by: The changed_by of this ApiQuote.  # noqa: E501
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """Gets the updated of this ApiQuote.  # noqa: E501


        :return: The updated of this ApiQuote.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ApiQuote.


        :param updated: The updated of this ApiQuote.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """Gets the id of this ApiQuote.  # noqa: E501


        :return: The id of this ApiQuote.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiQuote.


        :param id: The id of this ApiQuote.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def subtotal(self):
        """Gets the subtotal of this ApiQuote.  # noqa: E501


        :return: The subtotal of this ApiQuote.  # noqa: E501
        :rtype: float
        """
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        """Sets the subtotal of this ApiQuote.


        :param subtotal: The subtotal of this ApiQuote.  # noqa: E501
        :type: float
        """

        self._subtotal = subtotal

    @property
    def subtotal_excluding_tax(self):
        """Gets the subtotal_excluding_tax of this ApiQuote.  # noqa: E501


        :return: The subtotal_excluding_tax of this ApiQuote.  # noqa: E501
        :rtype: float
        """
        return self._subtotal_excluding_tax

    @subtotal_excluding_tax.setter
    def subtotal_excluding_tax(self, subtotal_excluding_tax):
        """Sets the subtotal_excluding_tax of this ApiQuote.


        :param subtotal_excluding_tax: The subtotal_excluding_tax of this ApiQuote.  # noqa: E501
        :type: float
        """

        self._subtotal_excluding_tax = subtotal_excluding_tax

    @property
    def total(self):
        """Gets the total of this ApiQuote.  # noqa: E501


        :return: The total of this ApiQuote.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ApiQuote.


        :param total: The total of this ApiQuote.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def total_excluding_tax(self):
        """Gets the total_excluding_tax of this ApiQuote.  # noqa: E501


        :return: The total_excluding_tax of this ApiQuote.  # noqa: E501
        :rtype: float
        """
        return self._total_excluding_tax

    @total_excluding_tax.setter
    def total_excluding_tax(self, total_excluding_tax):
        """Sets the total_excluding_tax of this ApiQuote.


        :param total_excluding_tax: The total_excluding_tax of this ApiQuote.  # noqa: E501
        :type: float
        """

        self._total_excluding_tax = total_excluding_tax

    @property
    def tax(self):
        """Gets the tax of this ApiQuote.  # noqa: E501


        :return: The tax of this ApiQuote.  # noqa: E501
        :rtype: float
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this ApiQuote.


        :param tax: The tax of this ApiQuote.  # noqa: E501
        :type: float
        """

        self._tax = tax

    @property
    def discount(self):
        """Gets the discount of this ApiQuote.  # noqa: E501


        :return: The discount of this ApiQuote.  # noqa: E501
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this ApiQuote.


        :param discount: The discount of this ApiQuote.  # noqa: E501
        :type: float
        """

        self._discount = discount

    @property
    def discount_excluding_tax(self):
        """Gets the discount_excluding_tax of this ApiQuote.  # noqa: E501


        :return: The discount_excluding_tax of this ApiQuote.  # noqa: E501
        :rtype: float
        """
        return self._discount_excluding_tax

    @discount_excluding_tax.setter
    def discount_excluding_tax(self, discount_excluding_tax):
        """Sets the discount_excluding_tax of this ApiQuote.


        :param discount_excluding_tax: The discount_excluding_tax of this ApiQuote.  # noqa: E501
        :type: float
        """

        self._discount_excluding_tax = discount_excluding_tax

    @property
    def currency(self):
        """Gets the currency of this ApiQuote.  # noqa: E501


        :return: The currency of this ApiQuote.  # noqa: E501
        :rtype: CreditNoteCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ApiQuote.


        :param currency: The currency of this ApiQuote.  # noqa: E501
        :type: CreditNoteCurrency
        """

        self._currency = currency

    @property
    def product_name(self):
        """Gets the product_name of this ApiQuote.  # noqa: E501


        :return: The product_name of this ApiQuote.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this ApiQuote.


        :param product_name: The product_name of this ApiQuote.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def public_product_name(self):
        """Gets the public_product_name of this ApiQuote.  # noqa: E501


        :return: The public_product_name of this ApiQuote.  # noqa: E501
        :rtype: str
        """
        return self._public_product_name

    @public_product_name.setter
    def public_product_name(self, public_product_name):
        """Sets the public_product_name of this ApiQuote.


        :param public_product_name: The public_product_name of this ApiQuote.  # noqa: E501
        :type: str
        """

        self._public_product_name = public_product_name

    @property
    def product_rate_plan_name(self):
        """Gets the product_rate_plan_name of this ApiQuote.  # noqa: E501


        :return: The product_rate_plan_name of this ApiQuote.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_name

    @product_rate_plan_name.setter
    def product_rate_plan_name(self, product_rate_plan_name):
        """Sets the product_rate_plan_name of this ApiQuote.


        :param product_rate_plan_name: The product_rate_plan_name of this ApiQuote.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_name = product_rate_plan_name

    @property
    def public_product_rate_plan_name(self):
        """Gets the public_product_rate_plan_name of this ApiQuote.  # noqa: E501


        :return: The public_product_rate_plan_name of this ApiQuote.  # noqa: E501
        :rtype: str
        """
        return self._public_product_rate_plan_name

    @public_product_rate_plan_name.setter
    def public_product_rate_plan_name(self, public_product_rate_plan_name):
        """Sets the public_product_rate_plan_name of this ApiQuote.


        :param public_product_rate_plan_name: The public_product_rate_plan_name of this ApiQuote.  # noqa: E501
        :type: str
        """

        self._public_product_rate_plan_name = public_product_rate_plan_name

    @property
    def product_id(self):
        """Gets the product_id of this ApiQuote.  # noqa: E501


        :return: The product_id of this ApiQuote.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ApiQuote.


        :param product_id: The product_id of this ApiQuote.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def product_rate_plan_id(self):
        """Gets the product_rate_plan_id of this ApiQuote.  # noqa: E501


        :return: The product_rate_plan_id of this ApiQuote.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_id

    @product_rate_plan_id.setter
    def product_rate_plan_id(self, product_rate_plan_id):
        """Sets the product_rate_plan_id of this ApiQuote.


        :param product_rate_plan_id: The product_rate_plan_id of this ApiQuote.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_id = product_rate_plan_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this ApiQuote.  # noqa: E501


        :return: The subscription_id of this ApiQuote.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this ApiQuote.


        :param subscription_id: The subscription_id of this ApiQuote.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def account_id(self):
        """Gets the account_id of this ApiQuote.  # noqa: E501


        :return: The account_id of this ApiQuote.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ApiQuote.


        :param account_id: The account_id of this ApiQuote.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def quantities(self):
        """Gets the quantities of this ApiQuote.  # noqa: E501


        :return: The quantities of this ApiQuote.  # noqa: E501
        :rtype: list[APIQuoteResponseQuantity]
        """
        return self._quantities

    @quantities.setter
    def quantities(self, quantities):
        """Sets the quantities of this ApiQuote.


        :param quantities: The quantities of this ApiQuote.  # noqa: E501
        :type: list[APIQuoteResponseQuantity]
        """

        self._quantities = quantities

    @property
    def discounts(self):
        """Gets the discounts of this ApiQuote.  # noqa: E501


        :return: The discounts of this ApiQuote.  # noqa: E501
        :rtype: list[CouponWrapperResponse]
        """
        return self._discounts

    @discounts.setter
    def discounts(self, discounts):
        """Sets the discounts of this ApiQuote.


        :param discounts: The discounts of this ApiQuote.  # noqa: E501
        :type: list[CouponWrapperResponse]
        """

        self._discounts = discounts

    @property
    def quote_for(self):
        """Gets the quote_for of this ApiQuote.  # noqa: E501


        :return: The quote_for of this ApiQuote.  # noqa: E501
        :rtype: str
        """
        return self._quote_for

    @quote_for.setter
    def quote_for(self, quote_for):
        """Sets the quote_for of this ApiQuote.


        :param quote_for: The quote_for of this ApiQuote.  # noqa: E501
        :type: str
        """
        allowed_values = ["InitialPeriod", "RecurringPeriod", "Upgrade", "Migration"]  # noqa: E501
        if quote_for not in allowed_values:
            raise ValueError(
                "Invalid value for `quote_for` ({0}), must be one of {1}"  # noqa: E501
                .format(quote_for, allowed_values)
            )

        self._quote_for = quote_for

    @property
    def period_start(self):
        """Gets the period_start of this ApiQuote.  # noqa: E501


        :return: The period_start of this ApiQuote.  # noqa: E501
        :rtype: datetime
        """
        return self._period_start

    @period_start.setter
    def period_start(self, period_start):
        """Sets the period_start of this ApiQuote.


        :param period_start: The period_start of this ApiQuote.  # noqa: E501
        :type: datetime
        """
        if period_start is None:
            raise ValueError("Invalid value for `period_start`, must not be `None`")  # noqa: E501

        self._period_start = period_start

    @property
    def period_end(self):
        """Gets the period_end of this ApiQuote.  # noqa: E501


        :return: The period_end of this ApiQuote.  # noqa: E501
        :rtype: datetime
        """
        return self._period_end

    @period_end.setter
    def period_end(self, period_end):
        """Sets the period_end of this ApiQuote.


        :param period_end: The period_end of this ApiQuote.  # noqa: E501
        :type: datetime
        """
        if period_end is None:
            raise ValueError("Invalid value for `period_end`, must not be `None`")  # noqa: E501

        self._period_end = period_end

    @property
    def total_periods(self):
        """Gets the total_periods of this ApiQuote.  # noqa: E501


        :return: The total_periods of this ApiQuote.  # noqa: E501
        :rtype: float
        """
        return self._total_periods

    @total_periods.setter
    def total_periods(self, total_periods):
        """Sets the total_periods of this ApiQuote.


        :param total_periods: The total_periods of this ApiQuote.  # noqa: E501
        :type: float
        """

        self._total_periods = total_periods

    @property
    def proration_enabled(self):
        """Gets the proration_enabled of this ApiQuote.  # noqa: E501


        :return: The proration_enabled of this ApiQuote.  # noqa: E501
        :rtype: bool
        """
        return self._proration_enabled

    @proration_enabled.setter
    def proration_enabled(self, proration_enabled):
        """Sets the proration_enabled of this ApiQuote.


        :param proration_enabled: The proration_enabled of this ApiQuote.  # noqa: E501
        :type: bool
        """

        self._proration_enabled = proration_enabled

    @property
    def uplift(self):
        """Gets the uplift of this ApiQuote.  # noqa: E501


        :return: The uplift of this ApiQuote.  # noqa: E501
        :rtype: float
        """
        return self._uplift

    @uplift.setter
    def uplift(self, uplift):
        """Sets the uplift of this ApiQuote.


        :param uplift: The uplift of this ApiQuote.  # noqa: E501
        :type: float
        """

        self._uplift = uplift

    @property
    def coupon_codes(self):
        """Gets the coupon_codes of this ApiQuote.  # noqa: E501


        :return: The coupon_codes of this ApiQuote.  # noqa: E501
        :rtype: list[str]
        """
        return self._coupon_codes

    @coupon_codes.setter
    def coupon_codes(self, coupon_codes):
        """Sets the coupon_codes of this ApiQuote.


        :param coupon_codes: The coupon_codes of this ApiQuote.  # noqa: E501
        :type: list[str]
        """

        self._coupon_codes = coupon_codes

    @property
    def organization_id(self):
        """Gets the organization_id of this ApiQuote.  # noqa: E501


        :return: The organization_id of this ApiQuote.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ApiQuote.


        :param organization_id: The organization_id of this ApiQuote.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def same_product_period(self):
        """Gets the same_product_period of this ApiQuote.  # noqa: E501


        :return: The same_product_period of this ApiQuote.  # noqa: E501
        :rtype: bool
        """
        return self._same_product_period

    @same_product_period.setter
    def same_product_period(self, same_product_period):
        """Sets the same_product_period of this ApiQuote.


        :param same_product_period: The same_product_period of this ApiQuote.  # noqa: E501
        :type: bool
        """

        self._same_product_period = same_product_period

    @property
    def purchase_order(self):
        """Gets the purchase_order of this ApiQuote.  # noqa: E501


        :return: The purchase_order of this ApiQuote.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order

    @purchase_order.setter
    def purchase_order(self, purchase_order):
        """Sets the purchase_order of this ApiQuote.


        :param purchase_order: The purchase_order of this ApiQuote.  # noqa: E501
        :type: str
        """

        self._purchase_order = purchase_order

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
        if issubclass(ApiQuote, dict):
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
        if not isinstance(other, ApiQuote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
