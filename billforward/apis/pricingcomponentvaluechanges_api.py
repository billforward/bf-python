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


class PricingcomponentvaluechangesApi(object):
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

    def create_pricing_component_value_change(self, pricing_component_value_change, **kwargs):
        """
        Create a pricing-component-value-change.
        {\"nickname\":\"Create\",\"request\":\"createPricingComponentValueChangeRequest.html\",\"response\":\"createPricingComponentValueChangeResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_pricing_component_value_change(pricing_component_value_change, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param InsertableBillingEntity pricing_component_value_change: The pricing-component-value-change object to be updated. (required)
        :return: PricingComponentValueChangePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_pricing_component_value_change_with_http_info(pricing_component_value_change, **kwargs)
        else:
            (data) = self.create_pricing_component_value_change_with_http_info(pricing_component_value_change, **kwargs)
            return data

    def create_pricing_component_value_change_with_http_info(self, pricing_component_value_change, **kwargs):
        """
        Create a pricing-component-value-change.
        {\"nickname\":\"Create\",\"request\":\"createPricingComponentValueChangeRequest.html\",\"response\":\"createPricingComponentValueChangeResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_pricing_component_value_change_with_http_info(pricing_component_value_change, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param InsertableBillingEntity pricing_component_value_change: The pricing-component-value-change object to be updated. (required)
        :return: PricingComponentValueChangePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pricing_component_value_change']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_pricing_component_value_change" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pricing_component_value_change' is set
        if ('pricing_component_value_change' not in params) or (params['pricing_component_value_change'] is None):
            raise ValueError("Missing the required parameter `pricing_component_value_change` when calling `create_pricing_component_value_change`")

        resource_path = '/pricing-component-value-changes'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'pricing_component_value_change' in params:
            body_params = params['pricing_component_value_change']

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
                                            response_type='PricingComponentValueChangePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_all_pricing_component_value_changes(self, **kwargs):
        """
        Returns a collection of pricing-component-value-changes. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Get All\",\"response\":\"getPricingComponentValueChangeAll.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_pricing_component_value_changes(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first pricing-component-value-change to return.
        :param int records: The maximum number of pricing-component-value-changes to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :return: PricingComponentValueChangePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_pricing_component_value_changes_with_http_info(**kwargs)
        else:
            (data) = self.get_all_pricing_component_value_changes_with_http_info(**kwargs)
            return data

    def get_all_pricing_component_value_changes_with_http_info(self, **kwargs):
        """
        Returns a collection of pricing-component-value-changes. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Get All\",\"response\":\"getPricingComponentValueChangeAll.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_pricing_component_value_changes_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first pricing-component-value-change to return.
        :param int records: The maximum number of pricing-component-value-changes to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :return: PricingComponentValueChangePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organizations', 'offset', 'records', 'order_by', 'order']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_pricing_component_value_changes" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/pricing-component-value-changes'.replace('{format}', 'json')
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
                                            response_type='PricingComponentValueChangePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_pricing_component_value_change(self, id, **kwargs):
        """
        Returns a single pricing-component-value-changes, specified by the ID parameter.
        {\"nickname\":\"Retrieve by id\",\"response\":\"getPricingComponentValueChangeByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_pricing_component_value_change(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The string ID of the pricing-component-value-change. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: PricingComponentValueChangePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_pricing_component_value_change_with_http_info(id, **kwargs)
        else:
            (data) = self.get_pricing_component_value_change_with_http_info(id, **kwargs)
            return data

    def get_pricing_component_value_change_with_http_info(self, id, **kwargs):
        """
        Returns a single pricing-component-value-changes, specified by the ID parameter.
        {\"nickname\":\"Retrieve by id\",\"response\":\"getPricingComponentValueChangeByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_pricing_component_value_change_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The string ID of the pricing-component-value-change. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: PricingComponentValueChangePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'organizations']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pricing_component_value_change" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_pricing_component_value_change`")

        resource_path = '/pricing-component-value-changes/{ID}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['ID'] = params['id']

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
                                            response_type='PricingComponentValueChangePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_pricing_component_value_change_by_component_id(self, pricing_component_id, **kwargs):
        """
        Returns a collection of pricing-component-value-changes, specified by the pricing-component-value-ID parameter. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Retrieve by Component-ID\",\"response\":\"getPricingComponentValueChangeByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_pricing_component_value_change_by_component_id(pricing_component_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str pricing_component_id: The string ID of the pricing-component-value. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first pricing-component-value-change to return.
        :param int records: The maximum number of pricing-component-value-changes to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :return: PricingComponentValueChangePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_pricing_component_value_change_by_component_id_with_http_info(pricing_component_id, **kwargs)
        else:
            (data) = self.get_pricing_component_value_change_by_component_id_with_http_info(pricing_component_id, **kwargs)
            return data

    def get_pricing_component_value_change_by_component_id_with_http_info(self, pricing_component_id, **kwargs):
        """
        Returns a collection of pricing-component-value-changes, specified by the pricing-component-value-ID parameter. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Retrieve by Component-ID\",\"response\":\"getPricingComponentValueChangeByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_pricing_component_value_change_by_component_id_with_http_info(pricing_component_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str pricing_component_id: The string ID of the pricing-component-value. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first pricing-component-value-change to return.
        :param int records: The maximum number of pricing-component-value-changes to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :return: PricingComponentValueChangePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pricing_component_id', 'organizations', 'offset', 'records', 'order_by', 'order']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pricing_component_value_change_by_component_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pricing_component_id' is set
        if ('pricing_component_id' not in params) or (params['pricing_component_id'] is None):
            raise ValueError("Missing the required parameter `pricing_component_id` when calling `get_pricing_component_value_change_by_component_id`")

        resource_path = '/pricing-component-value-changes/component-ID/{pricing-component-ID}'.replace('{format}', 'json')
        path_params = {}
        if 'pricing_component_id' in params:
            path_params['pricing-component-ID'] = params['pricing_component_id']

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
                                            response_type='PricingComponentValueChangePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_pricing_component_value_change_by_invoice_id(self, invoice_id, **kwargs):
        """
        Returns a collection of pricing-component-value-changes, specified by the invoice-ID parameter. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Retrieve by Invoice-ID\",\"response\":\"getPricingComponentValueChangeByInvoiceID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_pricing_component_value_change_by_invoice_id(invoice_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str invoice_id: The string invoice-ID of the pricing-component-value-change. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first pricing-component-value-change to return.
        :param int records: The maximum number of pricing-component-value-changes to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :return: PricingComponentValueChangePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_pricing_component_value_change_by_invoice_id_with_http_info(invoice_id, **kwargs)
        else:
            (data) = self.get_pricing_component_value_change_by_invoice_id_with_http_info(invoice_id, **kwargs)
            return data

    def get_pricing_component_value_change_by_invoice_id_with_http_info(self, invoice_id, **kwargs):
        """
        Returns a collection of pricing-component-value-changes, specified by the invoice-ID parameter. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Retrieve by Invoice-ID\",\"response\":\"getPricingComponentValueChangeByInvoiceID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_pricing_component_value_change_by_invoice_id_with_http_info(invoice_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str invoice_id: The string invoice-ID of the pricing-component-value-change. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first pricing-component-value-change to return.
        :param int records: The maximum number of pricing-component-value-changes to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :return: PricingComponentValueChangePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invoice_id', 'organizations', 'offset', 'records', 'order_by', 'order']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pricing_component_value_change_by_invoice_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invoice_id' is set
        if ('invoice_id' not in params) or (params['invoice_id'] is None):
            raise ValueError("Missing the required parameter `invoice_id` when calling `get_pricing_component_value_change_by_invoice_id`")

        resource_path = '/pricing-component-value-changes/invoice/{invoice-ID}'.replace('{format}', 'json')
        path_params = {}
        if 'invoice_id' in params:
            path_params['invoice-ID'] = params['invoice_id']

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
                                            response_type='PricingComponentValueChangePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_pricing_component_value_change_by_subscription_id(self, subscription_id, **kwargs):
        """
        Returns a collection of pricing-component-value-changes, specified by the subscription-ID parameter. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Retrieve by Subscription-ID\",\"response\":\"getPricingComponentValueChangeBySubscriptionID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_pricing_component_value_change_by_subscription_id(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str subscription_id: ID of the subscription. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first pricing-component-value-change to return.
        :param int records: The maximum number of pricing-component-value-changes to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :return: PricingComponentValueChangePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_pricing_component_value_change_by_subscription_id_with_http_info(subscription_id, **kwargs)
        else:
            (data) = self.get_pricing_component_value_change_by_subscription_id_with_http_info(subscription_id, **kwargs)
            return data

    def get_pricing_component_value_change_by_subscription_id_with_http_info(self, subscription_id, **kwargs):
        """
        Returns a collection of pricing-component-value-changes, specified by the subscription-ID parameter. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Retrieve by Subscription-ID\",\"response\":\"getPricingComponentValueChangeBySubscriptionID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_pricing_component_value_change_by_subscription_id_with_http_info(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str subscription_id: ID of the subscription. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first pricing-component-value-change to return.
        :param int records: The maximum number of pricing-component-value-changes to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :return: PricingComponentValueChangePagedMetadata
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
                    " to method get_pricing_component_value_change_by_subscription_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params) or (params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `get_pricing_component_value_change_by_subscription_id`")

        resource_path = '/pricing-component-value-changes/subscription/{subscription-ID}'.replace('{format}', 'json')
        path_params = {}
        if 'subscription_id' in params:
            path_params['subscription-ID'] = params['subscription_id']

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
                                            response_type='PricingComponentValueChangePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
