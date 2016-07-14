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


class PricingComponentValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, changed_by=None, updated=None, id=None, version_id=None, pricing_component_id=None, pricing_component_name=None, subscription_id=None, organization_id=None, value=None, applies_from=None, applies_till=None, pending_change=None):
        """
        PricingComponentValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'changed_by': 'str',
            'updated': 'datetime',
            'id': 'str',
            'version_id': 'str',
            'pricing_component_id': 'str',
            'pricing_component_name': 'str',
            'subscription_id': 'str',
            'organization_id': 'str',
            'value': 'int',
            'applies_from': 'datetime',
            'applies_till': 'datetime',
            'pending_change': 'PendingComponentValueChange'
        }

        self.attribute_map = {
            'created': 'created',
            'changed_by': 'changedBy',
            'updated': 'updated',
            'id': 'id',
            'version_id': 'versionID',
            'pricing_component_id': 'pricingComponentID',
            'pricing_component_name': 'pricingComponentName',
            'subscription_id': 'subscriptionID',
            'organization_id': 'organizationID',
            'value': 'value',
            'applies_from': 'appliesFrom',
            'applies_till': 'appliesTill',
            'pending_change': 'pendingChange'
        }

        self._created = created
        self._changed_by = changed_by
        self._updated = updated
        self._id = id
        self._version_id = version_id
        self._pricing_component_id = pricing_component_id
        self._pricing_component_name = pricing_component_name
        self._subscription_id = subscription_id
        self._organization_id = organization_id
        self._value = value
        self._applies_from = applies_from
        self._applies_till = applies_till
        self._pending_change = pending_change

    @property
    def created(self):
        """
        Gets the created of this PricingComponentValue.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this PricingComponentValue.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this PricingComponentValue.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this PricingComponentValue.
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """
        Gets the changed_by of this PricingComponentValue.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :return: The changed_by of this PricingComponentValue.
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """
        Sets the changed_by of this PricingComponentValue.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :param changed_by: The changed_by of this PricingComponentValue.
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """
        Gets the updated of this PricingComponentValue.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :return: The updated of this PricingComponentValue.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this PricingComponentValue.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :param updated: The updated of this PricingComponentValue.
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """
        Gets the id of this PricingComponentValue.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The id of this PricingComponentValue.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PricingComponentValue.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param id: The id of this PricingComponentValue.
        :type: str
        """

        self._id = id

    @property
    def version_id(self):
        """
        Gets the version_id of this PricingComponentValue.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The version_id of this PricingComponentValue.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """
        Sets the version_id of this PricingComponentValue.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param version_id: The version_id of this PricingComponentValue.
        :type: str
        """

        self._version_id = version_id

    @property
    def pricing_component_id(self):
        """
        Gets the pricing_component_id of this PricingComponentValue.
        { \"description\" : \"\", \"verbs\":[\"POST\",\"GET\"] }

        :return: The pricing_component_id of this PricingComponentValue.
        :rtype: str
        """
        return self._pricing_component_id

    @pricing_component_id.setter
    def pricing_component_id(self, pricing_component_id):
        """
        Sets the pricing_component_id of this PricingComponentValue.
        { \"description\" : \"\", \"verbs\":[\"POST\",\"GET\"] }

        :param pricing_component_id: The pricing_component_id of this PricingComponentValue.
        :type: str
        """

        self._pricing_component_id = pricing_component_id

    @property
    def pricing_component_name(self):
        """
        Gets the pricing_component_name of this PricingComponentValue.
        { \"description\" : \"Name of the pricing-component associated with the pricing-component-value.\", \"verbs\":[\"GET\"] }

        :return: The pricing_component_name of this PricingComponentValue.
        :rtype: str
        """
        return self._pricing_component_name

    @pricing_component_name.setter
    def pricing_component_name(self, pricing_component_name):
        """
        Sets the pricing_component_name of this PricingComponentValue.
        { \"description\" : \"Name of the pricing-component associated with the pricing-component-value.\", \"verbs\":[\"GET\"] }

        :param pricing_component_name: The pricing_component_name of this PricingComponentValue.
        :type: str
        """

        self._pricing_component_name = pricing_component_name

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this PricingComponentValue.
        { \"description\" : \"Value can be left null if setting the pricing component value on the subscription directly.\", \"verbs\":[\"GET\", \"POST\"] }

        :return: The subscription_id of this PricingComponentValue.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this PricingComponentValue.
        { \"description\" : \"Value can be left null if setting the pricing component value on the subscription directly.\", \"verbs\":[\"GET\", \"POST\"] }

        :param subscription_id: The subscription_id of this PricingComponentValue.
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def organization_id(self):
        """
        Gets the organization_id of this PricingComponentValue.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The organization_id of this PricingComponentValue.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this PricingComponentValue.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param organization_id: The organization_id of this PricingComponentValue.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def value(self):
        """
        Gets the value of this PricingComponentValue.
        { \"description\" : \"Quantity of a particular pricing component the subscription should have. For example if you have a pricing component for widgets, where $5/widget/month and you set the value to 10 then the customer will be charged $50 ($5 x 10) monthly.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The value of this PricingComponentValue.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this PricingComponentValue.
        { \"description\" : \"Quantity of a particular pricing component the subscription should have. For example if you have a pricing component for widgets, where $5/widget/month and you set the value to 10 then the customer will be charged $50 ($5 x 10) monthly.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param value: The value of this PricingComponentValue.
        :type: int
        """

        self._value = value

    @property
    def applies_from(self):
        """
        Gets the applies_from of this PricingComponentValue.
        { \"description\" : \"<p>The appliesFrom can be left null. If appliesFrom is set, it indicates when a value came into effect.</p>\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The applies_from of this PricingComponentValue.
        :rtype: datetime
        """
        return self._applies_from

    @applies_from.setter
    def applies_from(self, applies_from):
        """
        Sets the applies_from of this PricingComponentValue.
        { \"description\" : \"<p>The appliesFrom can be left null. If appliesFrom is set, it indicates when a value came into effect.</p>\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param applies_from: The applies_from of this PricingComponentValue.
        :type: datetime
        """

        self._applies_from = applies_from

    @property
    def applies_till(self):
        """
        Gets the applies_till of this PricingComponentValue.
        { \"description\" : \"<p>For <span class=\\\"label label-default\\\">setup</span>, <span class=\\\"label label-default\\\">subscription</span>, and <span class=\\\"label label-default\\\">arrears</span> pricing components if appliesTill is specificed the value will be used whilst the time has not been reached. If appliesTill is null the pricing component value will be used until a new value is added. When a new value is added appliesTill will be set to the time the new value will take effect.</p><p><span class=\\\"label label-default\\\">usage</span> pricing applies to the previous billing period as it is charged in-arrears. When adding usage a new pricing component value should be added with appliesTill set to the end of the usages billing period. For example a monthly subscription results in an invoice being generated on the 1<sup>st</sup> of March, the previous months usage period ended on the same date. A usage value should be added to the subscription with the appliesTill set to the invoices periodStart, the 1<sup>st</sup> of March.</p>\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The applies_till of this PricingComponentValue.
        :rtype: datetime
        """
        return self._applies_till

    @applies_till.setter
    def applies_till(self, applies_till):
        """
        Sets the applies_till of this PricingComponentValue.
        { \"description\" : \"<p>For <span class=\\\"label label-default\\\">setup</span>, <span class=\\\"label label-default\\\">subscription</span>, and <span class=\\\"label label-default\\\">arrears</span> pricing components if appliesTill is specificed the value will be used whilst the time has not been reached. If appliesTill is null the pricing component value will be used until a new value is added. When a new value is added appliesTill will be set to the time the new value will take effect.</p><p><span class=\\\"label label-default\\\">usage</span> pricing applies to the previous billing period as it is charged in-arrears. When adding usage a new pricing component value should be added with appliesTill set to the end of the usages billing period. For example a monthly subscription results in an invoice being generated on the 1<sup>st</sup> of March, the previous months usage period ended on the same date. A usage value should be added to the subscription with the appliesTill set to the invoices periodStart, the 1<sup>st</sup> of March.</p>\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param applies_till: The applies_till of this PricingComponentValue.
        :type: datetime
        """

        self._applies_till = applies_till

    @property
    def pending_change(self):
        """
        Gets the pending_change of this PricingComponentValue.


        :return: The pending_change of this PricingComponentValue.
        :rtype: PendingComponentValueChange
        """
        return self._pending_change

    @pending_change.setter
    def pending_change(self, pending_change):
        """
        Sets the pending_change of this PricingComponentValue.


        :param pending_change: The pending_change of this PricingComponentValue.
        :type: PendingComponentValueChange
        """

        self._pending_change = pending_change

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