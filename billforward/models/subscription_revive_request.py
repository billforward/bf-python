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

class SubscriptionReviveRequest(object):
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
        'organization_id': 'str',
        'subscription_id': 'str',
        'state': 'str',
        'start': 'datetime',
        'failed_payment_behaviour': 'str',
        'revive_children': 'bool'
    }

    attribute_map = {
        'organization_id': 'organizationID',
        'subscription_id': 'subscriptionID',
        'state': 'state',
        'start': 'start',
        'failed_payment_behaviour': 'failedPaymentBehaviour',
        'revive_children': 'reviveChildren'
    }

    def __init__(self, organization_id=None, subscription_id=None, state=None, start=None, failed_payment_behaviour=None, revive_children=None):  # noqa: E501
        """SubscriptionReviveRequest - a model defined in Swagger"""  # noqa: E501
        self._organization_id = None
        self._subscription_id = None
        self._state = None
        self._start = None
        self._failed_payment_behaviour = None
        self._revive_children = None
        self.discriminator = None
        if organization_id is not None:
            self.organization_id = organization_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if state is not None:
            self.state = state
        if start is not None:
            self.start = start
        if failed_payment_behaviour is not None:
            self.failed_payment_behaviour = failed_payment_behaviour
        if revive_children is not None:
            self.revive_children = revive_children

    @property
    def organization_id(self):
        """Gets the organization_id of this SubscriptionReviveRequest.  # noqa: E501


        :return: The organization_id of this SubscriptionReviveRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this SubscriptionReviveRequest.


        :param organization_id: The organization_id of this SubscriptionReviveRequest.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this SubscriptionReviveRequest.  # noqa: E501


        :return: The subscription_id of this SubscriptionReviveRequest.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this SubscriptionReviveRequest.


        :param subscription_id: The subscription_id of this SubscriptionReviveRequest.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def state(self):
        """Gets the state of this SubscriptionReviveRequest.  # noqa: E501


        :return: The state of this SubscriptionReviveRequest.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubscriptionReviveRequest.


        :param state: The state of this SubscriptionReviveRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Provisioned", "AwaitingPayment"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def start(self):
        """Gets the start of this SubscriptionReviveRequest.  # noqa: E501


        :return: The start of this SubscriptionReviveRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this SubscriptionReviveRequest.


        :param start: The start of this SubscriptionReviveRequest.  # noqa: E501
        :type: datetime
        """

        self._start = start

    @property
    def failed_payment_behaviour(self):
        """Gets the failed_payment_behaviour of this SubscriptionReviveRequest.  # noqa: E501


        :return: The failed_payment_behaviour of this SubscriptionReviveRequest.  # noqa: E501
        :rtype: str
        """
        return self._failed_payment_behaviour

    @failed_payment_behaviour.setter
    def failed_payment_behaviour(self, failed_payment_behaviour):
        """Sets the failed_payment_behaviour of this SubscriptionReviveRequest.


        :param failed_payment_behaviour: The failed_payment_behaviour of this SubscriptionReviveRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["CancelSubscription", "None"]  # noqa: E501
        if failed_payment_behaviour not in allowed_values:
            raise ValueError(
                "Invalid value for `failed_payment_behaviour` ({0}), must be one of {1}"  # noqa: E501
                .format(failed_payment_behaviour, allowed_values)
            )

        self._failed_payment_behaviour = failed_payment_behaviour

    @property
    def revive_children(self):
        """Gets the revive_children of this SubscriptionReviveRequest.  # noqa: E501


        :return: The revive_children of this SubscriptionReviveRequest.  # noqa: E501
        :rtype: bool
        """
        return self._revive_children

    @revive_children.setter
    def revive_children(self, revive_children):
        """Sets the revive_children of this SubscriptionReviveRequest.


        :param revive_children: The revive_children of this SubscriptionReviveRequest.  # noqa: E501
        :type: bool
        """

        self._revive_children = revive_children

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
        if issubclass(SubscriptionReviveRequest, dict):
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
        if not isinstance(other, SubscriptionReviveRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other