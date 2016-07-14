# MutableBillingEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | ID of the Synchronization Job. | [optional] 
**config_id** | **str** | This is config id which links to this sync job. | 
**organization_id** | **str** | Organization associated with the refund. | 
**state** | **str** | This is the state of job. Pending jobs have not run. Complete jobs have run without error. Failed jobs have one of more errors. Cancelled jobs did not run. | 
**type** | **str** | This is the type of job. Incremental jobs just sync changes, fully jobs sync all data. | 
**scope** | **str** | The scope of the data synch&#39;d. | 
**target** | **str** | This is the target of the job. | 
**name** | **str** | Name of the Job. | 
**description** | **str** | Description of the Job. | 
**data_from** | **datetime** | UTC DateTime of the start of the data to sync. | [optional] 
**data_till** | **datetime** | UTC DateTime of the start of the data to sync. | [optional] 
**started** | **datetime** | UTC DateTime of the end of the data to sync. | [optional] 
**stopped** | **datetime** | UTC DateTime of the start of the data to sync. | [optional] 
**created_by** | **str** | The account who created the synch job. | [optional] 
**max_retry_times** | **int** | The max number of times the records will try to resync. | 
**retry_attempted** | **int** | The number of times the records tried to resync. | 
**deleted** | **bool** | Is the sync job deleted. | [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


