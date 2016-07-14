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


class EmailprovidersApi(object):
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

    def create_email_provider(self, request, **kwargs):
        """
        Create an email provider.
        {\"nickname\":\"Create an email provider\",\"request\":\"createEmailProviderRequest.html\",\"response\":\"creatEmailProviderResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_email_provider(request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BillingEntityBase request: . (required)
        :return: EmailProviderPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_email_provider_with_http_info(request, **kwargs)
        else:
            (data) = self.create_email_provider_with_http_info(request, **kwargs)
            return data

    def create_email_provider_with_http_info(self, request, **kwargs):
        """
        Create an email provider.
        {\"nickname\":\"Create an email provider\",\"request\":\"createEmailProviderRequest.html\",\"response\":\"creatEmailProviderResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_email_provider_with_http_info(request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BillingEntityBase request: . (required)
        :return: EmailProviderPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_email_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params) or (params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `create_email_provider`")

        resource_path = '/email-providers'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']

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
                                            response_type='EmailProviderPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def delete(self, email_provider_id, **kwargs):
        """
        Deletes a single email provider, specified by id or name parameter.
        { \"nickname\" : \"delete\",\"response\" : \"deleteEmailProvider.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete(email_provider_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str email_provider_id:  (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: EmailProviderPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(email_provider_id, **kwargs)
        else:
            (data) = self.delete_with_http_info(email_provider_id, **kwargs)
            return data

    def delete_with_http_info(self, email_provider_id, **kwargs):
        """
        Deletes a single email provider, specified by id or name parameter.
        { \"nickname\" : \"delete\",\"response\" : \"deleteEmailProvider.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_with_http_info(email_provider_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str email_provider_id:  (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: EmailProviderPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email_provider_id', 'organizations']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email_provider_id' is set
        if ('email_provider_id' not in params) or (params['email_provider_id'] is None):
            raise ValueError("Missing the required parameter `email_provider_id` when calling `delete`")

        resource_path = '/email-providers/{email-provider-ID}'.replace('{format}', 'json')
        path_params = {}
        if 'email_provider_id' in params:
            path_params['email-provider-ID'] = params['email_provider_id']

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
                                            response_type='EmailProviderPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_all_email_providers(self, **kwargs):
        """
        Returns a collection of all email-providers. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Get all email providers\",\"response\":\"getEmailProvidersAll.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_email_providers(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first email-provider to return.
        :param int records: The maximum number of email-provider to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Include deleted email-providers
        :return: EmailProviderPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_email_providers_with_http_info(**kwargs)
        else:
            (data) = self.get_all_email_providers_with_http_info(**kwargs)
            return data

    def get_all_email_providers_with_http_info(self, **kwargs):
        """
        Returns a collection of all email-providers. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Get all email providers\",\"response\":\"getEmailProvidersAll.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_email_providers_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first email-provider to return.
        :param int records: The maximum number of email-provider to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Include deleted email-providers
        :return: EmailProviderPagedMetadata
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
                    " to method get_all_email_providers" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/email-providers'.replace('{format}', 'json')
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
                                            response_type='EmailProviderPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_email_by_provider_id(self, email_provider_id, **kwargs):
        """
        Retrieves a single email provider, specified by the version-ID parameter.
        { \"nickname\" : \"Retrieve by version\",\"response\" : \"getEmailProviderByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_email_by_provider_id(email_provider_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str email_provider_id:  (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param bool include_retired: Include deleted email-providers
        :return: EmailProviderPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_email_by_provider_id_with_http_info(email_provider_id, **kwargs)
        else:
            (data) = self.get_email_by_provider_id_with_http_info(email_provider_id, **kwargs)
            return data

    def get_email_by_provider_id_with_http_info(self, email_provider_id, **kwargs):
        """
        Retrieves a single email provider, specified by the version-ID parameter.
        { \"nickname\" : \"Retrieve by version\",\"response\" : \"getEmailProviderByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_email_by_provider_id_with_http_info(email_provider_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str email_provider_id:  (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param bool include_retired: Include deleted email-providers
        :return: EmailProviderPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email_provider_id', 'organizations', 'include_retired']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_email_by_provider_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email_provider_id' is set
        if ('email_provider_id' not in params) or (params['email_provider_id'] is None):
            raise ValueError("Missing the required parameter `email_provider_id` when calling `get_email_by_provider_id`")

        resource_path = '/email-providers/{email-provider-ID}'.replace('{format}', 'json')
        path_params = {}
        if 'email_provider_id' in params:
            path_params['email-provider-ID'] = params['email_provider_id']

        query_params = {}
        if 'organizations' in params:
            query_params['organizations'] = params['organizations']
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
                                            response_type='EmailProviderPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
