# PaymentMethod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | { \&quot;description\&quot; : \&quot;ID of the payment-method.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**crm_id** | **str** | { \&quot;description\&quot; : \&quot;CRM ID of the product-rate-plan.\&quot;, \&quot;verbs\&quot;:] } | [optional] 
**account_id** | **str** | { \&quot;description\&quot; : \&quot;ID of the account associated with the payment-method.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 
**organization_id** | **str** |  | [optional] 
**name** | **str** | { \&quot;description\&quot; : \&quot;Name of the payment-method.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**description** | **str** | { \&quot;description\&quot; : \&quot;Description of the payment-method.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**card_holder_name** | **str** | { \&quot;description\&quot; : \&quot;Name of the card holder\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**expiry_date** | **str** | { \&quot;description\&quot; : \&quot;In the case of card payment methods this is the expiry date of the card, format should be MMYY including leading 0&#39;s. For example 0115 for January 2015.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 
**card_type** | **str** | { \&quot;description\&quot; : \&quot;Type of the card. In the case of card payment methods this is the payment type, for example VISA, MasterCard.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | [optional] 
**country** | **str** |  | [optional] 
**province** | **str** |  | [optional] 
**first_six** | **str** |  | [optional] 
**last_four** | **str** |  | [optional] 
**expiry_year** | **int** |  | [optional] 
**expiry_month** | **int** |  | [optional] 
**link_id** | **str** |  | 
**gateway** | **str** | { \&quot;description\&quot; : \&quot;Gateway type for payment-method.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 
**ip_address** | **str** | {\&quot;description\&quot;:\&quot;IP address associated with this payment method.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | [optional] 
**ip_address_country** | **str** | {\&quot;description\&quot;:\&quot;Country of the IP address associated with this payment method.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | [optional] 
**state** | **str** | { \&quot;description\&quot; : \&quot;State of the payment-method.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 
**deleted** | **bool** | {\&quot;default\&quot; : \&quot;false\&quot;, \&quot;description\&quot; : \&quot;Indicates if a payment-method has been retired. If a payment-method has been retired it can still be retrieved using the appropriate flag on API requests. Generally payment-methods will be retired by customers wanting to remove the payment method from their account. Caution should be used when requested deleted payment methods.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] [default to False]
**default_payment_method** | **bool** | {\&quot;default\&quot; : \&quot;false\&quot;, \&quot;description\&quot; : \&quot;Indicates if this is the default payment method for the account.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;,\&quot;PUT\&quot;]  } | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


