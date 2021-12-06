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

class BraintreeToken(object):
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
        'account_id': 'str',
        'card_details_id': 'str',
        'organization_id': 'str',
        'customer_id': 'str',
        'credit_card_id': 'str',
        'device_data': 'str',
        'merchant_account_id': 'str',
        'deleted': 'bool'
    }

    attribute_map = {
        'created': 'created',
        'changed_by': 'changedBy',
        'updated': 'updated',
        'id': 'id',
        'account_id': 'accountID',
        'card_details_id': 'cardDetailsID',
        'organization_id': 'organizationID',
        'customer_id': 'customerID',
        'credit_card_id': 'creditCardID',
        'device_data': 'deviceData',
        'merchant_account_id': 'merchantAccountId',
        'deleted': 'deleted'
    }

    def __init__(self, created=None, changed_by=None, updated=None, id=None, account_id=None, card_details_id=None, organization_id=None, customer_id=None, credit_card_id=None, device_data=None, merchant_account_id=None, deleted=None):  # noqa: E501
        """BraintreeToken - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._changed_by = None
        self._updated = None
        self._id = None
        self._account_id = None
        self._card_details_id = None
        self._organization_id = None
        self._customer_id = None
        self._credit_card_id = None
        self._device_data = None
        self._merchant_account_id = None
        self._deleted = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if changed_by is not None:
            self.changed_by = changed_by
        if updated is not None:
            self.updated = updated
        if id is not None:
            self.id = id
        self.account_id = account_id
        if card_details_id is not None:
            self.card_details_id = card_details_id
        self.organization_id = organization_id
        self.customer_id = customer_id
        self.credit_card_id = credit_card_id
        if device_data is not None:
            self.device_data = device_data
        if merchant_account_id is not None:
            self.merchant_account_id = merchant_account_id
        self.deleted = deleted

    @property
    def created(self):
        """Gets the created of this BraintreeToken.  # noqa: E501


        :return: The created of this BraintreeToken.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this BraintreeToken.


        :param created: The created of this BraintreeToken.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """Gets the changed_by of this BraintreeToken.  # noqa: E501


        :return: The changed_by of this BraintreeToken.  # noqa: E501
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """Sets the changed_by of this BraintreeToken.


        :param changed_by: The changed_by of this BraintreeToken.  # noqa: E501
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """Gets the updated of this BraintreeToken.  # noqa: E501


        :return: The updated of this BraintreeToken.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this BraintreeToken.


        :param updated: The updated of this BraintreeToken.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """Gets the id of this BraintreeToken.  # noqa: E501


        :return: The id of this BraintreeToken.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BraintreeToken.


        :param id: The id of this BraintreeToken.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this BraintreeToken.  # noqa: E501


        :return: The account_id of this BraintreeToken.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this BraintreeToken.


        :param account_id: The account_id of this BraintreeToken.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def card_details_id(self):
        """Gets the card_details_id of this BraintreeToken.  # noqa: E501


        :return: The card_details_id of this BraintreeToken.  # noqa: E501
        :rtype: str
        """
        return self._card_details_id

    @card_details_id.setter
    def card_details_id(self, card_details_id):
        """Sets the card_details_id of this BraintreeToken.


        :param card_details_id: The card_details_id of this BraintreeToken.  # noqa: E501
        :type: str
        """

        self._card_details_id = card_details_id

    @property
    def organization_id(self):
        """Gets the organization_id of this BraintreeToken.  # noqa: E501


        :return: The organization_id of this BraintreeToken.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this BraintreeToken.


        :param organization_id: The organization_id of this BraintreeToken.  # noqa: E501
        :type: str
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def customer_id(self):
        """Gets the customer_id of this BraintreeToken.  # noqa: E501


        :return: The customer_id of this BraintreeToken.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this BraintreeToken.


        :param customer_id: The customer_id of this BraintreeToken.  # noqa: E501
        :type: str
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def credit_card_id(self):
        """Gets the credit_card_id of this BraintreeToken.  # noqa: E501


        :return: The credit_card_id of this BraintreeToken.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_id

    @credit_card_id.setter
    def credit_card_id(self, credit_card_id):
        """Sets the credit_card_id of this BraintreeToken.


        :param credit_card_id: The credit_card_id of this BraintreeToken.  # noqa: E501
        :type: str
        """
        if credit_card_id is None:
            raise ValueError("Invalid value for `credit_card_id`, must not be `None`")  # noqa: E501

        self._credit_card_id = credit_card_id

    @property
    def device_data(self):
        """Gets the device_data of this BraintreeToken.  # noqa: E501


        :return: The device_data of this BraintreeToken.  # noqa: E501
        :rtype: str
        """
        return self._device_data

    @device_data.setter
    def device_data(self, device_data):
        """Sets the device_data of this BraintreeToken.


        :param device_data: The device_data of this BraintreeToken.  # noqa: E501
        :type: str
        """

        self._device_data = device_data

    @property
    def merchant_account_id(self):
        """Gets the merchant_account_id of this BraintreeToken.  # noqa: E501


        :return: The merchant_account_id of this BraintreeToken.  # noqa: E501
        :rtype: str
        """
        return self._merchant_account_id

    @merchant_account_id.setter
    def merchant_account_id(self, merchant_account_id):
        """Sets the merchant_account_id of this BraintreeToken.


        :param merchant_account_id: The merchant_account_id of this BraintreeToken.  # noqa: E501
        :type: str
        """

        self._merchant_account_id = merchant_account_id

    @property
    def deleted(self):
        """Gets the deleted of this BraintreeToken.  # noqa: E501


        :return: The deleted of this BraintreeToken.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this BraintreeToken.


        :param deleted: The deleted of this BraintreeToken.  # noqa: E501
        :type: bool
        """
        if deleted is None:
            raise ValueError("Invalid value for `deleted`, must not be `None`")  # noqa: E501

        self._deleted = deleted

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
        if issubclass(BraintreeToken, dict):
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
        if not isinstance(other, BraintreeToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other