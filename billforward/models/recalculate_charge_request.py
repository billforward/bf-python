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


class RecalculateChargeRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, name=None, description=None, amount=None, invoicing_type=None, pricing_component_value=None, recalculation_behaviour=None, dry_run=False):
        """
        RecalculateChargeRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'name': 'str',
            'description': 'str',
            'amount': 'float',
            'invoicing_type': 'str',
            'pricing_component_value': 'int',
            'recalculation_behaviour': 'str',
            'dry_run': 'bool'
        }

        self.attribute_map = {
            'created': 'created',
            'name': 'name',
            'description': 'description',
            'amount': 'amount',
            'invoicing_type': 'invoicingType',
            'pricing_component_value': 'pricingComponentValue',
            'recalculation_behaviour': 'recalculationBehaviour',
            'dry_run': 'dryRun'
        }

        self._created = created
        self._name = name
        self._description = description
        self._amount = amount
        self._invoicing_type = invoicing_type
        self._pricing_component_value = pricing_component_value
        self._recalculation_behaviour = recalculation_behaviour
        self._dry_run = dry_run

    @property
    def created(self):
        """
        Gets the created of this RecalculateChargeRequest.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this RecalculateChargeRequest.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this RecalculateChargeRequest.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this RecalculateChargeRequest.
        :type: datetime
        """

        self._created = created

    @property
    def name(self):
        """
        Gets the name of this RecalculateChargeRequest.
        {\"description\":\"New friendly name given to the charge to help identify it.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The name of this RecalculateChargeRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RecalculateChargeRequest.
        {\"description\":\"New friendly name given to the charge to help identify it.\",\"verbs\":[\"POST\",\"GET\"]}

        :param name: The name of this RecalculateChargeRequest.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this RecalculateChargeRequest.
        {\"description\":\"New description given to the charge.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The description of this RecalculateChargeRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RecalculateChargeRequest.
        {\"description\":\"New description given to the charge.\",\"verbs\":[\"POST\",\"GET\"]}

        :param description: The description of this RecalculateChargeRequest.
        :type: str
        """

        self._description = description

    @property
    def amount(self):
        """
        Gets the amount of this RecalculateChargeRequest.
        {\"description\":\"(Applicable only if the existing charge has none of [`pricingComponentName`, `pricingComponentID`] defined)<br>New monetary amount for which to charge. Used only for ad-hoc charges (i.e charges not associated with any pricing component).<br>This amount excludes tax.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The amount of this RecalculateChargeRequest.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this RecalculateChargeRequest.
        {\"description\":\"(Applicable only if the existing charge has none of [`pricingComponentName`, `pricingComponentID`] defined)<br>New monetary amount for which to charge. Used only for ad-hoc charges (i.e charges not associated with any pricing component).<br>This amount excludes tax.\",\"verbs\":[\"POST\",\"GET\"]}

        :param amount: The amount of this RecalculateChargeRequest.
        :type: float
        """

        self._amount = amount

    @property
    def invoicing_type(self):
        """
        Gets the invoicing_type of this RecalculateChargeRequest.
        {\"default\":\"<span class=\\\"label label-default\\\">Aggregated</span>\",\"description\":\"The strategy for how to raise invoices describing the charges produced by this charge recalculation.<br><span class=\\\"label label-default\\\">Immediate</span> &mdash; Generate straight-away an invoice containing these charges.<br><span class=\\\"label label-default\\\">Aggregated</span> &mdash; Add these charges to the next invoice which is generated naturally &mdash; i.e. the invoice raised at the current period's end.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The invoicing_type of this RecalculateChargeRequest.
        :rtype: str
        """
        return self._invoicing_type

    @invoicing_type.setter
    def invoicing_type(self, invoicing_type):
        """
        Sets the invoicing_type of this RecalculateChargeRequest.
        {\"default\":\"<span class=\\\"label label-default\\\">Aggregated</span>\",\"description\":\"The strategy for how to raise invoices describing the charges produced by this charge recalculation.<br><span class=\\\"label label-default\\\">Immediate</span> &mdash; Generate straight-away an invoice containing these charges.<br><span class=\\\"label label-default\\\">Aggregated</span> &mdash; Add these charges to the next invoice which is generated naturally &mdash; i.e. the invoice raised at the current period's end.\",\"verbs\":[\"POST\",\"GET\"]}

        :param invoicing_type: The invoicing_type of this RecalculateChargeRequest.
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
    def pricing_component_value(self):
        """
        Gets the pricing_component_value of this RecalculateChargeRequest.
        {\"description\":\"(Applicable only if the existing charge has any of [`pricingComponentName`, `pricingComponentID`] defined)<br>The updated value consumed of the pricing component which this charge concerns.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The pricing_component_value of this RecalculateChargeRequest.
        :rtype: int
        """
        return self._pricing_component_value

    @pricing_component_value.setter
    def pricing_component_value(self, pricing_component_value):
        """
        Sets the pricing_component_value of this RecalculateChargeRequest.
        {\"description\":\"(Applicable only if the existing charge has any of [`pricingComponentName`, `pricingComponentID`] defined)<br>The updated value consumed of the pricing component which this charge concerns.\",\"verbs\":[\"POST\",\"GET\"]}

        :param pricing_component_value: The pricing_component_value of this RecalculateChargeRequest.
        :type: int
        """

        self._pricing_component_value = pricing_component_value

    @property
    def recalculation_behaviour(self):
        """
        Gets the recalculation_behaviour of this RecalculateChargeRequest.
        {\"default\":\"RecalculateWithLatestPricing\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The recalculation_behaviour of this RecalculateChargeRequest.
        :rtype: str
        """
        return self._recalculation_behaviour

    @recalculation_behaviour.setter
    def recalculation_behaviour(self, recalculation_behaviour):
        """
        Sets the recalculation_behaviour of this RecalculateChargeRequest.
        {\"default\":\"RecalculateWithLatestPricing\",\"verbs\":[\"POST\",\"GET\"]}

        :param recalculation_behaviour: The recalculation_behaviour of this RecalculateChargeRequest.
        :type: str
        """
        allowed_values = ["RecalculateWithLatestPricing", "RecalculateWithCurrentPricing"]
        if recalculation_behaviour not in allowed_values:
            raise ValueError(
                "Invalid value for `recalculation_behaviour` ({0}), must be one of {1}"
                .format(recalculation_behaviour, allowed_values)
            )

        self._recalculation_behaviour = recalculation_behaviour

    @property
    def dry_run(self):
        """
        Gets the dry_run of this RecalculateChargeRequest.
        {\"default\":false,\"description\":\"Changes described in the response:<br><span class=\\\"label label-default\\\">true</span> &mdash; Are not actually performed; your subscription remains unchanged, no billing events run, and no invoices are executed.<br><span class=\\\"label label-default\\\">false</span> &mdash; Are actually performed and committed.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The dry_run of this RecalculateChargeRequest.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """
        Sets the dry_run of this RecalculateChargeRequest.
        {\"default\":false,\"description\":\"Changes described in the response:<br><span class=\\\"label label-default\\\">true</span> &mdash; Are not actually performed; your subscription remains unchanged, no billing events run, and no invoices are executed.<br><span class=\\\"label label-default\\\">false</span> &mdash; Are actually performed and committed.\",\"verbs\":[\"POST\",\"GET\"]}

        :param dry_run: The dry_run of this RecalculateChargeRequest.
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
