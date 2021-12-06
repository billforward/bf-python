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

class Webhook(object):
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
        'changed_by': 'str',
        'updated': 'datetime',
        'id': 'str',
        'organization_id': 'str',
        'name': 'str',
        'consecutive_failures': 'int',
        'deleted': 'bool',
        'temporarily_inactive_until': 'datetime',
        'inactive_level': 'int',
        'webhook_subscriptions': 'list[WebhookSubscription]',
        'url': 'str',
        'url': 'str'
    }

    attribute_map = {
        'created': 'created',
        'changed_by': 'changedBy',
        'updated': 'updated',
        'id': 'id',
        'organization_id': 'organizationID',
        'name': 'name',
        'consecutive_failures': 'consecutiveFailures',
        'deleted': 'deleted',
        'temporarily_inactive_until': 'temporarilyInactiveUntil',
        'inactive_level': 'inactiveLevel',
        'webhook_subscriptions': 'webhookSubscriptions',
        'url': 'url',
        'url': 'URL'
    }

    def __init__(self, created=None, changed_by=None, updated=None, id=None, organization_id=None, name=None, consecutive_failures=None, deleted=None, temporarily_inactive_until=None, inactive_level=None, webhook_subscriptions=None, url=None, url=None):  # noqa: E501
        """Webhook - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._changed_by = None
        self._updated = None
        self._id = None
        self._organization_id = None
        self._name = None
        self._consecutive_failures = None
        self._deleted = None
        self._temporarily_inactive_until = None
        self._inactive_level = None
        self._webhook_subscriptions = None
        self._url = None
        self._url = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if changed_by is not None:
            self.changed_by = changed_by
        if updated is not None:
            self.updated = updated
        if id is not None:
            self.id = id
        if organization_id is not None:
            self.organization_id = organization_id
        if name is not None:
            self.name = name
        if consecutive_failures is not None:
            self.consecutive_failures = consecutive_failures
        if deleted is not None:
            self.deleted = deleted
        if temporarily_inactive_until is not None:
            self.temporarily_inactive_until = temporarily_inactive_until
        if inactive_level is not None:
            self.inactive_level = inactive_level
        if webhook_subscriptions is not None:
            self.webhook_subscriptions = webhook_subscriptions
        if url is not None:
            self.url = url
        if url is not None:
            self.url = url

    @property
    def created(self):
        """Gets the created of this Webhook.  # noqa: E501


        :return: The created of this Webhook.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Webhook.


        :param created: The created of this Webhook.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """Gets the changed_by of this Webhook.  # noqa: E501


        :return: The changed_by of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """Sets the changed_by of this Webhook.


        :param changed_by: The changed_by of this Webhook.  # noqa: E501
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """Gets the updated of this Webhook.  # noqa: E501


        :return: The updated of this Webhook.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Webhook.


        :param updated: The updated of this Webhook.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """Gets the id of this Webhook.  # noqa: E501


        :return: The id of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Webhook.


        :param id: The id of this Webhook.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def organization_id(self):
        """Gets the organization_id of this Webhook.  # noqa: E501


        :return: The organization_id of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Webhook.


        :param organization_id: The organization_id of this Webhook.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def name(self):
        """Gets the name of this Webhook.  # noqa: E501


        :return: The name of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Webhook.


        :param name: The name of this Webhook.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def consecutive_failures(self):
        """Gets the consecutive_failures of this Webhook.  # noqa: E501


        :return: The consecutive_failures of this Webhook.  # noqa: E501
        :rtype: int
        """
        return self._consecutive_failures

    @consecutive_failures.setter
    def consecutive_failures(self, consecutive_failures):
        """Sets the consecutive_failures of this Webhook.


        :param consecutive_failures: The consecutive_failures of this Webhook.  # noqa: E501
        :type: int
        """

        self._consecutive_failures = consecutive_failures

    @property
    def deleted(self):
        """Gets the deleted of this Webhook.  # noqa: E501


        :return: The deleted of this Webhook.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Webhook.


        :param deleted: The deleted of this Webhook.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def temporarily_inactive_until(self):
        """Gets the temporarily_inactive_until of this Webhook.  # noqa: E501


        :return: The temporarily_inactive_until of this Webhook.  # noqa: E501
        :rtype: datetime
        """
        return self._temporarily_inactive_until

    @temporarily_inactive_until.setter
    def temporarily_inactive_until(self, temporarily_inactive_until):
        """Sets the temporarily_inactive_until of this Webhook.


        :param temporarily_inactive_until: The temporarily_inactive_until of this Webhook.  # noqa: E501
        :type: datetime
        """

        self._temporarily_inactive_until = temporarily_inactive_until

    @property
    def inactive_level(self):
        """Gets the inactive_level of this Webhook.  # noqa: E501


        :return: The inactive_level of this Webhook.  # noqa: E501
        :rtype: int
        """
        return self._inactive_level

    @inactive_level.setter
    def inactive_level(self, inactive_level):
        """Sets the inactive_level of this Webhook.


        :param inactive_level: The inactive_level of this Webhook.  # noqa: E501
        :type: int
        """

        self._inactive_level = inactive_level

    @property
    def webhook_subscriptions(self):
        """Gets the webhook_subscriptions of this Webhook.  # noqa: E501


        :return: The webhook_subscriptions of this Webhook.  # noqa: E501
        :rtype: list[WebhookSubscription]
        """
        return self._webhook_subscriptions

    @webhook_subscriptions.setter
    def webhook_subscriptions(self, webhook_subscriptions):
        """Sets the webhook_subscriptions of this Webhook.


        :param webhook_subscriptions: The webhook_subscriptions of this Webhook.  # noqa: E501
        :type: list[WebhookSubscription]
        """

        self._webhook_subscriptions = webhook_subscriptions

    @property
    def url(self):
        """Gets the url of this Webhook.  # noqa: E501


        :return: The url of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Webhook.


        :param url: The url of this Webhook.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def url(self):
        """Gets the url of this Webhook.  # noqa: E501


        :return: The url of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Webhook.


        :param url: The url of this Webhook.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(Webhook, dict):
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
        if not isinstance(other, Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
