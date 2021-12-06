# coding: utf-8

"""
    Billforward API

    This is documentation for the Billforward API. You can find out more at billforward.io.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: team@billforward.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from billforward.api_client import ApiClient


class AffiliationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_invoice(self, account_id, **kwargs):  # noqa: E501
        """create_invoice  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_invoice(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: (required)
        :param CreateCommissionInvoiceRequest body:
        :return: InlineResponseDefault8
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_invoice_with_http_info(account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_invoice_with_http_info(account_id, **kwargs)  # noqa: E501
            return data

    def create_invoice_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """create_invoice  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_invoice_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: (required)
        :param CreateCommissionInvoiceRequest body:
        :return: InlineResponseDefault8
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_invoice`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account-id'] = params['account_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/affiliate/{account-id}/invoice', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault8',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_affiliate(self, product_rate_plan_id, **kwargs):  # noqa: E501
        """get_affiliate  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_affiliate(product_rate_plan_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_rate_plan_id: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault48
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_affiliate_with_http_info(product_rate_plan_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_affiliate_with_http_info(product_rate_plan_id, **kwargs)  # noqa: E501
            return data

    def get_affiliate_with_http_info(self, product_rate_plan_id, **kwargs):  # noqa: E501
        """get_affiliate  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_affiliate_with_http_info(product_rate_plan_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_rate_plan_id: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault48
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_rate_plan_id', 'organizations']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_affiliate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_rate_plan_id' is set
        if ('product_rate_plan_id' not in params or
                params['product_rate_plan_id'] is None):
            raise ValueError("Missing the required parameter `product_rate_plan_id` when calling `get_affiliate`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'product_rate_plan_id' in params:
            path_params['productRatePlanID'] = params['product_rate_plan_id']  # noqa: E501

        query_params = []
        if 'organizations' in params:
            query_params.append(('organizations', params['organizations']))  # noqa: E501
            collection_formats['organizations'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/product-rate-plans/{productRatePlanID}/affiliate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault48',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_affiliate1(self, subscription_id, **kwargs):  # noqa: E501
        """get_affiliate1  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_affiliate1(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str subscription_id: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault66
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_affiliate1_with_http_info(subscription_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_affiliate1_with_http_info(subscription_id, **kwargs)  # noqa: E501
            return data

    def get_affiliate1_with_http_info(self, subscription_id, **kwargs):  # noqa: E501
        """get_affiliate1  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_affiliate1_with_http_info(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str subscription_id: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault66
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id', 'organizations']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_affiliate1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `get_affiliate1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in params:
            path_params['subscriptionID'] = params['subscription_id']  # noqa: E501

        query_params = []
        if 'organizations' in params:
            query_params.append(('organizations', params['organizations']))  # noqa: E501
            collection_formats['organizations'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions/{subscriptionID}/affiliate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault66',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def quote_invoice(self, account_id, invoice_id, **kwargs):  # noqa: E501
        """quote_invoice  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.quote_invoice(account_id, invoice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: (required)
        :param str invoice_id: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault13
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.quote_invoice_with_http_info(account_id, invoice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.quote_invoice_with_http_info(account_id, invoice_id, **kwargs)  # noqa: E501
            return data

    def quote_invoice_with_http_info(self, account_id, invoice_id, **kwargs):  # noqa: E501
        """quote_invoice  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.quote_invoice_with_http_info(account_id, invoice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: (required)
        :param str invoice_id: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault13
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'invoice_id', 'organizations']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method quote_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `quote_invoice`")  # noqa: E501
        # verify the required parameter 'invoice_id' is set
        if ('invoice_id' not in params or
                params['invoice_id'] is None):
            raise ValueError("Missing the required parameter `invoice_id` when calling `quote_invoice`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account-id'] = params['account_id']  # noqa: E501
        if 'invoice_id' in params:
            path_params['invoice-id'] = params['invoice_id']  # noqa: E501

        query_params = []
        if 'organizations' in params:
            query_params.append(('organizations', params['organizations']))  # noqa: E501
            collection_formats['organizations'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/affiliate/{account-id}/quote/invoice/{invoice-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault13',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def quote_subscription(self, account_id, subscription_id, **kwargs):  # noqa: E501
        """quote_subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.quote_subscription(account_id, subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: (required)
        :param str subscription_id: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault13
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.quote_subscription_with_http_info(account_id, subscription_id, **kwargs)  # noqa: E501
        else:
            (data) = self.quote_subscription_with_http_info(account_id, subscription_id, **kwargs)  # noqa: E501
            return data

    def quote_subscription_with_http_info(self, account_id, subscription_id, **kwargs):  # noqa: E501
        """quote_subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.quote_subscription_with_http_info(account_id, subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: (required)
        :param str subscription_id: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault13
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'subscription_id', 'organizations']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method quote_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `quote_subscription`")  # noqa: E501
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `quote_subscription`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account-id'] = params['account_id']  # noqa: E501
        if 'subscription_id' in params:
            path_params['subscription-id'] = params['subscription_id']  # noqa: E501

        query_params = []
        if 'organizations' in params:
            query_params.append(('organizations', params['organizations']))  # noqa: E501
            collection_formats['organizations'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/affiliate/{account-id}/quote/subscription/{subscription-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault13',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_affiliate(self, product_rate_plan_id, **kwargs):  # noqa: E501
        """set_affiliate  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_affiliate(product_rate_plan_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_rate_plan_id: (required)
        :param SetRatePlanAffiliateRequest body:
        :return: InlineResponseDefault49
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_affiliate_with_http_info(product_rate_plan_id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_affiliate_with_http_info(product_rate_plan_id, **kwargs)  # noqa: E501
            return data

    def set_affiliate_with_http_info(self, product_rate_plan_id, **kwargs):  # noqa: E501
        """set_affiliate  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_affiliate_with_http_info(product_rate_plan_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_rate_plan_id: (required)
        :param SetRatePlanAffiliateRequest body:
        :return: InlineResponseDefault49
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_rate_plan_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_affiliate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_rate_plan_id' is set
        if ('product_rate_plan_id' not in params or
                params['product_rate_plan_id'] is None):
            raise ValueError("Missing the required parameter `product_rate_plan_id` when calling `set_affiliate`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'product_rate_plan_id' in params:
            path_params['product-rate-plan-ID'] = params['product_rate_plan_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/product-rate-plans/{product-rate-plan-ID}/affiliate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault49',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_affiliate1(self, subscription_id, **kwargs):  # noqa: E501
        """set_affiliate1  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_affiliate1(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str subscription_id: (required)
        :param SetSubscriptionAffiliateRequest body:
        :return: InlineResponseDefault67
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_affiliate1_with_http_info(subscription_id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_affiliate1_with_http_info(subscription_id, **kwargs)  # noqa: E501
            return data

    def set_affiliate1_with_http_info(self, subscription_id, **kwargs):  # noqa: E501
        """set_affiliate1  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_affiliate1_with_http_info(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str subscription_id: (required)
        :param SetSubscriptionAffiliateRequest body:
        :return: InlineResponseDefault67
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_affiliate1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `set_affiliate1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in params:
            path_params['subscriptionID'] = params['subscription_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions/{subscriptionID}/affiliate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault67',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_affiliate(self, product_rate_plan_id, **kwargs):  # noqa: E501
        """update_affiliate  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_affiliate(product_rate_plan_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_rate_plan_id: (required)
        :param UpdateRatePlanAffiliateRequest body:
        :return: InlineResponseDefault49
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_affiliate_with_http_info(product_rate_plan_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_affiliate_with_http_info(product_rate_plan_id, **kwargs)  # noqa: E501
            return data

    def update_affiliate_with_http_info(self, product_rate_plan_id, **kwargs):  # noqa: E501
        """update_affiliate  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_affiliate_with_http_info(product_rate_plan_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_rate_plan_id: (required)
        :param UpdateRatePlanAffiliateRequest body:
        :return: InlineResponseDefault49
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_rate_plan_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_affiliate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_rate_plan_id' is set
        if ('product_rate_plan_id' not in params or
                params['product_rate_plan_id'] is None):
            raise ValueError("Missing the required parameter `product_rate_plan_id` when calling `update_affiliate`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'product_rate_plan_id' in params:
            path_params['product-rate-plan-ID'] = params['product_rate_plan_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/product-rate-plans/{product-rate-plan-ID}/affiliate', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault49',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
