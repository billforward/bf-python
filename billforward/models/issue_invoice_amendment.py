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
from billforward.models.amendment import Amendment  # noqa: F401,E501

class IssueInvoiceAmendment(Amendment):
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
        'invoice_id': 'str'
    }
    if hasattr(Amendment, "swagger_types"):
        swagger_types.update(Amendment.swagger_types)

    attribute_map = {
        'invoice_id': 'invoiceID'
    }
    if hasattr(Amendment, "attribute_map"):
        attribute_map.update(Amendment.attribute_map)

    def __init__(self, invoice_id=None, *args, **kwargs):  # noqa: E501
        """IssueInvoiceAmendment - a model defined in Swagger"""  # noqa: E501
        self._invoice_id = None
        self.discriminator = None
        self.invoice_id = invoice_id
        Amendment.__init__(self, *args, **kwargs)

    @property
    def invoice_id(self):
        """Gets the invoice_id of this IssueInvoiceAmendment.  # noqa: E501


        :return: The invoice_id of this IssueInvoiceAmendment.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this IssueInvoiceAmendment.


        :param invoice_id: The invoice_id of this IssueInvoiceAmendment.  # noqa: E501
        :type: str
        """
        if invoice_id is None:
            raise ValueError("Invalid value for `invoice_id`, must not be `None`")  # noqa: E501

        self._invoice_id = invoice_id

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
        if issubclass(IssueInvoiceAmendment, dict):
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
        if not isinstance(other, IssueInvoiceAmendment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
