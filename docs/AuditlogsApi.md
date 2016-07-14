# billforward.AuditlogsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_audit_entries**](AuditlogsApi.md#get_all_audit_entries) | **GET** /audit-logs | Returns a collection of all audit-log objects. By default 10 values are returned. Records are returned in natural order.
[**get_audit_entries_by_created_date**](AuditlogsApi.md#get_audit_entries_by_created_date) | **GET** /audit-logs/created/{lower-threshold}/{upper-threshold} | Returns a collection of audit-log objects with created times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
[**get_audit_entry_by_entity_id**](AuditlogsApi.md#get_audit_entry_by_entity_id) | **GET** /audit-logs/entity/{entity-ID} | Returns a collection of audit-log entries, specified by the entity-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_audit_entry_by_entity_type**](AuditlogsApi.md#get_audit_entry_by_entity_type) | **GET** /audit-logs/entity-type/{entity-type} | Returns a collection of audit-log entries, specified by the entity-type parameter. By default 10 values are returned. Records are returned in natural order.
[**get_audit_entry_by_id**](AuditlogsApi.md#get_audit_entry_by_id) | **GET** /audit-logs/{audit-ID} | Returns a single audit-log entry, specified by the audit-ID parameter.


# **get_all_audit_entries**
> AuditEntryPagedMetadata get_all_audit_entries(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of all audit-log objects. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all\",\"response\":\"getAuditAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AuditlogsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first audit-log entry to return. (optional) (default to 0)
records = 10 # int | The maximum number of audit-log entry to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of all audit-log objects. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_audit_entries(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuditlogsApi->get_all_audit_entries: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first audit-log entry to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of audit-log entry to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**AuditEntryPagedMetadata**](AuditEntryPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_entries_by_created_date**
> AuditEntryPagedMetadata get_audit_entries_by_created_date(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of audit-log objects with created times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by created time\",\"response\":\"getAuditByCreated.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AuditlogsApi()
lower_threshold = 'lower_threshold_example' # str | The UTC DateTime specifying the start of the result period.
upper_threshold = 'upper_threshold_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first audit-log entry to return. (optional) (default to 0)
records = 10 # int | The maximum number of audit-log entry to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of audit-log objects with created times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_audit_entries_by_created_date(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuditlogsApi->get_audit_entries_by_created_date: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | **str**| The UTC DateTime specifying the start of the result period. | 
 **upper_threshold** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first audit-log entry to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of audit-log entry to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**AuditEntryPagedMetadata**](AuditEntryPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_entry_by_entity_id**
> AuditEntryPagedMetadata get_audit_entry_by_entity_id(entity_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of audit-log entries, specified by the entity-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by entity-ID\",\"response\":\"getAuditByEntityID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AuditlogsApi()
entity_id = 'entity_id_example' # str | The string ID of the entity whose changes are documented by the audit log.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first account to return. (optional) (default to 0)
records = 10 # int | The maximum number of accounts to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of audit-log entries, specified by the entity-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_audit_entry_by_entity_id(entity_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuditlogsApi->get_audit_entry_by_entity_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| The string ID of the entity whose changes are documented by the audit log. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first account to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of accounts to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**AuditEntryPagedMetadata**](AuditEntryPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_entry_by_entity_type**
> AuditEntryPagedMetadata get_audit_entry_by_entity_type(entity_type, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of audit-log entries, specified by the entity-type parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by entity type\",\"response\":\"getAuditByEntityType.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AuditlogsApi()
entity_type = 'entity_type_example' # str | The type of the entity whose changes are documented by the audit log.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first account to return. (optional) (default to 0)
records = 10 # int | The maximum number of accounts to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of audit-log entries, specified by the entity-type parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_audit_entry_by_entity_type(entity_type, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuditlogsApi->get_audit_entry_by_entity_type: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The type of the entity whose changes are documented by the audit log. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first account to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of accounts to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**AuditEntryPagedMetadata**](AuditEntryPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_entry_by_id**
> AuditEntryPagedMetadata get_audit_entry_by_id(audit_id, organizations=organizations)

Returns a single audit-log entry, specified by the audit-ID parameter.

{\"nickname\":\"Retrieve by id\",\"response\":\"getAuditByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AuditlogsApi()
audit_id = 'audit_id_example' # str | The string ID of the audit-log entry.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. Multiple organization-IDs may be specified by repeated use of the query parameter. Example: ...&organizations=org1&organizations=org2 (optional)

try: 
    # Returns a single audit-log entry, specified by the audit-ID parameter.
    api_response = api_instance.get_audit_entry_by_id(audit_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuditlogsApi->get_audit_entry_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_id** | **str**| The string ID of the audit-log entry. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. Multiple organization-IDs may be specified by repeated use of the query parameter. Example: ...&amp;organizations&#x3D;org1&amp;organizations&#x3D;org2 | [optional] 

### Return type

[**AuditEntryPagedMetadata**](AuditEntryPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

