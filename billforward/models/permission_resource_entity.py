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

class PermissionResourceEntity(object):
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
        'resources': 'list[str]'
    }

    attribute_map = {
        'created': 'created',
        'organization_id': 'organizationID',
        'resources': 'resources'
    }

    def __init__(self, created=None, organization_id=None, resources=None):  # noqa: E501
        """PermissionResourceEntity - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._organization_id = None
        self._resources = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if organization_id is not None:
            self.organization_id = organization_id
        if resources is not None:
            self.resources = resources

    @property
    def created(self):
        """Gets the created of this PermissionResourceEntity.  # noqa: E501


        :return: The created of this PermissionResourceEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PermissionResourceEntity.


        :param created: The created of this PermissionResourceEntity.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def organization_id(self):
        """Gets the organization_id of this PermissionResourceEntity.  # noqa: E501


        :return: The organization_id of this PermissionResourceEntity.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this PermissionResourceEntity.


        :param organization_id: The organization_id of this PermissionResourceEntity.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def resources(self):
        """Gets the resources of this PermissionResourceEntity.  # noqa: E501


        :return: The resources of this PermissionResourceEntity.  # noqa: E501
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this PermissionResourceEntity.


        :param resources: The resources of this PermissionResourceEntity.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["All", "Account", "Address", "Amendment", "Analytics", "Audit", "BFAdmin", "BFJS", "Charge", "CheckoutDefinition", "Client", "Configuration", "CouponBook", "CouponBookDefinition", "CouponDefinition", "CouponInstance", "CouponModifier", "CouponRule", "Coupon", "Credit", "CybersourceToken", "Dunning", "Email", "FixedTerm", "Gateway", "Invoice", "InvoiceTemplateConfiguration", "Metadata", "Notification", "Organization", "OrganizationProfile", "Password", "PaymentMethod", "Payment", "Permission", "PricingComponent", "PricingComponentTier", "PricingComponentValueChange", "PricingComponentValue", "ProductRatePlan", "Product", "ProductResources", "Profile", "SubscriptionNotificationConfiguration", "Quote", "Receipt", "Report", "Refund", "Salesforce", "Search", "Subscription", "Tax", "UnitOfMeasure", "Usage", "Username", "User", "UserResources", "Webhook", "Contract", "Xero", "QuickBooks", "ContractPeriod", "HubSpot", "EmailNotifications", "EmailNotificationsConfig", "Shuttle", "RequestLogging"]  # noqa: E501
        if not set(resources).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `resources` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(resources) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._resources = resources

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
        if issubclass(PermissionResourceEntity, dict):
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
        if not isinstance(other, PermissionResourceEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
