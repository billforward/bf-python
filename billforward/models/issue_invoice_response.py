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

class IssueInvoiceResponse(object):
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
        'issued': 'bool',
        'voided': 'bool',
        'reason': 'str',
        'invoice': 'Invoice',
        'reason_explanation': 'str'
    }

    attribute_map = {
        'created': 'created',
        'organization_id': 'organizationID',
        'issued': 'issued',
        'voided': 'voided',
        'reason': 'reason',
        'invoice': 'invoice',
        'reason_explanation': 'reasonExplanation'
    }

    def __init__(self, created=None, organization_id=None, issued=None, voided=None, reason=None, invoice=None, reason_explanation=None):  # noqa: E501
        """IssueInvoiceResponse - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._organization_id = None
        self._issued = None
        self._voided = None
        self._reason = None
        self._invoice = None
        self._reason_explanation = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if organization_id is not None:
            self.organization_id = organization_id
        if issued is not None:
            self.issued = issued
        if voided is not None:
            self.voided = voided
        if reason is not None:
            self.reason = reason
        if invoice is not None:
            self.invoice = invoice
        if reason_explanation is not None:
            self.reason_explanation = reason_explanation

    @property
    def created(self):
        """Gets the created of this IssueInvoiceResponse.  # noqa: E501


        :return: The created of this IssueInvoiceResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this IssueInvoiceResponse.


        :param created: The created of this IssueInvoiceResponse.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def organization_id(self):
        """Gets the organization_id of this IssueInvoiceResponse.  # noqa: E501


        :return: The organization_id of this IssueInvoiceResponse.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this IssueInvoiceResponse.


        :param organization_id: The organization_id of this IssueInvoiceResponse.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def issued(self):
        """Gets the issued of this IssueInvoiceResponse.  # noqa: E501


        :return: The issued of this IssueInvoiceResponse.  # noqa: E501
        :rtype: bool
        """
        return self._issued

    @issued.setter
    def issued(self, issued):
        """Sets the issued of this IssueInvoiceResponse.


        :param issued: The issued of this IssueInvoiceResponse.  # noqa: E501
        :type: bool
        """

        self._issued = issued

    @property
    def voided(self):
        """Gets the voided of this IssueInvoiceResponse.  # noqa: E501


        :return: The voided of this IssueInvoiceResponse.  # noqa: E501
        :rtype: bool
        """
        return self._voided

    @voided.setter
    def voided(self, voided):
        """Sets the voided of this IssueInvoiceResponse.


        :param voided: The voided of this IssueInvoiceResponse.  # noqa: E501
        :type: bool
        """

        self._voided = voided

    @property
    def reason(self):
        """Gets the reason of this IssueInvoiceResponse.  # noqa: E501


        :return: The reason of this IssueInvoiceResponse.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this IssueInvoiceResponse.


        :param reason: The reason of this IssueInvoiceResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["CostThreshold", "WasNotPending"]  # noqa: E501
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def invoice(self):
        """Gets the invoice of this IssueInvoiceResponse.  # noqa: E501


        :return: The invoice of this IssueInvoiceResponse.  # noqa: E501
        :rtype: Invoice
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this IssueInvoiceResponse.


        :param invoice: The invoice of this IssueInvoiceResponse.  # noqa: E501
        :type: Invoice
        """

        self._invoice = invoice

    @property
    def reason_explanation(self):
        """Gets the reason_explanation of this IssueInvoiceResponse.  # noqa: E501


        :return: The reason_explanation of this IssueInvoiceResponse.  # noqa: E501
        :rtype: str
        """
        return self._reason_explanation

    @reason_explanation.setter
    def reason_explanation(self, reason_explanation):
        """Sets the reason_explanation of this IssueInvoiceResponse.


        :param reason_explanation: The reason_explanation of this IssueInvoiceResponse.  # noqa: E501
        :type: str
        """

        self._reason_explanation = reason_explanation

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
        if issubclass(IssueInvoiceResponse, dict):
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
        if not isinstance(other, IssueInvoiceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other