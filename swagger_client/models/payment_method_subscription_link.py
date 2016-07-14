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


class PaymentMethodSubscriptionLink(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, changed_by=None, updated=None, id=None, crm_id=None, subscription_id=None, organization_id=None, payment_method_id=None, deleted=False, payment_method=None):
        """
        PaymentMethodSubscriptionLink - a model defined in Swagger

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
            'crm_id': 'str',
            'subscription_id': 'str',
            'organization_id': 'str',
            'payment_method_id': 'str',
            'deleted': 'bool',
            'payment_method': 'PaymentMethod'
        }

        self.attribute_map = {
            'created': 'created',
            'changed_by': 'changedBy',
            'updated': 'updated',
            'id': 'id',
            'crm_id': 'crmID',
            'subscription_id': 'subscriptionID',
            'organization_id': 'organizationID',
            'payment_method_id': 'paymentMethodID',
            'deleted': 'deleted',
            'payment_method': 'paymentMethod'
        }

        self._created = created
        self._changed_by = changed_by
        self._updated = updated
        self._id = id
        self._crm_id = crm_id
        self._subscription_id = subscription_id
        self._organization_id = organization_id
        self._payment_method_id = payment_method_id
        self._deleted = deleted
        self._payment_method = payment_method

    @property
    def created(self):
        """
        Gets the created of this PaymentMethodSubscriptionLink.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this PaymentMethodSubscriptionLink.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this PaymentMethodSubscriptionLink.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this PaymentMethodSubscriptionLink.
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """
        Gets the changed_by of this PaymentMethodSubscriptionLink.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :return: The changed_by of this PaymentMethodSubscriptionLink.
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """
        Sets the changed_by of this PaymentMethodSubscriptionLink.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :param changed_by: The changed_by of this PaymentMethodSubscriptionLink.
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """
        Gets the updated of this PaymentMethodSubscriptionLink.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :return: The updated of this PaymentMethodSubscriptionLink.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this PaymentMethodSubscriptionLink.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :param updated: The updated of this PaymentMethodSubscriptionLink.
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """
        Gets the id of this PaymentMethodSubscriptionLink.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The id of this PaymentMethodSubscriptionLink.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PaymentMethodSubscriptionLink.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param id: The id of this PaymentMethodSubscriptionLink.
        :type: str
        """

        self._id = id

    @property
    def crm_id(self):
        """
        Gets the crm_id of this PaymentMethodSubscriptionLink.
        { \"description\" : \"CRM ID of the product-rate-plan.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The crm_id of this PaymentMethodSubscriptionLink.
        :rtype: str
        """
        return self._crm_id

    @crm_id.setter
    def crm_id(self, crm_id):
        """
        Sets the crm_id of this PaymentMethodSubscriptionLink.
        { \"description\" : \"CRM ID of the product-rate-plan.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param crm_id: The crm_id of this PaymentMethodSubscriptionLink.
        :type: str
        """

        self._crm_id = crm_id

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this PaymentMethodSubscriptionLink.
        { \"description\" : \"Subscription to add payment method to.\", \"verbs\":[\"POST\",\"GET\"] }

        :return: The subscription_id of this PaymentMethodSubscriptionLink.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this PaymentMethodSubscriptionLink.
        { \"description\" : \"Subscription to add payment method to.\", \"verbs\":[\"POST\",\"GET\"] }

        :param subscription_id: The subscription_id of this PaymentMethodSubscriptionLink.
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def organization_id(self):
        """
        Gets the organization_id of this PaymentMethodSubscriptionLink.


        :return: The organization_id of this PaymentMethodSubscriptionLink.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this PaymentMethodSubscriptionLink.


        :param organization_id: The organization_id of this PaymentMethodSubscriptionLink.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def payment_method_id(self):
        """
        Gets the payment_method_id of this PaymentMethodSubscriptionLink.
        { \"description\" : \"Payment method to add to subscription.\", \"verbs\":[\"POST\",\"GET\"] }

        :return: The payment_method_id of this PaymentMethodSubscriptionLink.
        :rtype: str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """
        Sets the payment_method_id of this PaymentMethodSubscriptionLink.
        { \"description\" : \"Payment method to add to subscription.\", \"verbs\":[\"POST\",\"GET\"] }

        :param payment_method_id: The payment_method_id of this PaymentMethodSubscriptionLink.
        :type: str
        """

        self._payment_method_id = payment_method_id

    @property
    def deleted(self):
        """
        Gets the deleted of this PaymentMethodSubscriptionLink.


        :return: The deleted of this PaymentMethodSubscriptionLink.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of this PaymentMethodSubscriptionLink.


        :param deleted: The deleted of this PaymentMethodSubscriptionLink.
        :type: bool
        """

        self._deleted = deleted

    @property
    def payment_method(self):
        """
        Gets the payment_method of this PaymentMethodSubscriptionLink.


        :return: The payment_method of this PaymentMethodSubscriptionLink.
        :rtype: PaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """
        Sets the payment_method of this PaymentMethodSubscriptionLink.


        :param payment_method: The payment_method of this PaymentMethodSubscriptionLink.
        :type: PaymentMethod
        """

        self._payment_method = payment_method

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