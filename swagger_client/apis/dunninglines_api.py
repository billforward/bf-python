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

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DunninglinesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_dunning_line(self, dunning_line, **kwargs):
        """
        Create a dunning-line.
        {\"nickname\":\"Create a new dunning line\",\"request\":\"createDunningLineRequest.html\",\"response\":\"createDunningLineResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_dunning_line(dunning_line, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DunningLine dunning_line: The Dunning-Line object to be updated. (required)
        :return: DunningLinePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_dunning_line_with_http_info(dunning_line, **kwargs)
        else:
            (data) = self.create_dunning_line_with_http_info(dunning_line, **kwargs)
            return data

    def create_dunning_line_with_http_info(self, dunning_line, **kwargs):
        """
        Create a dunning-line.
        {\"nickname\":\"Create a new dunning line\",\"request\":\"createDunningLineRequest.html\",\"response\":\"createDunningLineResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_dunning_line_with_http_info(dunning_line, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DunningLine dunning_line: The Dunning-Line object to be updated. (required)
        :return: DunningLinePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dunning_line']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_dunning_line" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dunning_line' is set
        if ('dunning_line' not in params) or (params['dunning_line'] is None):
            raise ValueError("Missing the required parameter `dunning_line` when calling `create_dunning_line`")

        resource_path = '/dunning-lines'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'dunning_line' in params:
            body_params = params['dunning_line']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/xml', 'application/xml', 'application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DunningLinePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_all_dunning_lines(self, **kwargs):
        """
        Returns a collection of all dunning-lines. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Get all dunning lines\",\"response\":\"getDunningLineByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_dunning_lines(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first invoice to return.
        :param int records: The maximum number of invoices to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: DunningLinePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_dunning_lines_with_http_info(**kwargs)
        else:
            (data) = self.get_all_dunning_lines_with_http_info(**kwargs)
            return data

    def get_all_dunning_lines_with_http_info(self, **kwargs):
        """
        Returns a collection of all dunning-lines. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Get all dunning lines\",\"response\":\"getDunningLineByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_dunning_lines_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first invoice to return.
        :param int records: The maximum number of invoices to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: DunningLinePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organizations', 'offset', 'records', 'order_by', 'order', 'include_retired']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_dunning_lines" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/dunning-lines'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'organizations' in params:
            query_params['organizations'] = params['organizations']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'records' in params:
            query_params['records'] = params['records']
        if 'order_by' in params:
            query_params['order_by'] = params['order_by']
        if 'order' in params:
            query_params['order'] = params['order']
        if 'include_retired' in params:
            query_params['include_retired'] = params['include_retired']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DunningLinePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_dunning_line_by_attempt_index(self, index, **kwargs):
        """
        Returns a collection of dunning-lines specified by the index parameter. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Retrieve by attempt\",\"response\":\"getDunningLineByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_dunning_line_by_attempt_index(index, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int index: The attempt index of the dunning-line. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first invoice to return.
        :param int records: The maximum number of invoices to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: DunningLinePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_dunning_line_by_attempt_index_with_http_info(index, **kwargs)
        else:
            (data) = self.get_dunning_line_by_attempt_index_with_http_info(index, **kwargs)
            return data

    def get_dunning_line_by_attempt_index_with_http_info(self, index, **kwargs):
        """
        Returns a collection of dunning-lines specified by the index parameter. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Retrieve by attempt\",\"response\":\"getDunningLineByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_dunning_line_by_attempt_index_with_http_info(index, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int index: The attempt index of the dunning-line. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first invoice to return.
        :param int records: The maximum number of invoices to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: DunningLinePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['index', 'organizations', 'offset', 'records', 'order_by', 'order', 'include_retired']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dunning_line_by_attempt_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'index' is set
        if ('index' not in params) or (params['index'] is None):
            raise ValueError("Missing the required parameter `index` when calling `get_dunning_line_by_attempt_index`")

        resource_path = '/dunning-lines/attempt-index/{index}'.replace('{format}', 'json')
        path_params = {}
        if 'index' in params:
            path_params['index'] = params['index']

        query_params = {}
        if 'organizations' in params:
            query_params['organizations'] = params['organizations']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'records' in params:
            query_params['records'] = params['records']
        if 'order_by' in params:
            query_params['order_by'] = params['order_by']
        if 'order' in params:
            query_params['order'] = params['order']
        if 'include_retired' in params:
            query_params['include_retired'] = params['include_retired']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DunningLinePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_dunning_line_by_id(self, dunning_line_id, **kwargs):
        """
        Returns a single dunning-line, specified by the dunning-line-ID parameter.
        {\"nickname\":\"Retrieve an existing dunning line\",\"response\":\"getDunningLineByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_dunning_line_by_id(dunning_line_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str dunning_line_id: ID of the dunning-line. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: DunningLinePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_dunning_line_by_id_with_http_info(dunning_line_id, **kwargs)
        else:
            (data) = self.get_dunning_line_by_id_with_http_info(dunning_line_id, **kwargs)
            return data

    def get_dunning_line_by_id_with_http_info(self, dunning_line_id, **kwargs):
        """
        Returns a single dunning-line, specified by the dunning-line-ID parameter.
        {\"nickname\":\"Retrieve an existing dunning line\",\"response\":\"getDunningLineByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_dunning_line_by_id_with_http_info(dunning_line_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str dunning_line_id: ID of the dunning-line. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: DunningLinePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dunning_line_id', 'organizations']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dunning_line_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dunning_line_id' is set
        if ('dunning_line_id' not in params) or (params['dunning_line_id'] is None):
            raise ValueError("Missing the required parameter `dunning_line_id` when calling `get_dunning_line_by_id`")

        resource_path = '/dunning-lines/{dunning-line-ID}'.replace('{format}', 'json')
        path_params = {}
        if 'dunning_line_id' in params:
            path_params['dunning-line-ID'] = params['dunning_line_id']

        query_params = {}
        if 'organizations' in params:
            query_params['organizations'] = params['organizations']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['text/plain'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DunningLinePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def retire_dunning_line(self, dunning_line_id, organizations, **kwargs):
        """
        Retires the specified dunning-line.
        {\"nickname\":\"Delete a dunning line\",\"response\":\"deleteDunningLine.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.retire_dunning_line(dunning_line_id, organizations, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str dunning_line_id: ID of the dunning-line. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls. (required)
        :return: DunningLinePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.retire_dunning_line_with_http_info(dunning_line_id, organizations, **kwargs)
        else:
            (data) = self.retire_dunning_line_with_http_info(dunning_line_id, organizations, **kwargs)
            return data

    def retire_dunning_line_with_http_info(self, dunning_line_id, organizations, **kwargs):
        """
        Retires the specified dunning-line.
        {\"nickname\":\"Delete a dunning line\",\"response\":\"deleteDunningLine.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.retire_dunning_line_with_http_info(dunning_line_id, organizations, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str dunning_line_id: ID of the dunning-line. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls. (required)
        :return: DunningLinePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dunning_line_id', 'organizations']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retire_dunning_line" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dunning_line_id' is set
        if ('dunning_line_id' not in params) or (params['dunning_line_id'] is None):
            raise ValueError("Missing the required parameter `dunning_line_id` when calling `retire_dunning_line`")
        # verify the required parameter 'organizations' is set
        if ('organizations' not in params) or (params['organizations'] is None):
            raise ValueError("Missing the required parameter `organizations` when calling `retire_dunning_line`")

        resource_path = '/dunning-lines/{dunning-line-ID}'.replace('{format}', 'json')
        path_params = {}
        if 'dunning_line_id' in params:
            path_params['dunning-line-ID'] = params['dunning_line_id']

        query_params = {}
        if 'organizations' in params:
            query_params['organizations'] = params['organizations']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['text/plain'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DunningLinePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def update_dunning_line(self, dunning_line, **kwargs):
        """
        Update a dunning-line.
        {\"nickname\":\"Update a dunning line\",\"request\":\"updateDunningLineRequest.html\",\"response\":\"updateDunningLineResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_dunning_line(dunning_line, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DunningLine dunning_line: The Dunning-Line object to be updated. (required)
        :return: DunningLinePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_dunning_line_with_http_info(dunning_line, **kwargs)
        else:
            (data) = self.update_dunning_line_with_http_info(dunning_line, **kwargs)
            return data

    def update_dunning_line_with_http_info(self, dunning_line, **kwargs):
        """
        Update a dunning-line.
        {\"nickname\":\"Update a dunning line\",\"request\":\"updateDunningLineRequest.html\",\"response\":\"updateDunningLineResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_dunning_line_with_http_info(dunning_line, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DunningLine dunning_line: The Dunning-Line object to be updated. (required)
        :return: DunningLinePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dunning_line']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dunning_line" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dunning_line' is set
        if ('dunning_line' not in params) or (params['dunning_line'] is None):
            raise ValueError("Missing the required parameter `dunning_line` when calling `update_dunning_line`")

        resource_path = '/dunning-lines'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'dunning_line' in params:
            body_params = params['dunning_line']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/xml', 'application/xml', 'application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DunningLinePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
