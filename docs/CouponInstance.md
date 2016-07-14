# CouponInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **str** | { \&quot;description\&quot; : \&quot;Target ID of the coupon-instance. If the target is subscription, this is the subscription&#39;s ID. If the target is account, this is the account&#39;s ID.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**coupon_code** | **str** | { \&quot;description\&quot; : \&quot;Code for the coupon. This code can be used to apply coupon-instances to subscriptions or accounts.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**date_initialised** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime the coupon was initialised.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**valid_till** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime the coupon-instance is valid until.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | { \&quot;description\&quot; : \&quot;ID of the coupon-instance.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**crm_id** | **str** | { \&quot;description\&quot; : \&quot;CRM ID of the product-rate-plan.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**organization_id** | **str** | { \&quot;description\&quot; : \&quot;Organization associated with the\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**book_id** | **str** | { \&quot;description\&quot; : \&quot;ID of the coupon-book associated with the coupon-instance.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**coupon_definition_id** | **str** | { \&quot;description\&quot; : \&quot;ID of the coupon-definition associated with the coupon-instance.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**target** | **str** | { \&quot;description\&quot; : \&quot;Ttype of the target for the coupon-instance. Used in combination with the targetID.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**periods_valid_for** | **int** | { \&quot;description\&quot; : \&quot;Number of subscription periods the coupon is valid for. Unused.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**total_periods** | **int** | { \&quot;description\&quot; : \&quot;Unused.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**remaining_uses** | **int** | { \&quot;description\&quot; : \&quot;The number of remaining uses the coupon-instance has left.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**instance_discount_value** | **float** | { \&quot;description\&quot; : \&quot;(Optional) The value to be used for dynamic price calculation, if the coupon definition has an &#39;instance&#39; or &#39;instance_percent&#39; coupon modifier. If it is not set, the effect amount of the coupon modifier will be used.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**max_remaining_uses** | **int** | { \&quot;description\&quot; : \&quot;The number of remaining uses the coupon-instance had upon initialisation.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**coupon_instance_existing_values** | [**list[CouponInstanceExistingValue]**](CouponInstanceExistingValue.md) | { \&quot;description\&quot; : \&quot;The collection of coupon-instance-existing-value objects associated with the coupon-instance.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


