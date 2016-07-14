# swagger_client.TokenizationApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_capture**](TokenizationApi.md#auth_capture) | **POST** /tokenization/auth-capture | [Note: this API can be invoked more simply by our client-side card capture library, &lt;a href&#x3D;\&quot;https://github.com/billforward/billforward-js\&quot;&gt;BillForward.js&lt;/a&gt;; you should not need to interact with this API manually unless you have particularly bespoke requirements] 
[**braintree_card_capture**](TokenizationApi.md#braintree_card_capture) | **POST** /tokenization/braintree | [Warning: for use only in PCI-compliant environments; for more information, &lt;a href&#x3D;\&quot;mailto:support@billforward.net\&quot;&gt;contact us&lt;/a&gt; regarding provisioning of your own on-premise BillForward instance] Captures raw credit card details into Braintree&#39;s vault.
[**pay_vision_shout_v1**](TokenizationApi.md#pay_vision_shout_v1) | **POST** /tokenization/payvision-shout-v1 | [Note: this API is intended to be invoked by the PayVision servers -- they are BillForward&#39;s way of informing client-side of the result of card-capture from within an iframe] Generates iframe to which customer will be directed upon success or failure. The iframe contains JavaScript which attempts to send a message to BillForward.js on the client-side, which will handle the result.
[**pre_auth**](TokenizationApi.md#pre_auth) | **POST** /tokenization/pre-auth | [Note: this API can be invoked more simply by our client-side card capture library, &lt;a href&#x3D;\&quot;https://github.com/billforward/billforward-js\&quot;&gt;BillForward.js&lt;/a&gt;; you should not need to interact with this API manually unless you have particularly bespoke requirements] 
[**sage_pay_notify_v300**](TokenizationApi.md#sage_pay_notify_v300) | **POST** /tokenization/sagepay-notify-v3-00 | [Note: this API is intended to be invoked by the SagePay servers -- they are BillForward&#39;s way of receiving a callback from a SagePay card capture operation, using SagePay&#39;s FORM Protocol, v3.0] Handles SagePay Notification.
[**sage_pay_shout_v300**](TokenizationApi.md#sage_pay_shout_v300) | **GET** /tokenization/sagepay-shout-v3-00 | [Note: this API is intended to be invoked by the SagePay servers -- they are BillForward&#39;s way of informing client-side of the result of card-capture from within an iframe, using SagePay&#39;s FORM Protocol, v3.0] Generates iframe to which customer will be directed upon success or failure. The iframe contains JavaScript which attempts to send a message to BillForward.js on the client-side, which will handle the result.


# **auth_capture**
> PaymentMethodPagedMetadata auth_capture(auth_capture_request)

[Note: this API can be invoked more simply by our client-side card capture library, <a href=\"https://github.com/billforward/billforward-js\">BillForward.js</a>; you should not need to interact with this API manually unless you have particularly bespoke requirements] 

{\"nickname\":\"Authorized card capture\",\"response\":\"BFJSAuthCapture.html\",\"request\":\"BFJSAuthCapture.request.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenizationApi()
auth_capture_request = swagger_client.AuthCaptureRequest() # AuthCaptureRequest | The auth capture request.

try: 
    # [Note: this API can be invoked more simply by our client-side card capture library, <a href=\"https://github.com/billforward/billforward-js\">BillForward.js</a>; you should not need to interact with this API manually unless you have particularly bespoke requirements] 
    api_response = api_instance.auth_capture(auth_capture_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TokenizationApi->auth_capture: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_capture_request** | [**AuthCaptureRequest**](AuthCaptureRequest.md)| The auth capture request. | 

### Return type

[**PaymentMethodPagedMetadata**](PaymentMethodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **braintree_card_capture**
> PaymentMethodPagedMetadata braintree_card_capture(body=body)

[Warning: for use only in PCI-compliant environments; for more information, <a href=\"mailto:support@billforward.net\">contact us</a> regarding provisioning of your own on-premise BillForward instance] Captures raw credit card details into Braintree's vault.

{\"nickname\":\"Braintree Tokenization\",\"response\":\"braintreeDirectTokenization.html\",\"request\":\"braintreeDirectTokenization.request.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenizationApi()
body = swagger_client.BraintreeCaptureRequest() # BraintreeCaptureRequest |  (optional)

try: 
    # [Warning: for use only in PCI-compliant environments; for more information, <a href=\"mailto:support@billforward.net\">contact us</a> regarding provisioning of your own on-premise BillForward instance] Captures raw credit card details into Braintree's vault.
    api_response = api_instance.braintree_card_capture(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TokenizationApi->braintree_card_capture: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BraintreeCaptureRequest**](BraintreeCaptureRequest.md)|  | [optional] 

### Return type

[**PaymentMethodPagedMetadata**](PaymentMethodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_vision_shout_v1**
> str pay_vision_shout_v1(_resource_path=_resource_path, id=id)

[Note: this API is intended to be invoked by the PayVision servers -- they are BillForward's way of informing client-side of the result of card-capture from within an iframe] Generates iframe to which customer will be directed upon success or failure. The iframe contains JavaScript which attempts to send a message to BillForward.js on the client-side, which will handle the result.

{\"nickname\":\"Generate PayVision iframe redirect\",\"response\":\"payVisionShoutV1.html\",\"request\":\"payVisionShoutV1.request.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenizationApi()
_resource_path = '_resource_path_example' # str |  (optional)
id = 'id_example' # str |  (optional)

try: 
    # [Note: this API is intended to be invoked by the PayVision servers -- they are BillForward's way of informing client-side of the result of card-capture from within an iframe] Generates iframe to which customer will be directed upon success or failure. The iframe contains JavaScript which attempts to send a message to BillForward.js on the client-side, which will handle the result.
    api_response = api_instance.pay_vision_shout_v1(_resource_path=_resource_path, id=id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TokenizationApi->pay_vision_shout_v1: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_resource_path** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_auth**
> TokenizationPreAuthPagedMetadata pre_auth(pre_auth_request)

[Note: this API can be invoked more simply by our client-side card capture library, <a href=\"https://github.com/billforward/billforward-js\">BillForward.js</a>; you should not need to interact with this API manually unless you have particularly bespoke requirements] 

{\"nickname\":\"Pre-authorize card capture\",\"response\":\"BFJSPreAuth.html\",\"request\":\"BFJSPreAuth.request.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenizationApi()
pre_auth_request = swagger_client.InsertableBillingEntity() # InsertableBillingEntity | The auth request.

try: 
    # [Note: this API can be invoked more simply by our client-side card capture library, <a href=\"https://github.com/billforward/billforward-js\">BillForward.js</a>; you should not need to interact with this API manually unless you have particularly bespoke requirements] 
    api_response = api_instance.pre_auth(pre_auth_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TokenizationApi->pre_auth: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pre_auth_request** | [**InsertableBillingEntity**](InsertableBillingEntity.md)| The auth request. | 

### Return type

[**TokenizationPreAuthPagedMetadata**](TokenizationPreAuthPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sage_pay_notify_v300**
> str sage_pay_notify_v300(organizations=organizations, bill_forward_url_root=bill_forward_url_root, access_token=access_token, vps_protocol=vps_protocol, tx_type=tx_type, vendor_tx_code=vendor_tx_code, status=status, vps_tx_id=vps_tx_id, card_type=card_type, token=token, status_detail=status_detail, last4_digits=last4_digits, vps_signature=vps_signature, expiry_date=expiry_date)

[Note: this API is intended to be invoked by the SagePay servers -- they are BillForward's way of receiving a callback from a SagePay card capture operation, using SagePay's FORM Protocol, v3.0] Handles SagePay Notification.

{\"nickname\":\"Handle SagePay Notification\",\"response\":\"sagePayNotifyV3_00.html\",\"request\":\"sagePayNotifyV3_00.request.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenizationApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls.Multiple organization-IDs may be specified by repeated use of the queryparameter. Example: ...&organizations=org1&organizations=org2 (optional)
bill_forward_url_root = 'bill_forward_url_root_example' # str | The URL through which BFJS connected to BillForward. (optional)
access_token = 'access_token_example' # str | The public token through which BFJS connected to BillForward. (optional)
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

try: 
    # [Note: this API is intended to be invoked by the SagePay servers -- they are BillForward's way of receiving a callback from a SagePay card capture operation, using SagePay's FORM Protocol, v3.0] Handles SagePay Notification.
    api_response = api_instance.sage_pay_notify_v300(organizations=organizations, bill_forward_url_root=bill_forward_url_root, access_token=access_token, vps_protocol=vps_protocol, tx_type=tx_type, vendor_tx_code=vendor_tx_code, status=status, vps_tx_id=vps_tx_id, card_type=card_type, token=token, status_detail=status_detail, last4_digits=last4_digits, vps_signature=vps_signature, expiry_date=expiry_date)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TokenizationApi->sage_pay_notify_v300: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls.Multiple organization-IDs may be specified by repeated use of the queryparameter. Example: ...&amp;organizations&#x3D;org1&amp;organizations&#x3D;org2 | [optional] 
 **bill_forward_url_root** | **str**| The URL through which BFJS connected to BillForward. | [optional] 
 **access_token** | **str**| The public token through which BFJS connected to BillForward. | [optional] 
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

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sage_pay_shout_v300**
> str sage_pay_shout_v300(organizations=organizations, s=s, t=t, c=c, e=e, l=l, d=d)

[Note: this API is intended to be invoked by the SagePay servers -- they are BillForward's way of informing client-side of the result of card-capture from within an iframe, using SagePay's FORM Protocol, v3.0] Generates iframe to which customer will be directed upon success or failure. The iframe contains JavaScript which attempts to send a message to BillForward.js on the client-side, which will handle the result.

{\"nickname\":\"Generate SagePay iframe redirect\",\"response\":\"sagePayShoutV3_00.html\",\"request\":\"sagePayShoutV3_00.request.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenizationApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls.Multiple organization-IDs may be specified by repeated use of the queryparameter. Example: ...&organizations=org1&organizations=org2 (optional)
s = 's_example' # str |  (optional)
t = 't_example' # str |  (optional)
c = 'c_example' # str |  (optional)
e = 'e_example' # str |  (optional)
l = 'l_example' # str |  (optional)
d = 'd_example' # str |  (optional)

try: 
    # [Note: this API is intended to be invoked by the SagePay servers -- they are BillForward's way of informing client-side of the result of card-capture from within an iframe, using SagePay's FORM Protocol, v3.0] Generates iframe to which customer will be directed upon success or failure. The iframe contains JavaScript which attempts to send a message to BillForward.js on the client-side, which will handle the result.
    api_response = api_instance.sage_pay_shout_v300(organizations=organizations, s=s, t=t, c=c, e=e, l=l, d=d)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TokenizationApi->sage_pay_shout_v300: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls.Multiple organization-IDs may be specified by repeated use of the queryparameter. Example: ...&amp;organizations&#x3D;org1&amp;organizations&#x3D;org2 | [optional] 
 **s** | **str**|  | [optional] 
 **t** | **str**|  | [optional] 
 **c** | **str**|  | [optional] 
 **e** | **str**|  | [optional] 
 **l** | **str**|  | [optional] 
 **d** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

