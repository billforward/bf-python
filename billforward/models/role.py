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

class Role(object):
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
        'description': 'str',
        'revoked': 'datetime',
        'deleted': 'bool',
        'default_role': 'bool',
        'default_returned': 'bool',
        'permissions': 'list[BFPermission]'
    }

    attribute_map = {
        'created': 'created',
        'changed_by': 'changedBy',
        'updated': 'updated',
        'id': 'id',
        'organization_id': 'organizationID',
        'name': 'name',
        'description': 'description',
        'revoked': 'revoked',
        'deleted': 'deleted',
        'default_role': 'defaultRole',
        'default_returned': 'defaultReturned',
        'permissions': 'permissions'
    }

    def __init__(self, created=None, changed_by=None, updated=None, id=None, organization_id=None, name=None, description=None, revoked=None, deleted=None, default_role=None, default_returned=None, permissions=None):  # noqa: E501
        """Role - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._changed_by = None
        self._updated = None
        self._id = None
        self._organization_id = None
        self._name = None
        self._description = None
        self._revoked = None
        self._deleted = None
        self._default_role = None
        self._default_returned = None
        self._permissions = None
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
        if description is not None:
            self.description = description
        if revoked is not None:
            self.revoked = revoked
        if deleted is not None:
            self.deleted = deleted
        if default_role is not None:
            self.default_role = default_role
        if default_returned is not None:
            self.default_returned = default_returned
        if permissions is not None:
            self.permissions = permissions

    @property
    def created(self):
        """Gets the created of this Role.  # noqa: E501


        :return: The created of this Role.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Role.


        :param created: The created of this Role.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """Gets the changed_by of this Role.  # noqa: E501


        :return: The changed_by of this Role.  # noqa: E501
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """Sets the changed_by of this Role.


        :param changed_by: The changed_by of this Role.  # noqa: E501
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """Gets the updated of this Role.  # noqa: E501


        :return: The updated of this Role.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Role.


        :param updated: The updated of this Role.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """Gets the id of this Role.  # noqa: E501


        :return: The id of this Role.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Role.


        :param id: The id of this Role.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def organization_id(self):
        """Gets the organization_id of this Role.  # noqa: E501


        :return: The organization_id of this Role.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Role.


        :param organization_id: The organization_id of this Role.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def name(self):
        """Gets the name of this Role.  # noqa: E501


        :return: The name of this Role.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Role.


        :param name: The name of this Role.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Role.  # noqa: E501


        :return: The description of this Role.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Role.


        :param description: The description of this Role.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def revoked(self):
        """Gets the revoked of this Role.  # noqa: E501


        :return: The revoked of this Role.  # noqa: E501
        :rtype: datetime
        """
        return self._revoked

    @revoked.setter
    def revoked(self, revoked):
        """Sets the revoked of this Role.


        :param revoked: The revoked of this Role.  # noqa: E501
        :type: datetime
        """

        self._revoked = revoked

    @property
    def deleted(self):
        """Gets the deleted of this Role.  # noqa: E501


        :return: The deleted of this Role.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Role.


        :param deleted: The deleted of this Role.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def default_role(self):
        """Gets the default_role of this Role.  # noqa: E501


        :return: The default_role of this Role.  # noqa: E501
        :rtype: bool
        """
        return self._default_role

    @default_role.setter
    def default_role(self, default_role):
        """Sets the default_role of this Role.


        :param default_role: The default_role of this Role.  # noqa: E501
        :type: bool
        """

        self._default_role = default_role

    @property
    def default_returned(self):
        """Gets the default_returned of this Role.  # noqa: E501


        :return: The default_returned of this Role.  # noqa: E501
        :rtype: bool
        """
        return self._default_returned

    @default_returned.setter
    def default_returned(self, default_returned):
        """Sets the default_returned of this Role.


        :param default_returned: The default_returned of this Role.  # noqa: E501
        :type: bool
        """

        self._default_returned = default_returned

    @property
    def permissions(self):
        """Gets the permissions of this Role.  # noqa: E501


        :return: The permissions of this Role.  # noqa: E501
        :rtype: list[BFPermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Role.


        :param permissions: The permissions of this Role.  # noqa: E501
        :type: list[BFPermission]
        """

        self._permissions = permissions

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
        if issubclass(Role, dict):
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
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
