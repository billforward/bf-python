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

class UpdateInvoiceTemplateRequest(object):
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
        'organization_id': 'str',
        'representing_account_id': 'str',
        'tier_breakdown': 'bool',
        'inclusive_end': 'bool',
        'show_zero_cost': 'bool',
        'show_plan_only_when_ambiguous': 'bool',
        'include_footer': 'bool',
        'invoice_header_display': 'str',
        'group_invoice_line_items_by': 'str',
        'hide_tax_if_zero': 'bool',
        'show_unit_price': 'str',
        'company_address_on_top': 'bool',
        'upgrade_duration_wording': 'bool'
    }

    attribute_map = {
        'organization_id': 'organizationID',
        'representing_account_id': 'representingAccountID',
        'tier_breakdown': 'tierBreakdown',
        'inclusive_end': 'inclusiveEnd',
        'show_zero_cost': 'showZeroCost',
        'show_plan_only_when_ambiguous': 'showPlanOnlyWhenAmbiguous',
        'include_footer': 'includeFooter',
        'invoice_header_display': 'invoiceHeaderDisplay',
        'group_invoice_line_items_by': 'groupInvoiceLineItemsBy',
        'hide_tax_if_zero': 'hideTaxIfZero',
        'show_unit_price': 'showUnitPrice',
        'company_address_on_top': 'companyAddressOnTop',
        'upgrade_duration_wording': 'upgradeDurationWording'
    }

    def __init__(self, organization_id=None, representing_account_id=None, tier_breakdown=None, inclusive_end=None, show_zero_cost=None, show_plan_only_when_ambiguous=None, include_footer=None, invoice_header_display=None, group_invoice_line_items_by=None, hide_tax_if_zero=None, show_unit_price=None, company_address_on_top=None, upgrade_duration_wording=None):  # noqa: E501
        """UpdateInvoiceTemplateRequest - a model defined in Swagger"""  # noqa: E501
        self._organization_id = None
        self._representing_account_id = None
        self._tier_breakdown = None
        self._inclusive_end = None
        self._show_zero_cost = None
        self._show_plan_only_when_ambiguous = None
        self._include_footer = None
        self._invoice_header_display = None
        self._group_invoice_line_items_by = None
        self._hide_tax_if_zero = None
        self._show_unit_price = None
        self._company_address_on_top = None
        self._upgrade_duration_wording = None
        self.discriminator = None
        if organization_id is not None:
            self.organization_id = organization_id
        if representing_account_id is not None:
            self.representing_account_id = representing_account_id
        if tier_breakdown is not None:
            self.tier_breakdown = tier_breakdown
        if inclusive_end is not None:
            self.inclusive_end = inclusive_end
        if show_zero_cost is not None:
            self.show_zero_cost = show_zero_cost
        if show_plan_only_when_ambiguous is not None:
            self.show_plan_only_when_ambiguous = show_plan_only_when_ambiguous
        if include_footer is not None:
            self.include_footer = include_footer
        if invoice_header_display is not None:
            self.invoice_header_display = invoice_header_display
        if group_invoice_line_items_by is not None:
            self.group_invoice_line_items_by = group_invoice_line_items_by
        if hide_tax_if_zero is not None:
            self.hide_tax_if_zero = hide_tax_if_zero
        if show_unit_price is not None:
            self.show_unit_price = show_unit_price
        if company_address_on_top is not None:
            self.company_address_on_top = company_address_on_top
        if upgrade_duration_wording is not None:
            self.upgrade_duration_wording = upgrade_duration_wording

    @property
    def organization_id(self):
        """Gets the organization_id of this UpdateInvoiceTemplateRequest.  # noqa: E501


        :return: The organization_id of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this UpdateInvoiceTemplateRequest.


        :param organization_id: The organization_id of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def representing_account_id(self):
        """Gets the representing_account_id of this UpdateInvoiceTemplateRequest.  # noqa: E501


        :return: The representing_account_id of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._representing_account_id

    @representing_account_id.setter
    def representing_account_id(self, representing_account_id):
        """Sets the representing_account_id of this UpdateInvoiceTemplateRequest.


        :param representing_account_id: The representing_account_id of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :type: str
        """

        self._representing_account_id = representing_account_id

    @property
    def tier_breakdown(self):
        """Gets the tier_breakdown of this UpdateInvoiceTemplateRequest.  # noqa: E501


        :return: The tier_breakdown of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._tier_breakdown

    @tier_breakdown.setter
    def tier_breakdown(self, tier_breakdown):
        """Sets the tier_breakdown of this UpdateInvoiceTemplateRequest.


        :param tier_breakdown: The tier_breakdown of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :type: bool
        """

        self._tier_breakdown = tier_breakdown

    @property
    def inclusive_end(self):
        """Gets the inclusive_end of this UpdateInvoiceTemplateRequest.  # noqa: E501


        :return: The inclusive_end of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._inclusive_end

    @inclusive_end.setter
    def inclusive_end(self, inclusive_end):
        """Sets the inclusive_end of this UpdateInvoiceTemplateRequest.


        :param inclusive_end: The inclusive_end of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :type: bool
        """

        self._inclusive_end = inclusive_end

    @property
    def show_zero_cost(self):
        """Gets the show_zero_cost of this UpdateInvoiceTemplateRequest.  # noqa: E501


        :return: The show_zero_cost of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._show_zero_cost

    @show_zero_cost.setter
    def show_zero_cost(self, show_zero_cost):
        """Sets the show_zero_cost of this UpdateInvoiceTemplateRequest.


        :param show_zero_cost: The show_zero_cost of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :type: bool
        """

        self._show_zero_cost = show_zero_cost

    @property
    def show_plan_only_when_ambiguous(self):
        """Gets the show_plan_only_when_ambiguous of this UpdateInvoiceTemplateRequest.  # noqa: E501


        :return: The show_plan_only_when_ambiguous of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._show_plan_only_when_ambiguous

    @show_plan_only_when_ambiguous.setter
    def show_plan_only_when_ambiguous(self, show_plan_only_when_ambiguous):
        """Sets the show_plan_only_when_ambiguous of this UpdateInvoiceTemplateRequest.


        :param show_plan_only_when_ambiguous: The show_plan_only_when_ambiguous of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :type: bool
        """

        self._show_plan_only_when_ambiguous = show_plan_only_when_ambiguous

    @property
    def include_footer(self):
        """Gets the include_footer of this UpdateInvoiceTemplateRequest.  # noqa: E501


        :return: The include_footer of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_footer

    @include_footer.setter
    def include_footer(self, include_footer):
        """Sets the include_footer of this UpdateInvoiceTemplateRequest.


        :param include_footer: The include_footer of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :type: bool
        """

        self._include_footer = include_footer

    @property
    def invoice_header_display(self):
        """Gets the invoice_header_display of this UpdateInvoiceTemplateRequest.  # noqa: E501


        :return: The invoice_header_display of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._invoice_header_display

    @invoice_header_display.setter
    def invoice_header_display(self, invoice_header_display):
        """Sets the invoice_header_display of this UpdateInvoiceTemplateRequest.


        :param invoice_header_display: The invoice_header_display of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["ID_LEFT", "ID_RIGHT"]  # noqa: E501
        if invoice_header_display not in allowed_values:
            raise ValueError(
                "Invalid value for `invoice_header_display` ({0}), must be one of {1}"  # noqa: E501
                .format(invoice_header_display, allowed_values)
            )

        self._invoice_header_display = invoice_header_display

    @property
    def group_invoice_line_items_by(self):
        """Gets the group_invoice_line_items_by of this UpdateInvoiceTemplateRequest.  # noqa: E501


        :return: The group_invoice_line_items_by of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._group_invoice_line_items_by

    @group_invoice_line_items_by.setter
    def group_invoice_line_items_by(self, group_invoice_line_items_by):
        """Sets the group_invoice_line_items_by of this UpdateInvoiceTemplateRequest.


        :param group_invoice_line_items_by: The group_invoice_line_items_by of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Product", "RatePlan", "ProductAndRatePlan"]  # noqa: E501
        if group_invoice_line_items_by not in allowed_values:
            raise ValueError(
                "Invalid value for `group_invoice_line_items_by` ({0}), must be one of {1}"  # noqa: E501
                .format(group_invoice_line_items_by, allowed_values)
            )

        self._group_invoice_line_items_by = group_invoice_line_items_by

    @property
    def hide_tax_if_zero(self):
        """Gets the hide_tax_if_zero of this UpdateInvoiceTemplateRequest.  # noqa: E501


        :return: The hide_tax_if_zero of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._hide_tax_if_zero

    @hide_tax_if_zero.setter
    def hide_tax_if_zero(self, hide_tax_if_zero):
        """Sets the hide_tax_if_zero of this UpdateInvoiceTemplateRequest.


        :param hide_tax_if_zero: The hide_tax_if_zero of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :type: bool
        """

        self._hide_tax_if_zero = hide_tax_if_zero

    @property
    def show_unit_price(self):
        """Gets the show_unit_price of this UpdateInvoiceTemplateRequest.  # noqa: E501


        :return: The show_unit_price of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._show_unit_price

    @show_unit_price.setter
    def show_unit_price(self, show_unit_price):
        """Sets the show_unit_price of this UpdateInvoiceTemplateRequest.


        :param show_unit_price: The show_unit_price of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Hidden", "Column", "Inline"]  # noqa: E501
        if show_unit_price not in allowed_values:
            raise ValueError(
                "Invalid value for `show_unit_price` ({0}), must be one of {1}"  # noqa: E501
                .format(show_unit_price, allowed_values)
            )

        self._show_unit_price = show_unit_price

    @property
    def company_address_on_top(self):
        """Gets the company_address_on_top of this UpdateInvoiceTemplateRequest.  # noqa: E501


        :return: The company_address_on_top of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._company_address_on_top

    @company_address_on_top.setter
    def company_address_on_top(self, company_address_on_top):
        """Sets the company_address_on_top of this UpdateInvoiceTemplateRequest.


        :param company_address_on_top: The company_address_on_top of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :type: bool
        """

        self._company_address_on_top = company_address_on_top

    @property
    def upgrade_duration_wording(self):
        """Gets the upgrade_duration_wording of this UpdateInvoiceTemplateRequest.  # noqa: E501


        :return: The upgrade_duration_wording of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._upgrade_duration_wording

    @upgrade_duration_wording.setter
    def upgrade_duration_wording(self, upgrade_duration_wording):
        """Sets the upgrade_duration_wording of this UpdateInvoiceTemplateRequest.


        :param upgrade_duration_wording: The upgrade_duration_wording of this UpdateInvoiceTemplateRequest.  # noqa: E501
        :type: bool
        """

        self._upgrade_duration_wording = upgrade_duration_wording

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
        if issubclass(UpdateInvoiceTemplateRequest, dict):
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
        if not isinstance(other, UpdateInvoiceTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other