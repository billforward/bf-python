# billforward.TokenizationApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_capture**](TokenizationApi.md#auth_capture) | **POST** /tokenization/auth-capture | 
[**braintree_card_capture**](TokenizationApi.md#braintree_card_capture) | **POST** /tokenization/braintree | 
[**create_authorize_net_token**](TokenizationApi.md#create_authorize_net_token) | **POST** /vaulted-gateways/authorize-net | 
[**create_braintree_token**](TokenizationApi.md#create_braintree_token) | **POST** /vaulted-gateways/braintree | 
[**create_stripe_ach_token**](TokenizationApi.md#create_stripe_ach_token) | **POST** /vaulted-gateways/stripe-ACH | 
[**create_stripe_token**](TokenizationApi.md#create_stripe_token) | **POST** /vaulted-gateways/stripe | 
[**create_trust_commerce_token**](TokenizationApi.md#create_trust_commerce_token) | **POST** /vaulted-gateways/trustCommerce | 
[**display_card_capture_form**](TokenizationApi.md#display_card_capture_form) | **GET** /tokenization/card-capture-form | 
[**expire_email_redirect_capture**](TokenizationApi.md#expire_email_redirect_capture) | **DELETE** /tokenization/email-redirect/{id} | 
[**get_all_email_redirect_capture**](TokenizationApi.md#get_all_email_redirect_capture) | **GET** /tokenization/email-redirect | 
[**get_braintree_by_account_id**](TokenizationApi.md#get_braintree_by_account_id) | **GET** /vaulted-gateways/braintree/{accountID} | 
[**get_by_card_details_id**](TokenizationApi.md#get_by_card_details_id) | **GET** /vaulted-gateways/stripe/card-details-id/{cardDetailsID} | 
[**get_email_redirect_capture**](TokenizationApi.md#get_email_redirect_capture) | **GET** /tokenization/email-redirect/{id} | 
[**get_email_redirect_capture_invoice_html**](TokenizationApi.md#get_email_redirect_capture_invoice_html) | **GET** /tokenization/email-redirect/{id}/invoice.html | 
[**get_stripe_ach**](TokenizationApi.md#get_stripe_ach) | **GET** /vaulted-gateways/stripe-ACH/{stripeACHTokenID} | 
[**get_stripe_token**](TokenizationApi.md#get_stripe_token) | **GET** /vaulted-gateways/stripe/{stripeTokenID} | 
[**go_cardless_bank_account_capture**](TokenizationApi.md#go_cardless_bank_account_capture) | **POST** /tokenization/direct-debit | 
[**pay_vision_shout_v1**](TokenizationApi.md#pay_vision_shout_v1) | **POST** /tokenization/payvision-shout-v1 | 
[**pre_auth**](TokenizationApi.md#pre_auth) | **POST** /tokenization/pre-auth | 
[**sage_pay_notify_v300**](TokenizationApi.md#sage_pay_notify_v300) | **POST** /tokenization/sagepay-notify-v3-00 | 
[**sage_pay_shout_v300**](TokenizationApi.md#sage_pay_shout_v300) | **GET** /tokenization/sagepay-shout-v3-00 | 
[**send_email_redirect_capture**](TokenizationApi.md#send_email_redirect_capture) | **POST** /tokenization/email-redirect/{id}/send | 
[**start_email_redirect_capture**](TokenizationApi.md#start_email_redirect_capture) | **POST** /tokenization/email-redirect | 
[**stripe_ach_bank_account_capture**](TokenizationApi.md#stripe_ach_bank_account_capture) | **POST** /tokenization/ach | 
[**stripe_web_hook**](TokenizationApi.md#stripe_web_hook) | **POST** /vaulted-gateways/stripe/webhook | 
[**update_email_redirect_capture**](TokenizationApi.md#update_email_redirect_capture) | **PUT** /tokenization/email-redirect/{id} | 
[**update_profile_with_token**](TokenizationApi.md#update_profile_with_token) | **PUT** /tokenization/profile | 
[**update_stripe_ach_token**](TokenizationApi.md#update_stripe_ach_token) | **PUT** /vaulted-gateways/stripe-ACH | 
[**update_stripe_token**](TokenizationApi.md#update_stripe_token) | **PUT** /vaulted-gateways/stripe | 
[**zooz_card_capture**](TokenizationApi.md#zooz_card_capture) | **POST** /tokenization/zooz | 
[**zooz_web_hook**](TokenizationApi.md#zooz_web_hook) | **POST** /vaulted-gateways/zooz/webhook | 

# **auth_capture**
> InlineResponseDefault40 auth_capture(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = billforward.AuthCaptureRequest() # AuthCaptureRequest |  (optional)

try:
    api_response = api_instance.auth_capture(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->auth_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthCaptureRequest**](AuthCaptureRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault40**](InlineResponseDefault40.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **braintree_card_capture**
> InlineResponseDefault40 braintree_card_capture(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = billforward.BraintreeCaptureRequest() # BraintreeCaptureRequest |  (optional)

try:
    api_response = api_instance.braintree_card_capture(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->braintree_card_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BraintreeCaptureRequest**](BraintreeCaptureRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault40**](InlineResponseDefault40.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_authorize_net_token**
> InlineResponseDefault92 create_authorize_net_token(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = billforward.AuthorizeNetToken() # AuthorizeNetToken |  (optional)

try:
    api_response = api_instance.create_authorize_net_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->create_authorize_net_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizeNetToken**](AuthorizeNetToken.md)|  | [optional] 

### Return type

[**InlineResponseDefault92**](InlineResponseDefault92.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_braintree_token**
> InlineResponseDefault93 create_braintree_token(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = billforward.BraintreeToken() # BraintreeToken |  (optional)

try:
    api_response = api_instance.create_braintree_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->create_braintree_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BraintreeToken**](BraintreeToken.md)|  | [optional] 

### Return type

[**InlineResponseDefault93**](InlineResponseDefault93.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stripe_ach_token**
> InlineResponseDefault94 create_stripe_ach_token(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = billforward.StripeAchToken() # StripeAchToken |  (optional)

try:
    api_response = api_instance.create_stripe_ach_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->create_stripe_ach_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StripeAchToken**](StripeAchToken.md)|  | [optional] 

### Return type

[**InlineResponseDefault94**](InlineResponseDefault94.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stripe_token**
> InlineResponseDefault95 create_stripe_token(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = billforward.StripeToken() # StripeToken |  (optional)

try:
    api_response = api_instance.create_stripe_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->create_stripe_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StripeToken**](StripeToken.md)|  | [optional] 

### Return type

[**InlineResponseDefault95**](InlineResponseDefault95.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_trust_commerce_token**
> InlineResponseDefault96 create_trust_commerce_token(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = billforward.TrustCommerceToken() # TrustCommerceToken |  (optional)

try:
    api_response = api_instance.create_trust_commerce_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->create_trust_commerce_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrustCommerceToken**](TrustCommerceToken.md)|  | [optional] 

### Return type

[**InlineResponseDefault96**](InlineResponseDefault96.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_card_capture_form**
> display_card_capture_form(organizations=organizations, account_id=account_id)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
account_id = 'account_id_example' # str |  (optional)

try:
    api_instance.display_card_capture_form(organizations=organizations, account_id=account_id)
except ApiException as e:
    print("Exception when calling TokenizationApi->display_card_capture_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **account_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expire_email_redirect_capture**
> InlineResponseDefault79 expire_email_redirect_capture(id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
id = 'id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.expire_email_redirect_capture(id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->expire_email_redirect_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault79**](InlineResponseDefault79.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_email_redirect_capture**
> InlineResponseDefault80 get_all_email_redirect_capture(account_id=account_id, subscription_id=subscription_id, invoice_id=invoice_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str |  (optional)
subscription_id = 'subscription_id_example' # str |  (optional)
invoice_id = 'invoice_id_example' # str |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_all_email_redirect_capture(account_id=account_id, subscription_id=subscription_id, invoice_id=invoice_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->get_all_email_redirect_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | [optional] 
 **subscription_id** | **str**|  | [optional] 
 **invoice_id** | **str**|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault80**](InlineResponseDefault80.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_braintree_by_account_id**
> InlineResponseDefault97 get_braintree_by_account_id(account_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_braintree_by_account_id(account_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->get_braintree_by_account_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault97**](InlineResponseDefault97.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_card_details_id**
> InlineResponseDefault98 get_by_card_details_id(card_details_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
card_details_id = 'card_details_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_by_card_details_id(card_details_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->get_by_card_details_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_details_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault98**](InlineResponseDefault98.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_redirect_capture**
> InlineResponseDefault79 get_email_redirect_capture(id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
id = 'id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_email_redirect_capture(id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->get_email_redirect_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault79**](InlineResponseDefault79.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_redirect_capture_invoice_html**
> get_email_redirect_capture_invoice_html(id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
id = 'id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_instance.get_email_redirect_capture_invoice_html(id, organizations=organizations)
except ApiException as e:
    print("Exception when calling TokenizationApi->get_email_redirect_capture_invoice_html: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stripe_ach**
> InlineResponseDefault99 get_stripe_ach(stripe_ach_token_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
stripe_ach_token_id = 'stripe_ach_token_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_stripe_ach(stripe_ach_token_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->get_stripe_ach: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_ach_token_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault99**](InlineResponseDefault99.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stripe_token**
> InlineResponseDefault98 get_stripe_token(stripe_token_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
stripe_token_id = 'stripe_token_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_stripe_token(stripe_token_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->get_stripe_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_token_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault98**](InlineResponseDefault98.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **go_cardless_bank_account_capture**
> InlineResponseDefault40 go_cardless_bank_account_capture(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = billforward.GoCardlessTokenizationRequest() # GoCardlessTokenizationRequest |  (optional)

try:
    api_response = api_instance.go_cardless_bank_account_capture(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->go_cardless_bank_account_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GoCardlessTokenizationRequest**](GoCardlessTokenizationRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault40**](InlineResponseDefault40.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_vision_shout_v1**
> pay_vision_shout_v1(_resource_path=_resource_path, id=id)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
_resource_path = '_resource_path_example' # str |  (optional)
id = 'id_example' # str |  (optional)

try:
    api_instance.pay_vision_shout_v1(_resource_path=_resource_path, id=id)
except ApiException as e:
    print("Exception when calling TokenizationApi->pay_vision_shout_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_resource_path** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_auth**
> InlineResponseDefault81 pre_auth(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = billforward.TokenizationPreAuthRequest() # TokenizationPreAuthRequest |  (optional)

try:
    api_response = api_instance.pre_auth(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->pre_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenizationPreAuthRequest**](TokenizationPreAuthRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault81**](InlineResponseDefault81.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sage_pay_notify_v300**
> sage_pay_notify_v300(vps_protocol=vps_protocol, tx_type=tx_type, vendor_tx_code=vendor_tx_code, status=status, vps_tx_id=vps_tx_id, card_type=card_type, token=token, status_detail=status_detail, last4_digits=last4_digits, vps_signature=vps_signature, expiry_date=expiry_date, organizations=organizations, u=u, access_token=access_token)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
vps_protocol = 'vps_protocol_example' # str |  (optional)
tx_type = 'tx_type_example' # str |  (optional)
vendor_tx_code = 'vendor_tx_code_example' # str |  (optional)
status = 'status_example' # str |  (optional)
vps_tx_id = 'vps_tx_id_example' # str |  (optional)
card_type = 'card_type_example' # str |  (optional)
token = 'token_example' # str |  (optional)
status_detail = 'status_detail_example' # str |  (optional)
last4_digits = 'last4_digits_example' # str |  (optional)
vps_signature = 'vps_signature_example' # str |  (optional)
expiry_date = 'expiry_date_example' # str |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)
u = 'u_example' # str |  (optional)
access_token = 'access_token_example' # str |  (optional)

try:
    api_instance.sage_pay_notify_v300(vps_protocol=vps_protocol, tx_type=tx_type, vendor_tx_code=vendor_tx_code, status=status, vps_tx_id=vps_tx_id, card_type=card_type, token=token, status_detail=status_detail, last4_digits=last4_digits, vps_signature=vps_signature, expiry_date=expiry_date, organizations=organizations, u=u, access_token=access_token)
except ApiException as e:
    print("Exception when calling TokenizationApi->sage_pay_notify_v300: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vps_protocol** | **str**|  | [optional] 
 **tx_type** | **str**|  | [optional] 
 **vendor_tx_code** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **vps_tx_id** | **str**|  | [optional] 
 **card_type** | **str**|  | [optional] 
 **token** | **str**|  | [optional] 
 **status_detail** | **str**|  | [optional] 
 **last4_digits** | **str**|  | [optional] 
 **vps_signature** | **str**|  | [optional] 
 **expiry_date** | **str**|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **u** | **str**|  | [optional] 
 **access_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sage_pay_shout_v300**
> sage_pay_shout_v300(organizations=organizations, s=s, t=t, c=c, e=e, l=l, d=d)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
s = 's_example' # str |  (optional)
t = 't_example' # str |  (optional)
c = 'c_example' # str |  (optional)
e = 'e_example' # str |  (optional)
l = 'l_example' # str |  (optional)
d = 'd_example' # str |  (optional)

try:
    api_instance.sage_pay_shout_v300(organizations=organizations, s=s, t=t, c=c, e=e, l=l, d=d)
except ApiException as e:
    print("Exception when calling TokenizationApi->sage_pay_shout_v300: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **s** | **str**|  | [optional] 
 **t** | **str**|  | [optional] 
 **c** | **str**|  | [optional] 
 **e** | **str**|  | [optional] 
 **l** | **str**|  | [optional] 
 **d** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_redirect_capture**
> InlineResponseDefault79 send_email_redirect_capture(id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
id = 'id_example' # str | 
body = billforward.EmailTokenizationSendAPIRequest() # EmailTokenizationSendAPIRequest |  (optional)

try:
    api_response = api_instance.send_email_redirect_capture(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->send_email_redirect_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**EmailTokenizationSendAPIRequest**](EmailTokenizationSendAPIRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault79**](InlineResponseDefault79.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_email_redirect_capture**
> InlineResponseDefault79 start_email_redirect_capture(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = billforward.EmailTokenizationCreateAPIRequest() # EmailTokenizationCreateAPIRequest |  (optional)

try:
    api_response = api_instance.start_email_redirect_capture(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->start_email_redirect_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailTokenizationCreateAPIRequest**](EmailTokenizationCreateAPIRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault79**](InlineResponseDefault79.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stripe_ach_bank_account_capture**
> InlineResponseDefault40 stripe_ach_bank_account_capture(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = billforward.StripeACHCaptureRequest() # StripeACHCaptureRequest |  (optional)

try:
    api_response = api_instance.stripe_ach_bank_account_capture(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->stripe_ach_bank_account_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StripeACHCaptureRequest**](StripeACHCaptureRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault40**](InlineResponseDefault40.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stripe_web_hook**
> stripe_web_hook(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = 'body_example' # str |  (optional)

try:
    api_instance.stripe_web_hook(body=body)
except ApiException as e:
    print("Exception when calling TokenizationApi->stripe_web_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_redirect_capture**
> InlineResponseDefault79 update_email_redirect_capture(id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
id = 'id_example' # str | 
body = billforward.EmailTokenizationUpdateAPIRequest() # EmailTokenizationUpdateAPIRequest |  (optional)

try:
    api_response = api_instance.update_email_redirect_capture(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->update_email_redirect_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**EmailTokenizationUpdateAPIRequest**](EmailTokenizationUpdateAPIRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault79**](InlineResponseDefault79.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile_with_token**
> InlineResponseDefault82 update_profile_with_token(body=body, request_token=request_token)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = billforward.Profile() # Profile |  (optional)
request_token = 'request_token_example' # str |  (optional)

try:
    api_response = api_instance.update_profile_with_token(body=body, request_token=request_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->update_profile_with_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Profile**](Profile.md)|  | [optional] 
 **request_token** | **str**|  | [optional] 

### Return type

[**InlineResponseDefault82**](InlineResponseDefault82.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stripe_ach_token**
> InlineResponseDefault94 update_stripe_ach_token(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = billforward.StripeAchToken() # StripeAchToken |  (optional)

try:
    api_response = api_instance.update_stripe_ach_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->update_stripe_ach_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StripeAchToken**](StripeAchToken.md)|  | [optional] 

### Return type

[**InlineResponseDefault94**](InlineResponseDefault94.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stripe_token**
> InlineResponseDefault95 update_stripe_token(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = billforward.StripeToken() # StripeToken |  (optional)

try:
    api_response = api_instance.update_stripe_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->update_stripe_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StripeToken**](StripeToken.md)|  | [optional] 

### Return type

[**InlineResponseDefault95**](InlineResponseDefault95.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zooz_card_capture**
> InlineResponseDefault40 zooz_card_capture(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = billforward.ZoozCaptureRequest() # ZoozCaptureRequest |  (optional)

try:
    api_response = api_instance.zooz_card_capture(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenizationApi->zooz_card_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ZoozCaptureRequest**](ZoozCaptureRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault40**](InlineResponseDefault40.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zooz_web_hook**
> zooz_web_hook(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TokenizationApi(billforward.ApiClient(configuration))
body = 'body_example' # str |  (optional)

try:
    api_instance.zooz_web_hook(body=body)
except ApiException as e:
    print("Exception when calling TokenizationApi->zooz_web_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

