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

class PaymentMethod(object):
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
        'crm_id': 'str',
        'account_id': 'str',
        'organization_id': 'str',
        'name': 'str',
        'description': 'str',
        'card_holder_name': 'str',
        'expiry_date': 'str',
        'card_type': 'str',
        'country': 'str',
        'province': 'str',
        'first_six': 'str',
        'last_four': 'str',
        'expiry_year': 'int',
        'expiry_month': 'int',
        'link_id': 'str',
        'gateway': 'str',
        'api_configuration_id': 'str',
        'ip_address': 'str',
        'ip_address_country': 'str',
        'tokenization_method': 'str',
        'state': 'str',
        'gateway_refreshed': 'datetime',
        'deleted': 'bool',
        'default_payment_method': 'bool'
    }

    attribute_map = {
        'created': 'created',
        'changed_by': 'changedBy',
        'updated': 'updated',
        'id': 'id',
        'crm_id': 'crmID',
        'account_id': 'accountID',
        'organization_id': 'organizationID',
        'name': 'name',
        'description': 'description',
        'card_holder_name': 'cardHolderName',
        'expiry_date': 'expiryDate',
        'card_type': 'cardType',
        'country': 'country',
        'province': 'province',
        'first_six': 'firstSix',
        'last_four': 'lastFour',
        'expiry_year': 'expiryYear',
        'expiry_month': 'expiryMonth',
        'link_id': 'linkID',
        'gateway': 'gateway',
        'api_configuration_id': 'apiConfigurationID',
        'ip_address': 'ipAddress',
        'ip_address_country': 'ipAddressCountry',
        'tokenization_method': 'tokenizationMethod',
        'state': 'state',
        'gateway_refreshed': 'gatewayRefreshed',
        'deleted': 'deleted',
        'default_payment_method': 'defaultPaymentMethod'
    }

    def __init__(self, created=None, changed_by=None, updated=None, id=None, crm_id=None, account_id=None, organization_id=None, name=None, description=None, card_holder_name=None, expiry_date=None, card_type=None, country=None, province=None, first_six=None, last_four=None, expiry_year=None, expiry_month=None, link_id=None, gateway=None, api_configuration_id=None, ip_address=None, ip_address_country=None, tokenization_method=None, state=None, gateway_refreshed=None, deleted=None, default_payment_method=None):  # noqa: E501
        """PaymentMethod - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._changed_by = None
        self._updated = None
        self._id = None
        self._crm_id = None
        self._account_id = None
        self._organization_id = None
        self._name = None
        self._description = None
        self._card_holder_name = None
        self._expiry_date = None
        self._card_type = None
        self._country = None
        self._province = None
        self._first_six = None
        self._last_four = None
        self._expiry_year = None
        self._expiry_month = None
        self._link_id = None
        self._gateway = None
        self._api_configuration_id = None
        self._ip_address = None
        self._ip_address_country = None
        self._tokenization_method = None
        self._state = None
        self._gateway_refreshed = None
        self._deleted = None
        self._default_payment_method = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if changed_by is not None:
            self.changed_by = changed_by
        if updated is not None:
            self.updated = updated
        if id is not None:
            self.id = id
        if crm_id is not None:
            self.crm_id = crm_id
        if account_id is not None:
            self.account_id = account_id
        if organization_id is not None:
            self.organization_id = organization_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if card_holder_name is not None:
            self.card_holder_name = card_holder_name
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if card_type is not None:
            self.card_type = card_type
        if country is not None:
            self.country = country
        if province is not None:
            self.province = province
        if first_six is not None:
            self.first_six = first_six
        if last_four is not None:
            self.last_four = last_four
        if expiry_year is not None:
            self.expiry_year = expiry_year
        if expiry_month is not None:
            self.expiry_month = expiry_month
        if link_id is not None:
            self.link_id = link_id
        if gateway is not None:
            self.gateway = gateway
        if api_configuration_id is not None:
            self.api_configuration_id = api_configuration_id
        if ip_address is not None:
            self.ip_address = ip_address
        if ip_address_country is not None:
            self.ip_address_country = ip_address_country
        if tokenization_method is not None:
            self.tokenization_method = tokenization_method
        if state is not None:
            self.state = state
        if gateway_refreshed is not None:
            self.gateway_refreshed = gateway_refreshed
        if deleted is not None:
            self.deleted = deleted
        if default_payment_method is not None:
            self.default_payment_method = default_payment_method

    @property
    def created(self):
        """Gets the created of this PaymentMethod.  # noqa: E501


        :return: The created of this PaymentMethod.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PaymentMethod.


        :param created: The created of this PaymentMethod.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """Gets the changed_by of this PaymentMethod.  # noqa: E501


        :return: The changed_by of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """Sets the changed_by of this PaymentMethod.


        :param changed_by: The changed_by of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """Gets the updated of this PaymentMethod.  # noqa: E501


        :return: The updated of this PaymentMethod.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this PaymentMethod.


        :param updated: The updated of this PaymentMethod.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """Gets the id of this PaymentMethod.  # noqa: E501


        :return: The id of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentMethod.


        :param id: The id of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def crm_id(self):
        """Gets the crm_id of this PaymentMethod.  # noqa: E501


        :return: The crm_id of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._crm_id

    @crm_id.setter
    def crm_id(self, crm_id):
        """Sets the crm_id of this PaymentMethod.


        :param crm_id: The crm_id of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._crm_id = crm_id

    @property
    def account_id(self):
        """Gets the account_id of this PaymentMethod.  # noqa: E501


        :return: The account_id of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PaymentMethod.


        :param account_id: The account_id of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def organization_id(self):
        """Gets the organization_id of this PaymentMethod.  # noqa: E501


        :return: The organization_id of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this PaymentMethod.


        :param organization_id: The organization_id of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def name(self):
        """Gets the name of this PaymentMethod.  # noqa: E501


        :return: The name of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentMethod.


        :param name: The name of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this PaymentMethod.  # noqa: E501


        :return: The description of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PaymentMethod.


        :param description: The description of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def card_holder_name(self):
        """Gets the card_holder_name of this PaymentMethod.  # noqa: E501


        :return: The card_holder_name of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._card_holder_name

    @card_holder_name.setter
    def card_holder_name(self, card_holder_name):
        """Sets the card_holder_name of this PaymentMethod.


        :param card_holder_name: The card_holder_name of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._card_holder_name = card_holder_name

    @property
    def expiry_date(self):
        """Gets the expiry_date of this PaymentMethod.  # noqa: E501


        :return: The expiry_date of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this PaymentMethod.


        :param expiry_date: The expiry_date of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._expiry_date = expiry_date

    @property
    def card_type(self):
        """Gets the card_type of this PaymentMethod.  # noqa: E501


        :return: The card_type of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this PaymentMethod.


        :param card_type: The card_type of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._card_type = card_type

    @property
    def country(self):
        """Gets the country of this PaymentMethod.  # noqa: E501


        :return: The country of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PaymentMethod.


        :param country: The country of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def province(self):
        """Gets the province of this PaymentMethod.  # noqa: E501


        :return: The province of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this PaymentMethod.


        :param province: The province of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._province = province

    @property
    def first_six(self):
        """Gets the first_six of this PaymentMethod.  # noqa: E501


        :return: The first_six of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._first_six

    @first_six.setter
    def first_six(self, first_six):
        """Sets the first_six of this PaymentMethod.


        :param first_six: The first_six of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._first_six = first_six

    @property
    def last_four(self):
        """Gets the last_four of this PaymentMethod.  # noqa: E501


        :return: The last_four of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._last_four

    @last_four.setter
    def last_four(self, last_four):
        """Sets the last_four of this PaymentMethod.


        :param last_four: The last_four of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._last_four = last_four

    @property
    def expiry_year(self):
        """Gets the expiry_year of this PaymentMethod.  # noqa: E501


        :return: The expiry_year of this PaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._expiry_year

    @expiry_year.setter
    def expiry_year(self, expiry_year):
        """Sets the expiry_year of this PaymentMethod.


        :param expiry_year: The expiry_year of this PaymentMethod.  # noqa: E501
        :type: int
        """

        self._expiry_year = expiry_year

    @property
    def expiry_month(self):
        """Gets the expiry_month of this PaymentMethod.  # noqa: E501


        :return: The expiry_month of this PaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._expiry_month

    @expiry_month.setter
    def expiry_month(self, expiry_month):
        """Sets the expiry_month of this PaymentMethod.


        :param expiry_month: The expiry_month of this PaymentMethod.  # noqa: E501
        :type: int
        """

        self._expiry_month = expiry_month

    @property
    def link_id(self):
        """Gets the link_id of this PaymentMethod.  # noqa: E501


        :return: The link_id of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._link_id

    @link_id.setter
    def link_id(self, link_id):
        """Sets the link_id of this PaymentMethod.


        :param link_id: The link_id of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._link_id = link_id

    @property
    def gateway(self):
        """Gets the gateway of this PaymentMethod.  # noqa: E501


        :return: The gateway of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this PaymentMethod.


        :param gateway: The gateway of this PaymentMethod.  # noqa: E501
        :type: str
        """
        allowed_values = ["VOID", "cybersource_token", "card_vault", "paypal_simple", "locustworld", "free", "coupon", "credit_note", "stripe", "braintree", "zooz", "balanced", "paypal", "billforward_test", "offline", "trial", "stripeACH", "goCardless", "authorizeNet", "spreedly", "sagePay", "trustCommerce", "payvision", "kash", "epx", "shuttle", "square", "billforwardRandomizer", "cardConnect", "ebanx"]  # noqa: E501
        if gateway not in allowed_values:
            raise ValueError(
                "Invalid value for `gateway` ({0}), must be one of {1}"  # noqa: E501
                .format(gateway, allowed_values)
            )

        self._gateway = gateway

    @property
    def api_configuration_id(self):
        """Gets the api_configuration_id of this PaymentMethod.  # noqa: E501


        :return: The api_configuration_id of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._api_configuration_id

    @api_configuration_id.setter
    def api_configuration_id(self, api_configuration_id):
        """Sets the api_configuration_id of this PaymentMethod.


        :param api_configuration_id: The api_configuration_id of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._api_configuration_id = api_configuration_id

    @property
    def ip_address(self):
        """Gets the ip_address of this PaymentMethod.  # noqa: E501


        :return: The ip_address of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this PaymentMethod.


        :param ip_address: The ip_address of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def ip_address_country(self):
        """Gets the ip_address_country of this PaymentMethod.  # noqa: E501


        :return: The ip_address_country of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._ip_address_country

    @ip_address_country.setter
    def ip_address_country(self, ip_address_country):
        """Sets the ip_address_country of this PaymentMethod.


        :param ip_address_country: The ip_address_country of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._ip_address_country = ip_address_country

    @property
    def tokenization_method(self):
        """Gets the tokenization_method of this PaymentMethod.  # noqa: E501


        :return: The tokenization_method of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._tokenization_method

    @tokenization_method.setter
    def tokenization_method(self, tokenization_method):
        """Sets the tokenization_method of this PaymentMethod.


        :param tokenization_method: The tokenization_method of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._tokenization_method = tokenization_method

    @property
    def state(self):
        """Gets the state of this PaymentMethod.  # noqa: E501


        :return: The state of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentMethod.


        :param state: The state of this PaymentMethod.  # noqa: E501
        :type: str
        """
        allowed_values = ["Pending", "Active", "Expiring", "Expired"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def gateway_refreshed(self):
        """Gets the gateway_refreshed of this PaymentMethod.  # noqa: E501


        :return: The gateway_refreshed of this PaymentMethod.  # noqa: E501
        :rtype: datetime
        """
        return self._gateway_refreshed

    @gateway_refreshed.setter
    def gateway_refreshed(self, gateway_refreshed):
        """Sets the gateway_refreshed of this PaymentMethod.


        :param gateway_refreshed: The gateway_refreshed of this PaymentMethod.  # noqa: E501
        :type: datetime
        """

        self._gateway_refreshed = gateway_refreshed

    @property
    def deleted(self):
        """Gets the deleted of this PaymentMethod.  # noqa: E501


        :return: The deleted of this PaymentMethod.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this PaymentMethod.


        :param deleted: The deleted of this PaymentMethod.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def default_payment_method(self):
        """Gets the default_payment_method of this PaymentMethod.  # noqa: E501


        :return: The default_payment_method of this PaymentMethod.  # noqa: E501
        :rtype: bool
        """
        return self._default_payment_method

    @default_payment_method.setter
    def default_payment_method(self, default_payment_method):
        """Sets the default_payment_method of this PaymentMethod.


        :param default_payment_method: The default_payment_method of this PaymentMethod.  # noqa: E501
        :type: bool
        """

        self._default_payment_method = default_payment_method

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
        if issubclass(PaymentMethod, dict):
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
        if not isinstance(other, PaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
