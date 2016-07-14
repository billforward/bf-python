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


class UsagesessionsApi(object):
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

    def get_active_sessions_for_subscription(self, subscription_id, **kwargs):
        """
        Get active by subscription
        {\"nickname\":\"Get active by subscription\",\"response\":\"getActiveSessions.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_active_sessions_for_subscription(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str subscription_id: The subscriptionID of the subscription whose active sessions you wish to GET. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first amendment to return.
        :param int records: The maximum number of amendments to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: The direction of any ordering, either ASC or DESC.
        :return: UsageSessionPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_active_sessions_for_subscription_with_http_info(subscription_id, **kwargs)
        else:
            (data) = self.get_active_sessions_for_subscription_with_http_info(subscription_id, **kwargs)
            return data

    def get_active_sessions_for_subscription_with_http_info(self, subscription_id, **kwargs):
        """
        Get active by subscription
        {\"nickname\":\"Get active by subscription\",\"response\":\"getActiveSessions.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_active_sessions_for_subscription_with_http_info(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str subscription_id: The subscriptionID of the subscription whose active sessions you wish to GET. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first amendment to return.
        :param int records: The maximum number of amendments to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: The direction of any ordering, either ASC or DESC.
        :return: UsageSessionPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id', 'organizations', 'offset', 'records', 'order_by', 'order']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_active_sessions_for_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params) or (params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `get_active_sessions_for_subscription`")

        resource_path = '/usage-sessions/{subscription-id}/active'.replace('{format}', 'json')
        path_params = {}
        if 'subscription_id' in params:
            path_params['subscription-id'] = params['subscription_id']

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
                                            response_type='UsageSessionPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_usage_list_for_usage_session(self, subscription_id, **kwargs):
        """
        Retrieve by subscription
        {\"nickname\":\"Retrieve by subscription\",\"response\":\"getAllSessions.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_usage_list_for_usage_session(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str subscription_id: The subscriptionID of the subscription whose sessions you wish to GET. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first amendment to return.
        :param int records: The maximum number of amendments to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: The direction of any ordering, either ASC or DESC.
        :return: UsageSessionPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_usage_list_for_usage_session_with_http_info(subscription_id, **kwargs)
        else:
            (data) = self.get_usage_list_for_usage_session_with_http_info(subscription_id, **kwargs)
            return data

    def get_usage_list_for_usage_session_with_http_info(self, subscription_id, **kwargs):
        """
        Retrieve by subscription
        {\"nickname\":\"Retrieve by subscription\",\"response\":\"getAllSessions.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_usage_list_for_usage_session_with_http_info(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str subscription_id: The subscriptionID of the subscription whose sessions you wish to GET. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first amendment to return.
        :param int records: The maximum number of amendments to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: The direction of any ordering, either ASC or DESC.
        :return: UsageSessionPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id', 'organizations', 'offset', 'records', 'order_by', 'order']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_usage_list_for_usage_session" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params) or (params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `get_usage_list_for_usage_session`")

        resource_path = '/usage-sessions/{subscription-id}'.replace('{format}', 'json')
        path_params = {}
        if 'subscription_id' in params:
            path_params['subscription-id'] = params['subscription_id']

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
                                            response_type='UsageSessionPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def start_usage_session(self, usage_sessions, **kwargs):
        """
        Start a new session
        {\"nickname\":\"Start a new session\",\"request\":\"createStartUsageSessionRequest.html\",\"response\":\"createStartUsageSessionResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.start_usage_session(usage_sessions, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CompoundUsageSession usage_sessions: An array of 'Usage Session' objects whose sessions you wish to start. (required)
        :return: UsageSessionPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.start_usage_session_with_http_info(usage_sessions, **kwargs)
        else:
            (data) = self.start_usage_session_with_http_info(usage_sessions, **kwargs)
            return data

    def start_usage_session_with_http_info(self, usage_sessions, **kwargs):
        """
        Start a new session
        {\"nickname\":\"Start a new session\",\"request\":\"createStartUsageSessionRequest.html\",\"response\":\"createStartUsageSessionResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.start_usage_session_with_http_info(usage_sessions, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CompoundUsageSession usage_sessions: An array of 'Usage Session' objects whose sessions you wish to start. (required)
        :return: UsageSessionPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['usage_sessions']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_usage_session" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'usage_sessions' is set
        if ('usage_sessions' not in params) or (params['usage_sessions'] is None):
            raise ValueError("Missing the required parameter `usage_sessions` when calling `start_usage_session`")

        resource_path = '/usage-sessions/start'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'usage_sessions' in params:
            body_params = params['usage_sessions']

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
                                            response_type='UsageSessionPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def stop_usage_session(self, usage_sessions, **kwargs):
        """
        Stop a specified session
        {\"nickname\":\"Stop a specified session\",\"request\":\"createStopUsageSessionRequest.html\",\"response\":\"createStopUsageSessionResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.stop_usage_session(usage_sessions, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CompoundUsageSession usage_sessions: An array of 'Usage Session' objects whose sessions you wish to stop. (required)
        :return: UsageSessionPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.stop_usage_session_with_http_info(usage_sessions, **kwargs)
        else:
            (data) = self.stop_usage_session_with_http_info(usage_sessions, **kwargs)
            return data

    def stop_usage_session_with_http_info(self, usage_sessions, **kwargs):
        """
        Stop a specified session
        {\"nickname\":\"Stop a specified session\",\"request\":\"createStopUsageSessionRequest.html\",\"response\":\"createStopUsageSessionResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.stop_usage_session_with_http_info(usage_sessions, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CompoundUsageSession usage_sessions: An array of 'Usage Session' objects whose sessions you wish to stop. (required)
        :return: UsageSessionPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['usage_sessions']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_usage_session" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'usage_sessions' is set
        if ('usage_sessions' not in params) or (params['usage_sessions'] is None):
            raise ValueError("Missing the required parameter `usage_sessions` when calling `stop_usage_session`")

        resource_path = '/usage-sessions/stop'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'usage_sessions' in params:
            body_params = params['usage_sessions']

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
                                            response_type='UsageSessionPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
