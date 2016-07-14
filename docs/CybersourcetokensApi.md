# swagger_client.CybersourcetokensApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cybersource_token**](CybersourcetokensApi.md#create_cybersource_token) | **POST** /cybersource-tokens | Create a cybersource-token.
[**get_cybersource_token_by_id**](CybersourcetokensApi.md#get_cybersource_token_by_id) | **GET** /cybersource-tokens/{token-ID} | Returns a single cybersource-token, specified by the token-ID parameter.
[**get_cybersource_token_by_recurring_subscription_id**](CybersourcetokensApi.md#get_cybersource_token_by_recurring_subscription_id) | **GET** /cybersource-tokens/recurring-subscription-info/{recurring-subscription-ID} | Returns a single cybersource-token, specified by the recurring-subscription-ID parameter.
[**retire_cybersource_token**](CybersourcetokensApi.md#retire_cybersource_token) | **DELETE** /cybersource-tokens/{token-ID} | Retires the cybersource token specified by the token-ID parameter.
[**update_cybersource_token**](CybersourcetokensApi.md#update_cybersource_token) | **PUT** /cybersource-tokens | Update a cybersource-token.


# **create_cybersource_token**
> CybersourceTokenPagedMetadata create_cybersource_token(cybersource_token)

Create a cybersource-token.

{\"nickname\":\"Create a cybersource-token\",\"request\":\"createCybersourceTokenRequest.html\",\"response\":\"createCybersourceTokenResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CybersourcetokensApi()
cybersource_token = swagger_client.MutableBillingEntity() # MutableBillingEntity | The cybersource-token object to be created.

try: 
    # Create a cybersource-token.
    api_response = api_instance.create_cybersource_token(cybersource_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CybersourcetokensApi->create_cybersource_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cybersource_token** | [**MutableBillingEntity**](MutableBillingEntity.md)| The cybersource-token object to be created. | 

### Return type

[**CybersourceTokenPagedMetadata**](CybersourceTokenPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cybersource_token_by_id**
> CybersourceTokenPagedMetadata get_cybersource_token_by_id(token_id, organizations=organizations)

Returns a single cybersource-token, specified by the token-ID parameter.

{\"nickname\":\"NICKNAME\",\"response\":\"getCybersourceTokenByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CybersourcetokensApi()
token_id = 'token_id_example' # str | The unique sting ID of the cybersource token.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single cybersource-token, specified by the token-ID parameter.
    api_response = api_instance.get_cybersource_token_by_id(token_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CybersourcetokensApi->get_cybersource_token_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The unique sting ID of the cybersource token. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CybersourceTokenPagedMetadata**](CybersourceTokenPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cybersource_token_by_recurring_subscription_id**
> CybersourceTokenPagedMetadata get_cybersource_token_by_recurring_subscription_id(recurring_subscription_id, organizations=organizations)

Returns a single cybersource-token, specified by the recurring-subscription-ID parameter.

{\"nickname\":\"NICKNAME\",\"response\":\"getCybersourceTokenByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CybersourcetokensApi()
recurring_subscription_id = 'recurring_subscription_id_example' # str | The recurring-subscription-info-subscription-ID of the cybersource token.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single cybersource-token, specified by the recurring-subscription-ID parameter.
    api_response = api_instance.get_cybersource_token_by_recurring_subscription_id(recurring_subscription_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CybersourcetokensApi->get_cybersource_token_by_recurring_subscription_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurring_subscription_id** | **str**| The recurring-subscription-info-subscription-ID of the cybersource token. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CybersourceTokenPagedMetadata**](CybersourceTokenPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retire_cybersource_token**
> CybersourceTokenPagedMetadata retire_cybersource_token(token_id, organizations)

Retires the cybersource token specified by the token-ID parameter.

{\"nickname\":\"NICKNAME\",\"response\":\"deleteCybersourceToken.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CybersourcetokensApi()
token_id = 'token_id_example' # str | ID of the cybersource-token.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls.

try: 
    # Retires the cybersource token specified by the token-ID parameter.
    api_response = api_instance.retire_cybersource_token(token_id, organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CybersourcetokensApi->retire_cybersource_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| ID of the cybersource-token. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | 

### Return type

[**CybersourceTokenPagedMetadata**](CybersourceTokenPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cybersource_token**
> CybersourceTokenPagedMetadata update_cybersource_token(cybersource_token)

Update a cybersource-token.

{\"nickname\":\"Update a cybersource-token\",\"request\":\"updateCybersourceTokenRequest.html\",\"response\":\"updateCybersourceTokenResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CybersourcetokensApi()
cybersource_token = swagger_client.MutableBillingEntity() # MutableBillingEntity | The cybersource-token object to be updated.

try: 
    # Update a cybersource-token.
    api_response = api_instance.update_cybersource_token(cybersource_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CybersourcetokensApi->update_cybersource_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cybersource_token** | [**MutableBillingEntity**](MutableBillingEntity.md)| The cybersource-token object to be updated. | 

### Return type

[**CybersourceTokenPagedMetadata**](CybersourceTokenPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

