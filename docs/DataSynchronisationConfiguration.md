# DataSynchronisationConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | ID of the Synchronization Configuration. | [optional] 
**organization_id** | **str** | Organization associated with Synchronization Configuration. | 
**username** | **str** | This is the username for the platform. | 
**access_token** | **str** | This is the token for the platform. | 
**refresh_token** | **str** | This is the refresh token for the platform. | 
**instance_url** | **str** | This is the instance url for client&#39;s salesforce instance. | 
**platform** | **str** | This is the platform of the job. | 
**max_failed_retry** | **int** | This is maximum of the retry attempts when a synch is failed. | [optional] 
**synch_interval** | **int** | This is interval between each sync. | [optional] 
**deleted** | **bool** | Is the sync job deleted. | [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


