# CouponBookDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | { \&quot;description\&quot; : \&quot;ID of the coupon-book-definition.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**crm_id** | **str** | { \&quot;description\&quot; : \&quot;CRM ID of the product-rate-plan.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**organization_id** | **str** | { \&quot;description\&quot; : \&quot;Organization associated with the coupon-book-definition.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**coupon_definition_id** | **str** | { \&quot;description\&quot; : \&quot;The unique ID of the coupon-definition associated with the coupon-book-definition.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**name** | **str** | { \&quot;description\&quot; : \&quot;The human readable name of the coupon-book-definition.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**description** | **str** | { \&quot;description\&quot; : \&quot;The human readable description of the coupon-book-definition.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**minimum** | **int** | { \&quot;description\&quot; : \&quot;The minimum number of coupon-instances a coupon-book can hold.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**maximum** | **int** | { \&quot;description\&quot; : \&quot;The maximum number of coupon-instances a coupon-book can hold.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**step** | **int** | { \&quot;description\&quot; : \&quot;The stepping parameter between the minimum and the maximum value. E.g. if the minimum is 100, the maximum is 150, and the step is 10, this means the coupon-books can hold 100, 110, 120, 130, 140 or 150 coupon-instances.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**definition_valid_from** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime that the coupon-book-definition is valid from.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**definition_valid_till** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime that the coupon-book-definition is valid until.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**instance_duration** | **int** | { \&quot;description\&quot; : \&quot;Reserved for future use.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**instance_duration_period** | **str** | { \&quot;description\&quot; : \&quot;Reserved for future use.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**state** | **str** | { \&quot;description\&quot; : \&quot;The current state of the coupon-book-definition.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


