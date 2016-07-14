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


class UpdateProfileRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, account_id=None, organization_id=None, email=None, first_name=None, last_name=None, company_name=None, logo_url=None, addresses=None, mobile=None, landline=None, fax=None, dob=None, vat_number=None, additional_information=None):
        """
        UpdateProfileRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'account_id': 'str',
            'organization_id': 'str',
            'email': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'company_name': 'str',
            'logo_url': 'str',
            'addresses': 'list[Address]',
            'mobile': 'str',
            'landline': 'str',
            'fax': 'str',
            'dob': 'datetime',
            'vat_number': 'str',
            'additional_information': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'account_id': 'accountID',
            'organization_id': 'organizationID',
            'email': 'email',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'company_name': 'companyName',
            'logo_url': 'logoURL',
            'addresses': 'addresses',
            'mobile': 'mobile',
            'landline': 'landline',
            'fax': 'fax',
            'dob': 'dob',
            'vat_number': 'vatNumber',
            'additional_information': 'additionalInformation'
        }

        self._id = id
        self._account_id = account_id
        self._organization_id = organization_id
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._company_name = company_name
        self._logo_url = logo_url
        self._addresses = addresses
        self._mobile = mobile
        self._landline = landline
        self._fax = fax
        self._dob = dob
        self._vat_number = vat_number
        self._additional_information = additional_information

    @property
    def id(self):
        """
        Gets the id of this UpdateProfileRequest.


        :return: The id of this UpdateProfileRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UpdateProfileRequest.


        :param id: The id of this UpdateProfileRequest.
        :type: str
        """

        self._id = id

    @property
    def account_id(self):
        """
        Gets the account_id of this UpdateProfileRequest.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The account_id of this UpdateProfileRequest.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this UpdateProfileRequest.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param account_id: The account_id of this UpdateProfileRequest.
        :type: str
        """

        self._account_id = account_id

    @property
    def organization_id(self):
        """
        Gets the organization_id of this UpdateProfileRequest.
        { \"description\" : \"\", \"verbs\":[] }

        :return: The organization_id of this UpdateProfileRequest.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this UpdateProfileRequest.
        { \"description\" : \"\", \"verbs\":[] }

        :param organization_id: The organization_id of this UpdateProfileRequest.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def email(self):
        """
        Gets the email of this UpdateProfileRequest.
        { \"description\" : \"E-mail address\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The email of this UpdateProfileRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UpdateProfileRequest.
        { \"description\" : \"E-mail address\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param email: The email of this UpdateProfileRequest.
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this UpdateProfileRequest.
        { \"description\" : \"\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The first_name of this UpdateProfileRequest.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this UpdateProfileRequest.
        { \"description\" : \"\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param first_name: The first_name of this UpdateProfileRequest.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this UpdateProfileRequest.
        { \"description\" : \"\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The last_name of this UpdateProfileRequest.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this UpdateProfileRequest.
        { \"description\" : \"\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param last_name: The last_name of this UpdateProfileRequest.
        :type: str
        """

        self._last_name = last_name

    @property
    def company_name(self):
        """
        Gets the company_name of this UpdateProfileRequest.
        { \"description\" : \"\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The company_name of this UpdateProfileRequest.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this UpdateProfileRequest.
        { \"description\" : \"\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param company_name: The company_name of this UpdateProfileRequest.
        :type: str
        """

        self._company_name = company_name

    @property
    def logo_url(self):
        """
        Gets the logo_url of this UpdateProfileRequest.
        { \"description\" : \"\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The logo_url of this UpdateProfileRequest.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """
        Sets the logo_url of this UpdateProfileRequest.
        { \"description\" : \"\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param logo_url: The logo_url of this UpdateProfileRequest.
        :type: str
        """

        self._logo_url = logo_url

    @property
    def addresses(self):
        """
        Gets the addresses of this UpdateProfileRequest.
        { \"description\" : \"Address associated with the profile\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The addresses of this UpdateProfileRequest.
        :rtype: list[Address]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this UpdateProfileRequest.
        { \"description\" : \"Address associated with the profile\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param addresses: The addresses of this UpdateProfileRequest.
        :type: list[Address]
        """

        self._addresses = addresses

    @property
    def mobile(self):
        """
        Gets the mobile of this UpdateProfileRequest.
        { \"description\" : \"Mobile telephone number\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The mobile of this UpdateProfileRequest.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """
        Sets the mobile of this UpdateProfileRequest.
        { \"description\" : \"Mobile telephone number\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param mobile: The mobile of this UpdateProfileRequest.
        :type: str
        """

        self._mobile = mobile

    @property
    def landline(self):
        """
        Gets the landline of this UpdateProfileRequest.
        { \"description\" : \"Home telephone number\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The landline of this UpdateProfileRequest.
        :rtype: str
        """
        return self._landline

    @landline.setter
    def landline(self, landline):
        """
        Sets the landline of this UpdateProfileRequest.
        { \"description\" : \"Home telephone number\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param landline: The landline of this UpdateProfileRequest.
        :type: str
        """

        self._landline = landline

    @property
    def fax(self):
        """
        Gets the fax of this UpdateProfileRequest.
        { \"description\" : \"Fax number\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The fax of this UpdateProfileRequest.
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """
        Sets the fax of this UpdateProfileRequest.
        { \"description\" : \"Fax number\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param fax: The fax of this UpdateProfileRequest.
        :type: str
        """

        self._fax = fax

    @property
    def dob(self):
        """
        Gets the dob of this UpdateProfileRequest.
        { \"description\" : \"Date of birth in YYYY-MM-DD format\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The dob of this UpdateProfileRequest.
        :rtype: datetime
        """
        return self._dob

    @dob.setter
    def dob(self, dob):
        """
        Sets the dob of this UpdateProfileRequest.
        { \"description\" : \"Date of birth in YYYY-MM-DD format\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param dob: The dob of this UpdateProfileRequest.
        :type: datetime
        """

        self._dob = dob

    @property
    def vat_number(self):
        """
        Gets the vat_number of this UpdateProfileRequest.
        { \"description\" : \"VAT number\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The vat_number of this UpdateProfileRequest.
        :rtype: str
        """
        return self._vat_number

    @vat_number.setter
    def vat_number(self, vat_number):
        """
        Sets the vat_number of this UpdateProfileRequest.
        { \"description\" : \"VAT number\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param vat_number: The vat_number of this UpdateProfileRequest.
        :type: str
        """

        self._vat_number = vat_number

    @property
    def additional_information(self):
        """
        Gets the additional_information of this UpdateProfileRequest.
        { \"description\" : \"Any additional information\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The additional_information of this UpdateProfileRequest.
        :rtype: str
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """
        Sets the additional_information of this UpdateProfileRequest.
        { \"description\" : \"Any additional information\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param additional_information: The additional_information of this UpdateProfileRequest.
        :type: str
        """

        self._additional_information = additional_information

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
