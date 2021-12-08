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
from billforward.models.api_configuration import APIConfiguration  # noqa: F401,E501

class TrustCommerceConfiguration(APIConfiguration):
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
        'cust_id': 'str',
        'password': 'str'
    }
    if hasattr(APIConfiguration, "swagger_types"):
        swagger_types.update(APIConfiguration.swagger_types)

    attribute_map = {
        'cust_id': 'custID',
        'password': 'password'
    }
    if hasattr(APIConfiguration, "attribute_map"):
        attribute_map.update(APIConfiguration.attribute_map)

    def __init__(self, cust_id=None, password=None, *args, **kwargs):  # noqa: E501
        """TrustCommerceConfiguration - a model defined in Swagger"""  # noqa: E501
        self._cust_id = None
        self._password = None
        self.discriminator = None
        if cust_id is not None:
            self.cust_id = cust_id
        if password is not None:
            self.password = password
        APIConfiguration.__init__(self, *args, **kwargs)

    @property
    def cust_id(self):
        """Gets the cust_id of this TrustCommerceConfiguration.  # noqa: E501


        :return: The cust_id of this TrustCommerceConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._cust_id

    @cust_id.setter
    def cust_id(self, cust_id):
        """Sets the cust_id of this TrustCommerceConfiguration.


        :param cust_id: The cust_id of this TrustCommerceConfiguration.  # noqa: E501
        :type: str
        """

        self._cust_id = cust_id

    @property
    def password(self):
        """Gets the password of this TrustCommerceConfiguration.  # noqa: E501


        :return: The password of this TrustCommerceConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this TrustCommerceConfiguration.


        :param password: The password of this TrustCommerceConfiguration.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if issubclass(TrustCommerceConfiguration, dict):
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
        if not isinstance(other, TrustCommerceConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
