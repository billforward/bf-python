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


class UnitofmeasureApi(object):
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

    def create_unit_of_measure(self, unit_of_measure, **kwargs):
        """
        Create a unit-of-measure.
        {\"nickname\":\"Create a new unit of measure\",\"request\":\"createUnitOfMeasureRequest.html\",\"response\":\"createUnitOfMeasureResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_unit_of_measure(unit_of_measure, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UnitOfMeasure unit_of_measure: The unit-of-measure object to be created. (required)
        :return: UnitOfMeasurePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_unit_of_measure_with_http_info(unit_of_measure, **kwargs)
        else:
            (data) = self.create_unit_of_measure_with_http_info(unit_of_measure, **kwargs)
            return data

    def create_unit_of_measure_with_http_info(self, unit_of_measure, **kwargs):
        """
        Create a unit-of-measure.
        {\"nickname\":\"Create a new unit of measure\",\"request\":\"createUnitOfMeasureRequest.html\",\"response\":\"createUnitOfMeasureResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_unit_of_measure_with_http_info(unit_of_measure, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UnitOfMeasure unit_of_measure: The unit-of-measure object to be created. (required)
        :return: UnitOfMeasurePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['unit_of_measure']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_unit_of_measure" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'unit_of_measure' is set
        if ('unit_of_measure' not in params) or (params['unit_of_measure'] is None):
            raise ValueError("Missing the required parameter `unit_of_measure` when calling `create_unit_of_measure`")

        resource_path = '/units-of-measure'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'unit_of_measure' in params:
            body_params = params['unit_of_measure']

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
                                            response_type='UnitOfMeasurePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_all_units_of_measure(self, **kwargs):
        """
        Returns a collection of all unit-of-measure objects. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Get all units of measure\",\"response\":\"getUnitOfMeasureAll.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_units_of_measure(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first taxation-link to return.
        :param int records: The maximum number of taxation-links to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: UnitOfMeasurePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_units_of_measure_with_http_info(**kwargs)
        else:
            (data) = self.get_all_units_of_measure_with_http_info(**kwargs)
            return data

    def get_all_units_of_measure_with_http_info(self, **kwargs):
        """
        Returns a collection of all unit-of-measure objects. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Get all units of measure\",\"response\":\"getUnitOfMeasureAll.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_units_of_measure_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first taxation-link to return.
        :param int records: The maximum number of taxation-links to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: UnitOfMeasurePagedMetadata
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
                    " to method get_all_units_of_measure" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/units-of-measure'.replace('{format}', 'json')
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
                                            response_type='UnitOfMeasurePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_unit_of_measure_by_id(self, unit_of_measure_identifier, **kwargs):
        """
        Returns a single unit-of-measure corresponding to the unique id or name specified.
        {\"nickname\":\"Retrieve an existing unit of measure\",\"response\":\"getUnitOfMeasureByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_unit_of_measure_by_id(unit_of_measure_identifier, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str unit_of_measure_identifier: The unique id or name of the unit-of-measure. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: UnitOfMeasurePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_unit_of_measure_by_id_with_http_info(unit_of_measure_identifier, **kwargs)
        else:
            (data) = self.get_unit_of_measure_by_id_with_http_info(unit_of_measure_identifier, **kwargs)
            return data

    def get_unit_of_measure_by_id_with_http_info(self, unit_of_measure_identifier, **kwargs):
        """
        Returns a single unit-of-measure corresponding to the unique id or name specified.
        {\"nickname\":\"Retrieve an existing unit of measure\",\"response\":\"getUnitOfMeasureByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_unit_of_measure_by_id_with_http_info(unit_of_measure_identifier, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str unit_of_measure_identifier: The unique id or name of the unit-of-measure. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: UnitOfMeasurePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['unit_of_measure_identifier', 'organizations']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_unit_of_measure_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'unit_of_measure_identifier' is set
        if ('unit_of_measure_identifier' not in params) or (params['unit_of_measure_identifier'] is None):
            raise ValueError("Missing the required parameter `unit_of_measure_identifier` when calling `get_unit_of_measure_by_id`")

        resource_path = '/units-of-measure/{unit-of-measure-identifier}'.replace('{format}', 'json')
        path_params = {}
        if 'unit_of_measure_identifier' in params:
            path_params['unit-of-measure-identifier'] = params['unit_of_measure_identifier']

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

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='UnitOfMeasurePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def update_unit_of_measure(self, unit_of_measure, **kwargs):
        """
        Update a unit-of-measure.
        {\"nickname\":\"Update a unit of measure\",\"request\":\"updateUnitOfMeasureRequest.html\",\"response\":\"updateUnitOfMeasureResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_unit_of_measure(unit_of_measure, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UnitOfMeasure unit_of_measure: The unit-of-measure object to be updated. (required)
        :return: UnitOfMeasurePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_unit_of_measure_with_http_info(unit_of_measure, **kwargs)
        else:
            (data) = self.update_unit_of_measure_with_http_info(unit_of_measure, **kwargs)
            return data

    def update_unit_of_measure_with_http_info(self, unit_of_measure, **kwargs):
        """
        Update a unit-of-measure.
        {\"nickname\":\"Update a unit of measure\",\"request\":\"updateUnitOfMeasureRequest.html\",\"response\":\"updateUnitOfMeasureResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_unit_of_measure_with_http_info(unit_of_measure, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UnitOfMeasure unit_of_measure: The unit-of-measure object to be updated. (required)
        :return: UnitOfMeasurePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['unit_of_measure']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_unit_of_measure" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'unit_of_measure' is set
        if ('unit_of_measure' not in params) or (params['unit_of_measure'] is None):
            raise ValueError("Missing the required parameter `unit_of_measure` when calling `update_unit_of_measure`")

        resource_path = '/units-of-measure'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'unit_of_measure' in params:
            body_params = params['unit_of_measure']

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
                                            response_type='UnitOfMeasurePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
