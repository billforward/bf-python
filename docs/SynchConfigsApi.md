# billforward.SynchConfigsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sync_config**](SynchConfigsApi.md#create_sync_config) | **POST** /synchConfigs | Create a synch configuration.
[**get_all_sync_configs**](SynchConfigsApi.md#get_all_sync_configs) | **GET** /synchConfigs | Returns a collection of Users. By default 10 values are returned. Records are returned in natural order.
[**get_sync_config**](SynchConfigsApi.md#get_sync_config) | **GET** /synchConfigs/{synchConfigs-ID} | Returns a single config, specified by the ID parameter.
[**get_sync_config_by_platform**](SynchConfigsApi.md#get_sync_config_by_platform) | **GET** /synchConfigs/platform/{platform} | Returns a collection configurations, specified by the platform parameter.
[**get_sync_config_by_username**](SynchConfigsApi.md#get_sync_config_by_username) | **GET** /synchConfigs/username/{username} | Returns a collection configurations, specified by the username parameter.
[**update_sync_config**](SynchConfigsApi.md#update_sync_config) | **PUT** /synchConfigs | Update a synch configuration.


# **create_sync_config**
> DataSynchronisationConfigurationPagedMetadata create_sync_config(synch_config)

Create a synch configuration.

{\"nickname\":\"Create a new synch configuration\",\"request\":\"createSynchConfigRequest.html\",\"response\":\"createSynchConfigResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchConfigsApi()
synch_config = billforward.DataSynchronisationConfiguration() # DataSynchronisationConfiguration | The data synch config object to be created.

try: 
    # Create a synch configuration.
    api_response = api_instance.create_sync_config(synch_config)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchConfigsApi->create_sync_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synch_config** | [**DataSynchronisationConfiguration**](DataSynchronisationConfiguration.md)| The data synch config object to be created. | 

### Return type

[**DataSynchronisationConfigurationPagedMetadata**](DataSynchronisationConfigurationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_sync_configs**
> DataSynchronisationConfigurationPagedMetadata get_all_sync_configs(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of Users. By default 10 values are returned. Records are returned in natural order.

{ \"nickname\" : \"Get all synch configs\",\"response\" : \"getSynchConfigsAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchConfigsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first synch configuration to return. (optional) (default to 0)
records = 10 # int | The maximum number of configs to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of Users. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_sync_configs(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchConfigsApi->get_all_sync_configs: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first synch configuration to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of configs to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**DataSynchronisationConfigurationPagedMetadata**](DataSynchronisationConfigurationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_config**
> DataSynchronisationConfigurationPagedMetadata get_sync_config(synch_configs_id, organizations=organizations)

Returns a single config, specified by the ID parameter.

{ \"nickname\" : \"Retrieve an existing synch config\",\"response\" : \"getSynchConfigByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchConfigsApi()
synch_configs_id = 'synch_configs_id_example' # str | ID of the Synch Configuration.
organizations = ['organizations_example'] # list[str] | A list of organization -IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single config, specified by the ID parameter.
    api_response = api_instance.get_sync_config(synch_configs_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchConfigsApi->get_sync_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synch_configs_id** | **str**| ID of the Synch Configuration. | 
 **organizations** | [**list[str]**](str.md)| A list of organization -IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DataSynchronisationConfigurationPagedMetadata**](DataSynchronisationConfigurationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_config_by_platform**
> DataSynchronisationConfigurationPagedMetadata get_sync_config_by_platform(platform, organizations=organizations)

Returns a collection configurations, specified by the platform parameter.

{ \"nickname\" : \"Retrieve by platform\",\"response\" : \"getSynchConfigsByPlatform.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchConfigsApi()
platform = 'platform_example' # str | The type of the synch configuration.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a collection configurations, specified by the platform parameter.
    api_response = api_instance.get_sync_config_by_platform(platform, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchConfigsApi->get_sync_config_by_platform: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| The type of the synch configuration. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DataSynchronisationConfigurationPagedMetadata**](DataSynchronisationConfigurationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_config_by_username**
> DataSynchronisationConfigurationPagedMetadata get_sync_config_by_username(username, organizations=organizations)

Returns a collection configurations, specified by the username parameter.

{ \"nickname\" : \"Retrieve by username\",\"response\" : \"getSynchConfigByUsername.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchConfigsApi()
username = 'username_example' # str | The username in the synch configuration.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a collection configurations, specified by the username parameter.
    api_response = api_instance.get_sync_config_by_username(username, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchConfigsApi->get_sync_config_by_username: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username in the synch configuration. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DataSynchronisationConfigurationPagedMetadata**](DataSynchronisationConfigurationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sync_config**
> DataSynchronisationConfigurationPagedMetadata update_sync_config(synch_config)

Update a synch configuration.

{ \"nickname\" : \"Update a synch config\", \"request\" : \"updateSyncConfigRequest.html\" ,\"response\" : \"updateSyncConfigResponse.html\" }

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchConfigsApi()
synch_config = billforward.DataSynchronisationConfiguration() # DataSynchronisationConfiguration | The synch configuration object to be updated.

try: 
    # Update a synch configuration.
    api_response = api_instance.update_sync_config(synch_config)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchConfigsApi->update_sync_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synch_config** | [**DataSynchronisationConfiguration**](DataSynchronisationConfiguration.md)| The synch configuration object to be updated. | 

### Return type

[**DataSynchronisationConfigurationPagedMetadata**](DataSynchronisationConfigurationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

