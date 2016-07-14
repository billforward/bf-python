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


class InvoiceChargeRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, include_aggregated=False, include_invoiced_charges_only=False, invoice_state=None):
        """
        InvoiceChargeRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'include_aggregated': 'bool',
            'include_invoiced_charges_only': 'bool',
            'invoice_state': 'str'
        }

        self.attribute_map = {
            'created': 'created',
            'include_aggregated': 'includeAggregated',
            'include_invoiced_charges_only': 'includeInvoicedChargesOnly',
            'invoice_state': 'invoiceState'
        }

        self._created = created
        self._include_aggregated = include_aggregated
        self._include_invoiced_charges_only = include_invoiced_charges_only
        self._invoice_state = invoice_state

    @property
    def created(self):
        """
        Gets the created of this InvoiceChargeRequest.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this InvoiceChargeRequest.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this InvoiceChargeRequest.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this InvoiceChargeRequest.
        :type: datetime
        """

        self._created = created

    @property
    def include_aggregated(self):
        """
        Gets the include_aggregated of this InvoiceChargeRequest.
        {\"default\":false,\"description\":\"Outstanding charges for which invoices will be generated:<br><span class=\\\"label label-default\\\">true</span> &mdash; Include charges marked with 'Aggregated' `invoicingType` (i.e. charges that would otherwise be included anyway in the next naturally-occurring invoice)<br><span class=\\\"label label-default\\\">false</span> &mdash; Exclude charges marked with 'Aggregated' `invoicingType` (i.e. prefer that these charges be included instead on the next naturally-occurring invoice).\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The include_aggregated of this InvoiceChargeRequest.
        :rtype: bool
        """
        return self._include_aggregated

    @include_aggregated.setter
    def include_aggregated(self, include_aggregated):
        """
        Sets the include_aggregated of this InvoiceChargeRequest.
        {\"default\":false,\"description\":\"Outstanding charges for which invoices will be generated:<br><span class=\\\"label label-default\\\">true</span> &mdash; Include charges marked with 'Aggregated' `invoicingType` (i.e. charges that would otherwise be included anyway in the next naturally-occurring invoice)<br><span class=\\\"label label-default\\\">false</span> &mdash; Exclude charges marked with 'Aggregated' `invoicingType` (i.e. prefer that these charges be included instead on the next naturally-occurring invoice).\",\"verbs\":[\"POST\",\"GET\"]}

        :param include_aggregated: The include_aggregated of this InvoiceChargeRequest.
        :type: bool
        """

        self._include_aggregated = include_aggregated

    @property
    def include_invoiced_charges_only(self):
        """
        Gets the include_invoiced_charges_only of this InvoiceChargeRequest.
        {\"default\":false,\"description\":\"Outstanding charges for which invoices will be generated:<br><span class=\\\"label label-default\\\">true</span> &mdash; Include those charges raised with 'no invoice' specified (i.e. charges against the subscription) &mdash; as well as charges raised against some specific invoice.<br><span class=\\\"label label-default\\\">false</span> &mdash; Include only charges raised against some specific invoice.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The include_invoiced_charges_only of this InvoiceChargeRequest.
        :rtype: bool
        """
        return self._include_invoiced_charges_only

    @include_invoiced_charges_only.setter
    def include_invoiced_charges_only(self, include_invoiced_charges_only):
        """
        Sets the include_invoiced_charges_only of this InvoiceChargeRequest.
        {\"default\":false,\"description\":\"Outstanding charges for which invoices will be generated:<br><span class=\\\"label label-default\\\">true</span> &mdash; Include those charges raised with 'no invoice' specified (i.e. charges against the subscription) &mdash; as well as charges raised against some specific invoice.<br><span class=\\\"label label-default\\\">false</span> &mdash; Include only charges raised against some specific invoice.\",\"verbs\":[\"POST\",\"GET\"]}

        :param include_invoiced_charges_only: The include_invoiced_charges_only of this InvoiceChargeRequest.
        :type: bool
        """

        self._include_invoiced_charges_only = include_invoiced_charges_only

    @property
    def invoice_state(self):
        """
        Gets the invoice_state of this InvoiceChargeRequest.
        {\"default\":null (invoice is raised in its default initial state),\"description\":\"Initial state with which any invoices will be generated.\",\"verbs\":[\"POST\",\"GET\"]}

        :return: The invoice_state of this InvoiceChargeRequest.
        :rtype: str
        """
        return self._invoice_state

    @invoice_state.setter
    def invoice_state(self, invoice_state):
        """
        Sets the invoice_state of this InvoiceChargeRequest.
        {\"default\":null (invoice is raised in its default initial state),\"description\":\"Initial state with which any invoices will be generated.\",\"verbs\":[\"POST\",\"GET\"]}

        :param invoice_state: The invoice_state of this InvoiceChargeRequest.
        :type: str
        """
        allowed_values = ["Paid", "Unpaid", "Pending", "Voided"]
        if invoice_state not in allowed_values:
            raise ValueError(
                "Invalid value for `invoice_state` ({0}), must be one of {1}"
                .format(invoice_state, allowed_values)
            )

        self._invoice_state = invoice_state

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
