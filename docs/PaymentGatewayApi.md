# billforward.PaymentGatewayApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_configuration**](PaymentGatewayApi.md#create_api_configuration) | **POST** /configurations | 
[**get_all_api_configurations**](PaymentGatewayApi.md#get_all_api_configurations) | **GET** /configurations | 
[**get_api_configurations_by_type**](PaymentGatewayApi.md#get_api_configurations_by_type) | **GET** /configurations/type/{configuration-type} | 
[**public_configuration**](PaymentGatewayApi.md#public_configuration) | **GET** /configurations/public | 
[**update_api_configuration**](PaymentGatewayApi.md#update_api_configuration) | **PUT** /configurations | 

# **create_api_configuration**
> InlineResponseDefault14 create_api_configuration(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentGatewayApi(billforward.ApiClient(configuration))
body = billforward.APIConfiguration() # APIConfiguration |  (optional)

try:
    api_response = api_instance.create_api_configuration(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentGatewayApi->create_api_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**APIConfiguration**](APIConfiguration.md)|  | [optional] 

### Return type

[**InlineResponseDefault14**](InlineResponseDefault14.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_api_configurations**
> InlineResponseDefault18 get_all_api_configurations(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentGatewayApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_response = api_instance.get_all_api_configurations(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentGatewayApi->get_all_api_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

[**InlineResponseDefault18**](InlineResponseDefault18.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_configurations_by_type**
> InlineResponseDefault18 get_api_configurations_by_type(configuration_type, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentGatewayApi(billforward.ApiClient(configuration))
configuration_type = 'configuration_type_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_response = api_instance.get_api_configurations_by_type(configuration_type, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentGatewayApi->get_api_configurations_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_type** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

[**InlineResponseDefault18**](InlineResponseDefault18.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_configuration**
> PublicConfigurationResponse public_configuration(organization_id=organization_id)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentGatewayApi(billforward.ApiClient(configuration))
organization_id = 'organization_id_example' # str |  (optional)

try:
    api_response = api_instance.public_configuration(organization_id=organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentGatewayApi->public_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | [optional] 

### Return type

[**PublicConfigurationResponse**](PublicConfigurationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_configuration**
> InlineResponseDefault14 update_api_configuration(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentGatewayApi(billforward.ApiClient(configuration))
body = billforward.APIConfiguration() # APIConfiguration |  (optional)

try:
    api_response = api_instance.update_api_configuration(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentGatewayApi->update_api_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**APIConfiguration**](APIConfiguration.md)|  | [optional] 

### Return type

[**InlineResponseDefault14**](InlineResponseDefault14.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

