# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | {\&quot;description\&quot;:\&quot;ID of the user\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | [optional] 
**organization_id** | **str** | {\&quot;description\&quot;:\&quot;ID of the Organization to which the User belongs.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;]} | 
**password** | [**list[Password]**](Password.md) | {\&quot;description\&quot;:\&quot;Passwords associated with the user. A user must have one currently active password to login.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | 
**username** | [**list[Username]**](Username.md) | {\&quot;description\&quot;:\&quot;Usernames associated with the user. A user may have more than one username currently active. Usernames are enforced to be formatted as e-mail addresses.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | 
**password_reset_valid_till** | **datetime** | {\&quot;description\&quot;:\&quot;The UTC DateTime when a password reset would no longer be valid with the current code.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | 
**bf_admin** | **bool** |  | [optional] [default to False]
**account_non_expired** | **bool** | {\&quot;description\&quot;:\&quot;Whether the User has expired.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [default to False]
**account_non_locked** | **bool** | {\&quot;description\&quot;:\&quot;Is the User locked.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | [default to False]
**credentials_non_expired** | **bool** | {\&quot;description\&quot;:\&quot;Are the User credentials expired.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | [default to False]
**enabled** | **bool** | {\&quot;description\&quot;:\&quot;Is the User enabled.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | [default to False]
**timezone** | [**TimeZone**](TimeZone.md) | {\&quot;description\&quot;:\&quot;The timezone used when displaying time series data to the user.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


