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

class DataSyncJobErrorResponse(object):
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
        'id': 'str',
        'record_type': 'str',
        'record_id': 'str',
        'description': 'str',
        'raw_internal_error': 'str',
        'encountered': 'datetime',
        'run_number': 'int'
    }

    attribute_map = {
        'id': 'id',
        'record_type': 'recordType',
        'record_id': 'recordId',
        'description': 'description',
        'raw_internal_error': 'rawInternalError',
        'encountered': 'encountered',
        'run_number': 'runNumber'
    }

    def __init__(self, id=None, record_type=None, record_id=None, description=None, raw_internal_error=None, encountered=None, run_number=None):  # noqa: E501
        """DataSyncJobErrorResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._record_type = None
        self._record_id = None
        self._description = None
        self._raw_internal_error = None
        self._encountered = None
        self._run_number = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if record_type is not None:
            self.record_type = record_type
        if record_id is not None:
            self.record_id = record_id
        if description is not None:
            self.description = description
        if raw_internal_error is not None:
            self.raw_internal_error = raw_internal_error
        if encountered is not None:
            self.encountered = encountered
        if run_number is not None:
            self.run_number = run_number

    @property
    def id(self):
        """Gets the id of this DataSyncJobErrorResponse.  # noqa: E501


        :return: The id of this DataSyncJobErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataSyncJobErrorResponse.


        :param id: The id of this DataSyncJobErrorResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def record_type(self):
        """Gets the record_type of this DataSyncJobErrorResponse.  # noqa: E501


        :return: The record_type of this DataSyncJobErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this DataSyncJobErrorResponse.


        :param record_type: The record_type of this DataSyncJobErrorResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["AvataxConfiguration", "Notification", "Organization", "Product", "User", "Subscription", "Profile", "ProductRatePlan", "Client", "Invoice", "PricingComponentValue", "Account", "PricingComponentValueChange", "PricingComponentTier", "PricingComponent", "PricingCalculation", "CouponDefinition", "CouponInstance", "CouponModifier", "CouponRule", "CouponBookDefinition", "CouponBook", "InvoiceLine", "Webhook", "SubscriptionCancellation", "NotificationSnapshot", "InvoicePayment", "InvoiceLinePayment", "Payment", "PaymentMethod", "BankAccount", "PaymentMethodSubscriptionLink", "DunningLine", "CybersourceToken", "Card", "Alias", "CouponInstanceExistingValue", "TaxLine", "TaxationStrategy", "TaxationLink", "Address", "AmendmentPriceNTime", "Authority", "UnitOfMeasure", "Amendment", "AuditLog", "Password", "Username", "FixedTermDefinition", "FixedTerm", "Refund", "CreditNote", "Receipt", "AmendmentCompoundConstituent", "APIConfiguration", "StripeToken", "BraintreeToken", "PaypalToken", "AuthorizeNetToken", "SpreedlyToken", "AmendmentDiscardAmendment", "CancellationAmendment", "CompoundAmendment", "CompoundAmendmentConstituent", "FixedTermExpiryAmendment", "InvoiceNextExecutionAttemptAmendment", "PricingComponentValueAmendment", "BraintreeMerchantAccount", "WebhookSubscription", "Migration", "SubscriptionCharge", "StripeACHToken", "OfflinePayment", "CreditNotePayment", "CardVaultPayment", "BraintreePayment", "CybersourcePayment", "PaypalPayment", "StripeACHPayment", "AuthorizeNetPayment", "PricingComponentValueMigrationChargeAmendmentMapping", "ComponentChange", "QuoteRequest", "Quote", "CouponCharge", "CouponInstanceInvoiceLink", "Coupon", "CouponDiscount", "CouponUniqueCodesRequest", "CouponUniqueCodesResponse", "GetCouponsResponse", "AddCouponCodeRequest", "AddCouponCodeResponse", "RemoveCouponFromSubscriptionRequest", "TokenizationPreAuth", "StripeTokenizationPreAuth", "BraintreeTokenizationPreAuth", "SpreedlyTokenizationPreAuth", "SagePayTokenizationPreAuth", "PayVisionTokenizationPreAuth", "TokenizationPreAuthRequest", "AuthCaptureRequest", "StripeACHBankAccountVerification", "PasswordReset", "PricingRequest", "AmendmentPriceRequest", "AddTaxationStrategyRequest", "AddPaymentMethodRequest", "APIRequest", "SagePayToken", "SagePayNotificationRequest", "SagePayNotificationResponse", "SagePayOutstandingTransaction", "SagePayEnabledCardType", "TrustCommerceToken", "SagePayTransaction", "PricingComponentValueResponse", "MigrationResponse", "TimeResponse", "EntityTime", "Email", "MarketplaceConfiguration", "BFPermission", "Role", "PermissionLink", "PayVisionToken", "XeroConfiguration", "XeroMapping", "QuickBooksConfiguration", "QuickBooksWebhookEvent", "PayVisionTransaction", "KashToken", "EmailProvider", "DataSynchronizationJob", "DataSynchronizationJobError", "DataSynchronizationConfiguration", "DataSynchronizationAppConfiguration", "AggregationChildrenResponse", "MetadataKeyValue", "Metadata", "AggregatingComponent", "PricingComponentMigrationValue", "RegistrationResponse", "InvoiceRecalculationAmendment", "IssueInvoiceAmendment", "EmailSubscription", "SubscriptionCheckoutDefinition", "InvoiceCheckoutDefinition", "RevenueAttribution", "AddChargeToAccountResponse", "APIResponse", "PricingComponentUnitCredit", "CurrencyConfiguration", "SubscriptionNotificationConfiguration", "InvoiceTemplateConfig", "ChartMogulConfiguration", "BraintreeUpdateResult", "SubscriptionPricingComponentValueBatchUpdate", "InvoiceRender", "CouponWrapperResponse", "APIQuoteResponseQuantity", "APIQuote", "Contract", "HaltAggregationResponse", "ContractPeriod", "Affiliate", "AffiliateSubscriptionRelationship", "AffiliateRatePlanRelationship", "GoCardlessToken", "SetRatePlanAffiliateRequest", "CommissionStructure", "UserDefinableSalesforceObject", "EpxToken", "EpxPayment", "EpxApiConfiguration", "ZoozToken", "ZoozCustomer", "ZoozPayment", "EmailTokenization", "SubscriptionPlan", "SubscriptionGroup", "LoginAttempt", "InvoiceTemplateConfiguration", "OrganizationProfile", "PaymentMethodResponse", "ShuttleLink", "EmailNotification", "ShuttleHostedPayment", "EBANXPaymentMethod"]  # noqa: E501
        if record_type not in allowed_values:
            raise ValueError(
                "Invalid value for `record_type` ({0}), must be one of {1}"  # noqa: E501
                .format(record_type, allowed_values)
            )

        self._record_type = record_type

    @property
    def record_id(self):
        """Gets the record_id of this DataSyncJobErrorResponse.  # noqa: E501


        :return: The record_id of this DataSyncJobErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this DataSyncJobErrorResponse.


        :param record_id: The record_id of this DataSyncJobErrorResponse.  # noqa: E501
        :type: str
        """

        self._record_id = record_id

    @property
    def description(self):
        """Gets the description of this DataSyncJobErrorResponse.  # noqa: E501


        :return: The description of this DataSyncJobErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataSyncJobErrorResponse.


        :param description: The description of this DataSyncJobErrorResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def raw_internal_error(self):
        """Gets the raw_internal_error of this DataSyncJobErrorResponse.  # noqa: E501


        :return: The raw_internal_error of this DataSyncJobErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._raw_internal_error

    @raw_internal_error.setter
    def raw_internal_error(self, raw_internal_error):
        """Sets the raw_internal_error of this DataSyncJobErrorResponse.


        :param raw_internal_error: The raw_internal_error of this DataSyncJobErrorResponse.  # noqa: E501
        :type: str
        """

        self._raw_internal_error = raw_internal_error

    @property
    def encountered(self):
        """Gets the encountered of this DataSyncJobErrorResponse.  # noqa: E501


        :return: The encountered of this DataSyncJobErrorResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._encountered

    @encountered.setter
    def encountered(self, encountered):
        """Sets the encountered of this DataSyncJobErrorResponse.


        :param encountered: The encountered of this DataSyncJobErrorResponse.  # noqa: E501
        :type: datetime
        """

        self._encountered = encountered

    @property
    def run_number(self):
        """Gets the run_number of this DataSyncJobErrorResponse.  # noqa: E501


        :return: The run_number of this DataSyncJobErrorResponse.  # noqa: E501
        :rtype: int
        """
        return self._run_number

    @run_number.setter
    def run_number(self, run_number):
        """Sets the run_number of this DataSyncJobErrorResponse.


        :param run_number: The run_number of this DataSyncJobErrorResponse.  # noqa: E501
        :type: int
        """

        self._run_number = run_number

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
        if issubclass(DataSyncJobErrorResponse, dict):
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
        if not isinstance(other, DataSyncJobErrorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
