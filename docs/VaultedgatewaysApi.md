# billforward.VaultedgatewaysApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authorize_net_token**](VaultedgatewaysApi.md#create_authorize_net_token) | **POST** /vaulted-gateways/authorize-net | Create an authorize-net-token.
[**create_braintree_token**](VaultedgatewaysApi.md#create_braintree_token) | **POST** /vaulted-gateways/braintree | Create a braintree-token.
[**create_stripe_ach_token**](VaultedgatewaysApi.md#create_stripe_ach_token) | **POST** /vaulted-gateways/stripe-ACH | Create a stripe-ACH-token.
[**create_stripe_token**](VaultedgatewaysApi.md#create_stripe_token) | **POST** /vaulted-gateways/stripe | Create a stripe-token.
[**create_trust_commerce_token**](VaultedgatewaysApi.md#create_trust_commerce_token) | **POST** /vaulted-gateways/trustCommerce | Create a trust-commerce-token.
[**get_braintree_by_account_id**](VaultedgatewaysApi.md#get_braintree_by_account_id) | **GET** /vaulted-gateways/braintree/{accountID} | Returns a list of braintree-tokens backing PaymentMethods belonging to the specified account parameter.
[**get_by_card_details_id**](VaultedgatewaysApi.md#get_by_card_details_id) | **GET** /vaulted-gateways/stripe/card-details-id/{cardDetailsID} | Returns a single stripe-token, specified by the cardDetailsID parameter.
[**get_stripe_ach**](VaultedgatewaysApi.md#get_stripe_ach) | **GET** /vaulted-gateways/stripe-ACH/{stripeACHTokenID} | Returns a single stripe-ACH-token, specified by the stripeACHTokenID parameter.
[**get_stripe_token**](VaultedgatewaysApi.md#get_stripe_token) | **GET** /vaulted-gateways/stripe/{stripeTokenID} | Returns a single stripe-token, specified by the stripeTokenID parameter.
[**update_stripe_ach_token**](VaultedgatewaysApi.md#update_stripe_ach_token) | **PUT** /vaulted-gateways/stripe-ACH | Update a stripe-ACH-token.
[**update_stripe_token**](VaultedgatewaysApi.md#update_stripe_token) | **PUT** /vaulted-gateways/stripe | Update a stripe-token.
[**verify_bank_account**](VaultedgatewaysApi.md#verify_bank_account) | **POST** /vaulted-gateways/stripe/verify-bank-account | Verify Stripe bank account.
[**webhook**](VaultedgatewaysApi.md#webhook) | **POST** /vaulted-gateways/stripe/webhook | Receive and handle webhook from Stripe.


# **create_authorize_net_token**
> AuthorizeNetTokenPagedMetadata create_authorize_net_token(authorize_net_token)

Create an authorize-net-token.

{\"nickname\":\"Create a authorize-net-token\",\"request\":\"createAuthorizeNetTokenRequest.html\",\"response\":\"createAuthorizeNetTokenResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.VaultedgatewaysApi()
authorize_net_token = billforward.MutableBillingEntity() # MutableBillingEntity | The authorize-net-token object to be created.

try: 
    # Create an authorize-net-token.
    api_response = api_instance.create_authorize_net_token(authorize_net_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultedgatewaysApi->create_authorize_net_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorize_net_token** | [**MutableBillingEntity**](MutableBillingEntity.md)| The authorize-net-token object to be created. | 

### Return type

[**AuthorizeNetTokenPagedMetadata**](AuthorizeNetTokenPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_braintree_token**
> BraintreeTokenPagedMetadata create_braintree_token(braintree_token)

Create a braintree-token.

{\"nickname\":\"Create a braintree-token\",\"request\":\"createBraintreeTokenRequest.html\",\"response\":\"BraintreeTokenResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.VaultedgatewaysApi()
braintree_token = billforward.MutableBillingEntity() # MutableBillingEntity | The braintree-token object to be created.

try: 
    # Create a braintree-token.
    api_response = api_instance.create_braintree_token(braintree_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultedgatewaysApi->create_braintree_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **braintree_token** | [**MutableBillingEntity**](MutableBillingEntity.md)| The braintree-token object to be created. | 

### Return type

[**BraintreeTokenPagedMetadata**](BraintreeTokenPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stripe_ach_token**
> StripeACHTokenPagedMetadata create_stripe_ach_token(stripe_ach_token)

Create a stripe-ACH-token.

{\"nickname\":\"Create a stripe-ACH-token\",\"request\":\"createstripeACHTokenRequest.html\",\"response\":\"createstripeACHTokenResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.VaultedgatewaysApi()
stripe_ach_token = billforward.MutableBillingEntity() # MutableBillingEntity | The stripe-ACH-token object to be created.

try: 
    # Create a stripe-ACH-token.
    api_response = api_instance.create_stripe_ach_token(stripe_ach_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultedgatewaysApi->create_stripe_ach_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_ach_token** | [**MutableBillingEntity**](MutableBillingEntity.md)| The stripe-ACH-token object to be created. | 

### Return type

[**StripeACHTokenPagedMetadata**](StripeACHTokenPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stripe_token**
> StripeTokenPagedMetadata create_stripe_token(stripe_token)

Create a stripe-token.

{\"nickname\":\"Create a stripe-token\",\"request\":\"createstripeTokenRequest.html\",\"response\":\"createstripeTokenResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.VaultedgatewaysApi()
stripe_token = billforward.MutableBillingEntity() # MutableBillingEntity | The stripe-token object to be created.

try: 
    # Create a stripe-token.
    api_response = api_instance.create_stripe_token(stripe_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultedgatewaysApi->create_stripe_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_token** | [**MutableBillingEntity**](MutableBillingEntity.md)| The stripe-token object to be created. | 

### Return type

[**StripeTokenPagedMetadata**](StripeTokenPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_trust_commerce_token**
> TrustCommerceTokenPagedMetadata create_trust_commerce_token(trust_commerce_token)

Create a trust-commerce-token.

{\"nickname\":\"Create a trust-commerce-token\",\"request\":\"createTrustCommerceTokenRequest.html\",\"response\":\"TrustCommerceTokenResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.VaultedgatewaysApi()
trust_commerce_token = billforward.MutableBillingEntity() # MutableBillingEntity | The trust-commerce-token object to be created.

try: 
    # Create a trust-commerce-token.
    api_response = api_instance.create_trust_commerce_token(trust_commerce_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultedgatewaysApi->create_trust_commerce_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trust_commerce_token** | [**MutableBillingEntity**](MutableBillingEntity.md)| The trust-commerce-token object to be created. | 

### Return type

[**TrustCommerceTokenPagedMetadata**](TrustCommerceTokenPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_braintree_by_account_id**
> BraintreeTokenPagedMetadata get_braintree_by_account_id(account_id, organizations=organizations)

Returns a list of braintree-tokens backing PaymentMethods belonging to the specified account parameter.

{\"nickname\":\"Retrieve a list of braintree-token\",\"response\":\"getBraintreeByAccountID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.VaultedgatewaysApi()
account_id = 'account_id_example' # str | The string ID of the account-ID.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls.Multiple organization-IDs may be specified by repeated use of the query parameter. Example: ...&organizations=org1&organizations=org2 (optional)

try: 
    # Returns a list of braintree-tokens backing PaymentMethods belonging to the specified account parameter.
    api_response = api_instance.get_braintree_by_account_id(account_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultedgatewaysApi->get_braintree_by_account_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The string ID of the account-ID. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls.Multiple organization-IDs may be specified by repeated use of the query parameter. Example: ...&amp;organizations&#x3D;org1&amp;organizations&#x3D;org2 | [optional] 

### Return type

[**BraintreeTokenPagedMetadata**](BraintreeTokenPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_card_details_id**
> StripeTokenPagedMetadata get_by_card_details_id(card_details_id, organizations=organizations)

Returns a single stripe-token, specified by the cardDetailsID parameter.

{\"nickname\":\"Retrieve a stripe-token by cardDetailsID\",\"response\":\"getStripeTokenByCardDetailsID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.VaultedgatewaysApi()
card_details_id = 'card_details_id_example' # str | The card details id of the stripe-token.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single stripe-token, specified by the cardDetailsID parameter.
    api_response = api_instance.get_by_card_details_id(card_details_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultedgatewaysApi->get_by_card_details_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_details_id** | **str**| The card details id of the stripe-token. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**StripeTokenPagedMetadata**](StripeTokenPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stripe_ach**
> StripeACHTokenPagedMetadata get_stripe_ach(stripe_ach_token_id, organizations=organizations)

Returns a single stripe-ACH-token, specified by the stripeACHTokenID parameter.

{\"nickname\":\"Retrieve a stripe-ACH-token\",\"response\":\"getStripeACHTokenByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.VaultedgatewaysApi()
stripe_ach_token_id = 'stripe_ach_token_id_example' # str | The string ID of the stripe-ACH-token.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls.Multiple organization-IDs may be specified by repeated use of the query parameter. Example: ...&organizations=org1&organizations=org2 (optional)

try: 
    # Returns a single stripe-ACH-token, specified by the stripeACHTokenID parameter.
    api_response = api_instance.get_stripe_ach(stripe_ach_token_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultedgatewaysApi->get_stripe_ach: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_ach_token_id** | **str**| The string ID of the stripe-ACH-token. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls.Multiple organization-IDs may be specified by repeated use of the query parameter. Example: ...&amp;organizations&#x3D;org1&amp;organizations&#x3D;org2 | [optional] 

### Return type

[**StripeACHTokenPagedMetadata**](StripeACHTokenPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stripe_token**
> StripeTokenPagedMetadata get_stripe_token(stripe_token_id, organizations=organizations)

Returns a single stripe-token, specified by the stripeTokenID parameter.

{\"nickname\":\"Retrieve a stripe-token\",\"response\":\"getStripeTokenByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.VaultedgatewaysApi()
stripe_token_id = 'stripe_token_id_example' # str | The string ID of the stripe-token.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls.Multiple organization-IDs may be specified by repeated use of the query parameter. Example: ...&organizations=org1&organizations=org2 (optional)

try: 
    # Returns a single stripe-token, specified by the stripeTokenID parameter.
    api_response = api_instance.get_stripe_token(stripe_token_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultedgatewaysApi->get_stripe_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_token_id** | **str**| The string ID of the stripe-token. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls.Multiple organization-IDs may be specified by repeated use of the query parameter. Example: ...&amp;organizations&#x3D;org1&amp;organizations&#x3D;org2 | [optional] 

### Return type

[**StripeTokenPagedMetadata**](StripeTokenPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stripe_ach_token**
> StripeACHTokenPagedMetadata update_stripe_ach_token(stripe_token)

Update a stripe-ACH-token.

{\"nickname\":\"Update a stripe-ACH-token\",\"request\":\"updatestripeACHTokenRequest.html\",\"response\":\"updatestripeACHTokenResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.VaultedgatewaysApi()
stripe_token = billforward.MutableBillingEntity() # MutableBillingEntity | The stripe-ACH-token object to be updated.

try: 
    # Update a stripe-ACH-token.
    api_response = api_instance.update_stripe_ach_token(stripe_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultedgatewaysApi->update_stripe_ach_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_token** | [**MutableBillingEntity**](MutableBillingEntity.md)| The stripe-ACH-token object to be updated. | 

### Return type

[**StripeACHTokenPagedMetadata**](StripeACHTokenPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stripe_token**
> StripeTokenPagedMetadata update_stripe_token(stripe_token)

Update a stripe-token.

{\"nickname\":\"Update a stripe-token\",\"request\":\"updatestripeTokenRequest.html\",\"response\":\"updatestripeTokenResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.VaultedgatewaysApi()
stripe_token = billforward.MutableBillingEntity() # MutableBillingEntity | The stripe-token object to be updated.

try: 
    # Update a stripe-token.
    api_response = api_instance.update_stripe_token(stripe_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultedgatewaysApi->update_stripe_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_token** | [**MutableBillingEntity**](MutableBillingEntity.md)| The stripe-token object to be updated. | 

### Return type

[**StripeTokenPagedMetadata**](StripeTokenPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_bank_account**
> BankAccountVerificationPagedMetadata verify_bank_account(bank_account_verification)

Verify Stripe bank account.

{\"nickname\":\"Verify Stripe bank account\",\"response\":\"verifyStripeBankAccount.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.VaultedgatewaysApi()
bank_account_verification = billforward.BillingEntityBase() # BillingEntityBase | The Bank-Account-Verification object.

try: 
    # Verify Stripe bank account.
    api_response = api_instance.verify_bank_account(bank_account_verification)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultedgatewaysApi->verify_bank_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_verification** | [**BillingEntityBase**](BillingEntityBase.md)| The Bank-Account-Verification object. | 

### Return type

[**BankAccountVerificationPagedMetadata**](BankAccountVerificationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook**
> str webhook(event)

Receive and handle webhook from Stripe.

{\"nickname\":\"Receive Stripe webhook\",\"response\":\"receiveStripeWebhook.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.VaultedgatewaysApi()
event = billforward.Event() # Event | The event received.

try: 
    # Receive and handle webhook from Stripe.
    api_response = api_instance.webhook(event)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultedgatewaysApi->webhook: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | [**Event**](Event.md)| The event received. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

