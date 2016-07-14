# UserCreationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**organization_id** | **str** | {\&quot;description\&quot;:\&quot;Organization for which the User is created.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;]} | 
**email** | **str** | {\&quot;description\&quot;:\&quot;Login E-mail address of the User.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | 
**first_name** | **str** | {\&quot;description\&quot;:\&quot;First Name of the User.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | 
**last_name** | **str** | {\&quot;description\&quot;:\&quot;Last Name of the User.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | 
**company_name** | **str** | {\&quot;description\&quot;:\&quot;User&#39;s Company.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | 
**password** | **str** | {\&quot;description\&quot;:\&quot;Login Password for the User.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | 
**roles** | **list[str]** | {\&quot;description\&quot;:\&quot;The permission groups the user will belong to.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | 
**send_email** | **bool** | {\&quot;description\&quot;:\&quot;When an email should be sent upon creation.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


