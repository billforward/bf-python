# FixedTerm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | id | [optional] 
**subscription_id** | **str** | { \&quot;description\&quot; : \&quot;subscriptionID\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**organization_id** | **str** | { \&quot;description\&quot; : \&quot;The ID of the organization associated with the amendment.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**fixed_term_definition_id** | **str** | { \&quot;description\&quot; : \&quot;fixedTermDefinitionID\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**fixed_term_definition** | [**MutableBillingEntity**](MutableBillingEntity.md) |  | 
**expiry_behaviour** | **str** | fixedTermExpiryBehaviour | 
**state** | **str** | state | 
**product_rate_plan_as_of_time** | **datetime** | productRatePlanAsOfTime | 
**compound_uplift** | **float** | { \&quot;description\&quot; : \&quot;compoundUplift\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] }The proportional INCREASE in price applied every time the fixed terms recur. e.g. 0.03 is a 3% increase. -0.5 is a 50% decrease. 3 is a 300% increase | 
**start_time** | **datetime** | start_time | 
**expiry_time** | **datetime** | expiry_time | 
**periods** | **int** | { \&quot;description\&quot; : \&quot;The number of billing periods that this fixed term lasts for.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**fixed_term_number** | **int** | { \&quot;description\&quot; : \&quot;The number of sequential fixed terms previous to this one for the subscription (i.e. zero indexed &#39;fixedTermCount&#39;).\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**deleted** | **bool** | { \&quot;description\&quot; : \&quot;Is the fixedTerm deleted.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


