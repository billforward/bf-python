# InvoiceChargeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**include_aggregated** | **bool** | {\&quot;default\&quot;:false,\&quot;description\&quot;:\&quot;Outstanding charges for which invoices will be generated:&lt;br&gt;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;true&lt;/span&gt; &amp;mdash; Include charges marked with &#39;Aggregated&#39; &#x60;invoicingType&#x60; (i.e. charges that would otherwise be included anyway in the next naturally-occurring invoice)&lt;br&gt;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;false&lt;/span&gt; &amp;mdash; Exclude charges marked with &#39;Aggregated&#39; &#x60;invoicingType&#x60; (i.e. prefer that these charges be included instead on the next naturally-occurring invoice).\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] [default to False]
**include_invoiced_charges_only** | **bool** | {\&quot;default\&quot;:false,\&quot;description\&quot;:\&quot;Outstanding charges for which invoices will be generated:&lt;br&gt;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;true&lt;/span&gt; &amp;mdash; Include those charges raised with &#39;no invoice&#39; specified (i.e. charges against the subscription) &amp;mdash; as well as charges raised against some specific invoice.&lt;br&gt;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;false&lt;/span&gt; &amp;mdash; Include only charges raised against some specific invoice.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] [default to False]
**invoice_state** | **str** | {\&quot;default\&quot;:null (invoice is raised in its default initial state),\&quot;description\&quot;:\&quot;Initial state with which any invoices will be generated.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


