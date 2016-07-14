# swagger_client.ConfigurationsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_configuration**](ConfigurationsApi.md#create_api_configuration) | **POST** /configurations | Create a configuration.
[**get_all_api_configurations**](ConfigurationsApi.md#get_all_api_configurations) | **GET** /configurations | Returns a collection of configurations. By default 10 values are returned. Records are returned in natural order.
[**get_api_configurations_by_type**](ConfigurationsApi.md#get_api_configurations_by_type) | **GET** /configurations/type/{configuration-type} | Returns a single configuration, specified by the type parameter.
[**update_api_configuration**](ConfigurationsApi.md#update_api_configuration) | **PUT** /configurations | Update a configuration.


# **create_api_configuration**
> APIConfigurationPagedMetadata create_api_configuration(configuration)

Create a configuration.

{\"nickname\":\"Create a new configuration\",\"request\":\"createConfigurationRequest.html\",\"response\":\"createConfigurationResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationsApi()
configuration = swagger_client.MutableBillingEntity() # MutableBillingEntity | The configuration object to be created.

try: 
    # Create a configuration.
    api_response = api_instance.create_api_configuration(configuration)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConfigurationsApi->create_api_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration** | [**MutableBillingEntity**](MutableBillingEntity.md)| The configuration object to be created. | 

### Return type

[**APIConfigurationPagedMetadata**](APIConfigurationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_api_configurations**
> APIConfigurationPagedMetadata get_all_api_configurations(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of configurations. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all configurations\",\"response\":\"getConfigurationsAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-components to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of configurations. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_api_configurations(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConfigurationsApi->get_all_api_configurations: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-components to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**APIConfigurationPagedMetadata**](APIConfigurationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_configurations_by_type**
> APIConfigurationPagedMetadata get_api_configurations_by_type(configuration_type, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a single configuration, specified by the type parameter.

{\"nickname\":\"Retrieve by payment gateway\",\"response\":\"getConfigurationByType.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationsApi()
configuration_type = 'configuration_type_example' # str | The unique type of the configuration.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-components to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a single configuration, specified by the type parameter.
    api_response = api_instance.get_api_configurations_by_type(configuration_type, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConfigurationsApi->get_api_configurations_by_type: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_type** | **str**| The unique type of the configuration. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-components to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**APIConfigurationPagedMetadata**](APIConfigurationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_configuration**
> APIConfigurationPagedMetadata update_api_configuration(configuration)

Update a configuration.

{\"nickname\":\"Update a configuration\",\"request\":\"updateConfigurationRequest.html\",\"response\":\"updateConfigurationResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationsApi()
configuration = swagger_client.MutableBillingEntity() # MutableBillingEntity | The configuration object to be updated.

try: 
    # Update a configuration.
    api_response = api_instance.update_api_configuration(configuration)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConfigurationsApi->update_api_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration** | [**MutableBillingEntity**](MutableBillingEntity.md)| The configuration object to be updated. | 

### Return type

[**APIConfigurationPagedMetadata**](APIConfigurationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

