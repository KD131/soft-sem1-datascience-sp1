import pandas as pd
import requests
from bs4 import BeautifulSoup

def trustpilot(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    review_divs = soup.select('section.styles_reviewContentwrapper__zH_9M')
    reviews = []

    for div in review_divs:
        title = div.select_one('h2')
        title = title.text if title else None
        # Find the first p tag within the div
        body = div.select_one('p')
        body = body.text if body else None
        rating = div.select_one('div.styles_reviewHeader__iU9Px')
        rating = int(rating['data-service-review-rating']) if rating else None
        reviews.append({"title": title, "body": body, "rating": rating})
    return reviews