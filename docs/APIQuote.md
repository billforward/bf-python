# APIQuote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**subtotal** | **float** | {\&quot;description\&quot;:\&quot;The cost &amp;mdash; including tax, but excluding discounts &amp;mdash; of all items described in the quote.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**subtotal_excluding_tax** | **float** | {\&quot;description\&quot;:\&quot;The cost &amp;mdash; excluding tax, and excluding discounts &amp;mdash; of all items described in the quote.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**total** | **float** | {\&quot;description\&quot;:\&quot;The cost &amp;mdash; including tax, and with discounts (themselves including tax) applied &amp;mdash; of all items described in the quote.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**total_excluding_tax** | **float** | {\&quot;description\&quot;:\&quot;The cost &amp;mdash; excluding tax, and with discounts (themselves excluding tax) applied &amp;mdash; of all items described in the quote.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**tax** | **float** | {\&quot;description\&quot;:\&quot;The portion of this quote&#39;s cost which is comprised of tax.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**discount** | **float** | {\&quot;description\&quot;:\&quot;Total amount deducted from price via discounts &amp;mdash; includes any tax upon the discounts themselves.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**discount_excluding_tax** | **float** | {\&quot;description\&quot;:\&quot;Total amount deducted from price via discounts &amp;mdash; excludes any tax upon the discounts themselves.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**currency** | **str** | {\&quot;description\&quot;:\&quot;The currency of any quoted prices &amp;mdash; as specified by a three-character ISO 4217 currency code (i.e. USD).\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**product_name** | **str** | {\&quot;description\&quot;:\&quot;Name of the product for which a price quote is requested.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**public_product_name** | **str** | {\&quot;description\&quot;:\&quot;Public name of the product for which a price quote is requested.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**product_rate_plan_name** | **str** | {\&quot;description\&quot;:\&quot;Name of the rate plan (of some product) for which a price quote is requested.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**public_product_rate_plan_name** | **str** | {\&quot;description\&quot;:\&quot;Public name of the rate plan (of some product) for which a price quote is requested.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**product_id** | **str** | {\&quot;description\&quot;:\&quot;ID of the product for which a price quote is requested.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**product_rate_plan_id** | **str** | {\&quot;description\&quot;:\&quot;ID of the rate plan (of some product) for which a price quote is requested.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**subscription_id** | **str** | {\&quot;description\&quot;:\&quot;ID of the subscription for which a price quote is requested.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**account_id** | **str** | {\&quot;description\&quot;:\&quot;ID of the account for which a price quote is requested.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**quantities** | [**list[APIQuoteResponseQuantity]**](APIQuoteResponseQuantity.md) | {\&quot;description\&quot;:\&quot;A list of calculated prices for each pricing component described in the quote request.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**discounts** | [**list[CouponWrapperResponse]**](CouponWrapperResponse.md) | {\&quot;description\&quot;:\&quot;A list of discounts applied in calculating the quote.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**quote_for** | **str** | {\&quot;default\&quot;:\&quot;RecurringPeriod\&quot;,\&quot;description\&quot;:\&quot;Subscription scenario with which the quote is concerned.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**period_start** | **datetime** | {\&quot;default\&quot;:\&quot;(Time at which quote is requested)\&quot;,\&quot;description\&quot;:\&quot;The start date-time of the interval for which a price quote is requested.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | 
**period_end** | **datetime** | {\&quot;default\&quot;:\&quot;(End of period described in &#x60;periodStart&#x60;)\&quot;,\&quot;description\&quot;:\&quot;The end date-time of the interval for which a price quote is requested.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | 
**total_periods** | **float** | {\&quot;default\&quot;:\&quot;ZERO\&quot;,\&quot;description\&quot;:\&quot;\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**proration_enabled** | **bool** | {\&quot;default\&quot;:true,\&quot;description\&quot;:\&quot;Whether consumption for fractions/multiples of periods is calculated as a fraction/multiple of the cost of consumption for a whole period.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] [default to False]
**uplift** | **float** | {\&quot;description\&quot;:\&quot;\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**coupon_codes** | **list[str]** | {\&quot;description\&quot;:\&quot;A list of coupon codes to consider in calculating the quote.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**organization_id** | **str** | {\&quot;description\&quot;:\&quot;ID of the organization in whose name the quote was generated.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**same_product_period** | **bool** | {\&quot;description\&quot;:\&quot;If migration quote whether or not the rate plans have the same duration\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


