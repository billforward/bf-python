# CancellationAmendment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**type** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;default\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 
**id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**organization_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;\&quot;] } | [optional] 
**subscription_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**amendment_type** | **str** | { \&quot;description\&quot; : \&quot;Type of amendment\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 
**actioning_time** | **datetime** | { \&quot;description\&quot; : \&quot;When the amendment will run\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**actioned_time** | **datetime** | { \&quot;description\&quot; : \&quot;The time the amendment completed.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**state** | **str** | Whether the subscription-amendment is: pending (to be actioned in the future), succeeded (actioning completed), failed (actioning was attempted but no effect was made) or discarded (the amendment had been cancelled before being actioned). Default: Pending | 
**deleted** | **bool** | { \&quot;description\&quot; : \&quot;Is the amendment deleted.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [default to False]
**source** | **str** | { \&quot;description\&quot; : \&quot;Explanation for cancellation\&quot;, \&quot;default\&quot; : \&quot;API\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 
**subscription_cancellation_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**service_end** | **str** | { \&quot;description\&quot; : \&quot;If the serviceEnd parameter is &lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;AtPeriodEnd&lt;/span&gt; the cancellation will be delayed till the end of the current period.\&quot;, \&quot;default\&quot; : \&quot;AtPeriodEnd\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 
**cancellation_credit** | **str** | Specifies whether the service will end immediately on cancellation or if it will continue until the end of the current period. Default: AtPeriodEnd | 
**subscription_cancellation** | [**MutableBillingEntity**](MutableBillingEntity.md) | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[] } | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


