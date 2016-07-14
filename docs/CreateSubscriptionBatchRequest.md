# CreateSubscriptionBatchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**organization_id** | **str** | {\&quot;default\&quot;:\&quot;(Auto-populated using your authentication credentials)\&quot;,\&quot;description\&quot;:\&quot;ID of the BillForward Organization within which the requested Subscriptions should be created. If omitted, this will be auto-populated using your authentication credentials.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;]} | [optional] 
**subscriptions** | [**list[CreateSubscriptionRequest]**](CreateSubscriptionRequest.md) | {\&quot;default\&quot;:\&quot;(Empty list)\&quot;,\&quot;description\&quot;:\&quot;List of entities for requesting that subscriptions be created.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;]} | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


