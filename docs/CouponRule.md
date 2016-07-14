# CouponRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_rule_id** | **str** | { \&quot;description\&quot; : \&quot;ID of the parent of this coupon-rule.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | { \&quot;description\&quot; : \&quot;ID of the coupon-rule.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**organization_id** | **str** | { \&quot;description\&quot; : \&quot;ID of the organization associated with the coupon-rule.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**coupon_definition_id** | **str** | { \&quot;description\&quot; : \&quot;ID of the coupon-definition associated with the coupon-rule.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**subject** | **str** | { \&quot;description\&quot; : \&quot;The subject of the coupon-rule. The coupon-rule can operate on either the user or subscription that the coupon-instance is associated with.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**polarity** | **str** | { \&quot;description\&quot; : \&quot;Specifies whether the rule&#39;s result will affect the application of the coupon-instance positively or negatively.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**verb** | **str** | { \&quot;description\&quot; : \&quot;The verb of the coupon-rule. coupon-rules can check whether the user or subscription has a certain property.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**preposition** | **str** | { \&quot;description\&quot; : \&quot;This is the comparison operator of the coupon-rule&#39;s parameter and the subject&#39;s object.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**parameter** | **str** | { \&quot;description\&quot; : \&quot;The parameter for the coupon-rule. This specifies the ID or the quantity for the object of the subject.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**object** | **str** | { \&quot;description\&quot; : \&quot;The property of the subject of the coupon-rule. e.g. When the subject is &#39;subscription&#39; and the object is &#39;product-ID&#39;, the coupon-rule will observe the product-ID for that subscription.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**rule_validation_strategy** | **str** | { \&quot;description\&quot; : \&quot;The rule-validation-strategy object associated with the coupon-rule.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**specifier** | **str** | { \&quot;description\&quot; : \&quot;When the subject is subscription, the specifier is used to define which unit of measure the coupon rule will operate on. When the subject is user, the specifier defines which property of the user&#39;s account it will operate on.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**deleted** | **bool** | { \&quot;description\&quot; : \&quot;Has the coupon-modifier been deleted.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [default to False]
**child_rules** | [**list[CouponRule]**](CouponRule.md) | { \&quot;description\&quot; : \&quot;The collection of child coupon-rules associated with the coupon-rule.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


