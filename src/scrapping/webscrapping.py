import requests
from bs4 import BeautifulSoup


class WebScraper:
    """
    A class for web scraping using BeautifulSoup and requests.
    
    This class provides methods to fetch HTML content, parse it, and extract elements and text.
    It also includes methods to extract hyperlinks from the parsed HTML.
    
    Attributes:
        url (str): The URL to scrape.
        parser (str): The parser to use for BeautifulSoup (default is 'html.parser').
    """
    def __init__(self, url, index, parser="html.parser"):
        self.url = url
        self.index = index
        self.parser = parser

        self.html = self.__fetch_html(self.url)
        self.soup = self.__parse_html(self.html, self.parser)
    
    def __fetch_html(self, url):
        """
        Fetches the HTML content of a given URL.
        
        Args:
            url (str): The URL to fetch the HTML from.
        
        Returns:
            str: The raw HTML content of the page.
        """
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text

    def __parse_html(self, html, parser="html.parser"):
        """
        Parses the HTML content using BeautifulSoup.
        
        Args:
            html (str): The raw HTML content.
            parser (str): The parser to use (default is 'html.parser').
        
        Returns:
            BeautifulSoup: A BeautifulSoup object for navigating the HTML.
        """
        return BeautifulSoup(html, self.parser)

    
    def extract_elements(soup, tag, attributes=None):
        """
        Extracts elements from the parsed HTML based on tag and attributes.
        
        Args:
            soup (BeautifulSoup): The parsed HTML content.
            tag (str): The HTML tag to search for.
            attributes (dict, optional): Attributes to filter the elements (default is None).
        
        Returns:
            list: A list of matching elements.
        """
        return soup.find_all(tag, attrs=attributes)

    def extract_text_from_elements(elements):
        """
        Extracts text content from a list of HTML elements.
        
        Args:
            elements (list): A list of BeautifulSoup elements.
        
        Returns:
            list: A list of text content from the elements.
        """
        return [element.get_text(strip=True) for element in elements]

    def extract_links(soup, base_url=None):
        """
        Extracts all hyperlinks from the parsed HTML.
        
        Args:
            soup (BeautifulSoup): The parsed HTML content.
            base_url (str, optional): The base URL to resolve relative links (default is None).
        
        Returns:
            list: A list of hyperlinks.
        """
        links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if base_url and not href.startswith(('http://', 'https://')):
                href = requests.compat.urljoin(base_url, href)
            links.append(href)
        return links