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


class MigrationRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, next_subscription_name=None, next_subscription_description=None, product=None, product_rate_plan=None, invoicing_type=None, mappings=None, pricing_behaviour=None, dry_run=False):
        """
        MigrationRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'next_subscription_name': 'str',
            'next_subscription_description': 'str',
            'product': 'str',
            'product_rate_plan': 'str',
            'invoicing_type': 'str',
            'mappings': 'list[PricingComponentMigrationValue]',
            'pricing_behaviour': 'str',
            'dry_run': 'bool'
        }

        self.attribute_map = {
            'created': 'created',
            'next_subscription_name': 'nextSubscriptionName',
            'next_subscription_description': 'nextSubscriptionDescription',
            'product': 'product',
            'product_rate_plan': 'productRatePlan',
            'invoicing_type': 'invoicingType',
            'mappings': 'mappings',
            'pricing_behaviour': 'pricingBehaviour',
            'dry_run': 'dryRun'
        }

        self._created = created
        self._next_subscription_name = next_subscription_name
        self._next_subscription_description = next_subscription_description
        self._product = product
        self._product_rate_plan = product_rate_plan
        self._invoicing_type = invoicing_type
        self._mappings = mappings
        self._pricing_behaviour = pricing_behaviour
        self._dry_run = dry_run

    @property
    def created(self):
        """
        Gets the created of this MigrationRequest.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this MigrationRequest.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this MigrationRequest.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this MigrationRequest.
        :type: datetime
        """

        self._created = created

    @property
    def next_subscription_name(self):
        """
        Gets the next_subscription_name of this MigrationRequest.
        {\"description\":\"Name to which the subscription will change upon successful migration.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The next_subscription_name of this MigrationRequest.
        :rtype: str
        """
        return self._next_subscription_name

    @next_subscription_name.setter
    def next_subscription_name(self, next_subscription_name):
        """
        Sets the next_subscription_name of this MigrationRequest.
        {\"description\":\"Name to which the subscription will change upon successful migration.\",\"verbs\":[\"POST\",\"GET\"]}

        :param next_subscription_name: The next_subscription_name of this MigrationRequest.
        :type: str
        """

        self._next_subscription_name = next_subscription_name

    @property
    def next_subscription_description(self):
        """
        Gets the next_subscription_description of this MigrationRequest.
        {\"description\":\"Description to which the subscription will change upon successful migration.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The next_subscription_description of this MigrationRequest.
        :rtype: str
        """
        return self._next_subscription_description

    @next_subscription_description.setter
    def next_subscription_description(self, next_subscription_description):
        """
        Sets the next_subscription_description of this MigrationRequest.
        {\"description\":\"Description to which the subscription will change upon successful migration.\",\"verbs\":[\"POST\",\"GET\"]}

        :param next_subscription_description: The next_subscription_description of this MigrationRequest.
        :type: str
        """

        self._next_subscription_description = next_subscription_description

    @property
    def product(self):
        """
        Gets the product of this MigrationRequest.
        {\"description\":\"The product to which the subscription will be migrated.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The product of this MigrationRequest.
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this MigrationRequest.
        {\"description\":\"The product to which the subscription will be migrated.\",\"verbs\":[\"POST\",\"GET\"]}

        :param product: The product of this MigrationRequest.
        :type: str
        """

        self._product = product

    @property
    def product_rate_plan(self):
        """
        Gets the product_rate_plan of this MigrationRequest.
        {\"description\":\"The rate plan (of some product) to which the subscription will be migrated.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The product_rate_plan of this MigrationRequest.
        :rtype: str
        """
        return self._product_rate_plan

    @product_rate_plan.setter
    def product_rate_plan(self, product_rate_plan):
        """
        Sets the product_rate_plan of this MigrationRequest.
        {\"description\":\"The rate plan (of some product) to which the subscription will be migrated.\",\"verbs\":[\"POST\",\"GET\"]}

        :param product_rate_plan: The product_rate_plan of this MigrationRequest.
        :type: str
        """

        self._product_rate_plan = product_rate_plan

    @property
    def invoicing_type(self):
        """
        Gets the invoicing_type of this MigrationRequest.
        {\"default\":\"<span class=\\\"label label-default\\\">Aggregated</span>\",\"description\":\"The strategy for how to raise invoices for charges caused by this migration.<br><span class=\\\"label label-default\\\">Immediate</span> &mdash; Generate straight-away an invoice containing these charges.<br><span class=\\\"label label-default\\\">Aggregated</span> &mdash; Add these charges to the next invoice which is generated naturally &mdash; i.e. the invoice raised at the current period's end.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The invoicing_type of this MigrationRequest.
        :rtype: str
        """
        return self._invoicing_type

    @invoicing_type.setter
    def invoicing_type(self, invoicing_type):
        """
        Sets the invoicing_type of this MigrationRequest.
        {\"default\":\"<span class=\\\"label label-default\\\">Aggregated</span>\",\"description\":\"The strategy for how to raise invoices for charges caused by this migration.<br><span class=\\\"label label-default\\\">Immediate</span> &mdash; Generate straight-away an invoice containing these charges.<br><span class=\\\"label label-default\\\">Aggregated</span> &mdash; Add these charges to the next invoice which is generated naturally &mdash; i.e. the invoice raised at the current period's end.\",\"verbs\":[\"POST\",\"GET\"]}

        :param invoicing_type: The invoicing_type of this MigrationRequest.
        :type: str
        """
        allowed_values = ["Immediate", "Aggregated"]
        if invoicing_type not in allowed_values:
            raise ValueError(
                "Invalid value for `invoicing_type` ({0}), must be one of {1}"
                .format(invoicing_type, allowed_values)
            )

        self._invoicing_type = invoicing_type

    @property
    def mappings(self):
        """
        Gets the mappings of this MigrationRequest.
        {\"description\":\"List of pricing components and quantities thereof to be consumed in the new rate plan.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The mappings of this MigrationRequest.
        :rtype: list[PricingComponentMigrationValue]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """
        Sets the mappings of this MigrationRequest.
        {\"description\":\"List of pricing components and quantities thereof to be consumed in the new rate plan.\",\"verbs\":[\"POST\",\"GET\"]}

        :param mappings: The mappings of this MigrationRequest.
        :type: list[PricingComponentMigrationValue]
        """

        self._mappings = mappings

    @property
    def pricing_behaviour(self):
        """
        Gets the pricing_behaviour of this MigrationRequest.
        {\"default\":\"DifferenceProRated\",\"description\":\"Pricing behaviour defines how migration charges are calculated.<br><span class=\\\"label label-default\\\">DifferenceProRated</span> &mdash; Calculate the difference between in-advance charges of the existing and new rate-plan, then pro-rate based on time remaining.<br><span class=\\\"label label-default\\\">None</span> &mdash; Set the migration charge as zero cost.<br><span class=\\\"label label-default\\\">Full</span> &mdash; Set the costs as the total of the new rate-plan's in-advance charges.<br><span class=\\\"label label-default\\\">Difference</span> &mdash; The same calculation as in <span class=\\\"label label-default\\\">DifferenceProRated</span>, but with no pro-ration applied.<br><span class=\\\"label label-default\\\">ProRated</span> &mdash; When moving to a rate-plan of the same duration: Pro-rates the in-advance charges of the new rate-plan.<br>When moving to a rate-plan of a different duration: A credit-note will be issued for the price of any remaining time on the existing plan's billing period.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The pricing_behaviour of this MigrationRequest.
        :rtype: str
        """
        return self._pricing_behaviour

    @pricing_behaviour.setter
    def pricing_behaviour(self, pricing_behaviour):
        """
        Sets the pricing_behaviour of this MigrationRequest.
        {\"default\":\"DifferenceProRated\",\"description\":\"Pricing behaviour defines how migration charges are calculated.<br><span class=\\\"label label-default\\\">DifferenceProRated</span> &mdash; Calculate the difference between in-advance charges of the existing and new rate-plan, then pro-rate based on time remaining.<br><span class=\\\"label label-default\\\">None</span> &mdash; Set the migration charge as zero cost.<br><span class=\\\"label label-default\\\">Full</span> &mdash; Set the costs as the total of the new rate-plan's in-advance charges.<br><span class=\\\"label label-default\\\">Difference</span> &mdash; The same calculation as in <span class=\\\"label label-default\\\">DifferenceProRated</span>, but with no pro-ration applied.<br><span class=\\\"label label-default\\\">ProRated</span> &mdash; When moving to a rate-plan of the same duration: Pro-rates the in-advance charges of the new rate-plan.<br>When moving to a rate-plan of a different duration: A credit-note will be issued for the price of any remaining time on the existing plan's billing period.\",\"verbs\":[\"POST\",\"GET\"]}

        :param pricing_behaviour: The pricing_behaviour of this MigrationRequest.
        :type: str
        """
        allowed_values = ["None", "Full", "Difference", "DifferenceProRated", "ProRated"]
        if pricing_behaviour not in allowed_values:
            raise ValueError(
                "Invalid value for `pricing_behaviour` ({0}), must be one of {1}"
                .format(pricing_behaviour, allowed_values)
            )

        self._pricing_behaviour = pricing_behaviour

    @property
    def dry_run(self):
        """
        Gets the dry_run of this MigrationRequest.
        {\"default\":\"false\",\"description\":\"Calculate the effects of migration but do not actually perform a migration.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The dry_run of this MigrationRequest.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """
        Sets the dry_run of this MigrationRequest.
        {\"default\":\"false\",\"description\":\"Calculate the effects of migration but do not actually perform a migration.\",\"verbs\":[\"POST\",\"GET\"]}

        :param dry_run: The dry_run of this MigrationRequest.
        :type: bool
        """

        self._dry_run = dry_run

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
