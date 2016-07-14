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


class AmendmentPagedMetadata(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, next_page=None, current_page=None, current_offset=None, records_requested=None, records_returned=None, execution_time=None, results=None):
        """
        AmendmentPagedMetadata - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'next_page': 'str',
            'current_page': 'int',
            'current_offset': 'int',
            'records_requested': 'int',
            'records_returned': 'int',
            'execution_time': 'int',
            'results': 'list[Amendment]'
        }

        self.attribute_map = {
            'next_page': 'nextPage',
            'current_page': 'currentPage',
            'current_offset': 'currentOffset',
            'records_requested': 'recordsRequested',
            'records_returned': 'recordsReturned',
            'execution_time': 'executionTime',
            'results': 'results'
        }

        self._next_page = next_page
        self._current_page = current_page
        self._current_offset = current_offset
        self._records_requested = records_requested
        self._records_returned = records_returned
        self._execution_time = execution_time
        self._results = results

    @property
    def next_page(self):
        """
        Gets the next_page of this AmendmentPagedMetadata.
        {\"description\":\"Paging parameter. URL fragment that can be used to fetch next page of results.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :return: The next_page of this AmendmentPagedMetadata.
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """
        Sets the next_page of this AmendmentPagedMetadata.
        {\"description\":\"Paging parameter. URL fragment that can be used to fetch next page of results.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :param next_page: The next_page of this AmendmentPagedMetadata.
        :type: str
        """

        self._next_page = next_page

    @property
    def current_page(self):
        """
        Gets the current_page of this AmendmentPagedMetadata.
        {\"description\":\"Paging parameter. 0-indexed. Describes which page (given a page size of `recordsRequested`) of the result set you are viewing.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :return: The current_page of this AmendmentPagedMetadata.
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """
        Sets the current_page of this AmendmentPagedMetadata.
        {\"description\":\"Paging parameter. 0-indexed. Describes which page (given a page size of `recordsRequested`) of the result set you are viewing.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :param current_page: The current_page of this AmendmentPagedMetadata.
        :type: int
        """

        self._current_page = current_page

    @property
    def current_offset(self):
        """
        Gets the current_offset of this AmendmentPagedMetadata.
        {\"description\":\"Paging parameter. 0-indexed. Describes your current location within a pageable list of query results.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :return: The current_offset of this AmendmentPagedMetadata.
        :rtype: int
        """
        return self._current_offset

    @current_offset.setter
    def current_offset(self, current_offset):
        """
        Sets the current_offset of this AmendmentPagedMetadata.
        {\"description\":\"Paging parameter. 0-indexed. Describes your current location within a pageable list of query results.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :param current_offset: The current_offset of this AmendmentPagedMetadata.
        :type: int
        """

        self._current_offset = current_offset

    @property
    def records_requested(self):
        """
        Gets the records_requested of this AmendmentPagedMetadata.
        {\"default\":10,\"description\":\"Paging parameter. Describes how many records you requested.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :return: The records_requested of this AmendmentPagedMetadata.
        :rtype: int
        """
        return self._records_requested

    @records_requested.setter
    def records_requested(self, records_requested):
        """
        Sets the records_requested of this AmendmentPagedMetadata.
        {\"default\":10,\"description\":\"Paging parameter. Describes how many records you requested.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :param records_requested: The records_requested of this AmendmentPagedMetadata.
        :type: int
        """

        self._records_requested = records_requested

    @property
    def records_returned(self):
        """
        Gets the records_returned of this AmendmentPagedMetadata.
        {\"description\":\"Describes how many records were returned by your query.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :return: The records_returned of this AmendmentPagedMetadata.
        :rtype: int
        """
        return self._records_returned

    @records_returned.setter
    def records_returned(self, records_returned):
        """
        Sets the records_returned of this AmendmentPagedMetadata.
        {\"description\":\"Describes how many records were returned by your query.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :param records_returned: The records_returned of this AmendmentPagedMetadata.
        :type: int
        """

        self._records_returned = records_returned

    @property
    def execution_time(self):
        """
        Gets the execution_time of this AmendmentPagedMetadata.
        {\"description\":\"Number of milliseconds taken by API to calculate response.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :return: The execution_time of this AmendmentPagedMetadata.
        :rtype: int
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """
        Sets the execution_time of this AmendmentPagedMetadata.
        {\"description\":\"Number of milliseconds taken by API to calculate response.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :param execution_time: The execution_time of this AmendmentPagedMetadata.
        :type: int
        """

        self._execution_time = execution_time

    @property
    def results(self):
        """
        Gets the results of this AmendmentPagedMetadata.
        {\"description\":\"The results returned by your query.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :return: The results of this AmendmentPagedMetadata.
        :rtype: list[Amendment]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this AmendmentPagedMetadata.
        {\"description\":\"The results returned by your query.\",\"verbs\":[\"GET\",\"PUT\",\"POST\"]}

        :param results: The results of this AmendmentPagedMetadata.
        :type: list[Amendment]
        """

        self._results = results

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
