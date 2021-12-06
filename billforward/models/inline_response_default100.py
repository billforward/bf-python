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

class InlineResponseDefault100(object):
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
        'next_page': 'str',
        'current_page': 'int',
        'current_offset': 'int',
        'records_requested': 'int',
        'records_returned': 'int',
        'total_records': 'int',
        'execution_time': 'int',
        'results': 'list[StripeAchToken]'
    }

    attribute_map = {
        'next_page': 'nextPage',
        'current_page': 'currentPage',
        'current_offset': 'currentOffset',
        'records_requested': 'recordsRequested',
        'records_returned': 'recordsReturned',
        'total_records': 'totalRecords',
        'execution_time': 'executionTime',
        'results': 'results'
    }

    def __init__(self, next_page=None, current_page=None, current_offset=None, records_requested=None, records_returned=None, total_records=None, execution_time=None, results=None):  # noqa: E501
        """InlineResponseDefault100 - a model defined in Swagger"""  # noqa: E501
        self._next_page = None
        self._current_page = None
        self._current_offset = None
        self._records_requested = None
        self._records_returned = None
        self._total_records = None
        self._execution_time = None
        self._results = None
        self.discriminator = None
        if next_page is not None:
            self.next_page = next_page
        if current_page is not None:
            self.current_page = current_page
        if current_offset is not None:
            self.current_offset = current_offset
        if records_requested is not None:
            self.records_requested = records_requested
        if records_returned is not None:
            self.records_returned = records_returned
        if total_records is not None:
            self.total_records = total_records
        self.execution_time = execution_time
        self.results = results

    @property
    def next_page(self):
        """Gets the next_page of this InlineResponseDefault100.  # noqa: E501


        :return: The next_page of this InlineResponseDefault100.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this InlineResponseDefault100.


        :param next_page: The next_page of this InlineResponseDefault100.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    @property
    def current_page(self):
        """Gets the current_page of this InlineResponseDefault100.  # noqa: E501


        :return: The current_page of this InlineResponseDefault100.  # noqa: E501
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this InlineResponseDefault100.


        :param current_page: The current_page of this InlineResponseDefault100.  # noqa: E501
        :type: int
        """

        self._current_page = current_page

    @property
    def current_offset(self):
        """Gets the current_offset of this InlineResponseDefault100.  # noqa: E501


        :return: The current_offset of this InlineResponseDefault100.  # noqa: E501
        :rtype: int
        """
        return self._current_offset

    @current_offset.setter
    def current_offset(self, current_offset):
        """Sets the current_offset of this InlineResponseDefault100.


        :param current_offset: The current_offset of this InlineResponseDefault100.  # noqa: E501
        :type: int
        """

        self._current_offset = current_offset

    @property
    def records_requested(self):
        """Gets the records_requested of this InlineResponseDefault100.  # noqa: E501


        :return: The records_requested of this InlineResponseDefault100.  # noqa: E501
        :rtype: int
        """
        return self._records_requested

    @records_requested.setter
    def records_requested(self, records_requested):
        """Sets the records_requested of this InlineResponseDefault100.


        :param records_requested: The records_requested of this InlineResponseDefault100.  # noqa: E501
        :type: int
        """

        self._records_requested = records_requested

    @property
    def records_returned(self):
        """Gets the records_returned of this InlineResponseDefault100.  # noqa: E501


        :return: The records_returned of this InlineResponseDefault100.  # noqa: E501
        :rtype: int
        """
        return self._records_returned

    @records_returned.setter
    def records_returned(self, records_returned):
        """Sets the records_returned of this InlineResponseDefault100.


        :param records_returned: The records_returned of this InlineResponseDefault100.  # noqa: E501
        :type: int
        """

        self._records_returned = records_returned

    @property
    def total_records(self):
        """Gets the total_records of this InlineResponseDefault100.  # noqa: E501


        :return: The total_records of this InlineResponseDefault100.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this InlineResponseDefault100.


        :param total_records: The total_records of this InlineResponseDefault100.  # noqa: E501
        :type: int
        """

        self._total_records = total_records

    @property
    def execution_time(self):
        """Gets the execution_time of this InlineResponseDefault100.  # noqa: E501


        :return: The execution_time of this InlineResponseDefault100.  # noqa: E501
        :rtype: int
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """Sets the execution_time of this InlineResponseDefault100.


        :param execution_time: The execution_time of this InlineResponseDefault100.  # noqa: E501
        :type: int
        """
        if execution_time is None:
            raise ValueError("Invalid value for `execution_time`, must not be `None`")  # noqa: E501

        self._execution_time = execution_time

    @property
    def results(self):
        """Gets the results of this InlineResponseDefault100.  # noqa: E501


        :return: The results of this InlineResponseDefault100.  # noqa: E501
        :rtype: list[StripeAchToken]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this InlineResponseDefault100.


        :param results: The results of this InlineResponseDefault100.  # noqa: E501
        :type: list[StripeAchToken]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

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
        if issubclass(InlineResponseDefault100, dict):
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
        if not isinstance(other, InlineResponseDefault100):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
