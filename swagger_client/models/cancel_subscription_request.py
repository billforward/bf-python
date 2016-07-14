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


class CancelSubscriptionRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, subscription_id=None, state=None, source=None, service_end=None, cancellation_credit=None, cancel_children=None, cancel_empty_parent=None):
        """
        CancelSubscriptionRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'subscription_id': 'str',
            'state': 'str',
            'source': 'str',
            'service_end': 'str',
            'cancellation_credit': 'str',
            'cancel_children': 'bool',
            'cancel_empty_parent': 'bool'
        }

        self.attribute_map = {
            'subscription_id': 'subscriptionID',
            'state': 'state',
            'source': 'source',
            'service_end': 'serviceEnd',
            'cancellation_credit': 'cancellationCredit',
            'cancel_children': 'cancelChildren',
            'cancel_empty_parent': 'cancelEmptyParent'
        }

        self._subscription_id = subscription_id
        self._state = state
        self._source = source
        self._service_end = service_end
        self._cancellation_credit = cancellation_credit
        self._cancel_children = cancel_children
        self._cancel_empty_parent = cancel_empty_parent

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this CancelSubscriptionRequest.


        :return: The subscription_id of this CancelSubscriptionRequest.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this CancelSubscriptionRequest.


        :param subscription_id: The subscription_id of this CancelSubscriptionRequest.
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def state(self):
        """
        Gets the state of this CancelSubscriptionRequest.


        :return: The state of this CancelSubscriptionRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this CancelSubscriptionRequest.


        :param state: The state of this CancelSubscriptionRequest.
        :type: str
        """

        self._state = state

    @property
    def source(self):
        """
        Gets the source of this CancelSubscriptionRequest.


        :return: The source of this CancelSubscriptionRequest.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this CancelSubscriptionRequest.


        :param source: The source of this CancelSubscriptionRequest.
        :type: str
        """

        self._source = source

    @property
    def service_end(self):
        """
        Gets the service_end of this CancelSubscriptionRequest.


        :return: The service_end of this CancelSubscriptionRequest.
        :rtype: str
        """
        return self._service_end

    @service_end.setter
    def service_end(self, service_end):
        """
        Sets the service_end of this CancelSubscriptionRequest.


        :param service_end: The service_end of this CancelSubscriptionRequest.
        :type: str
        """
        allowed_values = ["Immediate", "AtPeriodEnd"]
        if service_end not in allowed_values:
            raise ValueError(
                "Invalid value for `service_end` ({0}), must be one of {1}"
                .format(service_end, allowed_values)
            )

        self._service_end = service_end

    @property
    def cancellation_credit(self):
        """
        Gets the cancellation_credit of this CancelSubscriptionRequest.
        Specifies whether the service will end immediately on cancellation or if it will continue until the end of the current period. Default: AtPeriodEnd

        :return: The cancellation_credit of this CancelSubscriptionRequest.
        :rtype: str
        """
        return self._cancellation_credit

    @cancellation_credit.setter
    def cancellation_credit(self, cancellation_credit):
        """
        Sets the cancellation_credit of this CancelSubscriptionRequest.
        Specifies whether the service will end immediately on cancellation or if it will continue until the end of the current period. Default: AtPeriodEnd

        :param cancellation_credit: The cancellation_credit of this CancelSubscriptionRequest.
        :type: str
        """
        allowed_values = ["Credit", "None"]
        if cancellation_credit not in allowed_values:
            raise ValueError(
                "Invalid value for `cancellation_credit` ({0}), must be one of {1}"
                .format(cancellation_credit, allowed_values)
            )

        self._cancellation_credit = cancellation_credit

    @property
    def cancel_children(self):
        """
        Gets the cancel_children of this CancelSubscriptionRequest.


        :return: The cancel_children of this CancelSubscriptionRequest.
        :rtype: bool
        """
        return self._cancel_children

    @cancel_children.setter
    def cancel_children(self, cancel_children):
        """
        Sets the cancel_children of this CancelSubscriptionRequest.


        :param cancel_children: The cancel_children of this CancelSubscriptionRequest.
        :type: bool
        """

        self._cancel_children = cancel_children

    @property
    def cancel_empty_parent(self):
        """
        Gets the cancel_empty_parent of this CancelSubscriptionRequest.


        :return: The cancel_empty_parent of this CancelSubscriptionRequest.
        :rtype: bool
        """
        return self._cancel_empty_parent

    @cancel_empty_parent.setter
    def cancel_empty_parent(self, cancel_empty_parent):
        """
        Sets the cancel_empty_parent of this CancelSubscriptionRequest.


        :param cancel_empty_parent: The cancel_empty_parent of this CancelSubscriptionRequest.
        :type: bool
        """

        self._cancel_empty_parent = cancel_empty_parent

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
