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


class PermissionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_permission(self, **kwargs):  # noqa: E501
        """create_permission  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_permission(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePermissionRequest body:
        :return: InlineResponseDefault45
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_permission_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_permission_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_permission_with_http_info(self, **kwargs):  # noqa: E501
        """create_permission  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_permission_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePermissionRequest body:
        :return: InlineResponseDefault45
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
                    " to method create_permission" % key
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
            '/permissions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault45',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_permissions(self, **kwargs):  # noqa: E501
        """get_all_permissions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_permissions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] organizations:
        :param int offset:
        :param int records:
        :param str order_by:
        :param str order:
        :param bool include_retired:
        :return: InlineResponseDefault44
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_permissions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_permissions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_permissions_with_http_info(self, **kwargs):  # noqa: E501
        """get_all_permissions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_permissions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] organizations:
        :param int offset:
        :param int records:
        :param str order_by:
        :param str order:
        :param bool include_retired:
        :return: InlineResponseDefault44
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
                    " to method get_all_permissions" % key
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
            '/permissions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault44',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_available_actions_for_resource(self, resource, **kwargs):  # noqa: E501
        """get_available_actions_for_resource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_available_actions_for_resource(resource, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str resource: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault46
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_available_actions_for_resource_with_http_info(resource, **kwargs)  # noqa: E501
        else:
            (data) = self.get_available_actions_for_resource_with_http_info(resource, **kwargs)  # noqa: E501
            return data

    def get_available_actions_for_resource_with_http_info(self, resource, **kwargs):  # noqa: E501
        """get_available_actions_for_resource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_available_actions_for_resource_with_http_info(resource, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str resource: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault46
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['resource', 'organizations']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_available_actions_for_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'resource' is set
        if ('resource' not in params or
                params['resource'] is None):
            raise ValueError("Missing the required parameter `resource` when calling `get_available_actions_for_resource`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'resource' in params:
            path_params['resource'] = params['resource']  # noqa: E501

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
            '/permissions/resources/{resource}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault46',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_available_resources(self, **kwargs):  # noqa: E501
        """get_available_resources  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_available_resources(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] organizations:
        :return: InlineResponseDefault47
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_available_resources_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_available_resources_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_available_resources_with_http_info(self, **kwargs):  # noqa: E501
        """get_available_resources  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_available_resources_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] organizations:
        :return: InlineResponseDefault47
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
                    " to method get_available_resources" % key
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
            '/permissions/resources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault47',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_permission_by_id(self, permission_id, **kwargs):  # noqa: E501
        """get_permission_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_permission_by_id(permission_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str permission_id: (required)
        :param list[str] organizations:
        :param bool include_retired:
        :return: InlineResponseDefault45
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_permission_by_id_with_http_info(permission_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_permission_by_id_with_http_info(permission_id, **kwargs)  # noqa: E501
            return data

    def get_permission_by_id_with_http_info(self, permission_id, **kwargs):  # noqa: E501
        """get_permission_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_permission_by_id_with_http_info(permission_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str permission_id: (required)
        :param list[str] organizations:
        :param bool include_retired:
        :return: InlineResponseDefault45
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['permission_id', 'organizations', 'include_retired']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_permission_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'permission_id' is set
        if ('permission_id' not in params or
                params['permission_id'] is None):
            raise ValueError("Missing the required parameter `permission_id` when calling `get_permission_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'permission_id' in params:
            path_params['permission-ID'] = params['permission_id']  # noqa: E501

        query_params = []
        if 'organizations' in params:
            query_params.append(('organizations', params['organizations']))  # noqa: E501
            collection_formats['organizations'] = 'multi'  # noqa: E501
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
            '/permissions/{permission-ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault45',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def revoke_permission(self, permission_id, **kwargs):  # noqa: E501
        """revoke_permission  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_permission(permission_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str permission_id: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault45
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.revoke_permission_with_http_info(permission_id, **kwargs)  # noqa: E501
        else:
            (data) = self.revoke_permission_with_http_info(permission_id, **kwargs)  # noqa: E501
            return data

    def revoke_permission_with_http_info(self, permission_id, **kwargs):  # noqa: E501
        """revoke_permission  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_permission_with_http_info(permission_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str permission_id: (required)
        :param list[str] organizations:
        :return: InlineResponseDefault45
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['permission_id', 'organizations']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method revoke_permission" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'permission_id' is set
        if ('permission_id' not in params or
                params['permission_id'] is None):
            raise ValueError("Missing the required parameter `permission_id` when calling `revoke_permission`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'permission_id' in params:
            path_params['permission-ID'] = params['permission_id']  # noqa: E501

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
            '/permissions/{permission-ID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault45',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
