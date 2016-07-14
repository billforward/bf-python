# ProductCouponModifier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | { \&quot;description\&quot; : \&quot;ID of the coupon-modifier.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**organization_id** | **str** | { \&quot;description\&quot; : \&quot;ID of the organization associated with the coupon-modifier.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**coupon_definition_id** | **str** | { \&quot;description\&quot; : \&quot;The unique ID of the coupon-definition associated with the coupon-modifier.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**effect_amount** | **float** | { \&quot;description\&quot; : \&quot;The effect amount for the coupon-modifier. This is affected by the operand field.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**operand** | **str** | { \&quot;description\&quot; : \&quot;The operand field affects the effect amount of the coupon-modifier. If the operand is fixed, it is an exact amount of the currency defined by the coupon-definition. If the operand is percent, this means the coupon will be affecting a percentage of the unaltered cost. E.g. a 25% modifier will apply a 25% discount on a subscription or a pricing-component.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**effect** | **str** | { \&quot;description\&quot; : \&quot;The effect of the coupon-modifier. The coupon-modifier can affect first, last, and cheapest value of a specific unit-of-measure-id for a subscription. The coupon-modifier can also affect all of the values for a unit-of-measure-id, or can affect all of the subscription cost.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**effect_additional** | **bool** | { \&quot;description\&quot; : \&quot;Specifies whether the coupon-modifier will be affecting only additional units. If this field is set, the coupon-instance-existing-values for the coupon-instance are observed, and any units of the unit-of-measure-id defined by the modifier below the coupon-instance-existing-values for that unit-of-measure-id will be ignored.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [default to False]
**specifier_amount** | **int** | { \&quot;description\&quot; : \&quot;The number of units that will be affected by the coupon-modifier, if the domain is set to uom\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**domain** | **str** | { \&quot;description\&quot; : \&quot;The domain of the coupon-modifier\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**specifier** | **str** | { \&quot;description\&quot; : \&quot;The specifier is domain-specific. If the domain is uom, this field is used to limit the coupon-modifier to a specific unit-of-measure-id.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**precedence** | **int** | { \&quot;description\&quot; : \&quot;The precedence of the coupon-modifier. This is used to order application of coupon-modifiers. Higher precedence means the coupon-modifier will be applied before others.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**deleted** | **bool** | { \&quot;description\&quot; : \&quot;Has the coupon-modifier been deleted.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


