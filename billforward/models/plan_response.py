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

class PlanResponse(object):
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
        'id': 'str',
        'path': 'str',
        'name': 'str',
        'display_name': 'str',
        'description': 'str',
        'currency': 'CreditNoteCurrency',
        'tax_status': 'str',
        'failed_payment_behaviour': 'str',
        'duration': 'int',
        'duration_period': 'str',
        'trial': 'int',
        'trial_period': 'str',
        'pro_rata_mode': 'str',
        'localised_tax': 'bool',
        'create_zero_valued_invoices': 'bool',
        'migration_behaviour': 'str',
        'invoice_issue_type': 'str',
        'issue_duration': 'int',
        'issue_period': 'str',
        'payment_terms': 'int',
        'generate_service_end_invoice': 'bool',
        'fixed_term': 'FixedTerm',
        'taxation_strategies': 'list[str]',
        'pricing': 'PricingComponentsByChargeType',
        'valid_from': 'datetime',
        'valid_till': 'datetime',
        'metadata': 'dict(str, object)'
    }

    attribute_map = {
        'created': 'created',
        'organization_id': 'organizationID',
        'id': 'id',
        'path': 'path',
        'name': 'name',
        'display_name': 'displayName',
        'description': 'description',
        'currency': 'currency',
        'tax_status': 'taxStatus',
        'failed_payment_behaviour': 'failedPaymentBehaviour',
        'duration': 'duration',
        'duration_period': 'durationPeriod',
        'trial': 'trial',
        'trial_period': 'trialPeriod',
        'pro_rata_mode': 'proRataMode',
        'localised_tax': 'localisedTax',
        'create_zero_valued_invoices': 'createZeroValuedInvoices',
        'migration_behaviour': 'migrationBehaviour',
        'invoice_issue_type': 'invoiceIssueType',
        'issue_duration': 'issueDuration',
        'issue_period': 'issuePeriod',
        'payment_terms': 'paymentTerms',
        'generate_service_end_invoice': 'generateServiceEndInvoice',
        'fixed_term': 'fixedTerm',
        'taxation_strategies': 'taxationStrategies',
        'pricing': 'pricing',
        'valid_from': 'validFrom',
        'valid_till': 'validTill',
        'metadata': 'metadata'
    }

    def __init__(self, created=None, organization_id=None, id=None, path=None, name=None, display_name=None, description=None, currency=None, tax_status=None, failed_payment_behaviour=None, duration=None, duration_period=None, trial=None, trial_period=None, pro_rata_mode=None, localised_tax=None, create_zero_valued_invoices=None, migration_behaviour=None, invoice_issue_type=None, issue_duration=None, issue_period=None, payment_terms=None, generate_service_end_invoice=None, fixed_term=None, taxation_strategies=None, pricing=None, valid_from=None, valid_till=None, metadata=None):  # noqa: E501
        """PlanResponse - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._organization_id = None
        self._id = None
        self._path = None
        self._name = None
        self._display_name = None
        self._description = None
        self._currency = None
        self._tax_status = None
        self._failed_payment_behaviour = None
        self._duration = None
        self._duration_period = None
        self._trial = None
        self._trial_period = None
        self._pro_rata_mode = None
        self._localised_tax = None
        self._create_zero_valued_invoices = None
        self._migration_behaviour = None
        self._invoice_issue_type = None
        self._issue_duration = None
        self._issue_period = None
        self._payment_terms = None
        self._generate_service_end_invoice = None
        self._fixed_term = None
        self._taxation_strategies = None
        self._pricing = None
        self._valid_from = None
        self._valid_till = None
        self._metadata = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if organization_id is not None:
            self.organization_id = organization_id
        if id is not None:
            self.id = id
        if path is not None:
            self.path = path
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if currency is not None:
            self.currency = currency
        if tax_status is not None:
            self.tax_status = tax_status
        if failed_payment_behaviour is not None:
            self.failed_payment_behaviour = failed_payment_behaviour
        if duration is not None:
            self.duration = duration
        if duration_period is not None:
            self.duration_period = duration_period
        if trial is not None:
            self.trial = trial
        if trial_period is not None:
            self.trial_period = trial_period
        if pro_rata_mode is not None:
            self.pro_rata_mode = pro_rata_mode
        if localised_tax is not None:
            self.localised_tax = localised_tax
        if create_zero_valued_invoices is not None:
            self.create_zero_valued_invoices = create_zero_valued_invoices
        if migration_behaviour is not None:
            self.migration_behaviour = migration_behaviour
        if invoice_issue_type is not None:
            self.invoice_issue_type = invoice_issue_type
        if issue_duration is not None:
            self.issue_duration = issue_duration
        if issue_period is not None:
            self.issue_period = issue_period
        if payment_terms is not None:
            self.payment_terms = payment_terms
        if generate_service_end_invoice is not None:
            self.generate_service_end_invoice = generate_service_end_invoice
        if fixed_term is not None:
            self.fixed_term = fixed_term
        if taxation_strategies is not None:
            self.taxation_strategies = taxation_strategies
        if pricing is not None:
            self.pricing = pricing
        if valid_from is not None:
            self.valid_from = valid_from
        if valid_till is not None:
            self.valid_till = valid_till
        if metadata is not None:
            self.metadata = metadata

    @property
    def created(self):
        """Gets the created of this PlanResponse.  # noqa: E501


        :return: The created of this PlanResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PlanResponse.


        :param created: The created of this PlanResponse.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def organization_id(self):
        """Gets the organization_id of this PlanResponse.  # noqa: E501


        :return: The organization_id of this PlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this PlanResponse.


        :param organization_id: The organization_id of this PlanResponse.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def id(self):
        """Gets the id of this PlanResponse.  # noqa: E501


        :return: The id of this PlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlanResponse.


        :param id: The id of this PlanResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def path(self):
        """Gets the path of this PlanResponse.  # noqa: E501


        :return: The path of this PlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PlanResponse.


        :param path: The path of this PlanResponse.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def name(self):
        """Gets the name of this PlanResponse.  # noqa: E501


        :return: The name of this PlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlanResponse.


        :param name: The name of this PlanResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this PlanResponse.  # noqa: E501


        :return: The display_name of this PlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PlanResponse.


        :param display_name: The display_name of this PlanResponse.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this PlanResponse.  # noqa: E501


        :return: The description of this PlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PlanResponse.


        :param description: The description of this PlanResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def currency(self):
        """Gets the currency of this PlanResponse.  # noqa: E501


        :return: The currency of this PlanResponse.  # noqa: E501
        :rtype: CreditNoteCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PlanResponse.


        :param currency: The currency of this PlanResponse.  # noqa: E501
        :type: CreditNoteCurrency
        """

        self._currency = currency

    @property
    def tax_status(self):
        """Gets the tax_status of this PlanResponse.  # noqa: E501


        :return: The tax_status of this PlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._tax_status

    @tax_status.setter
    def tax_status(self, tax_status):
        """Sets the tax_status of this PlanResponse.


        :param tax_status: The tax_status of this PlanResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["inclusive", "exclusive"]  # noqa: E501
        if tax_status not in allowed_values:
            raise ValueError(
                "Invalid value for `tax_status` ({0}), must be one of {1}"  # noqa: E501
                .format(tax_status, allowed_values)
            )

        self._tax_status = tax_status

    @property
    def failed_payment_behaviour(self):
        """Gets the failed_payment_behaviour of this PlanResponse.  # noqa: E501


        :return: The failed_payment_behaviour of this PlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._failed_payment_behaviour

    @failed_payment_behaviour.setter
    def failed_payment_behaviour(self, failed_payment_behaviour):
        """Sets the failed_payment_behaviour of this PlanResponse.


        :param failed_payment_behaviour: The failed_payment_behaviour of this PlanResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["CancelSubscription", "None"]  # noqa: E501
        if failed_payment_behaviour not in allowed_values:
            raise ValueError(
                "Invalid value for `failed_payment_behaviour` ({0}), must be one of {1}"  # noqa: E501
                .format(failed_payment_behaviour, allowed_values)
            )

        self._failed_payment_behaviour = failed_payment_behaviour

    @property
    def duration(self):
        """Gets the duration of this PlanResponse.  # noqa: E501


        :return: The duration of this PlanResponse.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this PlanResponse.


        :param duration: The duration of this PlanResponse.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def duration_period(self):
        """Gets the duration_period of this PlanResponse.  # noqa: E501


        :return: The duration_period of this PlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._duration_period

    @duration_period.setter
    def duration_period(self, duration_period):
        """Sets the duration_period of this PlanResponse.


        :param duration_period: The duration_period of this PlanResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["minutes", "days", "months", "years"]  # noqa: E501
        if duration_period not in allowed_values:
            raise ValueError(
                "Invalid value for `duration_period` ({0}), must be one of {1}"  # noqa: E501
                .format(duration_period, allowed_values)
            )

        self._duration_period = duration_period

    @property
    def trial(self):
        """Gets the trial of this PlanResponse.  # noqa: E501


        :return: The trial of this PlanResponse.  # noqa: E501
        :rtype: int
        """
        return self._trial

    @trial.setter
    def trial(self, trial):
        """Sets the trial of this PlanResponse.


        :param trial: The trial of this PlanResponse.  # noqa: E501
        :type: int
        """

        self._trial = trial

    @property
    def trial_period(self):
        """Gets the trial_period of this PlanResponse.  # noqa: E501


        :return: The trial_period of this PlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._trial_period

    @trial_period.setter
    def trial_period(self, trial_period):
        """Sets the trial_period of this PlanResponse.


        :param trial_period: The trial_period of this PlanResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "minutes", "days", "months"]  # noqa: E501
        if trial_period not in allowed_values:
            raise ValueError(
                "Invalid value for `trial_period` ({0}), must be one of {1}"  # noqa: E501
                .format(trial_period, allowed_values)
            )

        self._trial_period = trial_period

    @property
    def pro_rata_mode(self):
        """Gets the pro_rata_mode of this PlanResponse.  # noqa: E501


        :return: The pro_rata_mode of this PlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._pro_rata_mode

    @pro_rata_mode.setter
    def pro_rata_mode(self, pro_rata_mode):
        """Sets the pro_rata_mode of this PlanResponse.


        :param pro_rata_mode: The pro_rata_mode of this PlanResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "WithCoupon", "WithoutCoupon", "Full"]  # noqa: E501
        if pro_rata_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `pro_rata_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(pro_rata_mode, allowed_values)
            )

        self._pro_rata_mode = pro_rata_mode

    @property
    def localised_tax(self):
        """Gets the localised_tax of this PlanResponse.  # noqa: E501


        :return: The localised_tax of this PlanResponse.  # noqa: E501
        :rtype: bool
        """
        return self._localised_tax

    @localised_tax.setter
    def localised_tax(self, localised_tax):
        """Sets the localised_tax of this PlanResponse.


        :param localised_tax: The localised_tax of this PlanResponse.  # noqa: E501
        :type: bool
        """

        self._localised_tax = localised_tax

    @property
    def create_zero_valued_invoices(self):
        """Gets the create_zero_valued_invoices of this PlanResponse.  # noqa: E501


        :return: The create_zero_valued_invoices of this PlanResponse.  # noqa: E501
        :rtype: bool
        """
        return self._create_zero_valued_invoices

    @create_zero_valued_invoices.setter
    def create_zero_valued_invoices(self, create_zero_valued_invoices):
        """Sets the create_zero_valued_invoices of this PlanResponse.


        :param create_zero_valued_invoices: The create_zero_valued_invoices of this PlanResponse.  # noqa: E501
        :type: bool
        """

        self._create_zero_valued_invoices = create_zero_valued_invoices

    @property
    def migration_behaviour(self):
        """Gets the migration_behaviour of this PlanResponse.  # noqa: E501


        :return: The migration_behaviour of this PlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._migration_behaviour

    @migration_behaviour.setter
    def migration_behaviour(self, migration_behaviour):
        """Sets the migration_behaviour of this PlanResponse.


        :param migration_behaviour: The migration_behaviour of this PlanResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["NoCharge", "CreditAccount"]  # noqa: E501
        if migration_behaviour not in allowed_values:
            raise ValueError(
                "Invalid value for `migration_behaviour` ({0}), must be one of {1}"  # noqa: E501
                .format(migration_behaviour, allowed_values)
            )

        self._migration_behaviour = migration_behaviour

    @property
    def invoice_issue_type(self):
        """Gets the invoice_issue_type of this PlanResponse.  # noqa: E501


        :return: The invoice_issue_type of this PlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._invoice_issue_type

    @invoice_issue_type.setter
    def invoice_issue_type(self, invoice_issue_type):
        """Sets the invoice_issue_type of this PlanResponse.


        :param invoice_issue_type: The invoice_issue_type of this PlanResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Immediate", "Delayed", "Manual"]  # noqa: E501
        if invoice_issue_type not in allowed_values:
            raise ValueError(
                "Invalid value for `invoice_issue_type` ({0}), must be one of {1}"  # noqa: E501
                .format(invoice_issue_type, allowed_values)
            )

        self._invoice_issue_type = invoice_issue_type

    @property
    def issue_duration(self):
        """Gets the issue_duration of this PlanResponse.  # noqa: E501


        :return: The issue_duration of this PlanResponse.  # noqa: E501
        :rtype: int
        """
        return self._issue_duration

    @issue_duration.setter
    def issue_duration(self, issue_duration):
        """Sets the issue_duration of this PlanResponse.


        :param issue_duration: The issue_duration of this PlanResponse.  # noqa: E501
        :type: int
        """

        self._issue_duration = issue_duration

    @property
    def issue_period(self):
        """Gets the issue_period of this PlanResponse.  # noqa: E501


        :return: The issue_period of this PlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._issue_period

    @issue_period.setter
    def issue_period(self, issue_period):
        """Sets the issue_period of this PlanResponse.


        :param issue_period: The issue_period of this PlanResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["minutes", "days", "months", "years"]  # noqa: E501
        if issue_period not in allowed_values:
            raise ValueError(
                "Invalid value for `issue_period` ({0}), must be one of {1}"  # noqa: E501
                .format(issue_period, allowed_values)
            )

        self._issue_period = issue_period

    @property
    def payment_terms(self):
        """Gets the payment_terms of this PlanResponse.  # noqa: E501


        :return: The payment_terms of this PlanResponse.  # noqa: E501
        :rtype: int
        """
        return self._payment_terms

    @payment_terms.setter
    def payment_terms(self, payment_terms):
        """Sets the payment_terms of this PlanResponse.


        :param payment_terms: The payment_terms of this PlanResponse.  # noqa: E501
        :type: int
        """

        self._payment_terms = payment_terms

    @property
    def generate_service_end_invoice(self):
        """Gets the generate_service_end_invoice of this PlanResponse.  # noqa: E501


        :return: The generate_service_end_invoice of this PlanResponse.  # noqa: E501
        :rtype: bool
        """
        return self._generate_service_end_invoice

    @generate_service_end_invoice.setter
    def generate_service_end_invoice(self, generate_service_end_invoice):
        """Sets the generate_service_end_invoice of this PlanResponse.


        :param generate_service_end_invoice: The generate_service_end_invoice of this PlanResponse.  # noqa: E501
        :type: bool
        """

        self._generate_service_end_invoice = generate_service_end_invoice

    @property
    def fixed_term(self):
        """Gets the fixed_term of this PlanResponse.  # noqa: E501


        :return: The fixed_term of this PlanResponse.  # noqa: E501
        :rtype: FixedTerm
        """
        return self._fixed_term

    @fixed_term.setter
    def fixed_term(self, fixed_term):
        """Sets the fixed_term of this PlanResponse.


        :param fixed_term: The fixed_term of this PlanResponse.  # noqa: E501
        :type: FixedTerm
        """

        self._fixed_term = fixed_term

    @property
    def taxation_strategies(self):
        """Gets the taxation_strategies of this PlanResponse.  # noqa: E501


        :return: The taxation_strategies of this PlanResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._taxation_strategies

    @taxation_strategies.setter
    def taxation_strategies(self, taxation_strategies):
        """Sets the taxation_strategies of this PlanResponse.


        :param taxation_strategies: The taxation_strategies of this PlanResponse.  # noqa: E501
        :type: list[str]
        """

        self._taxation_strategies = taxation_strategies

    @property
    def pricing(self):
        """Gets the pricing of this PlanResponse.  # noqa: E501


        :return: The pricing of this PlanResponse.  # noqa: E501
        :rtype: PricingComponentsByChargeType
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """Sets the pricing of this PlanResponse.


        :param pricing: The pricing of this PlanResponse.  # noqa: E501
        :type: PricingComponentsByChargeType
        """

        self._pricing = pricing

    @property
    def valid_from(self):
        """Gets the valid_from of this PlanResponse.  # noqa: E501


        :return: The valid_from of this PlanResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this PlanResponse.


        :param valid_from: The valid_from of this PlanResponse.  # noqa: E501
        :type: datetime
        """

        self._valid_from = valid_from

    @property
    def valid_till(self):
        """Gets the valid_till of this PlanResponse.  # noqa: E501


        :return: The valid_till of this PlanResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_till

    @valid_till.setter
    def valid_till(self, valid_till):
        """Sets the valid_till of this PlanResponse.


        :param valid_till: The valid_till of this PlanResponse.  # noqa: E501
        :type: datetime
        """

        self._valid_till = valid_till

    @property
    def metadata(self):
        """Gets the metadata of this PlanResponse.  # noqa: E501


        :return: The metadata of this PlanResponse.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PlanResponse.


        :param metadata: The metadata of this PlanResponse.  # noqa: E501
        :type: dict(str, object)
        """

        self._metadata = metadata

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
        if issubclass(PlanResponse, dict):
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
        if not isinstance(other, PlanResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
