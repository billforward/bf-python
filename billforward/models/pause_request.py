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

class PauseRequest(object):
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
        'resume': 'datetime',
        'new_subscription_start': 'datetime',
        'new_subscription_state': 'str',
        'organization_id': 'str',
        'subscription_id': 'str',
        'dry_run': 'bool'
    }

    attribute_map = {
        'created': 'created',
        'resume': 'resume',
        'new_subscription_start': 'newSubscriptionStart',
        'new_subscription_state': 'newSubscriptionState',
        'organization_id': 'organizationID',
        'subscription_id': 'subscriptionID',
        'dry_run': 'dryRun'
    }

    def __init__(self, created=None, resume=None, new_subscription_start=None, new_subscription_state=None, organization_id=None, subscription_id=None, dry_run=None):  # noqa: E501
        """PauseRequest - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._resume = None
        self._new_subscription_start = None
        self._new_subscription_state = None
        self._organization_id = None
        self._subscription_id = None
        self._dry_run = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if resume is not None:
            self.resume = resume
        if new_subscription_start is not None:
            self.new_subscription_start = new_subscription_start
        if new_subscription_state is not None:
            self.new_subscription_state = new_subscription_state
        if organization_id is not None:
            self.organization_id = organization_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if dry_run is not None:
            self.dry_run = dry_run

    @property
    def created(self):
        """Gets the created of this PauseRequest.  # noqa: E501


        :return: The created of this PauseRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PauseRequest.


        :param created: The created of this PauseRequest.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def resume(self):
        """Gets the resume of this PauseRequest.  # noqa: E501


        :return: The resume of this PauseRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this PauseRequest.


        :param resume: The resume of this PauseRequest.  # noqa: E501
        :type: datetime
        """

        self._resume = resume

    @property
    def new_subscription_start(self):
        """Gets the new_subscription_start of this PauseRequest.  # noqa: E501


        :return: The new_subscription_start of this PauseRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._new_subscription_start

    @new_subscription_start.setter
    def new_subscription_start(self, new_subscription_start):
        """Sets the new_subscription_start of this PauseRequest.


        :param new_subscription_start: The new_subscription_start of this PauseRequest.  # noqa: E501
        :type: datetime
        """

        self._new_subscription_start = new_subscription_start

    @property
    def new_subscription_state(self):
        """Gets the new_subscription_state of this PauseRequest.  # noqa: E501


        :return: The new_subscription_state of this PauseRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_subscription_state

    @new_subscription_state.setter
    def new_subscription_state(self, new_subscription_state):
        """Sets the new_subscription_state of this PauseRequest.


        :param new_subscription_state: The new_subscription_state of this PauseRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Trial", "Provisioned", "Paid", "AwaitingPayment", "Cancelled", "Failed", "Expired"]  # noqa: E501
        if new_subscription_state not in allowed_values:
            raise ValueError(
                "Invalid value for `new_subscription_state` ({0}), must be one of {1}"  # noqa: E501
                .format(new_subscription_state, allowed_values)
            )

        self._new_subscription_state = new_subscription_state

    @property
    def organization_id(self):
        """Gets the organization_id of this PauseRequest.  # noqa: E501


        :return: The organization_id of this PauseRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this PauseRequest.


        :param organization_id: The organization_id of this PauseRequest.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this PauseRequest.  # noqa: E501


        :return: The subscription_id of this PauseRequest.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this PauseRequest.


        :param subscription_id: The subscription_id of this PauseRequest.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def dry_run(self):
        """Gets the dry_run of this PauseRequest.  # noqa: E501


        :return: The dry_run of this PauseRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this PauseRequest.


        :param dry_run: The dry_run of this PauseRequest.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

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
        if issubclass(PauseRequest, dict):
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
        if not isinstance(other, PauseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
