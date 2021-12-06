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
from billforward.models.additional_data import AdditionalData  # noqa: F401,E501

class StripeAdditionalData(AdditionalData):
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
        'setup_intent_client_secret': 'str',
        'setup_intent_status': 'str'
    }
    if hasattr(AdditionalData, "swagger_types"):
        swagger_types.update(AdditionalData.swagger_types)

    attribute_map = {
        'setup_intent_client_secret': 'setupIntentClientSecret',
        'setup_intent_status': 'setupIntentStatus'
    }
    if hasattr(AdditionalData, "attribute_map"):
        attribute_map.update(AdditionalData.attribute_map)

    def __init__(self, setup_intent_client_secret=None, setup_intent_status=None, *args, **kwargs):  # noqa: E501
        """StripeAdditionalData - a model defined in Swagger"""  # noqa: E501
        self._setup_intent_client_secret = None
        self._setup_intent_status = None
        self.discriminator = None
        if setup_intent_client_secret is not None:
            self.setup_intent_client_secret = setup_intent_client_secret
        if setup_intent_status is not None:
            self.setup_intent_status = setup_intent_status
        AdditionalData.__init__(self, *args, **kwargs)

    @property
    def setup_intent_client_secret(self):
        """Gets the setup_intent_client_secret of this StripeAdditionalData.  # noqa: E501


        :return: The setup_intent_client_secret of this StripeAdditionalData.  # noqa: E501
        :rtype: str
        """
        return self._setup_intent_client_secret

    @setup_intent_client_secret.setter
    def setup_intent_client_secret(self, setup_intent_client_secret):
        """Sets the setup_intent_client_secret of this StripeAdditionalData.


        :param setup_intent_client_secret: The setup_intent_client_secret of this StripeAdditionalData.  # noqa: E501
        :type: str
        """

        self._setup_intent_client_secret = setup_intent_client_secret

    @property
    def setup_intent_status(self):
        """Gets the setup_intent_status of this StripeAdditionalData.  # noqa: E501


        :return: The setup_intent_status of this StripeAdditionalData.  # noqa: E501
        :rtype: str
        """
        return self._setup_intent_status

    @setup_intent_status.setter
    def setup_intent_status(self, setup_intent_status):
        """Sets the setup_intent_status of this StripeAdditionalData.


        :param setup_intent_status: The setup_intent_status of this StripeAdditionalData.  # noqa: E501
        :type: str
        """

        self._setup_intent_status = setup_intent_status

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
        if issubclass(StripeAdditionalData, dict):
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
        if not isinstance(other, StripeAdditionalData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
