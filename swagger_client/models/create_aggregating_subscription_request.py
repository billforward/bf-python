# coding: utf-8

"""
    BillForward REST API


    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class CreateAggregatingSubscriptionRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, account_id=None, organization_id=None, name=None, description=None, start=None, state=None, product_rate_plan=None, duration=None, duration_period=None, product_type=None, aggregating_components=None, aggregate_all_subscriptions_on_account=False, currency=None):
        """
        CreateAggregatingSubscriptionRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'account_id': 'str',
            'organization_id': 'str',
            'name': 'str',
            'description': 'str',
            'start': 'datetime',
            'state': 'str',
            'product_rate_plan': 'str',
            'duration': 'int',
            'duration_period': 'str',
            'product_type': 'str',
            'aggregating_components': 'list[CreateAggregatingComponentRequest]',
            'aggregate_all_subscriptions_on_account': 'bool',
            'currency': 'str'
        }

        self.attribute_map = {
            'created': 'created',
            'account_id': 'accountID',
            'organization_id': 'organizationID',
            'name': 'name',
            'description': 'description',
            'start': 'start',
            'state': 'state',
            'product_rate_plan': 'productRatePlan',
            'duration': 'duration',
            'duration_period': 'durationPeriod',
            'product_type': 'productType',
            'aggregating_components': 'aggregatingComponents',
            'aggregate_all_subscriptions_on_account': 'aggregateAllSubscriptionsOnAccount',
            'currency': 'currency'
        }

        self._created = created
        self._account_id = account_id
        self._organization_id = organization_id
        self._name = name
        self._description = description
        self._start = start
        self._state = state
        self._product_rate_plan = product_rate_plan
        self._duration = duration
        self._duration_period = duration_period
        self._product_type = product_type
        self._aggregating_components = aggregating_components
        self._aggregate_all_subscriptions_on_account = aggregate_all_subscriptions_on_account
        self._currency = currency

    @property
    def created(self):
        """
        Gets the created of this CreateAggregatingSubscriptionRequest.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this CreateAggregatingSubscriptionRequest.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this CreateAggregatingSubscriptionRequest.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this CreateAggregatingSubscriptionRequest.
        :type: datetime
        """

        self._created = created

    @property
    def account_id(self):
        """
        Gets the account_id of this CreateAggregatingSubscriptionRequest.
        {\"description\":\"ID of the BillForward Account who will own this aggregating subscription. You should ensure beforehand that the customer has had a BillForward Account created for them.\",\"verbs\":[\"POST\"]}

        :return: The account_id of this CreateAggregatingSubscriptionRequest.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this CreateAggregatingSubscriptionRequest.
        {\"description\":\"ID of the BillForward Account who will own this aggregating subscription. You should ensure beforehand that the customer has had a BillForward Account created for them.\",\"verbs\":[\"POST\"]}

        :param account_id: The account_id of this CreateAggregatingSubscriptionRequest.
        :type: str
        """

        self._account_id = account_id

    @property
    def organization_id(self):
        """
        Gets the organization_id of this CreateAggregatingSubscriptionRequest.
        {\"default\":\"(Auto-populated using your authentication credentials)\",\"description\":\"ID of the BillForward Organization within which the requested Subscription should be created. If omitted, this will be auto-populated using your authentication credentials.\",\"verbs\":[\"POST\"]}

        :return: The organization_id of this CreateAggregatingSubscriptionRequest.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this CreateAggregatingSubscriptionRequest.
        {\"default\":\"(Auto-populated using your authentication credentials)\",\"description\":\"ID of the BillForward Organization within which the requested Subscription should be created. If omitted, this will be auto-populated using your authentication credentials.\",\"verbs\":[\"POST\"]}

        :param organization_id: The organization_id of this CreateAggregatingSubscriptionRequest.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def name(self):
        """
        Gets the name of this CreateAggregatingSubscriptionRequest.
        {\"default\":\"(Subscription will be named after the rate plan to which the subscription subscribes)\",\"description\":\"Name of the created subscription. This is primarily for your benefit &mdash; for example, to enable you to identify subscriptions at a glance in the BillForward web interface (e.g. 'BusinessCorp subscriptions, care of Mr Business (mr@busy.com)').\",\"verbs\":[\"POST\"]}

        :return: The name of this CreateAggregatingSubscriptionRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateAggregatingSubscriptionRequest.
        {\"default\":\"(Subscription will be named after the rate plan to which the subscription subscribes)\",\"description\":\"Name of the created subscription. This is primarily for your benefit &mdash; for example, to enable you to identify subscriptions at a glance in the BillForward web interface (e.g. 'BusinessCorp subscriptions, care of Mr Business (mr@busy.com)').\",\"verbs\":[\"POST\"]}

        :param name: The name of this CreateAggregatingSubscriptionRequest.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateAggregatingSubscriptionRequest.
        {\"default\":\"(null)\",\"description\":\"Description of the created subscription. This is primarily for your benefit &mdash; for example, you could write here the mechanism through which you obtained this customer. (e.g. 'Business signed up using BUSYGUYS coupon, at management trade show').\",\"verbs\":[\"POST\"]}

        :return: The description of this CreateAggregatingSubscriptionRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateAggregatingSubscriptionRequest.
        {\"default\":\"(null)\",\"description\":\"Description of the created subscription. This is primarily for your benefit &mdash; for example, you could write here the mechanism through which you obtained this customer. (e.g. 'Business signed up using BUSYGUYS coupon, at management trade show').\",\"verbs\":[\"POST\"]}

        :param description: The description of this CreateAggregatingSubscriptionRequest.
        :type: str
        """

        self._description = description

    @property
    def start(self):
        """
        Gets the start of this CreateAggregatingSubscriptionRequest.
        {\"default\":\"(ServerNow upon receiving request)\",\"description\":\"ISO 8601 UTC DateTime (e.g. 2015-06-16T11:58:41Z) describing the date at which the subscription should enter its first service period.\",\"verbs\":[\"POST\"]}

        :return: The start of this CreateAggregatingSubscriptionRequest.
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this CreateAggregatingSubscriptionRequest.
        {\"default\":\"(ServerNow upon receiving request)\",\"description\":\"ISO 8601 UTC DateTime (e.g. 2015-06-16T11:58:41Z) describing the date at which the subscription should enter its first service period.\",\"verbs\":[\"POST\"]}

        :param start: The start of this CreateAggregatingSubscriptionRequest.
        :type: datetime
        """

        self._start = start

    @property
    def state(self):
        """
        Gets the state of this CreateAggregatingSubscriptionRequest.
        {\"default\":\"Provisioned\",\"description\":\"The state in which the created subscription will begin.<br><span class=\\\"label label-default\\\">Provisioned</span> &mdash; The subscription will wait (without raising any invoices or beginning its service) until explicit action is taken to change its state.<br><span class=\\\"label label-default\\\">AwaitingPayment</span> &mdash; The subscription is activated. After `start` time is surpassed, it will begin service and raise its first invoice.\",\"verbs\":[\"POST\"]}

        :return: The state of this CreateAggregatingSubscriptionRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this CreateAggregatingSubscriptionRequest.
        {\"default\":\"Provisioned\",\"description\":\"The state in which the created subscription will begin.<br><span class=\\\"label label-default\\\">Provisioned</span> &mdash; The subscription will wait (without raising any invoices or beginning its service) until explicit action is taken to change its state.<br><span class=\\\"label label-default\\\">AwaitingPayment</span> &mdash; The subscription is activated. After `start` time is surpassed, it will begin service and raise its first invoice.\",\"verbs\":[\"POST\"]}

        :param state: The state of this CreateAggregatingSubscriptionRequest.
        :type: str
        """
        allowed_values = ["Trial", "Provisioned", "Paid", "AwaitingPayment", "Cancelled", "Failed", "Expired"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def product_rate_plan(self):
        """
        Gets the product_rate_plan of this CreateAggregatingSubscriptionRequest.
        {\"description\":\"ID of the rate plan to which the subscription will be subscribing. If omitted: it will be assumed you wish to create a new rate plan as part of this request &mdash; this subscription will subscribe to that newly-created rate plan.\",\"verbs\":[\"POST\"]}

        :return: The product_rate_plan of this CreateAggregatingSubscriptionRequest.
        :rtype: str
        """
        return self._product_rate_plan

    @product_rate_plan.setter
    def product_rate_plan(self, product_rate_plan):
        """
        Sets the product_rate_plan of this CreateAggregatingSubscriptionRequest.
        {\"description\":\"ID of the rate plan to which the subscription will be subscribing. If omitted: it will be assumed you wish to create a new rate plan as part of this request &mdash; this subscription will subscribe to that newly-created rate plan.\",\"verbs\":[\"POST\"]}

        :param product_rate_plan: The product_rate_plan of this CreateAggregatingSubscriptionRequest.
        :type: str
        """

        self._product_rate_plan = product_rate_plan

    @property
    def duration(self):
        """
        Gets the duration of this CreateAggregatingSubscriptionRequest.
        {\"description\":\"[Required if and only if `productRatePlan` is omitted] Number of length-measures which constitute the rate plan's period.\",\"verbs\":[\"POST\"]}

        :return: The duration of this CreateAggregatingSubscriptionRequest.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this CreateAggregatingSubscriptionRequest.
        {\"description\":\"[Required if and only if `productRatePlan` is omitted] Number of length-measures which constitute the rate plan's period.\",\"verbs\":[\"POST\"]}

        :param duration: The duration of this CreateAggregatingSubscriptionRequest.
        :type: int
        """

        self._duration = duration

    @property
    def duration_period(self):
        """
        Gets the duration_period of this CreateAggregatingSubscriptionRequest.
        {\"description\":\"[Required if and only if `productRatePlan` is omitted] Measure describing the magnitude of the rate plan's period.\",\"verbs\":[\"POST\"]}

        :return: The duration_period of this CreateAggregatingSubscriptionRequest.
        :rtype: str
        """
        return self._duration_period

    @duration_period.setter
    def duration_period(self, duration_period):
        """
        Sets the duration_period of this CreateAggregatingSubscriptionRequest.
        {\"description\":\"[Required if and only if `productRatePlan` is omitted] Measure describing the magnitude of the rate plan's period.\",\"verbs\":[\"POST\"]}

        :param duration_period: The duration_period of this CreateAggregatingSubscriptionRequest.
        :type: str
        """
        allowed_values = ["minutes", "days", "months", "years"]
        if duration_period not in allowed_values:
            raise ValueError(
                "Invalid value for `duration_period` ({0}), must be one of {1}"
                .format(duration_period, allowed_values)
            )

        self._duration_period = duration_period

    @property
    def product_type(self):
        """
        Gets the product_type of this CreateAggregatingSubscriptionRequest.
        {\"description\":\"[Required if and only if `productRatePlan` is omitted] The frequency of the rate plan &mdash; either recurring or non-recurring.\",\"verbs\":[\"POST\"]}

        :return: The product_type of this CreateAggregatingSubscriptionRequest.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """
        Sets the product_type of this CreateAggregatingSubscriptionRequest.
        {\"description\":\"[Required if and only if `productRatePlan` is omitted] The frequency of the rate plan &mdash; either recurring or non-recurring.\",\"verbs\":[\"POST\"]}

        :param product_type: The product_type of this CreateAggregatingSubscriptionRequest.
        :type: str
        """
        allowed_values = ["nonrecurring", "recurring"]
        if product_type not in allowed_values:
            raise ValueError(
                "Invalid value for `product_type` ({0}), must be one of {1}"
                .format(product_type, allowed_values)
            )

        self._product_type = product_type

    @property
    def aggregating_components(self):
        """
        Gets the aggregating_components of this CreateAggregatingSubscriptionRequest.
        {\"default\":\"(empty list)\",\"description\":\"[Required if and only if `productRatePlan` is omitted] List of components whose prices should be recalculated upon invoice aggregation. For example: two subscriptions' individual consumptions may neither of them be large enough to achieve bulk buy discounts. When aggregated, though, the same two subscriptions' consumption may add up to a quantity which does merit a bulk buy discount within your tiering system.\",\"verbs\":[\"POST\"]}

        :return: The aggregating_components of this CreateAggregatingSubscriptionRequest.
        :rtype: list[CreateAggregatingComponentRequest]
        """
        return self._aggregating_components

    @aggregating_components.setter
    def aggregating_components(self, aggregating_components):
        """
        Sets the aggregating_components of this CreateAggregatingSubscriptionRequest.
        {\"default\":\"(empty list)\",\"description\":\"[Required if and only if `productRatePlan` is omitted] List of components whose prices should be recalculated upon invoice aggregation. For example: two subscriptions' individual consumptions may neither of them be large enough to achieve bulk buy discounts. When aggregated, though, the same two subscriptions' consumption may add up to a quantity which does merit a bulk buy discount within your tiering system.\",\"verbs\":[\"POST\"]}

        :param aggregating_components: The aggregating_components of this CreateAggregatingSubscriptionRequest.
        :type: list[CreateAggregatingComponentRequest]
        """

        self._aggregating_components = aggregating_components

    @property
    def aggregate_all_subscriptions_on_account(self):
        """
        Gets the aggregate_all_subscriptions_on_account of this CreateAggregatingSubscriptionRequest.
        {\"default\":false,\"description\":\"Whether this 'aggregating subscription' should collect charges (starting now) from all other subscriptions (current and future) belonging to this BillForward Account.\",\"verbs\":[\"POST\"]}

        :return: The aggregate_all_subscriptions_on_account of this CreateAggregatingSubscriptionRequest.
        :rtype: bool
        """
        return self._aggregate_all_subscriptions_on_account

    @aggregate_all_subscriptions_on_account.setter
    def aggregate_all_subscriptions_on_account(self, aggregate_all_subscriptions_on_account):
        """
        Sets the aggregate_all_subscriptions_on_account of this CreateAggregatingSubscriptionRequest.
        {\"default\":false,\"description\":\"Whether this 'aggregating subscription' should collect charges (starting now) from all other subscriptions (current and future) belonging to this BillForward Account.\",\"verbs\":[\"POST\"]}

        :param aggregate_all_subscriptions_on_account: The aggregate_all_subscriptions_on_account of this CreateAggregatingSubscriptionRequest.
        :type: bool
        """

        self._aggregate_all_subscriptions_on_account = aggregate_all_subscriptions_on_account

    @property
    def currency(self):
        """
        Gets the currency of this CreateAggregatingSubscriptionRequest.
        {\"description\":\"[Required if and only if `productRatePlan` is omitted] The currency of the product-rate-plan &mdash; as specified by a three-character ISO 4217 currency code (i.e. USD).\",\"verbs\":[\"POST\"]}

        :return: The currency of this CreateAggregatingSubscriptionRequest.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this CreateAggregatingSubscriptionRequest.
        {\"description\":\"[Required if and only if `productRatePlan` is omitted] The currency of the product-rate-plan &mdash; as specified by a three-character ISO 4217 currency code (i.e. USD).\",\"verbs\":[\"POST\"]}

        :param currency: The currency of this CreateAggregatingSubscriptionRequest.
        :type: str
        """

        self._currency = currency

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
