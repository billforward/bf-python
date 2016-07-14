# swagger_client.OrganizationsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization**](OrganizationsApi.md#create_organization) | **POST** /organizations | Create an organization.
[**get_all_my_organizations**](OrganizationsApi.md#get_all_my_organizations) | **GET** /organizations/mine | Returns a collection of all my asociated organizations. By default 10 values are returned. Records are returned in natural order.
[**get_all_organizations**](OrganizationsApi.md#get_all_organizations) | **GET** /organizations | Returns a collection of all organizations. By default 10 values are returned. Records are returned in natural order.
[**get_organization_by_customer_code**](OrganizationsApi.md#get_organization_by_customer_code) | **GET** /organizations/customer-code/{customer-code} | Returns a single organization, specified by the customer-code parameter.
[**get_organization_by_id**](OrganizationsApi.md#get_organization_by_id) | **GET** /organizations/{organization-ID} | Returns a single Organization, specified by the organization-ID parameter.
[**get_organization_by_name**](OrganizationsApi.md#get_organization_by_name) | **GET** /organizations/name/{name} | Returns a single Organization, specified by the name parameter.
[**update_organization**](OrganizationsApi.md#update_organization) | **PUT** /organizations | Update an organization.


# **create_organization**
> OrganizationPagedMetadata create_organization(organization)

Create an organization.

{\"nickname\":\"Create\",\"request\":\"createOrganizationRequest.html\",\"response\":\"createOrganizationResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationsApi()
organization = swagger_client.Organization() # Organization | The organization object to be updated.

try: 
    # Create an organization.
    api_response = api_instance.create_organization(organization)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrganizationsApi->create_organization: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | [**Organization**](Organization.md)| The organization object to be updated. | 

### Return type

[**OrganizationPagedMetadata**](OrganizationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_my_organizations**
> OrganizationPagedMetadata get_all_my_organizations(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of all my asociated organizations. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get Mine\",\"response\":\"getOrganizationAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first organization to return. (optional) (default to 0)
records = 10 # int | The maximum number of organizations to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of all my asociated organizations. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_my_organizations(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrganizationsApi->get_all_my_organizations: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first organization to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of organizations to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**OrganizationPagedMetadata**](OrganizationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_organizations**
> OrganizationPagedMetadata get_all_organizations(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of all organizations. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get All\",\"response\":\"getOrganizationAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first organization to return. (optional) (default to 0)
records = 10 # int | The maximum number of organizations to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of all organizations. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_organizations(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrganizationsApi->get_all_organizations: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first organization to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of organizations to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**OrganizationPagedMetadata**](OrganizationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_by_customer_code**
> OrganizationPagedMetadata get_organization_by_customer_code(customer_code, organizations=organizations)

Returns a single organization, specified by the customer-code parameter.

{\"nickname\":\"Retrieve by Customer-Code\",\"response\":\"getOrganizationByCustomer.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationsApi()
customer_code = 'customer_code_example' # str | The unique customer code of the organization.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single organization, specified by the customer-code parameter.
    api_response = api_instance.get_organization_by_customer_code(customer_code, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrganizationsApi->get_organization_by_customer_code: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_code** | **str**| The unique customer code of the organization. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**OrganizationPagedMetadata**](OrganizationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_by_id**
> OrganizationPagedMetadata get_organization_by_id(organization_id, organizations=organizations)

Returns a single Organization, specified by the organization-ID parameter.

{\"nickname\":\"Retrieve by id\",\"response\":\"getOrganizationByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationsApi()
organization_id = 'organization_id_example' # str | ID of the organization.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single Organization, specified by the organization-ID parameter.
    api_response = api_instance.get_organization_by_id(organization_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrganizationsApi->get_organization_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| ID of the organization. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**OrganizationPagedMetadata**](OrganizationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_by_name**
> OrganizationPagedMetadata get_organization_by_name(name, organizations=organizations)

Returns a single Organization, specified by the name parameter.

{\"nickname\":\"Retrieve by Name\",\"response\":\"getOrganizationByName.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationsApi()
name = 'name_example' # str | The name of the Organization.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single Organization, specified by the name parameter.
    api_response = api_instance.get_organization_by_name(name, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrganizationsApi->get_organization_by_name: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Organization. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**OrganizationPagedMetadata**](OrganizationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization**
> OrganizationPagedMetadata update_organization(organization)

Update an organization.

{\"nickname\":\"Updated\",\"request\":\"updateOrganizationRequest.html\",\"response\":\"updateOrganizationResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationsApi()
organization = swagger_client.Organization() # Organization | The organization object to be updated.

try: 
    # Update an organization.
    api_response = api_instance.update_organization(organization)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrganizationsApi->update_organization: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | [**Organization**](Organization.md)| The organization object to be updated. | 

### Return type

[**OrganizationPagedMetadata**](OrganizationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

