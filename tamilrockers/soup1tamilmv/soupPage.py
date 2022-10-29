import requests
from bs4 import BeautifulSoup


def makeSoup(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')
