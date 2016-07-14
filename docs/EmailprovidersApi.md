# swagger_client.EmailprovidersApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_provider**](EmailprovidersApi.md#create_email_provider) | **POST** /email-providers | Create an email provider.
[**delete**](EmailprovidersApi.md#delete) | **DELETE** /email-providers/{email-provider-ID} | Deletes a single email provider, specified by id or name parameter.
[**get_all_email_providers**](EmailprovidersApi.md#get_all_email_providers) | **GET** /email-providers | Returns a collection of all email-providers. By default 10 values are returned. Records are returned in natural order.
[**get_email_by_provider_id**](EmailprovidersApi.md#get_email_by_provider_id) | **GET** /email-providers/{email-provider-ID} | Retrieves a single email provider, specified by the version-ID parameter.


# **create_email_provider**
> EmailProviderPagedMetadata create_email_provider(request)

Create an email provider.

{\"nickname\":\"Create an email provider\",\"request\":\"createEmailProviderRequest.html\",\"response\":\"creatEmailProviderResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmailprovidersApi()
request = swagger_client.BillingEntityBase() # BillingEntityBase | .

try: 
    # Create an email provider.
    api_response = api_instance.create_email_provider(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EmailprovidersApi->create_email_provider: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingEntityBase**](BillingEntityBase.md)| . | 

### Return type

[**EmailProviderPagedMetadata**](EmailProviderPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> EmailProviderPagedMetadata delete(email_provider_id, organizations=organizations)

Deletes a single email provider, specified by id or name parameter.

{ \"nickname\" : \"delete\",\"response\" : \"deleteEmailProvider.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmailprovidersApi()
email_provider_id = 'email_provider_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Deletes a single email provider, specified by id or name parameter.
    api_response = api_instance.delete(email_provider_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EmailprovidersApi->delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_provider_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**EmailProviderPagedMetadata**](EmailProviderPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_email_providers**
> EmailProviderPagedMetadata get_all_email_providers(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of all email-providers. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all email providers\",\"response\":\"getEmailProvidersAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmailprovidersApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first email-provider to return. (optional) (default to 0)
records = 10 # int | The maximum number of email-provider to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Include deleted email-providers (optional) (default to false)

try: 
    # Returns a collection of all email-providers. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_email_providers(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EmailprovidersApi->get_all_email_providers: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first email-provider to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of email-provider to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Include deleted email-providers | [optional] [default to false]

### Return type

[**EmailProviderPagedMetadata**](EmailProviderPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_by_provider_id**
> EmailProviderPagedMetadata get_email_by_provider_id(email_provider_id, organizations=organizations, include_retired=include_retired)

Retrieves a single email provider, specified by the version-ID parameter.

{ \"nickname\" : \"Retrieve by version\",\"response\" : \"getEmailProviderByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmailprovidersApi()
email_provider_id = 'email_provider_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
include_retired = false # bool | Include deleted email-providers (optional) (default to false)

try: 
    # Retrieves a single email provider, specified by the version-ID parameter.
    api_response = api_instance.get_email_by_provider_id(email_provider_id, organizations=organizations, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EmailprovidersApi->get_email_by_provider_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_provider_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **include_retired** | **bool**| Include deleted email-providers | [optional] [default to false]

### Return type

[**EmailProviderPagedMetadata**](EmailProviderPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

