# UnitOfMeasurePagedMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** | {\&quot;description\&quot;:\&quot;Paging parameter. URL fragment that can be used to fetch next page of results.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;PUT\&quot;,\&quot;POST\&quot;]} | 
**current_page** | **int** | {\&quot;description\&quot;:\&quot;Paging parameter. 0-indexed. Describes which page (given a page size of &#x60;recordsRequested&#x60;) of the result set you are viewing.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;PUT\&quot;,\&quot;POST\&quot;]} | 
**current_offset** | **int** | {\&quot;description\&quot;:\&quot;Paging parameter. 0-indexed. Describes your current location within a pageable list of query results.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;PUT\&quot;,\&quot;POST\&quot;]} | 
**records_requested** | **int** | {\&quot;default\&quot;:10,\&quot;description\&quot;:\&quot;Paging parameter. Describes how many records you requested.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;PUT\&quot;,\&quot;POST\&quot;]} | 
**records_returned** | **int** | {\&quot;description\&quot;:\&quot;Describes how many records were returned by your query.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;PUT\&quot;,\&quot;POST\&quot;]} | 
**execution_time** | **int** | {\&quot;description\&quot;:\&quot;Number of milliseconds taken by API to calculate response.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;PUT\&quot;,\&quot;POST\&quot;]} | 
**results** | [**list[UnitOfMeasure]**](UnitOfMeasure.md) | {\&quot;description\&quot;:\&quot;The results returned by your query.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;PUT\&quot;,\&quot;POST\&quot;]} | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


