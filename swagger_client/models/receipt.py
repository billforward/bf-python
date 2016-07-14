# coding: utf-8

"""
    BillForward REST API


    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Receipt(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, refund_id=None, created=None, changed_by=None, id=None, crm_id=None, invoice_id=None, gateway_reference_id=None, account_id=None, payment_id=None, payment_method_id=None, organization_id=None, cardholder_name=None, card_last_four=None, card_description=None, card_country=None, card_province=None, card_type=None, ip_address=None, ip_address_country=None, type=None, currency=None, value=None, payment_gateway=None, invoice_type=None, execution_attempt=None, decision=None, reason_code=None, raw_reason_code=None, raw_data=None):
        """
        Receipt - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'refund_id': 'str',
            'created': 'datetime',
            'changed_by': 'str',
            'id': 'str',
            'crm_id': 'str',
            'invoice_id': 'str',
            'gateway_reference_id': 'str',
            'account_id': 'str',
            'payment_id': 'str',
            'payment_method_id': 'str',
            'organization_id': 'str',
            'cardholder_name': 'str',
            'card_last_four': 'str',
            'card_description': 'str',
            'card_country': 'str',
            'card_province': 'str',
            'card_type': 'str',
            'ip_address': 'str',
            'ip_address_country': 'str',
            'type': 'str',
            'currency': 'str',
            'value': 'float',
            'payment_gateway': 'str',
            'invoice_type': 'str',
            'execution_attempt': 'int',
            'decision': 'str',
            'reason_code': 'int',
            'raw_reason_code': 'str',
            'raw_data': 'list[str]'
        }

        self.attribute_map = {
            'refund_id': 'refundID',
            'created': 'created',
            'changed_by': 'changedBy',
            'id': 'id',
            'crm_id': 'crmID',
            'invoice_id': 'invoiceID',
            'gateway_reference_id': 'gatewayReferenceID',
            'account_id': 'accountID',
            'payment_id': 'paymentID',
            'payment_method_id': 'paymentMethodID',
            'organization_id': 'organizationID',
            'cardholder_name': 'cardholderName',
            'card_last_four': 'cardLastFour',
            'card_description': 'cardDescription',
            'card_country': 'cardCountry',
            'card_province': 'cardProvince',
            'card_type': 'cardType',
            'ip_address': 'ipAddress',
            'ip_address_country': 'ipAddressCountry',
            'type': 'type',
            'currency': 'currency',
            'value': 'value',
            'payment_gateway': 'paymentGateway',
            'invoice_type': 'invoiceType',
            'execution_attempt': 'executionAttempt',
            'decision': 'decision',
            'reason_code': 'reasonCode',
            'raw_reason_code': 'rawReasonCode',
            'raw_data': 'rawData'
        }

        self._refund_id = refund_id
        self._created = created
        self._changed_by = changed_by
        self._id = id
        self._crm_id = crm_id
        self._invoice_id = invoice_id
        self._gateway_reference_id = gateway_reference_id
        self._account_id = account_id
        self._payment_id = payment_id
        self._payment_method_id = payment_method_id
        self._organization_id = organization_id
        self._cardholder_name = cardholder_name
        self._card_last_four = card_last_four
        self._card_description = card_description
        self._card_country = card_country
        self._card_province = card_province
        self._card_type = card_type
        self._ip_address = ip_address
        self._ip_address_country = ip_address_country
        self._type = type
        self._currency = currency
        self._value = value
        self._payment_gateway = payment_gateway
        self._invoice_type = invoice_type
        self._execution_attempt = execution_attempt
        self._decision = decision
        self._reason_code = reason_code
        self._raw_reason_code = raw_reason_code
        self._raw_data = raw_data

    @property
    def refund_id(self):
        """
        Gets the refund_id of this Receipt.


        :return: The refund_id of this Receipt.
        :rtype: str
        """
        return self._refund_id

    @refund_id.setter
    def refund_id(self, refund_id):
        """
        Sets the refund_id of this Receipt.


        :param refund_id: The refund_id of this Receipt.
        :type: str
        """

        self._refund_id = refund_id

    @property
    def created(self):
        """
        Gets the created of this Receipt.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this Receipt.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Receipt.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this Receipt.
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """
        Gets the changed_by of this Receipt.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :return: The changed_by of this Receipt.
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """
        Sets the changed_by of this Receipt.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :param changed_by: The changed_by of this Receipt.
        :type: str
        """

        self._changed_by = changed_by

    @property
    def id(self):
        """
        Gets the id of this Receipt.


        :return: The id of this Receipt.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Receipt.


        :param id: The id of this Receipt.
        :type: str
        """

        self._id = id

    @property
    def crm_id(self):
        """
        Gets the crm_id of this Receipt.
        { \"description\" : \"CRM ID of the subscription.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The crm_id of this Receipt.
        :rtype: str
        """
        return self._crm_id

    @crm_id.setter
    def crm_id(self, crm_id):
        """
        Sets the crm_id of this Receipt.
        { \"description\" : \"CRM ID of the subscription.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param crm_id: The crm_id of this Receipt.
        :type: str
        """

        self._crm_id = crm_id

    @property
    def invoice_id(self):
        """
        Gets the invoice_id of this Receipt.


        :return: The invoice_id of this Receipt.
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this Receipt.


        :param invoice_id: The invoice_id of this Receipt.
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def gateway_reference_id(self):
        """
        Gets the gateway_reference_id of this Receipt.


        :return: The gateway_reference_id of this Receipt.
        :rtype: str
        """
        return self._gateway_reference_id

    @gateway_reference_id.setter
    def gateway_reference_id(self, gateway_reference_id):
        """
        Sets the gateway_reference_id of this Receipt.


        :param gateway_reference_id: The gateway_reference_id of this Receipt.
        :type: str
        """

        self._gateway_reference_id = gateway_reference_id

    @property
    def account_id(self):
        """
        Gets the account_id of this Receipt.


        :return: The account_id of this Receipt.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this Receipt.


        :param account_id: The account_id of this Receipt.
        :type: str
        """

        self._account_id = account_id

    @property
    def payment_id(self):
        """
        Gets the payment_id of this Receipt.


        :return: The payment_id of this Receipt.
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """
        Sets the payment_id of this Receipt.


        :param payment_id: The payment_id of this Receipt.
        :type: str
        """

        self._payment_id = payment_id

    @property
    def payment_method_id(self):
        """
        Gets the payment_method_id of this Receipt.


        :return: The payment_method_id of this Receipt.
        :rtype: str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """
        Sets the payment_method_id of this Receipt.


        :param payment_method_id: The payment_method_id of this Receipt.
        :type: str
        """

        self._payment_method_id = payment_method_id

    @property
    def organization_id(self):
        """
        Gets the organization_id of this Receipt.


        :return: The organization_id of this Receipt.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this Receipt.


        :param organization_id: The organization_id of this Receipt.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def cardholder_name(self):
        """
        Gets the cardholder_name of this Receipt.


        :return: The cardholder_name of this Receipt.
        :rtype: str
        """
        return self._cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, cardholder_name):
        """
        Sets the cardholder_name of this Receipt.


        :param cardholder_name: The cardholder_name of this Receipt.
        :type: str
        """

        self._cardholder_name = cardholder_name

    @property
    def card_last_four(self):
        """
        Gets the card_last_four of this Receipt.


        :return: The card_last_four of this Receipt.
        :rtype: str
        """
        return self._card_last_four

    @card_last_four.setter
    def card_last_four(self, card_last_four):
        """
        Sets the card_last_four of this Receipt.


        :param card_last_four: The card_last_four of this Receipt.
        :type: str
        """

        self._card_last_four = card_last_four

    @property
    def card_description(self):
        """
        Gets the card_description of this Receipt.


        :return: The card_description of this Receipt.
        :rtype: str
        """
        return self._card_description

    @card_description.setter
    def card_description(self, card_description):
        """
        Sets the card_description of this Receipt.


        :param card_description: The card_description of this Receipt.
        :type: str
        """

        self._card_description = card_description

    @property
    def card_country(self):
        """
        Gets the card_country of this Receipt.


        :return: The card_country of this Receipt.
        :rtype: str
        """
        return self._card_country

    @card_country.setter
    def card_country(self, card_country):
        """
        Sets the card_country of this Receipt.


        :param card_country: The card_country of this Receipt.
        :type: str
        """

        self._card_country = card_country

    @property
    def card_province(self):
        """
        Gets the card_province of this Receipt.


        :return: The card_province of this Receipt.
        :rtype: str
        """
        return self._card_province

    @card_province.setter
    def card_province(self, card_province):
        """
        Sets the card_province of this Receipt.


        :param card_province: The card_province of this Receipt.
        :type: str
        """

        self._card_province = card_province

    @property
    def card_type(self):
        """
        Gets the card_type of this Receipt.


        :return: The card_type of this Receipt.
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """
        Sets the card_type of this Receipt.


        :param card_type: The card_type of this Receipt.
        :type: str
        """

        self._card_type = card_type

    @property
    def ip_address(self):
        """
        Gets the ip_address of this Receipt.
        {\"description\":\"IP address associated with this payment method.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :return: The ip_address of this Receipt.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Receipt.
        {\"description\":\"IP address associated with this payment method.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :param ip_address: The ip_address of this Receipt.
        :type: str
        """

        self._ip_address = ip_address

    @property
    def ip_address_country(self):
        """
        Gets the ip_address_country of this Receipt.
        {\"description\":\"Country of the IP address associated with this payment method.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :return: The ip_address_country of this Receipt.
        :rtype: str
        """
        return self._ip_address_country

    @ip_address_country.setter
    def ip_address_country(self, ip_address_country):
        """
        Sets the ip_address_country of this Receipt.
        {\"description\":\"Country of the IP address associated with this payment method.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :param ip_address_country: The ip_address_country of this Receipt.
        :type: str
        """

        self._ip_address_country = ip_address_country

    @property
    def type(self):
        """
        Gets the type of this Receipt.
        { \"description\" : \"Type of transaction.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The type of this Receipt.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Receipt.
        { \"description\" : \"Type of transaction.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param type: The type of this Receipt.
        :type: str
        """
        allowed_values = ["credit", "debit"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def currency(self):
        """
        Gets the currency of this Receipt.
        { \"description\" : \"Currency of the invoice specified by a three character ISO 4217 currency code.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The currency of this Receipt.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Receipt.
        { \"description\" : \"Currency of the invoice specified by a three character ISO 4217 currency code.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param currency: The currency of this Receipt.
        :type: str
        """

        self._currency = currency

    @property
    def value(self):
        """
        Gets the value of this Receipt.


        :return: The value of this Receipt.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Receipt.


        :param value: The value of this Receipt.
        :type: float
        """

        self._value = value

    @property
    def payment_gateway(self):
        """
        Gets the payment_gateway of this Receipt.


        :return: The payment_gateway of this Receipt.
        :rtype: str
        """
        return self._payment_gateway

    @payment_gateway.setter
    def payment_gateway(self, payment_gateway):
        """
        Sets the payment_gateway of this Receipt.


        :param payment_gateway: The payment_gateway of this Receipt.
        :type: str
        """
        allowed_values = ["cybersource_token", "card_vault", "paypal_simple", "locustworld", "free", "coupon", "credit_note", "stripe", "braintree", "balanced", "paypal", "billforward_test", "offline", "trial", "stripeACH", "authorizeNet", "spreedly", "sagePay", "trustCommerce", "payvision", "kash"]
        if payment_gateway not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_gateway` ({0}), must be one of {1}"
                .format(payment_gateway, allowed_values)
            )

        self._payment_gateway = payment_gateway

    @property
    def invoice_type(self):
        """
        Gets the invoice_type of this Receipt.
        { \"description\" : \"The type of the invoice. A subscription invoice is raised every time a subscription recurs. An amendment is created for intra-contract changes. An Adhoc invoice is created for payment that is taken out-of-band of a subscription. Finally the invoice generated for a trial period is marked as Trial.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The invoice_type of this Receipt.
        :rtype: str
        """
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, invoice_type):
        """
        Sets the invoice_type of this Receipt.
        { \"description\" : \"The type of the invoice. A subscription invoice is raised every time a subscription recurs. An amendment is created for intra-contract changes. An Adhoc invoice is created for payment that is taken out-of-band of a subscription. Finally the invoice generated for a trial period is marked as Trial.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param invoice_type: The invoice_type of this Receipt.
        :type: str
        """
        allowed_values = ["Subscription", "Trial", "Charge", "FinalArrears", "Amendment", "Aggregated"]
        if invoice_type not in allowed_values:
            raise ValueError(
                "Invalid value for `invoice_type` ({0}), must be one of {1}"
                .format(invoice_type, allowed_values)
            )

        self._invoice_type = invoice_type

    @property
    def execution_attempt(self):
        """
        Gets the execution_attempt of this Receipt.


        :return: The execution_attempt of this Receipt.
        :rtype: int
        """
        return self._execution_attempt

    @execution_attempt.setter
    def execution_attempt(self, execution_attempt):
        """
        Sets the execution_attempt of this Receipt.


        :param execution_attempt: The execution_attempt of this Receipt.
        :type: int
        """

        self._execution_attempt = execution_attempt

    @property
    def decision(self):
        """
        Gets the decision of this Receipt.


        :return: The decision of this Receipt.
        :rtype: str
        """
        return self._decision

    @decision.setter
    def decision(self, decision):
        """
        Sets the decision of this Receipt.


        :param decision: The decision of this Receipt.
        :type: str
        """
        allowed_values = ["Accept", "Reject", "Error"]
        if decision not in allowed_values:
            raise ValueError(
                "Invalid value for `decision` ({0}), must be one of {1}"
                .format(decision, allowed_values)
            )

        self._decision = decision

    @property
    def reason_code(self):
        """
        Gets the reason_code of this Receipt.


        :return: The reason_code of this Receipt.
        :rtype: int
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """
        Sets the reason_code of this Receipt.


        :param reason_code: The reason_code of this Receipt.
        :type: int
        """

        self._reason_code = reason_code

    @property
    def raw_reason_code(self):
        """
        Gets the raw_reason_code of this Receipt.


        :return: The raw_reason_code of this Receipt.
        :rtype: str
        """
        return self._raw_reason_code

    @raw_reason_code.setter
    def raw_reason_code(self, raw_reason_code):
        """
        Sets the raw_reason_code of this Receipt.


        :param raw_reason_code: The raw_reason_code of this Receipt.
        :type: str
        """

        self._raw_reason_code = raw_reason_code

    @property
    def raw_data(self):
        """
        Gets the raw_data of this Receipt.


        :return: The raw_data of this Receipt.
        :rtype: list[str]
        """
        return self._raw_data

    @raw_data.setter
    def raw_data(self, raw_data):
        """
        Sets the raw_data of this Receipt.


        :param raw_data: The raw_data of this Receipt.
        :type: list[str]
        """

        self._raw_data = raw_data

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
