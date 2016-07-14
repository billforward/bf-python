# billforward.ProfilesApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_profiles**](ProfilesApi.md#get_all_profiles) | **GET** /profiles | Returns a collection of all profiles. By default 10 values are returned. Records are returned in natural order
[**get_profile**](ProfilesApi.md#get_profile) | **GET** /profiles/{profile-ID} | Returns a single profile, specified by the ID parameter.
[**get_profile_by_account_id**](ProfilesApi.md#get_profile_by_account_id) | **GET** /profiles/account/{account-ID} | Returns a collection of profiles, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order
[**get_profile_by_email_address**](ProfilesApi.md#get_profile_by_email_address) | **GET** /profiles/email/{email} | Returns a single profile, specified by the email parameter.
[**update_profile**](ProfilesApi.md#update_profile) | **PUT** /profiles | Update a profile


# **get_all_profiles**
> ProfilePagedMetadata get_all_profiles(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of all profiles. By default 10 values are returned. Records are returned in natural order

{\"nickname\":\"Get all profiles\",\"response\":\"getProfileAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProfilesApi()
organizations = ['organizations_example'] # list[str] | A list of organizations used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first profile to return. (optional) (default to 0)
records = 10 # int | The maximum number of profiles to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of all profiles. By default 10 values are returned. Records are returned in natural order
    api_response = api_instance.get_all_profiles(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProfilesApi->get_all_profiles: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organizations used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first profile to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of profiles to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**ProfilePagedMetadata**](ProfilePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**
> ProfilePagedMetadata get_profile(profile_id, organizations=organizations)

Returns a single profile, specified by the ID parameter.

{\"nickname\":\"Retrieve an existing profile\",\"response\":\"getProfileByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProfilesApi()
profile_id = 'profile_id_example' # str | ID of the Profile.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single profile, specified by the ID parameter.
    api_response = api_instance.get_profile(profile_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProfilesApi->get_profile: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| ID of the Profile. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**ProfilePagedMetadata**](ProfilePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_by_account_id**
> ProfilePagedMetadata get_profile_by_account_id(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of profiles, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order

{\"nickname\":\"Retrieve by account\",\"response\":\"getProfileByAccountID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProfilesApi()
account_id = 'account_id_example' # str | The account-ID of the profile.
organizations = ['organizations_example'] # list[str] | A list of organizations used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first profile to return. (optional) (default to 0)
records = 10 # int | The maximum number of profiles to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of profiles, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order
    api_response = api_instance.get_profile_by_account_id(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProfilesApi->get_profile_by_account_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account-ID of the profile. | 
 **organizations** | [**list[str]**](str.md)| A list of organizations used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first profile to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of profiles to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**ProfilePagedMetadata**](ProfilePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_by_email_address**
> ProfilePagedMetadata get_profile_by_email_address(email, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a single profile, specified by the email parameter.

{\"nickname\":\"Retrieve by e-mail\",\"response\":\"getProfileByEmail.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProfilesApi()
email = 'email_example' # str | The email address of the profile.
organizations = ['organizations_example'] # list[str] | A list of organizations used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first profile to return. (optional) (default to 0)
records = 10 # int | The maximum number of profiles to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired profiles should be returned. (optional) (default to false)

try: 
    # Returns a single profile, specified by the email parameter.
    api_response = api_instance.get_profile_by_email_address(email, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProfilesApi->get_profile_by_email_address: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address of the profile. | 
 **organizations** | [**list[str]**](str.md)| A list of organizations used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first profile to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of profiles to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired profiles should be returned. | [optional] [default to false]

### Return type

[**ProfilePagedMetadata**](ProfilePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> ProfilePagedMetadata update_profile(request)

Update a profile

{\"nickname\":\"Update a profile\",\"request\":\"updateProfileRequest.html\",\"response\":\"updateProfileResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProfilesApi()
request = billforward.UpdateProfileRequest() # UpdateProfileRequest | The profile object to be updated.

try: 
    # Update a profile
    api_response = api_instance.update_profile(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProfilesApi->update_profile: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UpdateProfileRequest**](UpdateProfileRequest.md)| The profile object to be updated. | 

### Return type

[**ProfilePagedMetadata**](ProfilePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

