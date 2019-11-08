# Sitemap

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sitemaps** | **list[str]** | List of sitemap URLs that were examined. The zeroth item is always the URL provided in the request.  | 
**evaluated_date** | **datetime** | The timestamp for when the evaluation of sitemaps.xml was initiated.  | 
**log** | [**list[LogEntry]**](LogEntry.md) |  | 
**urlset** | [**list[SitemapUrlset]**](SitemapUrlset.md) | A list of location entries retieved from the sitemap. Includes locations obtained from referenced sitemaps, if any.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


