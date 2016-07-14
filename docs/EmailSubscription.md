# EmailSubscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | { \&quot;description\&quot; : \&quot;ID of the email provider.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**organization_id** | **str** | { \&quot;description\&quot; : \&quot;ID of the organization associated with the email provider.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**type** | **str** |  | [optional] 
**state** | **str** |  | 
**_from** | **str** |  | 
**bcc** | **str** |  | [optional] 
**cc** | **str** |  | [optional] 
**subject_template** | **str** |  | [optional] 
**send_to_customer** | **bool** |  | [optional] [default to False]
**attach_invoice** | **bool** |  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


