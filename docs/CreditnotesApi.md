# swagger_client.CreditnotesApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credit_note**](CreditnotesApi.md#create_credit_note) | **POST** /credit-notes | Create a credit note.
[**get_credit_note_by_id**](CreditnotesApi.md#get_credit_note_by_id) | **GET** /credit-notes/{credit-note-ID} | Returns a single credit-note, specified by the ID parameter.
[**get_credit_note_for_account**](CreditnotesApi.md#get_credit_note_for_account) | **GET** /credit-notes/account/{account-ID} | Returns credit notes for an account.
[**get_credit_note_for_invoice**](CreditnotesApi.md#get_credit_note_for_invoice) | **GET** /credit-notes/invoice/{invoice-ID} | Returns credit notes for an invoice.
[**get_credit_note_for_subscription**](CreditnotesApi.md#get_credit_note_for_subscription) | **GET** /credit-notes/subscription/{subscription-ID} | Returns credit notes for an subscription.
[**retire_credit_note**](CreditnotesApi.md#retire_credit_note) | **DELETE** /credit-notes/{credit-note-ID} | Removes any remaining value from credit note


# **create_credit_note**
> CreditNotePagedMetadata create_credit_note(credit_note)

Create a credit note.

{\"nickname\":\"Create a new credit note\",\"request\":\"createCreditNoteRequest.html\",\"response\":\"createCreditNoteResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditnotesApi()
credit_note = swagger_client.CreditNote() # CreditNote | The credit note object to be created.

try: 
    # Create a credit note.
    api_response = api_instance.create_credit_note(credit_note)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CreditnotesApi->create_credit_note: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note** | [**CreditNote**](CreditNote.md)| The credit note object to be created. | 

### Return type

[**CreditNotePagedMetadata**](CreditNotePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_by_id**
> CreditNotePagedMetadata get_credit_note_by_id(credit_note_id, organizations=organizations)

Returns a single credit-note, specified by the ID parameter.

{\"nickname\":\"Retrieve an existing credit note\",\"response\":\"getCreditNoteByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditnotesApi()
credit_note_id = 'credit_note_id_example' # str | ID of the credit-note.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single credit-note, specified by the ID parameter.
    api_response = api_instance.get_credit_note_by_id(credit_note_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CreditnotesApi->get_credit_note_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | **str**| ID of the credit-note. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CreditNotePagedMetadata**](CreditNotePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_for_account**
> CreditNotePagedMetadata get_credit_note_for_account(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns credit notes for an account.

{\"nickname\":\"Retrieve by account\",\"response\":\"getCreditNotesByAccount.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditnotesApi()
account_id = 'account_id_example' # str | ID of the account.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first payment to return. (optional) (default to 0)
records = 10 # int | The maximum number of payments to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns credit notes for an account.
    api_response = api_instance.get_credit_note_for_account(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CreditnotesApi->get_credit_note_for_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first payment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of payments to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**CreditNotePagedMetadata**](CreditNotePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_for_invoice**
> CreditNotePagedMetadata get_credit_note_for_invoice(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns credit notes for an invoice.

{\"nickname\":\"Retrieve by invoice\",\"response\":\"getCreditNotesByInvoice.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditnotesApi()
invoice_id = 'invoice_id_example' # str | ID of the Invoice.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first payment to return. (optional) (default to 0)
records = 10 # int | The maximum number of payments to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns credit notes for an invoice.
    api_response = api_instance.get_credit_note_for_invoice(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CreditnotesApi->get_credit_note_for_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| ID of the Invoice. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first payment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of payments to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**CreditNotePagedMetadata**](CreditNotePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_for_subscription**
> CreditNotePagedMetadata get_credit_note_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns credit notes for an subscription.

{\"nickname\":\"Retrieve by subscription\",\"response\":\"getCreditNotesSubscription.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditnotesApi()
subscription_id = 'subscription_id_example' # str | ID of the subscription.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first payment to return. (optional) (default to 0)
records = 10 # int | The maximum number of payments to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns credit notes for an subscription.
    api_response = api_instance.get_credit_note_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CreditnotesApi->get_credit_note_for_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| ID of the subscription. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first payment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of payments to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**CreditNotePagedMetadata**](CreditNotePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retire_credit_note**
> CreditNotePagedMetadata retire_credit_note(credit_note_id, organizations)

Removes any remaining value from credit note

{\"nickname\":\"Removes remaining value from credit note\",\"response\":\"deleteCreditNote.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditnotesApi()
credit_note_id = 'credit_note_id_example' # str | ID of the credit-note.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls.

try: 
    # Removes any remaining value from credit note
    api_response = api_instance.retire_credit_note(credit_note_id, organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CreditnotesApi->retire_credit_note: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | **str**| ID of the credit-note. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | 

### Return type

[**CreditNotePagedMetadata**](CreditNotePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

