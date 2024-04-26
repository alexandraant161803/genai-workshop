from langchain_community.document_loaders import PlaywrightURLLoader

async def fetch_and_transform_content(url: str) -> str:
    """
    Fetches HTML content from a URL
    :param url: URL to fetch the content from
    :return: Content from URL parts
    """
    loader = PlaywrightURLLoader(urls=[url])
    html = await loader.aload()
    if html:  # Check if the list is not empty
    # Directly use the HTML content from the first Document object in the list
        html_content = html[0].page_content
        return html_content
    return []
