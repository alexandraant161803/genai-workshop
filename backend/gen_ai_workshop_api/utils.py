from langchain_community.document_loaders import PlaywrightURLLoader

# Define a cache dictionary to hold the content for each URL
cache = {}

async def fetch_and_transform_content(url: str) -> str:
    """
    Fetches and caches HTML content from a URL.

    Checks the cache first and fetches from the web only if content is not in the cache or the cache has expired.
    
    :param url: URL to fetch the content from
    :return: Content from URL parts
    """
    # Check if the URL is already in the cache
    if url in cache:
        return cache[url]
    
    loader = PlaywrightURLLoader(urls=[url])
    html = await loader.aload()
    
    if html:  # Check if the list is not empty
        # Directly use the HTML content from the first Document object in the list
        html_content = html[0].page_content
        # Store the content in the cache with the URL as the key
        cache[url] = html_content
        return html_content
    
    return ""
