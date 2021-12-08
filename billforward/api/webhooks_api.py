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


class WebhooksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_webhook(self, **kwargs):  # noqa: E501
        """create_webhook  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_webhook(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Webhook body:
        :return: InlineResponseDefault101
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_webhook_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_webhook_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_webhook_with_http_info(self, **kwargs):  # noqa: E501
        """create_webhook  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_webhook_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Webhook body:
        :return: InlineResponseDefault101
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_webhook" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/webhooks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault101',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_webhook_v2(self, **kwargs):  # noqa: E501
        """create_webhook_v2  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_webhook_v2(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LegacyCreateWebhookRequest body:
        :return: InlineResponseDefault101
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_webhook_v2_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_webhook_v2_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_webhook_v2_with_http_info(self, **kwargs):  # noqa: E501
        """create_webhook_v2  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_webhook_v2_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LegacyCreateWebhookRequest body:
        :return: InlineResponseDefault101
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_webhook_v2" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/webhooks/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault101',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_webhooks(self, **kwargs):  # noqa: E501
        """get_all_webhooks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_webhooks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] organizations:
        :param int offset:
        :param int records:
        :param str order_by:
        :param str order:
        :param bool include_retired:
        :return: InlineResponseDefault100
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_webhooks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_webhooks_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_webhooks_with_http_info(self, **kwargs):  # noqa: E501
        """get_all_webhooks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_webhooks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] organizations:
        :param int offset:
        :param int records:
        :param str order_by:
        :param str order:
        :param bool include_retired:
        :return: InlineResponseDefault100
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organizations', 'offset', 'records', 'order_by', 'order', 'include_retired']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_webhooks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organizations' in params:
            query_params.append(('organizations', params['organizations']))  # noqa: E501
            collection_formats['organizations'] = 'multi'  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'records' in params:
            query_params.append(('records', params['records']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'include_retired' in params:
            query_params.append(('include_retired', params['include_retired']))  # noqa: E501

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
            '/webhooks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault100',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_allowed_webhook_subscriptions(self, **kwargs):  # noqa: E501
        """get_allowed_webhook_subscriptions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_allowed_webhook_subscriptions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] organizations:
        :return: InlineResponseDefault102
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_allowed_webhook_subscriptions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_allowed_webhook_subscriptions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_allowed_webhook_subscriptions_with_http_info(self, **kwargs):  # noqa: E501
        """get_allowed_webhook_subscriptions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_allowed_webhook_subscriptions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] organizations:
        :return: InlineResponseDefault102
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organizations']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_allowed_webhook_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/webhooks/allowed-subscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault102',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_webhook_by_id(self, webhook_id, **kwargs):  # noqa: E501
        """get_webhook_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_webhook_by_id(webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str webhook_id: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault101
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_webhook_by_id_with_http_info(webhook_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_webhook_by_id_with_http_info(webhook_id, **kwargs)  # noqa: E501
            return data

    def get_webhook_by_id_with_http_info(self, webhook_id, **kwargs):  # noqa: E501
        """get_webhook_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_webhook_by_id_with_http_info(webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str webhook_id: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault101
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webhook_id', 'organizations']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_webhook_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webhook_id' is set
        if ('webhook_id' not in params or
                params['webhook_id'] is None):
            raise ValueError("Missing the required parameter `webhook_id` when calling `get_webhook_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'webhook_id' in params:
            path_params['webhook-ID'] = params['webhook_id']  # noqa: E501

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
            '/webhooks/{webhook-ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault101',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retire_webhook(self, webhook_id, **kwargs):  # noqa: E501
        """retire_webhook  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retire_webhook(webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str webhook_id: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault101
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retire_webhook_with_http_info(webhook_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retire_webhook_with_http_info(webhook_id, **kwargs)  # noqa: E501
            return data

    def retire_webhook_with_http_info(self, webhook_id, **kwargs):  # noqa: E501
        """retire_webhook  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retire_webhook_with_http_info(webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str webhook_id: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault101
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webhook_id', 'organizations']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retire_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webhook_id' is set
        if ('webhook_id' not in params or
                params['webhook_id'] is None):
            raise ValueError("Missing the required parameter `webhook_id` when calling `retire_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'webhook_id' in params:
            path_params['webhook-ID'] = params['webhook_id']  # noqa: E501

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
            '/webhooks/{webhook-ID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault101',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_webhook(self, **kwargs):  # noqa: E501
        """update_webhook  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_webhook(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Webhook body:
        :return: InlineResponseDefault101
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_webhook_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_webhook_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_webhook_with_http_info(self, **kwargs):  # noqa: E501
        """update_webhook  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_webhook_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Webhook body:
        :return: InlineResponseDefault101
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_webhook" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/webhooks', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault101',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def verify_webhook(self, verification_id, **kwargs):  # noqa: E501
        """verify_webhook  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_webhook(verification_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str verification_id: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault101
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.verify_webhook_with_http_info(verification_id, **kwargs)  # noqa: E501
        else:
            (data) = self.verify_webhook_with_http_info(verification_id, **kwargs)  # noqa: E501
            return data

    def verify_webhook_with_http_info(self, verification_id, **kwargs):  # noqa: E501
        """verify_webhook  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_webhook_with_http_info(verification_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str verification_id: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault101
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['verification_id', 'organizations']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method verify_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'verification_id' is set
        if ('verification_id' not in params or
                params['verification_id'] is None):
            raise ValueError("Missing the required parameter `verification_id` when calling `verify_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'verification_id' in params:
            path_params['verification-ID'] = params['verification_id']  # noqa: E501

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
            '/webhooks/verify/{verification-ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault101',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
