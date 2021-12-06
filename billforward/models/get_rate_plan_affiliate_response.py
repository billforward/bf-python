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

class GetRatePlanAffiliateResponse(object):
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
        'product_rate_plan_id': 'str',
        'account_id': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'commission_structure': 'CommissionStructure'
    }

    attribute_map = {
        'created': 'created',
        'organization_id': 'organizationID',
        'id': 'id',
        'product_rate_plan_id': 'productRatePlanID',
        'account_id': 'accountID',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'commission_structure': 'commissionStructure'
    }

    def __init__(self, created=None, organization_id=None, id=None, product_rate_plan_id=None, account_id=None, start_date=None, end_date=None, commission_structure=None):  # noqa: E501
        """GetRatePlanAffiliateResponse - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._organization_id = None
        self._id = None
        self._product_rate_plan_id = None
        self._account_id = None
        self._start_date = None
        self._end_date = None
        self._commission_structure = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if organization_id is not None:
            self.organization_id = organization_id
        if id is not None:
            self.id = id
        if product_rate_plan_id is not None:
            self.product_rate_plan_id = product_rate_plan_id
        if account_id is not None:
            self.account_id = account_id
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if commission_structure is not None:
            self.commission_structure = commission_structure

    @property
    def created(self):
        """Gets the created of this GetRatePlanAffiliateResponse.  # noqa: E501


        :return: The created of this GetRatePlanAffiliateResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GetRatePlanAffiliateResponse.


        :param created: The created of this GetRatePlanAffiliateResponse.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def organization_id(self):
        """Gets the organization_id of this GetRatePlanAffiliateResponse.  # noqa: E501


        :return: The organization_id of this GetRatePlanAffiliateResponse.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this GetRatePlanAffiliateResponse.


        :param organization_id: The organization_id of this GetRatePlanAffiliateResponse.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def id(self):
        """Gets the id of this GetRatePlanAffiliateResponse.  # noqa: E501


        :return: The id of this GetRatePlanAffiliateResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetRatePlanAffiliateResponse.


        :param id: The id of this GetRatePlanAffiliateResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def product_rate_plan_id(self):
        """Gets the product_rate_plan_id of this GetRatePlanAffiliateResponse.  # noqa: E501


        :return: The product_rate_plan_id of this GetRatePlanAffiliateResponse.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_id

    @product_rate_plan_id.setter
    def product_rate_plan_id(self, product_rate_plan_id):
        """Sets the product_rate_plan_id of this GetRatePlanAffiliateResponse.


        :param product_rate_plan_id: The product_rate_plan_id of this GetRatePlanAffiliateResponse.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_id = product_rate_plan_id

    @property
    def account_id(self):
        """Gets the account_id of this GetRatePlanAffiliateResponse.  # noqa: E501


        :return: The account_id of this GetRatePlanAffiliateResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GetRatePlanAffiliateResponse.


        :param account_id: The account_id of this GetRatePlanAffiliateResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def start_date(self):
        """Gets the start_date of this GetRatePlanAffiliateResponse.  # noqa: E501


        :return: The start_date of this GetRatePlanAffiliateResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this GetRatePlanAffiliateResponse.


        :param start_date: The start_date of this GetRatePlanAffiliateResponse.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this GetRatePlanAffiliateResponse.  # noqa: E501


        :return: The end_date of this GetRatePlanAffiliateResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this GetRatePlanAffiliateResponse.


        :param end_date: The end_date of this GetRatePlanAffiliateResponse.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def commission_structure(self):
        """Gets the commission_structure of this GetRatePlanAffiliateResponse.  # noqa: E501


        :return: The commission_structure of this GetRatePlanAffiliateResponse.  # noqa: E501
        :rtype: CommissionStructure
        """
        return self._commission_structure

    @commission_structure.setter
    def commission_structure(self, commission_structure):
        """Sets the commission_structure of this GetRatePlanAffiliateResponse.


        :param commission_structure: The commission_structure of this GetRatePlanAffiliateResponse.  # noqa: E501
        :type: CommissionStructure
        """

        self._commission_structure = commission_structure

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
        if issubclass(GetRatePlanAffiliateResponse, dict):
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
        if not isinstance(other, GetRatePlanAffiliateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
