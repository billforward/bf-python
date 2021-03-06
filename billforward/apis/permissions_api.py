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


class PermissionsApi(object):
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

    def create_permission(self, permission_request, **kwargs):
        """
        Create a new permission.
        {\"nickname\":\"Create a new permission\",\"request\":\"createPermissionRequest.html\",\"response\":\"createPermissionResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_permission(permission_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BillingEntityBase permission_request:  (required)
        :return: BFPermissionPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_permission_with_http_info(permission_request, **kwargs)
        else:
            (data) = self.create_permission_with_http_info(permission_request, **kwargs)
            return data

    def create_permission_with_http_info(self, permission_request, **kwargs):
        """
        Create a new permission.
        {\"nickname\":\"Create a new permission\",\"request\":\"createPermissionRequest.html\",\"response\":\"createPermissionResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_permission_with_http_info(permission_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BillingEntityBase permission_request:  (required)
        :return: BFPermissionPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['permission_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_permission" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'permission_request' is set
        if ('permission_request' not in params) or (params['permission_request'] is None):
            raise ValueError("Missing the required parameter `permission_request` when calling `create_permission`")

        resource_path = '/permissions'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'permission_request' in params:
            body_params = params['permission_request']

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
                                            response_type='BFPermissionPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_all_permissions(self, **kwargs):
        """
        Retrieves a collection of all permissions. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Retrieve all permissions\",\"response\":\"getPermissionAll.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_permissions(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first subscription to return.
        :param int records: The maximum number of subscriptions to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired subscriptions should be returned.
        :return: BFPermissionPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_permissions_with_http_info(**kwargs)
        else:
            (data) = self.get_all_permissions_with_http_info(**kwargs)
            return data

    def get_all_permissions_with_http_info(self, **kwargs):
        """
        Retrieves a collection of all permissions. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Retrieve all permissions\",\"response\":\"getPermissionAll.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_permissions_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first subscription to return.
        :param int records: The maximum number of subscriptions to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired subscriptions should be returned.
        :return: BFPermissionPagedMetadata
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
                    " to method get_all_permissions" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/permissions'.replace('{format}', 'json')
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
                                            response_type='BFPermissionPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_available_actions_for_resource(self, resource, **kwargs):
        """
        Retrieves all the available actions for the specified resource.
        {\"nickname\":\"Retrieve available actions\",\"response\":\"getAvailableActions.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_available_actions_for_resource(resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str resource:  (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: PermissionActionEntityPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_available_actions_for_resource_with_http_info(resource, **kwargs)
        else:
            (data) = self.get_available_actions_for_resource_with_http_info(resource, **kwargs)
            return data

    def get_available_actions_for_resource_with_http_info(self, resource, **kwargs):
        """
        Retrieves all the available actions for the specified resource.
        {\"nickname\":\"Retrieve available actions\",\"response\":\"getAvailableActions.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_available_actions_for_resource_with_http_info(resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str resource:  (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: PermissionActionEntityPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['resource', 'organizations']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_available_actions_for_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'resource' is set
        if ('resource' not in params) or (params['resource'] is None):
            raise ValueError("Missing the required parameter `resource` when calling `get_available_actions_for_resource`")

        resource_path = '/permissions/resources/{resource}'.replace('{format}', 'json')
        path_params = {}
        if 'resource' in params:
            path_params['resource'] = params['resource']

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
                                            response_type='PermissionActionEntityPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_available_resources(self, **kwargs):
        """
        Retrieves all available resource.
        {\"nickname\":\"Retrieve available resources\",\"response\":\"getAvailableResources.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_available_resources(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: PermissionResourceEntityPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_available_resources_with_http_info(**kwargs)
        else:
            (data) = self.get_available_resources_with_http_info(**kwargs)
            return data

    def get_available_resources_with_http_info(self, **kwargs):
        """
        Retrieves all available resource.
        {\"nickname\":\"Retrieve available resources\",\"response\":\"getAvailableResources.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_available_resources_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: PermissionResourceEntityPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organizations']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_available_resources" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/permissions/resources'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='PermissionResourceEntityPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_permission_by_id(self, permission_id, **kwargs):
        """
        Retrieves a single permission, specified by the ID parameter.
        {\"nickname\":\"Retrieve a permission\",\"response\":\"getPermissionByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_permission_by_id(permission_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str permission_id:  (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param bool include_retired: Whether retired subscriptions should be returned.
        :return: BFPermissionPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_permission_by_id_with_http_info(permission_id, **kwargs)
        else:
            (data) = self.get_permission_by_id_with_http_info(permission_id, **kwargs)
            return data

    def get_permission_by_id_with_http_info(self, permission_id, **kwargs):
        """
        Retrieves a single permission, specified by the ID parameter.
        {\"nickname\":\"Retrieve a permission\",\"response\":\"getPermissionByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_permission_by_id_with_http_info(permission_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str permission_id:  (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param bool include_retired: Whether retired subscriptions should be returned.
        :return: BFPermissionPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['permission_id', 'organizations', 'include_retired']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_permission_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'permission_id' is set
        if ('permission_id' not in params) or (params['permission_id'] is None):
            raise ValueError("Missing the required parameter `permission_id` when calling `get_permission_by_id`")

        resource_path = '/permissions/{permission-ID}'.replace('{format}', 'json')
        path_params = {}
        if 'permission_id' in params:
            path_params['permission-ID'] = params['permission_id']

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
                                            response_type='BFPermissionPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def revoke_permission(self, permission_id, **kwargs):
        """
        Revokes a permission
        {\"nickname\":\"Revoke permission\",\"response\":\"revokePermission.html\",\"request\":\"revokePErmissionRequest.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.revoke_permission(permission_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str permission_id:  (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: BFPermissionPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.revoke_permission_with_http_info(permission_id, **kwargs)
        else:
            (data) = self.revoke_permission_with_http_info(permission_id, **kwargs)
            return data

    def revoke_permission_with_http_info(self, permission_id, **kwargs):
        """
        Revokes a permission
        {\"nickname\":\"Revoke permission\",\"response\":\"revokePermission.html\",\"request\":\"revokePErmissionRequest.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.revoke_permission_with_http_info(permission_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str permission_id:  (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: BFPermissionPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['permission_id', 'organizations']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method revoke_permission" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'permission_id' is set
        if ('permission_id' not in params) or (params['permission_id'] is None):
            raise ValueError("Missing the required parameter `permission_id` when calling `revoke_permission`")

        resource_path = '/permissions/{permission-ID}'.replace('{format}', 'json')
        path_params = {}
        if 'permission_id' in params:
            path_params['permission-ID'] = params['permission_id']

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
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BFPermissionPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
