import requests
from bs4 import BeautifulSoup

def get_page_content(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.text
    except:
        return ""