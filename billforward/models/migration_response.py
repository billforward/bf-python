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

class MigrationResponse(object):
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
        'organization_id': 'str',
        'subscription_id': 'str',
        'next_subscription_name': 'str',
        'next_subscription_description': 'str',
        'product': 'str',
        'product_rate_plan': 'str',
        'invoicing_type': 'str',
        'mappings': 'list[PricingComponentMigrationValue]',
        'pricing_behaviour': 'str',
        'void_existing_coupons': 'bool',
        'force_trial_end': 'bool',
        'dry_run': 'bool',
        'new_subscription_id': 'str',
        'new_subscription': 'Subscription',
        'previous_subscription': 'Subscription',
        'previous_product_rate_plan_id': 'str',
        'previous_product_rate_plan_name': 'str',
        'new_product_rate_plan_id': 'str',
        'new_product_rate_plan_name': 'str',
        'charge_type': 'str',
        'amount': 'float',
        'tax': 'float',
        'invoices': 'list[Invoice]',
        'amendment': 'Amendment'
    }

    attribute_map = {
        'created': 'created',
        'organization_id': 'organizationID',
        'subscription_id': 'subscriptionID',
        'next_subscription_name': 'nextSubscriptionName',
        'next_subscription_description': 'nextSubscriptionDescription',
        'product': 'product',
        'product_rate_plan': 'productRatePlan',
        'invoicing_type': 'invoicingType',
        'mappings': 'mappings',
        'pricing_behaviour': 'pricingBehaviour',
        'void_existing_coupons': 'voidExistingCoupons',
        'force_trial_end': 'forceTrialEnd',
        'dry_run': 'dryRun',
        'new_subscription_id': 'newSubscriptionID',
        'new_subscription': 'newSubscription',
        'previous_subscription': 'previousSubscription',
        'previous_product_rate_plan_id': 'previousProductRatePlanID',
        'previous_product_rate_plan_name': 'previousProductRatePlanName',
        'new_product_rate_plan_id': 'newProductRatePlanID',
        'new_product_rate_plan_name': 'newProductRatePlanName',
        'charge_type': 'chargeType',
        'amount': 'amount',
        'tax': 'tax',
        'invoices': 'invoices',
        'amendment': 'amendment'
    }

    def __init__(self, created=None, organization_id=None, subscription_id=None, next_subscription_name=None, next_subscription_description=None, product=None, product_rate_plan=None, invoicing_type=None, mappings=None, pricing_behaviour=None, void_existing_coupons=None, force_trial_end=None, dry_run=None, new_subscription_id=None, new_subscription=None, previous_subscription=None, previous_product_rate_plan_id=None, previous_product_rate_plan_name=None, new_product_rate_plan_id=None, new_product_rate_plan_name=None, charge_type=None, amount=None, tax=None, invoices=None, amendment=None):  # noqa: E501
        """MigrationResponse - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._organization_id = None
        self._subscription_id = None
        self._next_subscription_name = None
        self._next_subscription_description = None
        self._product = None
        self._product_rate_plan = None
        self._invoicing_type = None
        self._mappings = None
        self._pricing_behaviour = None
        self._void_existing_coupons = None
        self._force_trial_end = None
        self._dry_run = None
        self._new_subscription_id = None
        self._new_subscription = None
        self._previous_subscription = None
        self._previous_product_rate_plan_id = None
        self._previous_product_rate_plan_name = None
        self._new_product_rate_plan_id = None
        self._new_product_rate_plan_name = None
        self._charge_type = None
        self._amount = None
        self._tax = None
        self._invoices = None
        self._amendment = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if organization_id is not None:
            self.organization_id = organization_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if next_subscription_name is not None:
            self.next_subscription_name = next_subscription_name
        if next_subscription_description is not None:
            self.next_subscription_description = next_subscription_description
        if product is not None:
            self.product = product
        if product_rate_plan is not None:
            self.product_rate_plan = product_rate_plan
        self.invoicing_type = invoicing_type
        if mappings is not None:
            self.mappings = mappings
        self.pricing_behaviour = pricing_behaviour
        if void_existing_coupons is not None:
            self.void_existing_coupons = void_existing_coupons
        if force_trial_end is not None:
            self.force_trial_end = force_trial_end
        if dry_run is not None:
            self.dry_run = dry_run
        if new_subscription_id is not None:
            self.new_subscription_id = new_subscription_id
        if new_subscription is not None:
            self.new_subscription = new_subscription
        if previous_subscription is not None:
            self.previous_subscription = previous_subscription
        if previous_product_rate_plan_id is not None:
            self.previous_product_rate_plan_id = previous_product_rate_plan_id
        if previous_product_rate_plan_name is not None:
            self.previous_product_rate_plan_name = previous_product_rate_plan_name
        if new_product_rate_plan_id is not None:
            self.new_product_rate_plan_id = new_product_rate_plan_id
        if new_product_rate_plan_name is not None:
            self.new_product_rate_plan_name = new_product_rate_plan_name
        if charge_type is not None:
            self.charge_type = charge_type
        if amount is not None:
            self.amount = amount
        if tax is not None:
            self.tax = tax
        if invoices is not None:
            self.invoices = invoices
        if amendment is not None:
            self.amendment = amendment

    @property
    def created(self):
        """Gets the created of this MigrationResponse.  # noqa: E501


        :return: The created of this MigrationResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this MigrationResponse.


        :param created: The created of this MigrationResponse.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def organization_id(self):
        """Gets the organization_id of this MigrationResponse.  # noqa: E501


        :return: The organization_id of this MigrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this MigrationResponse.


        :param organization_id: The organization_id of this MigrationResponse.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this MigrationResponse.  # noqa: E501


        :return: The subscription_id of this MigrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this MigrationResponse.


        :param subscription_id: The subscription_id of this MigrationResponse.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def next_subscription_name(self):
        """Gets the next_subscription_name of this MigrationResponse.  # noqa: E501


        :return: The next_subscription_name of this MigrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_subscription_name

    @next_subscription_name.setter
    def next_subscription_name(self, next_subscription_name):
        """Sets the next_subscription_name of this MigrationResponse.


        :param next_subscription_name: The next_subscription_name of this MigrationResponse.  # noqa: E501
        :type: str
        """

        self._next_subscription_name = next_subscription_name

    @property
    def next_subscription_description(self):
        """Gets the next_subscription_description of this MigrationResponse.  # noqa: E501


        :return: The next_subscription_description of this MigrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_subscription_description

    @next_subscription_description.setter
    def next_subscription_description(self, next_subscription_description):
        """Sets the next_subscription_description of this MigrationResponse.


        :param next_subscription_description: The next_subscription_description of this MigrationResponse.  # noqa: E501
        :type: str
        """

        self._next_subscription_description = next_subscription_description

    @property
    def product(self):
        """Gets the product of this MigrationResponse.  # noqa: E501


        :return: The product of this MigrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this MigrationResponse.


        :param product: The product of this MigrationResponse.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def product_rate_plan(self):
        """Gets the product_rate_plan of this MigrationResponse.  # noqa: E501


        :return: The product_rate_plan of this MigrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan

    @product_rate_plan.setter
    def product_rate_plan(self, product_rate_plan):
        """Sets the product_rate_plan of this MigrationResponse.


        :param product_rate_plan: The product_rate_plan of this MigrationResponse.  # noqa: E501
        :type: str
        """

        self._product_rate_plan = product_rate_plan

    @property
    def invoicing_type(self):
        """Gets the invoicing_type of this MigrationResponse.  # noqa: E501


        :return: The invoicing_type of this MigrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._invoicing_type

    @invoicing_type.setter
    def invoicing_type(self, invoicing_type):
        """Sets the invoicing_type of this MigrationResponse.


        :param invoicing_type: The invoicing_type of this MigrationResponse.  # noqa: E501
        :type: str
        """
        if invoicing_type is None:
            raise ValueError("Invalid value for `invoicing_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Immediate", "Aggregated"]  # noqa: E501
        if invoicing_type not in allowed_values:
            raise ValueError(
                "Invalid value for `invoicing_type` ({0}), must be one of {1}"  # noqa: E501
                .format(invoicing_type, allowed_values)
            )

        self._invoicing_type = invoicing_type

    @property
    def mappings(self):
        """Gets the mappings of this MigrationResponse.  # noqa: E501


        :return: The mappings of this MigrationResponse.  # noqa: E501
        :rtype: list[PricingComponentMigrationValue]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this MigrationResponse.


        :param mappings: The mappings of this MigrationResponse.  # noqa: E501
        :type: list[PricingComponentMigrationValue]
        """

        self._mappings = mappings

    @property
    def pricing_behaviour(self):
        """Gets the pricing_behaviour of this MigrationResponse.  # noqa: E501


        :return: The pricing_behaviour of this MigrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._pricing_behaviour

    @pricing_behaviour.setter
    def pricing_behaviour(self, pricing_behaviour):
        """Sets the pricing_behaviour of this MigrationResponse.


        :param pricing_behaviour: The pricing_behaviour of this MigrationResponse.  # noqa: E501
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
    def void_existing_coupons(self):
        """Gets the void_existing_coupons of this MigrationResponse.  # noqa: E501


        :return: The void_existing_coupons of this MigrationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._void_existing_coupons

    @void_existing_coupons.setter
    def void_existing_coupons(self, void_existing_coupons):
        """Sets the void_existing_coupons of this MigrationResponse.


        :param void_existing_coupons: The void_existing_coupons of this MigrationResponse.  # noqa: E501
        :type: bool
        """

        self._void_existing_coupons = void_existing_coupons

    @property
    def force_trial_end(self):
        """Gets the force_trial_end of this MigrationResponse.  # noqa: E501


        :return: The force_trial_end of this MigrationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._force_trial_end

    @force_trial_end.setter
    def force_trial_end(self, force_trial_end):
        """Sets the force_trial_end of this MigrationResponse.


        :param force_trial_end: The force_trial_end of this MigrationResponse.  # noqa: E501
        :type: bool
        """

        self._force_trial_end = force_trial_end

    @property
    def dry_run(self):
        """Gets the dry_run of this MigrationResponse.  # noqa: E501


        :return: The dry_run of this MigrationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this MigrationResponse.


        :param dry_run: The dry_run of this MigrationResponse.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def new_subscription_id(self):
        """Gets the new_subscription_id of this MigrationResponse.  # noqa: E501


        :return: The new_subscription_id of this MigrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._new_subscription_id

    @new_subscription_id.setter
    def new_subscription_id(self, new_subscription_id):
        """Sets the new_subscription_id of this MigrationResponse.


        :param new_subscription_id: The new_subscription_id of this MigrationResponse.  # noqa: E501
        :type: str
        """

        self._new_subscription_id = new_subscription_id

    @property
    def new_subscription(self):
        """Gets the new_subscription of this MigrationResponse.  # noqa: E501


        :return: The new_subscription of this MigrationResponse.  # noqa: E501
        :rtype: Subscription
        """
        return self._new_subscription

    @new_subscription.setter
    def new_subscription(self, new_subscription):
        """Sets the new_subscription of this MigrationResponse.


        :param new_subscription: The new_subscription of this MigrationResponse.  # noqa: E501
        :type: Subscription
        """

        self._new_subscription = new_subscription

    @property
    def previous_subscription(self):
        """Gets the previous_subscription of this MigrationResponse.  # noqa: E501


        :return: The previous_subscription of this MigrationResponse.  # noqa: E501
        :rtype: Subscription
        """
        return self._previous_subscription

    @previous_subscription.setter
    def previous_subscription(self, previous_subscription):
        """Sets the previous_subscription of this MigrationResponse.


        :param previous_subscription: The previous_subscription of this MigrationResponse.  # noqa: E501
        :type: Subscription
        """

        self._previous_subscription = previous_subscription

    @property
    def previous_product_rate_plan_id(self):
        """Gets the previous_product_rate_plan_id of this MigrationResponse.  # noqa: E501


        :return: The previous_product_rate_plan_id of this MigrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._previous_product_rate_plan_id

    @previous_product_rate_plan_id.setter
    def previous_product_rate_plan_id(self, previous_product_rate_plan_id):
        """Sets the previous_product_rate_plan_id of this MigrationResponse.


        :param previous_product_rate_plan_id: The previous_product_rate_plan_id of this MigrationResponse.  # noqa: E501
        :type: str
        """

        self._previous_product_rate_plan_id = previous_product_rate_plan_id

    @property
    def previous_product_rate_plan_name(self):
        """Gets the previous_product_rate_plan_name of this MigrationResponse.  # noqa: E501


        :return: The previous_product_rate_plan_name of this MigrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._previous_product_rate_plan_name

    @previous_product_rate_plan_name.setter
    def previous_product_rate_plan_name(self, previous_product_rate_plan_name):
        """Sets the previous_product_rate_plan_name of this MigrationResponse.


        :param previous_product_rate_plan_name: The previous_product_rate_plan_name of this MigrationResponse.  # noqa: E501
        :type: str
        """

        self._previous_product_rate_plan_name = previous_product_rate_plan_name

    @property
    def new_product_rate_plan_id(self):
        """Gets the new_product_rate_plan_id of this MigrationResponse.  # noqa: E501


        :return: The new_product_rate_plan_id of this MigrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._new_product_rate_plan_id

    @new_product_rate_plan_id.setter
    def new_product_rate_plan_id(self, new_product_rate_plan_id):
        """Sets the new_product_rate_plan_id of this MigrationResponse.


        :param new_product_rate_plan_id: The new_product_rate_plan_id of this MigrationResponse.  # noqa: E501
        :type: str
        """

        self._new_product_rate_plan_id = new_product_rate_plan_id

    @property
    def new_product_rate_plan_name(self):
        """Gets the new_product_rate_plan_name of this MigrationResponse.  # noqa: E501


        :return: The new_product_rate_plan_name of this MigrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._new_product_rate_plan_name

    @new_product_rate_plan_name.setter
    def new_product_rate_plan_name(self, new_product_rate_plan_name):
        """Sets the new_product_rate_plan_name of this MigrationResponse.


        :param new_product_rate_plan_name: The new_product_rate_plan_name of this MigrationResponse.  # noqa: E501
        :type: str
        """

        self._new_product_rate_plan_name = new_product_rate_plan_name

    @property
    def charge_type(self):
        """Gets the charge_type of this MigrationResponse.  # noqa: E501


        :return: The charge_type of this MigrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this MigrationResponse.


        :param charge_type: The charge_type of this MigrationResponse.  # noqa: E501
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
    def amount(self):
        """Gets the amount of this MigrationResponse.  # noqa: E501


        :return: The amount of this MigrationResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this MigrationResponse.


        :param amount: The amount of this MigrationResponse.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def tax(self):
        """Gets the tax of this MigrationResponse.  # noqa: E501


        :return: The tax of this MigrationResponse.  # noqa: E501
        :rtype: float
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this MigrationResponse.


        :param tax: The tax of this MigrationResponse.  # noqa: E501
        :type: float
        """

        self._tax = tax

    @property
    def invoices(self):
        """Gets the invoices of this MigrationResponse.  # noqa: E501


        :return: The invoices of this MigrationResponse.  # noqa: E501
        :rtype: list[Invoice]
        """
        return self._invoices

    @invoices.setter
    def invoices(self, invoices):
        """Sets the invoices of this MigrationResponse.


        :param invoices: The invoices of this MigrationResponse.  # noqa: E501
        :type: list[Invoice]
        """

        self._invoices = invoices

    @property
    def amendment(self):
        """Gets the amendment of this MigrationResponse.  # noqa: E501


        :return: The amendment of this MigrationResponse.  # noqa: E501
        :rtype: Amendment
        """
        return self._amendment

    @amendment.setter
    def amendment(self, amendment):
        """Sets the amendment of this MigrationResponse.


        :param amendment: The amendment of this MigrationResponse.  # noqa: E501
        :type: Amendment
        """

        self._amendment = amendment

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
        if issubclass(MigrationResponse, dict):
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
        if not isinstance(other, MigrationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other