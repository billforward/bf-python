# billforward.SynchAppConfigsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sync_app_config**](SynchAppConfigsApi.md#create_sync_app_config) | **POST** /synchAppConfigs | Create a synch app configuration.
[**get_sync_app_config**](SynchAppConfigsApi.md#get_sync_app_config) | **GET** /synchAppConfigs/{synchAppConfigs-ID} | Returns a single config, specified by the ID parameter.
[**get_sync_app_config_by_platform**](SynchAppConfigsApi.md#get_sync_app_config_by_platform) | **GET** /synchAppConfigs/platform/{platform} | Returns a collection configurations, specified by the platform parameter.
[**update_sync_app_config**](SynchAppConfigsApi.md#update_sync_app_config) | **PUT** /synchAppConfigs | Update a synch app configuration.


# **create_sync_app_config**
> DataSynchronisationAppConfigurationPagedMetadata create_sync_app_config(synch_app_config)

Create a synch app configuration.

{\"nickname\":\"Create a new synch app configuration\",\"request\":\"createSynchAppConfigurationRequest.html\",\"response\":\"createSynchAppConfigurationResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchAppConfigsApi()
synch_app_config = billforward.MutableBillingEntity() # MutableBillingEntity | The data synch app config object to be created.

try: 
    # Create a synch app configuration.
    api_response = api_instance.create_sync_app_config(synch_app_config)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchAppConfigsApi->create_sync_app_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synch_app_config** | [**MutableBillingEntity**](MutableBillingEntity.md)| The data synch app config object to be created. | 

### Return type

[**DataSynchronisationAppConfigurationPagedMetadata**](DataSynchronisationAppConfigurationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_app_config**
> DataSynchronisationAppConfigurationPagedMetadata get_sync_app_config(synch_app_configs_id, organizations=organizations)

Returns a single config, specified by the ID parameter.

{ \"nickname\" : \"Retrieve an existing synch config\",\"response\" : \"getSynchAppConfigByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchAppConfigsApi()
synch_app_configs_id = 'synch_app_configs_id_example' # str | ID of the Synch App Configuration.
organizations = ['organizations_example'] # list[str] | A list of organization -IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single config, specified by the ID parameter.
    api_response = api_instance.get_sync_app_config(synch_app_configs_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchAppConfigsApi->get_sync_app_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synch_app_configs_id** | **str**| ID of the Synch App Configuration. | 
 **organizations** | [**list[str]**](str.md)| A list of organization -IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DataSynchronisationAppConfigurationPagedMetadata**](DataSynchronisationAppConfigurationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_app_config_by_platform**
> DataSynchronisationAppConfigurationPagedMetadata get_sync_app_config_by_platform(platform, organizations=organizations)

Returns a collection configurations, specified by the platform parameter.

{ \"nickname\" : \"Retrieve by platform\",\"response\" : \"getSynchAppConfigsByPlatform.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchAppConfigsApi()
platform = 'platform_example' # str | The type of the synch app configuration.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a collection configurations, specified by the platform parameter.
    api_response = api_instance.get_sync_app_config_by_platform(platform, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchAppConfigsApi->get_sync_app_config_by_platform: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| The type of the synch app configuration. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DataSynchronisationAppConfigurationPagedMetadata**](DataSynchronisationAppConfigurationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sync_app_config**
> DataSynchronisationAppConfigurationPagedMetadata update_sync_app_config(synch_app_config)

Update a synch app configuration.

{ \"nickname\" : \"Update a sync app configuration\", \"request\" : \"updateSyncAppConfigRequest.html\" ,\"response\" : \"updateSyncAppConfigResponse.html\" }

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchAppConfigsApi()
synch_app_config = billforward.MutableBillingEntity() # MutableBillingEntity | The synch app configuration object to be updated.

try: 
    # Update a synch app configuration.
    api_response = api_instance.update_sync_app_config(synch_app_config)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchAppConfigsApi->update_sync_app_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synch_app_config** | [**MutableBillingEntity**](MutableBillingEntity.md)| The synch app configuration object to be updated. | 

### Return type

[**DataSynchronisationAppConfigurationPagedMetadata**](DataSynchronisationAppConfigurationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

