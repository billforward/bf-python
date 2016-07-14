# billforward.SynchJobsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sync_job**](SynchJobsApi.md#create_sync_job) | **POST** /synchJobs | Create a synch job.
[**get_all_sync_jobs**](SynchJobsApi.md#get_all_sync_jobs) | **GET** /synchJobs | Returns a collection of Users. By default 10 values are returned. Records are returned in natural order.
[**get_sync_job_by_id**](SynchJobsApi.md#get_sync_job_by_id) | **GET** /synchJobs/{synchJob-ID} | Returns a single job, specified by the ID parameter.
[**get_sync_job_by_scope**](SynchJobsApi.md#get_sync_job_by_scope) | **GET** /synchJobs/scope/{scope} | Returns a collection jobs, specified by the scope parameter.
[**get_sync_job_by_state**](SynchJobsApi.md#get_sync_job_by_state) | **GET** /synchJobs/state/{state} | Returns a collection jobs, specified by the state parameter.
[**get_sync_job_by_target**](SynchJobsApi.md#get_sync_job_by_target) | **GET** /synchJobs/target/{target} | Returns a collection jobs, specified by the target parameter.
[**get_sync_job_by_type**](SynchJobsApi.md#get_sync_job_by_type) | **GET** /synchJobs/type/{type} | Returns a collection jobs, specified by the type parameter.
[**update_sync_job**](SynchJobsApi.md#update_sync_job) | **PUT** /synchJobs | Update a synch job.


# **create_sync_job**
> DataSynchronizationJobPagedMetadata create_sync_job(synch_job)

Create a synch job.

{\"nickname\":\"Create a new sync job\",\"request\":\"createSynchJobRequest.html\",\"response\":\"createSynchJobResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchJobsApi()
synch_job = billforward.MutableBillingEntity() # MutableBillingEntity | The data synch job object to be created.

try: 
    # Create a synch job.
    api_response = api_instance.create_sync_job(synch_job)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchJobsApi->create_sync_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synch_job** | [**MutableBillingEntity**](MutableBillingEntity.md)| The data synch job object to be created. | 

### Return type

[**DataSynchronizationJobPagedMetadata**](DataSynchronizationJobPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_sync_jobs**
> DataSynchronizationJobPagedMetadata get_all_sync_jobs(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of Users. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all synch jobs\",\"response\":\"getSynchJobsAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchJobsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first synch job to return. (optional) (default to 0)
records = 10 # int | The maximum number of synch jobs to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of Users. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_sync_jobs(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchJobsApi->get_all_sync_jobs: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first synch job to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of synch jobs to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**DataSynchronizationJobPagedMetadata**](DataSynchronizationJobPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_job_by_id**
> DataSynchronizationJobPagedMetadata get_sync_job_by_id(synch_job_id, organizations=organizations)

Returns a single job, specified by the ID parameter.

{\"nickname\":\"Retrieve an existing synch job\",\"response\":\"getSyncJobByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchJobsApi()
synch_job_id = 'synch_job_id_example' # str | ID of the Sync Job.
organizations = ['organizations_example'] # list[str] | A list of organization -IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single job, specified by the ID parameter.
    api_response = api_instance.get_sync_job_by_id(synch_job_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchJobsApi->get_sync_job_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synch_job_id** | **str**| ID of the Sync Job. | 
 **organizations** | [**list[str]**](str.md)| A list of organization -IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DataSynchronizationJobPagedMetadata**](DataSynchronizationJobPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_job_by_scope**
> DataSynchronizationJobPagedMetadata get_sync_job_by_scope(scope, organizations=organizations)

Returns a collection jobs, specified by the scope parameter.

{\"nickname\":\"Retrieve by scope\",\"response\":\"getSyncJobByScope.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchJobsApi()
scope = 'scope_example' # str | The scope of the synch job.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a collection jobs, specified by the scope parameter.
    api_response = api_instance.get_sync_job_by_scope(scope, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchJobsApi->get_sync_job_by_scope: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the synch job. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DataSynchronizationJobPagedMetadata**](DataSynchronizationJobPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_job_by_state**
> DataSynchronizationJobPagedMetadata get_sync_job_by_state(state, organizations=organizations)

Returns a collection jobs, specified by the state parameter.

{\"nickname\":\"Retrieve by state\",\"response\":\"getSyncJobByState.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchJobsApi()
state = 'state_example' # str | The state of the synch job.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a collection jobs, specified by the state parameter.
    api_response = api_instance.get_sync_job_by_state(state, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchJobsApi->get_sync_job_by_state: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| The state of the synch job. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DataSynchronizationJobPagedMetadata**](DataSynchronizationJobPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_job_by_target**
> DataSynchronizationJobPagedMetadata get_sync_job_by_target(target, organizations=organizations)

Returns a collection jobs, specified by the target parameter.

{\"nickname\":\"Retrieve by target\",\"response\":\"getSyncJobByTarget.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchJobsApi()
target = 'target_example' # str | The target of the synch job.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a collection jobs, specified by the target parameter.
    api_response = api_instance.get_sync_job_by_target(target, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchJobsApi->get_sync_job_by_target: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| The target of the synch job. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DataSynchronizationJobPagedMetadata**](DataSynchronizationJobPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_job_by_type**
> DataSynchronizationJobPagedMetadata get_sync_job_by_type(type, organizations=organizations)

Returns a collection jobs, specified by the type parameter.

{\"nickname\":\"Retrieve by type\",\"response\":\"getSyncJobByType.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchJobsApi()
type = 'type_example' # str | The type of the synch job.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a collection jobs, specified by the type parameter.
    api_response = api_instance.get_sync_job_by_type(type, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchJobsApi->get_sync_job_by_type: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of the synch job. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DataSynchronizationJobPagedMetadata**](DataSynchronizationJobPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sync_job**
> DataSynchronizationJobPagedMetadata update_sync_job(synch_job)

Update a synch job.

{\"nickname\":\"Update a synch job\",\"request\":\"updateSyncJobRequest.html\",\"response\":\"updateSyncJobResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SynchJobsApi()
synch_job = billforward.MutableBillingEntity() # MutableBillingEntity | The synch job object to be updated.

try: 
    # Update a synch job.
    api_response = api_instance.update_sync_job(synch_job)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchJobsApi->update_sync_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synch_job** | [**MutableBillingEntity**](MutableBillingEntity.md)| The synch job object to be updated. | 

### Return type

[**DataSynchronizationJobPagedMetadata**](DataSynchronizationJobPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

