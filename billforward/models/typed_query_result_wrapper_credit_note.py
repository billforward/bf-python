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

class TypedQueryResultWrapperCreditNote(object):
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
        'entity_name': 'str',
        'total_records_returned': 'int',
        'total_records': 'int',
        'results': 'list[BillingEntityBase]',
        'arguments': 'list[str]',
        'organizations': 'list[str]',
        'types': 'list[str]',
        'offset': 'int',
        'records': 'int',
        'order_by': 'str',
        'order_direction': 'str',
        'include_retired': 'bool',
        'wildcard': 'bool',
        'entity': 'bool',
        'typed_single_result': 'CreditNote',
        'typed_results': 'list[CreditNote]',
        'single_result': 'BillingEntityBase'
    }

    attribute_map = {
        'entity_name': 'entityName',
        'total_records_returned': 'totalRecordsReturned',
        'total_records': 'totalRecords',
        'results': 'results',
        'arguments': 'arguments',
        'organizations': 'organizations',
        'types': 'types',
        'offset': 'offset',
        'records': 'records',
        'order_by': 'orderBy',
        'order_direction': 'orderDirection',
        'include_retired': 'includeRetired',
        'wildcard': 'wildcard',
        'entity': 'entity',
        'typed_single_result': 'typedSingleResult',
        'typed_results': 'typedResults',
        'single_result': 'singleResult'
    }

    def __init__(self, entity_name=None, total_records_returned=None, total_records=None, results=None, arguments=None, organizations=None, types=None, offset=None, records=None, order_by=None, order_direction=None, include_retired=None, wildcard=None, entity=None, typed_single_result=None, typed_results=None, single_result=None):  # noqa: E501
        """TypedQueryResultWrapperCreditNote - a model defined in Swagger"""  # noqa: E501
        self._entity_name = None
        self._total_records_returned = None
        self._total_records = None
        self._results = None
        self._arguments = None
        self._organizations = None
        self._types = None
        self._offset = None
        self._records = None
        self._order_by = None
        self._order_direction = None
        self._include_retired = None
        self._wildcard = None
        self._entity = None
        self._typed_single_result = None
        self._typed_results = None
        self._single_result = None
        self.discriminator = None
        if entity_name is not None:
            self.entity_name = entity_name
        if total_records_returned is not None:
            self.total_records_returned = total_records_returned
        if total_records is not None:
            self.total_records = total_records
        if results is not None:
            self.results = results
        if arguments is not None:
            self.arguments = arguments
        if organizations is not None:
            self.organizations = organizations
        if types is not None:
            self.types = types
        if offset is not None:
            self.offset = offset
        if records is not None:
            self.records = records
        if order_by is not None:
            self.order_by = order_by
        if order_direction is not None:
            self.order_direction = order_direction
        if include_retired is not None:
            self.include_retired = include_retired
        if wildcard is not None:
            self.wildcard = wildcard
        if entity is not None:
            self.entity = entity
        if typed_single_result is not None:
            self.typed_single_result = typed_single_result
        if typed_results is not None:
            self.typed_results = typed_results
        if single_result is not None:
            self.single_result = single_result

    @property
    def entity_name(self):
        """Gets the entity_name of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The entity_name of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """Sets the entity_name of this TypedQueryResultWrapperCreditNote.


        :param entity_name: The entity_name of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: str
        """
        allowed_values = ["AvataxConfiguration", "Notification", "Organization", "Product", "User", "Subscription", "Profile", "ProductRatePlan", "Client", "Invoice", "PricingComponentValue", "Account", "PricingComponentValueChange", "PricingComponentTier", "PricingComponent", "PricingCalculation", "CouponDefinition", "CouponInstance", "CouponModifier", "CouponRule", "CouponBookDefinition", "CouponBook", "InvoiceLine", "Webhook", "SubscriptionCancellation", "NotificationSnapshot", "InvoicePayment", "InvoiceLinePayment", "Payment", "PaymentMethod", "BankAccount", "PaymentMethodSubscriptionLink", "DunningLine", "CybersourceToken", "Card", "Alias", "CouponInstanceExistingValue", "TaxLine", "TaxationStrategy", "TaxationLink", "Address", "AmendmentPriceNTime", "Authority", "UnitOfMeasure", "Amendment", "AuditLog", "Password", "Username", "FixedTermDefinition", "FixedTerm", "Refund", "CreditNote", "Receipt", "AmendmentCompoundConstituent", "APIConfiguration", "StripeToken", "BraintreeToken", "PaypalToken", "AuthorizeNetToken", "SpreedlyToken", "AmendmentDiscardAmendment", "CancellationAmendment", "CompoundAmendment", "CompoundAmendmentConstituent", "FixedTermExpiryAmendment", "InvoiceNextExecutionAttemptAmendment", "PricingComponentValueAmendment", "BraintreeMerchantAccount", "WebhookSubscription", "Migration", "SubscriptionCharge", "StripeACHToken", "OfflinePayment", "CreditNotePayment", "CardVaultPayment", "BraintreePayment", "CybersourcePayment", "PaypalPayment", "StripeACHPayment", "AuthorizeNetPayment", "PricingComponentValueMigrationChargeAmendmentMapping", "ComponentChange", "QuoteRequest", "Quote", "CouponCharge", "CouponInstanceInvoiceLink", "Coupon", "CouponDiscount", "CouponUniqueCodesRequest", "CouponUniqueCodesResponse", "GetCouponsResponse", "AddCouponCodeRequest", "AddCouponCodeResponse", "RemoveCouponFromSubscriptionRequest", "TokenizationPreAuth", "StripeTokenizationPreAuth", "BraintreeTokenizationPreAuth", "SpreedlyTokenizationPreAuth", "SagePayTokenizationPreAuth", "PayVisionTokenizationPreAuth", "TokenizationPreAuthRequest", "AuthCaptureRequest", "StripeACHBankAccountVerification", "PasswordReset", "PricingRequest", "AmendmentPriceRequest", "AddTaxationStrategyRequest", "AddPaymentMethodRequest", "APIRequest", "SagePayToken", "SagePayNotificationRequest", "SagePayNotificationResponse", "SagePayOutstandingTransaction", "SagePayEnabledCardType", "TrustCommerceToken", "SagePayTransaction", "PricingComponentValueResponse", "MigrationResponse", "TimeResponse", "EntityTime", "Email", "MarketplaceConfiguration", "BFPermission", "Role", "PermissionLink", "PayVisionToken", "XeroConfiguration", "XeroMapping", "QuickBooksConfiguration", "QuickBooksWebhookEvent", "PayVisionTransaction", "KashToken", "EmailProvider", "DataSynchronizationJob", "DataSynchronizationJobError", "DataSynchronizationConfiguration", "DataSynchronizationAppConfiguration", "AggregationChildrenResponse", "MetadataKeyValue", "Metadata", "AggregatingComponent", "PricingComponentMigrationValue", "RegistrationResponse", "InvoiceRecalculationAmendment", "IssueInvoiceAmendment", "EmailSubscription", "SubscriptionCheckoutDefinition", "InvoiceCheckoutDefinition", "RevenueAttribution", "AddChargeToAccountResponse", "APIResponse", "PricingComponentUnitCredit", "CurrencyConfiguration", "SubscriptionNotificationConfiguration", "InvoiceTemplateConfig", "ChartMogulConfiguration", "BraintreeUpdateResult", "SubscriptionPricingComponentValueBatchUpdate", "InvoiceRender", "CouponWrapperResponse", "APIQuoteResponseQuantity", "APIQuote", "Contract", "HaltAggregationResponse", "ContractPeriod", "Affiliate", "AffiliateSubscriptionRelationship", "AffiliateRatePlanRelationship", "GoCardlessToken", "SetRatePlanAffiliateRequest", "CommissionStructure", "UserDefinableSalesforceObject", "EpxToken", "EpxPayment", "EpxApiConfiguration", "ZoozToken", "ZoozCustomer", "ZoozPayment", "EmailTokenization", "SubscriptionPlan", "SubscriptionGroup", "LoginAttempt", "InvoiceTemplateConfiguration", "OrganizationProfile", "PaymentMethodResponse", "ShuttleLink", "EmailNotification", "ShuttleHostedPayment", "EBANXPaymentMethod"]  # noqa: E501
        if entity_name not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_name` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_name, allowed_values)
            )

        self._entity_name = entity_name

    @property
    def total_records_returned(self):
        """Gets the total_records_returned of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The total_records_returned of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: int
        """
        return self._total_records_returned

    @total_records_returned.setter
    def total_records_returned(self, total_records_returned):
        """Sets the total_records_returned of this TypedQueryResultWrapperCreditNote.


        :param total_records_returned: The total_records_returned of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: int
        """

        self._total_records_returned = total_records_returned

    @property
    def total_records(self):
        """Gets the total_records of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The total_records of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this TypedQueryResultWrapperCreditNote.


        :param total_records: The total_records of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: int
        """

        self._total_records = total_records

    @property
    def results(self):
        """Gets the results of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The results of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: list[BillingEntityBase]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this TypedQueryResultWrapperCreditNote.


        :param results: The results of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: list[BillingEntityBase]
        """

        self._results = results

    @property
    def arguments(self):
        """Gets the arguments of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The arguments of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: list[str]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this TypedQueryResultWrapperCreditNote.


        :param arguments: The arguments of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: list[str]
        """

        self._arguments = arguments

    @property
    def organizations(self):
        """Gets the organizations of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The organizations of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: list[str]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this TypedQueryResultWrapperCreditNote.


        :param organizations: The organizations of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: list[str]
        """

        self._organizations = organizations

    @property
    def types(self):
        """Gets the types of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The types of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this TypedQueryResultWrapperCreditNote.


        :param types: The types of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: list[str]
        """

        self._types = types

    @property
    def offset(self):
        """Gets the offset of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The offset of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TypedQueryResultWrapperCreditNote.


        :param offset: The offset of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def records(self):
        """Gets the records of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The records of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: int
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this TypedQueryResultWrapperCreditNote.


        :param records: The records of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: int
        """

        self._records = records

    @property
    def order_by(self):
        """Gets the order_by of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The order_by of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this TypedQueryResultWrapperCreditNote.


        :param order_by: The order_by of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: str
        """

        self._order_by = order_by

    @property
    def order_direction(self):
        """Gets the order_direction of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The order_direction of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: str
        """
        return self._order_direction

    @order_direction.setter
    def order_direction(self, order_direction):
        """Sets the order_direction of this TypedQueryResultWrapperCreditNote.


        :param order_direction: The order_direction of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: str
        """
        allowed_values = ["ASC", "DESC"]  # noqa: E501
        if order_direction not in allowed_values:
            raise ValueError(
                "Invalid value for `order_direction` ({0}), must be one of {1}"  # noqa: E501
                .format(order_direction, allowed_values)
            )

        self._order_direction = order_direction

    @property
    def include_retired(self):
        """Gets the include_retired of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The include_retired of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: bool
        """
        return self._include_retired

    @include_retired.setter
    def include_retired(self, include_retired):
        """Sets the include_retired of this TypedQueryResultWrapperCreditNote.


        :param include_retired: The include_retired of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: bool
        """

        self._include_retired = include_retired

    @property
    def wildcard(self):
        """Gets the wildcard of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The wildcard of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: bool
        """
        return self._wildcard

    @wildcard.setter
    def wildcard(self, wildcard):
        """Sets the wildcard of this TypedQueryResultWrapperCreditNote.


        :param wildcard: The wildcard of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: bool
        """

        self._wildcard = wildcard

    @property
    def entity(self):
        """Gets the entity of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The entity of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: bool
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this TypedQueryResultWrapperCreditNote.


        :param entity: The entity of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: bool
        """

        self._entity = entity

    @property
    def typed_single_result(self):
        """Gets the typed_single_result of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The typed_single_result of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: CreditNote
        """
        return self._typed_single_result

    @typed_single_result.setter
    def typed_single_result(self, typed_single_result):
        """Sets the typed_single_result of this TypedQueryResultWrapperCreditNote.


        :param typed_single_result: The typed_single_result of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: CreditNote
        """

        self._typed_single_result = typed_single_result

    @property
    def typed_results(self):
        """Gets the typed_results of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The typed_results of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: list[CreditNote]
        """
        return self._typed_results

    @typed_results.setter
    def typed_results(self, typed_results):
        """Sets the typed_results of this TypedQueryResultWrapperCreditNote.


        :param typed_results: The typed_results of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: list[CreditNote]
        """

        self._typed_results = typed_results

    @property
    def single_result(self):
        """Gets the single_result of this TypedQueryResultWrapperCreditNote.  # noqa: E501


        :return: The single_result of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :rtype: BillingEntityBase
        """
        return self._single_result

    @single_result.setter
    def single_result(self, single_result):
        """Sets the single_result of this TypedQueryResultWrapperCreditNote.


        :param single_result: The single_result of this TypedQueryResultWrapperCreditNote.  # noqa: E501
        :type: BillingEntityBase
        """

        self._single_result = single_result

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
        if issubclass(TypedQueryResultWrapperCreditNote, dict):
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
        if not isinstance(other, TypedQueryResultWrapperCreditNote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
