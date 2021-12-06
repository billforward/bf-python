# billforward.SalesforceApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_salesforce_job_state**](SalesforceApi.md#change_salesforce_job_state) | **POST** /salesforce/sync/action | 
[**connect_to_salesforce**](SalesforceApi.md#connect_to_salesforce) | **POST** /salesforce/connect | 
[**get_all_salesforce_jobs**](SalesforceApi.md#get_all_salesforce_jobs) | **GET** /salesforce/sync | 
[**get_salesforce_configuration**](SalesforceApi.md#get_salesforce_configuration) | **GET** /salesforce/configuration | 
[**update_salesforce_configuration**](SalesforceApi.md#update_salesforce_configuration) | **PUT** /salesforce/configuration | 

# **change_salesforce_job_state**
> InlineResponseDefault58 change_salesforce_job_state(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SalesforceApi(billforward.ApiClient(configuration))
body = billforward.SyncActionRequest() # SyncActionRequest |  (optional)

try:
    api_response = api_instance.change_salesforce_job_state(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesforceApi->change_salesforce_job_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SyncActionRequest**](SyncActionRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault58**](InlineResponseDefault58.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_to_salesforce**
> InlineResponseDefault27 connect_to_salesforce(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SalesforceApi(billforward.ApiClient(configuration))
body = billforward.CreateSalesforceConfigurationRequest() # CreateSalesforceConfigurationRequest |  (optional)

try:
    api_response = api_instance.connect_to_salesforce(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesforceApi->connect_to_salesforce: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSalesforceConfigurationRequest**](CreateSalesforceConfigurationRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault27**](InlineResponseDefault27.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_salesforce_jobs**
> InlineResponseDefault59 get_all_salesforce_jobs(organization_id=organization_id)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SalesforceApi(billforward.ApiClient(configuration))
organization_id = 'organization_id_example' # str |  (optional)

try:
    api_response = api_instance.get_all_salesforce_jobs(organization_id=organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesforceApi->get_all_salesforce_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | [optional] 

### Return type

[**InlineResponseDefault59**](InlineResponseDefault59.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_salesforce_configuration**
> InlineResponseDefault60 get_salesforce_configuration(organization_id=organization_id)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SalesforceApi(billforward.ApiClient(configuration))
organization_id = 'organization_id_example' # str |  (optional)

try:
    api_response = api_instance.get_salesforce_configuration(organization_id=organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesforceApi->get_salesforce_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | [optional] 

### Return type

[**InlineResponseDefault60**](InlineResponseDefault60.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_salesforce_configuration**
> InlineResponseDefault60 update_salesforce_configuration(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SalesforceApi(billforward.ApiClient(configuration))
body = billforward.UpdateSalesforceConfigurationRequest() # UpdateSalesforceConfigurationRequest |  (optional)

try:
    api_response = api_instance.update_salesforce_configuration(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesforceApi->update_salesforce_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSalesforceConfigurationRequest**](UpdateSalesforceConfigurationRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault60**](InlineResponseDefault60.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

