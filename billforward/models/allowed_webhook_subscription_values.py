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

class AllowedWebhookSubscriptionValues(object):
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
        'domains': 'list[str]',
        'actions': 'list[str]',
        'organization_id': 'str'
    }

    attribute_map = {
        'created': 'created',
        'domains': 'domains',
        'actions': 'actions',
        'organization_id': 'organizationID'
    }

    def __init__(self, created=None, domains=None, actions=None, organization_id=None):  # noqa: E501
        """AllowedWebhookSubscriptionValues - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._domains = None
        self._actions = None
        self._organization_id = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if domains is not None:
            self.domains = domains
        if actions is not None:
            self.actions = actions
        if organization_id is not None:
            self.organization_id = organization_id

    @property
    def created(self):
        """Gets the created of this AllowedWebhookSubscriptionValues.  # noqa: E501


        :return: The created of this AllowedWebhookSubscriptionValues.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AllowedWebhookSubscriptionValues.


        :param created: The created of this AllowedWebhookSubscriptionValues.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def domains(self):
        """Gets the domains of this AllowedWebhookSubscriptionValues.  # noqa: E501


        :return: The domains of this AllowedWebhookSubscriptionValues.  # noqa: E501
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this AllowedWebhookSubscriptionValues.


        :param domains: The domains of this AllowedWebhookSubscriptionValues.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["AvataxConfiguration", "Notification", "Organization", "Product", "User", "Subscription", "Profile", "ProductRatePlan", "Client", "Invoice", "PricingComponentValue", "Account", "PricingComponentValueChange", "PricingComponentTier", "PricingComponent", "PricingCalculation", "CouponDefinition", "CouponInstance", "CouponModifier", "CouponRule", "CouponBookDefinition", "CouponBook", "InvoiceLine", "Webhook", "SubscriptionCancellation", "NotificationSnapshot", "InvoicePayment", "InvoiceLinePayment", "Payment", "PaymentMethod", "BankAccount", "PaymentMethodSubscriptionLink", "DunningLine", "CybersourceToken", "Card", "Alias", "CouponInstanceExistingValue", "TaxLine", "TaxationStrategy", "TaxationLink", "Address", "AmendmentPriceNTime", "Authority", "UnitOfMeasure", "Amendment", "AuditLog", "Password", "Username", "FixedTermDefinition", "FixedTerm", "Refund", "CreditNote", "Receipt", "AmendmentCompoundConstituent", "APIConfiguration", "StripeToken", "BraintreeToken", "PaypalToken", "AuthorizeNetToken", "SpreedlyToken", "AmendmentDiscardAmendment", "CancellationAmendment", "CompoundAmendment", "CompoundAmendmentConstituent", "FixedTermExpiryAmendment", "InvoiceNextExecutionAttemptAmendment", "PricingComponentValueAmendment", "BraintreeMerchantAccount", "WebhookSubscription", "Migration", "SubscriptionCharge", "StripeACHToken", "OfflinePayment", "CreditNotePayment", "CardVaultPayment", "BraintreePayment", "CybersourcePayment", "PaypalPayment", "StripeACHPayment", "AuthorizeNetPayment", "PricingComponentValueMigrationChargeAmendmentMapping", "ComponentChange", "QuoteRequest", "Quote", "CouponCharge", "CouponInstanceInvoiceLink", "Coupon", "CouponDiscount", "CouponUniqueCodesRequest", "CouponUniqueCodesResponse", "GetCouponsResponse", "AddCouponCodeRequest", "AddCouponCodeResponse", "RemoveCouponFromSubscriptionRequest", "TokenizationPreAuth", "StripeTokenizationPreAuth", "BraintreeTokenizationPreAuth", "SpreedlyTokenizationPreAuth", "SagePayTokenizationPreAuth", "PayVisionTokenizationPreAuth", "TokenizationPreAuthRequest", "AuthCaptureRequest", "StripeACHBankAccountVerification", "PasswordReset", "PricingRequest", "AmendmentPriceRequest", "AddTaxationStrategyRequest", "AddPaymentMethodRequest", "APIRequest", "SagePayToken", "SagePayNotificationRequest", "SagePayNotificationResponse", "SagePayOutstandingTransaction", "SagePayEnabledCardType", "TrustCommerceToken", "SagePayTransaction", "PricingComponentValueResponse", "MigrationResponse", "TimeResponse", "EntityTime", "Email", "MarketplaceConfiguration", "BFPermission", "Role", "PermissionLink", "PayVisionToken", "XeroConfiguration", "XeroMapping", "QuickBooksConfiguration", "QuickBooksWebhookEvent", "PayVisionTransaction", "KashToken", "EmailProvider", "DataSynchronizationJob", "DataSynchronizationJobError", "DataSynchronizationConfiguration", "DataSynchronizationAppConfiguration", "AggregationChildrenResponse", "MetadataKeyValue", "Metadata", "AggregatingComponent", "PricingComponentMigrationValue", "RegistrationResponse", "InvoiceRecalculationAmendment", "IssueInvoiceAmendment", "EmailSubscription", "SubscriptionCheckoutDefinition", "InvoiceCheckoutDefinition", "RevenueAttribution", "AddChargeToAccountResponse", "APIResponse", "PricingComponentUnitCredit", "CurrencyConfiguration", "SubscriptionNotificationConfiguration", "InvoiceTemplateConfig", "ChartMogulConfiguration", "BraintreeUpdateResult", "SubscriptionPricingComponentValueBatchUpdate", "InvoiceRender", "CouponWrapperResponse", "APIQuoteResponseQuantity", "APIQuote", "Contract", "HaltAggregationResponse", "ContractPeriod", "Affiliate", "AffiliateSubscriptionRelationship", "AffiliateRatePlanRelationship", "GoCardlessToken", "SetRatePlanAffiliateRequest", "CommissionStructure", "UserDefinableSalesforceObject", "EpxToken", "EpxPayment", "EpxApiConfiguration", "ZoozToken", "ZoozCustomer", "ZoozPayment", "EmailTokenization", "SubscriptionPlan", "SubscriptionGroup", "LoginAttempt", "InvoiceTemplateConfiguration", "OrganizationProfile", "PaymentMethodResponse", "ShuttleLink", "EmailNotification", "ShuttleHostedPayment", "EBANXPaymentMethod"]  # noqa: E501
        if not set(domains).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `domains` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(domains) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._domains = domains

    @property
    def actions(self):
        """Gets the actions of this AllowedWebhookSubscriptionValues.  # noqa: E501


        :return: The actions of this AllowedWebhookSubscriptionValues.  # noqa: E501
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this AllowedWebhookSubscriptionValues.


        :param actions: The actions of this AllowedWebhookSubscriptionValues.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Accept", "Active", "AwaitingPayment", "AwaitingRefund", "Cancelled", "Completed", "Created", "Current", "Error", "Expiring", "Expired", "Failed", "Migrated", "NeedsAmendments", "Paid", "Pending", "Provisioned", "Refunded", "Reject", "Restarted", "Trial", "Unknown", "Unpaid", "Updated", "Voided", "PaymentFailed", "ProcessingPayment", "ServiceEnded", "AdvanceNotification"]  # noqa: E501
        if not set(actions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `actions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(actions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._actions = actions

    @property
    def organization_id(self):
        """Gets the organization_id of this AllowedWebhookSubscriptionValues.  # noqa: E501


        :return: The organization_id of this AllowedWebhookSubscriptionValues.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this AllowedWebhookSubscriptionValues.


        :param organization_id: The organization_id of this AllowedWebhookSubscriptionValues.  # noqa: E501
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
        if issubclass(AllowedWebhookSubscriptionValues, dict):
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
        if not isinstance(other, AllowedWebhookSubscriptionValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other