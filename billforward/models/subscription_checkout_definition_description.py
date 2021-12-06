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

class SubscriptionCheckoutDefinitionDescription(object):
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
        'id': 'str',
        'plan_id': 'str',
        'plan_name': 'str',
        'plan_public_name': 'str',
        'path': 'str',
        'organization_id': 'str'
    }

    attribute_map = {
        'created': 'created',
        'id': 'id',
        'plan_id': 'planID',
        'plan_name': 'planName',
        'plan_public_name': 'planPublicName',
        'path': 'path',
        'organization_id': 'organizationID'
    }

    def __init__(self, created=None, id=None, plan_id=None, plan_name=None, plan_public_name=None, path=None, organization_id=None):  # noqa: E501
        """SubscriptionCheckoutDefinitionDescription - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._id = None
        self._plan_id = None
        self._plan_name = None
        self._plan_public_name = None
        self._path = None
        self._organization_id = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if plan_id is not None:
            self.plan_id = plan_id
        if plan_name is not None:
            self.plan_name = plan_name
        if plan_public_name is not None:
            self.plan_public_name = plan_public_name
        if path is not None:
            self.path = path
        if organization_id is not None:
            self.organization_id = organization_id

    @property
    def created(self):
        """Gets the created of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501


        :return: The created of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SubscriptionCheckoutDefinitionDescription.


        :param created: The created of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501


        :return: The id of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionCheckoutDefinitionDescription.


        :param id: The id of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def plan_id(self):
        """Gets the plan_id of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501


        :return: The plan_id of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this SubscriptionCheckoutDefinitionDescription.


        :param plan_id: The plan_id of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501
        :type: str
        """

        self._plan_id = plan_id

    @property
    def plan_name(self):
        """Gets the plan_name of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501


        :return: The plan_name of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this SubscriptionCheckoutDefinitionDescription.


        :param plan_name: The plan_name of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501
        :type: str
        """

        self._plan_name = plan_name

    @property
    def plan_public_name(self):
        """Gets the plan_public_name of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501


        :return: The plan_public_name of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501
        :rtype: str
        """
        return self._plan_public_name

    @plan_public_name.setter
    def plan_public_name(self, plan_public_name):
        """Sets the plan_public_name of this SubscriptionCheckoutDefinitionDescription.


        :param plan_public_name: The plan_public_name of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501
        :type: str
        """

        self._plan_public_name = plan_public_name

    @property
    def path(self):
        """Gets the path of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501


        :return: The path of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SubscriptionCheckoutDefinitionDescription.


        :param path: The path of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def organization_id(self):
        """Gets the organization_id of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501


        :return: The organization_id of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this SubscriptionCheckoutDefinitionDescription.


        :param organization_id: The organization_id of this SubscriptionCheckoutDefinitionDescription.  # noqa: E501
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
        if issubclass(SubscriptionCheckoutDefinitionDescription, dict):
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
        if not isinstance(other, SubscriptionCheckoutDefinitionDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other