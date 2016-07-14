# InvoicePayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_received** | **datetime** | {\&quot;description\&quot;:\&quot;The date when the associated payment was received.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | 
**refund_received** | **datetime** | {\&quot;description\&quot;:\&quot;The date when the associated payment was refunded.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | 
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | { \&quot;description\&quot; : \&quot;ID of the payment-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**crm_id** | **str** | { \&quot;description\&quot; : \&quot;CRM ID of the invoice.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**payment_id** | **str** | { \&quot;description\&quot; : \&quot;ID of the payment used.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**invoice_id** | **str** | { \&quot;description\&quot; : \&quot;ID of the invoice associated with the payment-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**organization_id** | **str** | { \&quot;description\&quot; : \&quot;ID of the organization associated with the invoice-payment.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**currency** | **str** | { \&quot;description\&quot; : \&quot;The currency of the payment specified by a three character ISO 4217 currency code.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**gateway** | **str** | Payment gateway associated with the payment | 
**nominal_amount** | **float** | { \&quot;description\&quot; : \&quot;The value that this payment-line represents.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**actual_amount** | **float** | { \&quot;description\&quot; : \&quot;The value of the payment used by payment-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**refunded_amount** | **float** | { \&quot;description\&quot; : \&quot;The refunded amount of the invoice-payment.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


