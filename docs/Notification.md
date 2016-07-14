# Notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | { \&quot;description\&quot; : \&quot;ID of the notification.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**domain** | **str** | { \&quot;description\&quot; : \&quot;The domain of the notification.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**action** | **str** | { \&quot;description\&quot; : \&quot;The action associated with the notification.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**organization_id** | **str** | { \&quot;description\&quot; : \&quot;Organization associated with the notification.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**webhook_id** | **str** | { \&quot;description\&quot; : \&quot;Webhook associated with the notification.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**entity_id** | **str** | { \&quot;description\&quot; : \&quot;The id of the entity associated with the notification.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**destination_url** | **str** | { \&quot;description\&quot; : \&quot;The URL the notification will be sent to.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**format** | **str** | { \&quot;description\&quot; : \&quot;Format of the notification.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**ack_enabled** | **bool** | { \&quot;description\&quot; : \&quot;If true notifications will continue to be sent until an acknowledgment is received.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [default to False]
**entity** | **list[str]** |  | [optional] 
**changes** | **list[str]** |  | [optional] 
**last_send_attempt** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime of the notifications&#39;s last send attempt.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**next_send_attempt** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime of the notification&#39;s next send attempt.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**final_send_attempt** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime of the notification&#39;s final send attempt.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**total_send_attempts** | **int** | { \&quot;description\&quot; : \&quot;The number of send attempts for this notification.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**state** | **str** | { \&quot;description\&quot; : \&quot;Whether the notification has been sent.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**acked** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the notification was acked if it is ack enabled.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


