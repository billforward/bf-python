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

class SalesforceConfigurationResponse(object):
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
        'created': 'datetime',
        'organization_id': 'str',
        'username': 'str',
        'access_token': 'str',
        'authorized': 'bool',
        'refresh_token': 'str',
        'instance_url': 'str',
        'user_role': 'str',
        'notification_email_addresses': 'str',
        'use_test_environment': 'bool'
    }

    attribute_map = {
        'created': 'created',
        'organization_id': 'organizationID',
        'username': 'username',
        'access_token': 'accessToken',
        'authorized': 'authorized',
        'refresh_token': 'refreshToken',
        'instance_url': 'instanceUrl',
        'user_role': 'userRole',
        'notification_email_addresses': 'notificationEmailAddresses',
        'use_test_environment': 'useTestEnvironment'
    }

    def __init__(self, created=None, organization_id=None, username=None, access_token=None, authorized=None, refresh_token=None, instance_url=None, user_role=None, notification_email_addresses=None, use_test_environment=None):  # noqa: E501
        """SalesforceConfigurationResponse - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._organization_id = None
        self._username = None
        self._access_token = None
        self._authorized = None
        self._refresh_token = None
        self._instance_url = None
        self._user_role = None
        self._notification_email_addresses = None
        self._use_test_environment = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if organization_id is not None:
            self.organization_id = organization_id
        if username is not None:
            self.username = username
        if access_token is not None:
            self.access_token = access_token
        if authorized is not None:
            self.authorized = authorized
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if instance_url is not None:
            self.instance_url = instance_url
        if user_role is not None:
            self.user_role = user_role
        if notification_email_addresses is not None:
            self.notification_email_addresses = notification_email_addresses
        if use_test_environment is not None:
            self.use_test_environment = use_test_environment

    @property
    def created(self):
        """Gets the created of this SalesforceConfigurationResponse.  # noqa: E501


        :return: The created of this SalesforceConfigurationResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SalesforceConfigurationResponse.


        :param created: The created of this SalesforceConfigurationResponse.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def organization_id(self):
        """Gets the organization_id of this SalesforceConfigurationResponse.  # noqa: E501


        :return: The organization_id of this SalesforceConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this SalesforceConfigurationResponse.


        :param organization_id: The organization_id of this SalesforceConfigurationResponse.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def username(self):
        """Gets the username of this SalesforceConfigurationResponse.  # noqa: E501


        :return: The username of this SalesforceConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SalesforceConfigurationResponse.


        :param username: The username of this SalesforceConfigurationResponse.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def access_token(self):
        """Gets the access_token of this SalesforceConfigurationResponse.  # noqa: E501


        :return: The access_token of this SalesforceConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this SalesforceConfigurationResponse.


        :param access_token: The access_token of this SalesforceConfigurationResponse.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def authorized(self):
        """Gets the authorized of this SalesforceConfigurationResponse.  # noqa: E501


        :return: The authorized of this SalesforceConfigurationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._authorized

    @authorized.setter
    def authorized(self, authorized):
        """Sets the authorized of this SalesforceConfigurationResponse.


        :param authorized: The authorized of this SalesforceConfigurationResponse.  # noqa: E501
        :type: bool
        """

        self._authorized = authorized

    @property
    def refresh_token(self):
        """Gets the refresh_token of this SalesforceConfigurationResponse.  # noqa: E501


        :return: The refresh_token of this SalesforceConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this SalesforceConfigurationResponse.


        :param refresh_token: The refresh_token of this SalesforceConfigurationResponse.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def instance_url(self):
        """Gets the instance_url of this SalesforceConfigurationResponse.  # noqa: E501


        :return: The instance_url of this SalesforceConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._instance_url

    @instance_url.setter
    def instance_url(self, instance_url):
        """Sets the instance_url of this SalesforceConfigurationResponse.


        :param instance_url: The instance_url of this SalesforceConfigurationResponse.  # noqa: E501
        :type: str
        """

        self._instance_url = instance_url

    @property
    def user_role(self):
        """Gets the user_role of this SalesforceConfigurationResponse.  # noqa: E501


        :return: The user_role of this SalesforceConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_role

    @user_role.setter
    def user_role(self, user_role):
        """Sets the user_role of this SalesforceConfigurationResponse.


        :param user_role: The user_role of this SalesforceConfigurationResponse.  # noqa: E501
        :type: str
        """

        self._user_role = user_role

    @property
    def notification_email_addresses(self):
        """Gets the notification_email_addresses of this SalesforceConfigurationResponse.  # noqa: E501


        :return: The notification_email_addresses of this SalesforceConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._notification_email_addresses

    @notification_email_addresses.setter
    def notification_email_addresses(self, notification_email_addresses):
        """Sets the notification_email_addresses of this SalesforceConfigurationResponse.


        :param notification_email_addresses: The notification_email_addresses of this SalesforceConfigurationResponse.  # noqa: E501
        :type: str
        """

        self._notification_email_addresses = notification_email_addresses

    @property
    def use_test_environment(self):
        """Gets the use_test_environment of this SalesforceConfigurationResponse.  # noqa: E501


        :return: The use_test_environment of this SalesforceConfigurationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._use_test_environment

    @use_test_environment.setter
    def use_test_environment(self, use_test_environment):
        """Sets the use_test_environment of this SalesforceConfigurationResponse.


        :param use_test_environment: The use_test_environment of this SalesforceConfigurationResponse.  # noqa: E501
        :type: bool
        """

        self._use_test_environment = use_test_environment

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
        if issubclass(SalesforceConfigurationResponse, dict):
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
        if not isinstance(other, SalesforceConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
