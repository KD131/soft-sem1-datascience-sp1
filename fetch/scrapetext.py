import requests
from bs4 import BeautifulSoup

def scrapetext(url):
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    tags = soup.select('h1, h2, p')
    return [tag.text for tag in tags]