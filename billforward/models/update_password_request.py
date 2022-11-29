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

class UpdatePasswordRequest(object):
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
        'old_password': 'str',
        'new_password': 'str',
        'confirm_new_password': 'str',
        'organization_id': 'str'
    }

    attribute_map = {
        'old_password': 'oldPassword',
        'new_password': 'newPassword',
        'confirm_new_password': 'confirmNewPassword',
        'organization_id': 'organizationID'
    }

    def __init__(self, old_password=None, new_password=None, confirm_new_password=None, organization_id=None):  # noqa: E501
        """UpdatePasswordRequest - a model defined in Swagger"""  # noqa: E501
        self._old_password = None
        self._new_password = None
        self._confirm_new_password = None
        self._organization_id = None
        self.discriminator = None
        if old_password is not None:
            self.old_password = old_password
        if new_password is not None:
            self.new_password = new_password
        if confirm_new_password is not None:
            self.confirm_new_password = confirm_new_password
        if organization_id is not None:
            self.organization_id = organization_id

    @property
    def old_password(self):
        """Gets the old_password of this UpdatePasswordRequest.  # noqa: E501


        :return: The old_password of this UpdatePasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        """Sets the old_password of this UpdatePasswordRequest.


        :param old_password: The old_password of this UpdatePasswordRequest.  # noqa: E501
        :type: str
        """

        self._old_password = old_password

    @property
    def new_password(self):
        """Gets the new_password of this UpdatePasswordRequest.  # noqa: E501


        :return: The new_password of this UpdatePasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this UpdatePasswordRequest.


        :param new_password: The new_password of this UpdatePasswordRequest.  # noqa: E501
        :type: str
        """

        self._new_password = new_password

    @property
    def confirm_new_password(self):
        """Gets the confirm_new_password of this UpdatePasswordRequest.  # noqa: E501


        :return: The confirm_new_password of this UpdatePasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._confirm_new_password

    @confirm_new_password.setter
    def confirm_new_password(self, confirm_new_password):
        """Sets the confirm_new_password of this UpdatePasswordRequest.


        :param confirm_new_password: The confirm_new_password of this UpdatePasswordRequest.  # noqa: E501
        :type: str
        """

        self._confirm_new_password = confirm_new_password

    @property
    def organization_id(self):
        """Gets the organization_id of this UpdatePasswordRequest.  # noqa: E501


        :return: The organization_id of this UpdatePasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this UpdatePasswordRequest.


        :param organization_id: The organization_id of this UpdatePasswordRequest.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

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
        if issubclass(UpdatePasswordRequest, dict):
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
        if not isinstance(other, UpdatePasswordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
