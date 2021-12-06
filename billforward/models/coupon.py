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

class Coupon(object):
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
        'name': 'str',
        'coupon_code': 'str',
        'coupons': 'int',
        'uses': 'int',
        'product': 'str',
        'product_name': 'str',
        'product_id': 'str',
        'product_rate_plan': 'str',
        'product_rate_plan_name': 'str',
        'product_rate_plan_id': 'str',
        'currency': 'CreditNoteCurrency',
        'parent_coupon_code_redeemable': 'bool',
        'organization_id': 'str',
        'discounts': 'list[CouponDiscount]',
        'deleted': 'bool',
        'parent_coupon_code': 'str',
        'applies_to': 'str',
        'applies_to_id': 'str',
        'remaining_uses': 'int',
        'used': 'int',
        'valid_until': 'datetime',
        'instance_details': 'CouponInstance',
        'master_code_redeemable': 'bool'
    }

    attribute_map = {
        'created': 'created',
        'changed_by': 'changedBy',
        'updated': 'updated',
        'id': 'id',
        'name': 'name',
        'coupon_code': 'couponCode',
        'coupons': 'coupons',
        'uses': 'uses',
        'product': 'product',
        'product_name': 'productName',
        'product_id': 'productID',
        'product_rate_plan': 'productRatePlan',
        'product_rate_plan_name': 'productRatePlanName',
        'product_rate_plan_id': 'productRatePlanID',
        'currency': 'currency',
        'parent_coupon_code_redeemable': 'parentCouponCodeRedeemable',
        'organization_id': 'organizationID',
        'discounts': 'discounts',
        'deleted': 'deleted',
        'parent_coupon_code': 'parentCouponCode',
        'applies_to': 'appliesTo',
        'applies_to_id': 'appliesToID',
        'remaining_uses': 'remainingUses',
        'used': 'used',
        'valid_until': 'validUntil',
        'instance_details': 'instanceDetails',
        'master_code_redeemable': 'masterCodeRedeemable'
    }

    def __init__(self, created=None, changed_by=None, updated=None, id=None, name=None, coupon_code=None, coupons=None, uses=None, product=None, product_name=None, product_id=None, product_rate_plan=None, product_rate_plan_name=None, product_rate_plan_id=None, currency=None, parent_coupon_code_redeemable=None, organization_id=None, discounts=None, deleted=None, parent_coupon_code=None, applies_to=None, applies_to_id=None, remaining_uses=None, used=None, valid_until=None, instance_details=None, master_code_redeemable=None):  # noqa: E501
        """Coupon - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._changed_by = None
        self._updated = None
        self._id = None
        self._name = None
        self._coupon_code = None
        self._coupons = None
        self._uses = None
        self._product = None
        self._product_name = None
        self._product_id = None
        self._product_rate_plan = None
        self._product_rate_plan_name = None
        self._product_rate_plan_id = None
        self._currency = None
        self._parent_coupon_code_redeemable = None
        self._organization_id = None
        self._discounts = None
        self._deleted = None
        self._parent_coupon_code = None
        self._applies_to = None
        self._applies_to_id = None
        self._remaining_uses = None
        self._used = None
        self._valid_until = None
        self._instance_details = None
        self._master_code_redeemable = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if changed_by is not None:
            self.changed_by = changed_by
        if updated is not None:
            self.updated = updated
        if id is not None:
            self.id = id
        self.name = name
        self.coupon_code = coupon_code
        self.coupons = coupons
        self.uses = uses
        if product is not None:
            self.product = product
        if product_name is not None:
            self.product_name = product_name
        if product_id is not None:
            self.product_id = product_id
        if product_rate_plan is not None:
            self.product_rate_plan = product_rate_plan
        if product_rate_plan_name is not None:
            self.product_rate_plan_name = product_rate_plan_name
        if product_rate_plan_id is not None:
            self.product_rate_plan_id = product_rate_plan_id
        if currency is not None:
            self.currency = currency
        self.parent_coupon_code_redeemable = parent_coupon_code_redeemable
        self.organization_id = organization_id
        if discounts is not None:
            self.discounts = discounts
        if deleted is not None:
            self.deleted = deleted
        if parent_coupon_code is not None:
            self.parent_coupon_code = parent_coupon_code
        if applies_to is not None:
            self.applies_to = applies_to
        if applies_to_id is not None:
            self.applies_to_id = applies_to_id
        if remaining_uses is not None:
            self.remaining_uses = remaining_uses
        if used is not None:
            self.used = used
        if valid_until is not None:
            self.valid_until = valid_until
        if instance_details is not None:
            self.instance_details = instance_details
        if master_code_redeemable is not None:
            self.master_code_redeemable = master_code_redeemable

    @property
    def created(self):
        """Gets the created of this Coupon.  # noqa: E501


        :return: The created of this Coupon.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Coupon.


        :param created: The created of this Coupon.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """Gets the changed_by of this Coupon.  # noqa: E501


        :return: The changed_by of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """Sets the changed_by of this Coupon.


        :param changed_by: The changed_by of this Coupon.  # noqa: E501
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """Gets the updated of this Coupon.  # noqa: E501


        :return: The updated of this Coupon.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Coupon.


        :param updated: The updated of this Coupon.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """Gets the id of this Coupon.  # noqa: E501


        :return: The id of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Coupon.


        :param id: The id of this Coupon.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Coupon.  # noqa: E501


        :return: The name of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Coupon.


        :param name: The name of this Coupon.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def coupon_code(self):
        """Gets the coupon_code of this Coupon.  # noqa: E501


        :return: The coupon_code of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._coupon_code

    @coupon_code.setter
    def coupon_code(self, coupon_code):
        """Sets the coupon_code of this Coupon.


        :param coupon_code: The coupon_code of this Coupon.  # noqa: E501
        :type: str
        """
        if coupon_code is None:
            raise ValueError("Invalid value for `coupon_code`, must not be `None`")  # noqa: E501

        self._coupon_code = coupon_code

    @property
    def coupons(self):
        """Gets the coupons of this Coupon.  # noqa: E501


        :return: The coupons of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._coupons

    @coupons.setter
    def coupons(self, coupons):
        """Sets the coupons of this Coupon.


        :param coupons: The coupons of this Coupon.  # noqa: E501
        :type: int
        """
        if coupons is None:
            raise ValueError("Invalid value for `coupons`, must not be `None`")  # noqa: E501

        self._coupons = coupons

    @property
    def uses(self):
        """Gets the uses of this Coupon.  # noqa: E501


        :return: The uses of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._uses

    @uses.setter
    def uses(self, uses):
        """Sets the uses of this Coupon.


        :param uses: The uses of this Coupon.  # noqa: E501
        :type: int
        """
        if uses is None:
            raise ValueError("Invalid value for `uses`, must not be `None`")  # noqa: E501

        self._uses = uses

    @property
    def product(self):
        """Gets the product of this Coupon.  # noqa: E501


        :return: The product of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this Coupon.


        :param product: The product of this Coupon.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def product_name(self):
        """Gets the product_name of this Coupon.  # noqa: E501


        :return: The product_name of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this Coupon.


        :param product_name: The product_name of this Coupon.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def product_id(self):
        """Gets the product_id of this Coupon.  # noqa: E501


        :return: The product_id of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this Coupon.


        :param product_id: The product_id of this Coupon.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def product_rate_plan(self):
        """Gets the product_rate_plan of this Coupon.  # noqa: E501


        :return: The product_rate_plan of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan

    @product_rate_plan.setter
    def product_rate_plan(self, product_rate_plan):
        """Sets the product_rate_plan of this Coupon.


        :param product_rate_plan: The product_rate_plan of this Coupon.  # noqa: E501
        :type: str
        """

        self._product_rate_plan = product_rate_plan

    @property
    def product_rate_plan_name(self):
        """Gets the product_rate_plan_name of this Coupon.  # noqa: E501


        :return: The product_rate_plan_name of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_name

    @product_rate_plan_name.setter
    def product_rate_plan_name(self, product_rate_plan_name):
        """Sets the product_rate_plan_name of this Coupon.


        :param product_rate_plan_name: The product_rate_plan_name of this Coupon.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_name = product_rate_plan_name

    @property
    def product_rate_plan_id(self):
        """Gets the product_rate_plan_id of this Coupon.  # noqa: E501


        :return: The product_rate_plan_id of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_id

    @product_rate_plan_id.setter
    def product_rate_plan_id(self, product_rate_plan_id):
        """Sets the product_rate_plan_id of this Coupon.


        :param product_rate_plan_id: The product_rate_plan_id of this Coupon.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_id = product_rate_plan_id

    @property
    def currency(self):
        """Gets the currency of this Coupon.  # noqa: E501


        :return: The currency of this Coupon.  # noqa: E501
        :rtype: CreditNoteCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Coupon.


        :param currency: The currency of this Coupon.  # noqa: E501
        :type: CreditNoteCurrency
        """

        self._currency = currency

    @property
    def parent_coupon_code_redeemable(self):
        """Gets the parent_coupon_code_redeemable of this Coupon.  # noqa: E501


        :return: The parent_coupon_code_redeemable of this Coupon.  # noqa: E501
        :rtype: bool
        """
        return self._parent_coupon_code_redeemable

    @parent_coupon_code_redeemable.setter
    def parent_coupon_code_redeemable(self, parent_coupon_code_redeemable):
        """Sets the parent_coupon_code_redeemable of this Coupon.


        :param parent_coupon_code_redeemable: The parent_coupon_code_redeemable of this Coupon.  # noqa: E501
        :type: bool
        """
        if parent_coupon_code_redeemable is None:
            raise ValueError("Invalid value for `parent_coupon_code_redeemable`, must not be `None`")  # noqa: E501

        self._parent_coupon_code_redeemable = parent_coupon_code_redeemable

    @property
    def organization_id(self):
        """Gets the organization_id of this Coupon.  # noqa: E501


        :return: The organization_id of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Coupon.


        :param organization_id: The organization_id of this Coupon.  # noqa: E501
        :type: str
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def discounts(self):
        """Gets the discounts of this Coupon.  # noqa: E501


        :return: The discounts of this Coupon.  # noqa: E501
        :rtype: list[CouponDiscount]
        """
        return self._discounts

    @discounts.setter
    def discounts(self, discounts):
        """Sets the discounts of this Coupon.


        :param discounts: The discounts of this Coupon.  # noqa: E501
        :type: list[CouponDiscount]
        """

        self._discounts = discounts

    @property
    def deleted(self):
        """Gets the deleted of this Coupon.  # noqa: E501


        :return: The deleted of this Coupon.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Coupon.


        :param deleted: The deleted of this Coupon.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def parent_coupon_code(self):
        """Gets the parent_coupon_code of this Coupon.  # noqa: E501


        :return: The parent_coupon_code of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._parent_coupon_code

    @parent_coupon_code.setter
    def parent_coupon_code(self, parent_coupon_code):
        """Sets the parent_coupon_code of this Coupon.


        :param parent_coupon_code: The parent_coupon_code of this Coupon.  # noqa: E501
        :type: str
        """

        self._parent_coupon_code = parent_coupon_code

    @property
    def applies_to(self):
        """Gets the applies_to of this Coupon.  # noqa: E501


        :return: The applies_to of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._applies_to

    @applies_to.setter
    def applies_to(self, applies_to):
        """Sets the applies_to of this Coupon.


        :param applies_to: The applies_to of this Coupon.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "subscription", "account"]  # noqa: E501
        if applies_to not in allowed_values:
            raise ValueError(
                "Invalid value for `applies_to` ({0}), must be one of {1}"  # noqa: E501
                .format(applies_to, allowed_values)
            )

        self._applies_to = applies_to

    @property
    def applies_to_id(self):
        """Gets the applies_to_id of this Coupon.  # noqa: E501


        :return: The applies_to_id of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._applies_to_id

    @applies_to_id.setter
    def applies_to_id(self, applies_to_id):
        """Sets the applies_to_id of this Coupon.


        :param applies_to_id: The applies_to_id of this Coupon.  # noqa: E501
        :type: str
        """

        self._applies_to_id = applies_to_id

    @property
    def remaining_uses(self):
        """Gets the remaining_uses of this Coupon.  # noqa: E501


        :return: The remaining_uses of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._remaining_uses

    @remaining_uses.setter
    def remaining_uses(self, remaining_uses):
        """Sets the remaining_uses of this Coupon.


        :param remaining_uses: The remaining_uses of this Coupon.  # noqa: E501
        :type: int
        """

        self._remaining_uses = remaining_uses

    @property
    def used(self):
        """Gets the used of this Coupon.  # noqa: E501


        :return: The used of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this Coupon.


        :param used: The used of this Coupon.  # noqa: E501
        :type: int
        """

        self._used = used

    @property
    def valid_until(self):
        """Gets the valid_until of this Coupon.  # noqa: E501


        :return: The valid_until of this Coupon.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """Sets the valid_until of this Coupon.


        :param valid_until: The valid_until of this Coupon.  # noqa: E501
        :type: datetime
        """

        self._valid_until = valid_until

    @property
    def instance_details(self):
        """Gets the instance_details of this Coupon.  # noqa: E501


        :return: The instance_details of this Coupon.  # noqa: E501
        :rtype: CouponInstance
        """
        return self._instance_details

    @instance_details.setter
    def instance_details(self, instance_details):
        """Sets the instance_details of this Coupon.


        :param instance_details: The instance_details of this Coupon.  # noqa: E501
        :type: CouponInstance
        """

        self._instance_details = instance_details

    @property
    def master_code_redeemable(self):
        """Gets the master_code_redeemable of this Coupon.  # noqa: E501


        :return: The master_code_redeemable of this Coupon.  # noqa: E501
        :rtype: bool
        """
        return self._master_code_redeemable

    @master_code_redeemable.setter
    def master_code_redeemable(self, master_code_redeemable):
        """Sets the master_code_redeemable of this Coupon.


        :param master_code_redeemable: The master_code_redeemable of this Coupon.  # noqa: E501
        :type: bool
        """

        self._master_code_redeemable = master_code_redeemable

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
        if issubclass(Coupon, dict):
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
        if not isinstance(other, Coupon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
