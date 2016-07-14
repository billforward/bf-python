# CouponDiscount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**pricing_component** | **str** | { \&quot;description\&quot; : \&quot;Name or ID of the pricing component to apply the discount to. If not set blank discount is applied at the invoice level.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;] } | [optional] 
**pricing_component_name** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**pricing_component_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**unit_of_measure_name** | **str** |  | [optional] 
**unit_of_measure_id** | **str** |  | [optional] 
**units_free** | **int** | { \&quot;description\&quot; : \&quot;Number of units that are free for a pricing-component.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | [optional] 
**percentage_discount** | **float** | { \&quot;description\&quot; : \&quot;Percentage to be discounted\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | [optional] 
**cash_discount** | **float** | { \&quot;description\&quot; : \&quot;Fixed monetary amount to be discounted\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


