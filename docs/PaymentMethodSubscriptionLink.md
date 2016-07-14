# PaymentMethodSubscriptionLink

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**crm_id** | **str** | { \&quot;description\&quot; : \&quot;CRM ID of the product-rate-plan.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**subscription_id** | **str** | { \&quot;description\&quot; : \&quot;Subscription to add payment method to.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 
**organization_id** | **str** |  | [optional] 
**payment_method_id** | **str** | { \&quot;description\&quot; : \&quot;Payment method to add to subscription.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 
**deleted** | **bool** |  | [optional] [default to False]
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


