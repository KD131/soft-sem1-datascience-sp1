from typing import Optional

import requests
from bs4 import BeautifulSoup


def trustpilot(url: str, page_limit: Optional[int]=10) -> list:
    """Scrapes reviews from a Trustpilot page.

    :param url: page url
    :param page_limit: max pages to scrape, defaults to 10, None for no limit
    :return: list of reviews
    """
    reviews = []
    i = 0
    
    while page_limit == None or i < page_limit:
        response = requests.get(url, params={
            'page': i+1
        })
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        review_divs = soup.select('section.styles_reviewContentwrapper__zH_9M')

        for div in review_divs:
            title = div.select_one('h2')
            title = title.text if title else None
            # Find the first p tag within the div
            body = div.select_one('p')
            body = body.text if body else None
            rating = div.select_one('div.styles_reviewHeader__iU9Px')
            rating = int(rating['data-service-review-rating']) if rating else None
            reviews.append({"title": title, "body": body, "rating": rating})
        
        i += 1
        is_last_page = soup.select_one('a.pagination-link_next__SDNU4.pagination-link_disabled__7qfis') is not None
        if is_last_page:
            break
        
    print(f"{url}: {len(reviews)} reviews from {i} page{'s'[:i^1]}.{' There are more pages left.' if not is_last_page else ''}")
    return reviews

# There are a couple ways to find and evaluate if there are more pages.
# You can check if the next button is disabled, or if the current page number equals the last page number.
# The last page button only shows up if there are more than a certain amount of pages.
# So don't do that.

# # find button
# name="pagination-button-next"
# data-pagination-button-next-link="true"
# pagination-link_next__SDNU4

# # state of button
# aria-disabled="true"
# pagination-link_disabled__7qfis
# link_disabled__mIxH1

# # find last page
# name="pagination-button-last"
# data-pagination-button-last-link="true"