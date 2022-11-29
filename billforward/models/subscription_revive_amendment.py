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
from billforward.models.amendment import Amendment  # noqa: F401,E501

class SubscriptionReviveAmendment(Amendment):
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
        'revive_children': 'bool',
        'failed_payment_behaviour': 'str'
    }
    if hasattr(Amendment, "swagger_types"):
        swagger_types.update(Amendment.swagger_types)

    attribute_map = {
        'revive_children': 'reviveChildren',
        'failed_payment_behaviour': 'failedPaymentBehaviour'
    }
    if hasattr(Amendment, "attribute_map"):
        attribute_map.update(Amendment.attribute_map)

    def __init__(self, revive_children=None, failed_payment_behaviour=None, *args, **kwargs):  # noqa: E501
        """SubscriptionReviveAmendment - a model defined in Swagger"""  # noqa: E501
        self._revive_children = None
        self._failed_payment_behaviour = None
        self.discriminator = None
        if revive_children is not None:
            self.revive_children = revive_children
        if failed_payment_behaviour is not None:
            self.failed_payment_behaviour = failed_payment_behaviour
        Amendment.__init__(self, *args, **kwargs)

    @property
    def revive_children(self):
        """Gets the revive_children of this SubscriptionReviveAmendment.  # noqa: E501


        :return: The revive_children of this SubscriptionReviveAmendment.  # noqa: E501
        :rtype: bool
        """
        return self._revive_children

    @revive_children.setter
    def revive_children(self, revive_children):
        """Sets the revive_children of this SubscriptionReviveAmendment.


        :param revive_children: The revive_children of this SubscriptionReviveAmendment.  # noqa: E501
        :type: bool
        """

        self._revive_children = revive_children

    @property
    def failed_payment_behaviour(self):
        """Gets the failed_payment_behaviour of this SubscriptionReviveAmendment.  # noqa: E501


        :return: The failed_payment_behaviour of this SubscriptionReviveAmendment.  # noqa: E501
        :rtype: str
        """
        return self._failed_payment_behaviour

    @failed_payment_behaviour.setter
    def failed_payment_behaviour(self, failed_payment_behaviour):
        """Sets the failed_payment_behaviour of this SubscriptionReviveAmendment.


        :param failed_payment_behaviour: The failed_payment_behaviour of this SubscriptionReviveAmendment.  # noqa: E501
        :type: str
        """
        allowed_values = ["CancelSubscription", "None"]  # noqa: E501
        if failed_payment_behaviour not in allowed_values:
            raise ValueError(
                "Invalid value for `failed_payment_behaviour` ({0}), must be one of {1}"  # noqa: E501
                .format(failed_payment_behaviour, allowed_values)
            )

        self._failed_payment_behaviour = failed_payment_behaviour

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
        if issubclass(SubscriptionReviveAmendment, dict):
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
        if not isinstance(other, SubscriptionReviveAmendment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
