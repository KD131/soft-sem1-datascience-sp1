from urllib.parse import urlparse

import pandas as pd
import requests
from bs4 import BeautifulSoup


# Instead of manipulating the URL, we could also get the regnskab URL from the link on the page.
def url_regnskab(url):
    """Returns the url to the regnskab page of a proff.dk url"""
    # Using urllib to parse the url and replace the first path element
    # Could've used string manipulation to replace 'firma' with 'regnskab', but that could be error prone
    # Could've also used split and join on the string, but this seems more robust. Specifically targets the path of the URL.
    parsed = urlparse(url)
    path = parsed.path.split('/')
    path[1] = 'regnskab'                                    # will error if path is empty (a single '/' is good enough)
    return parsed._replace(path='/'.join(path)).geturl()    # geturl should be the same as urlunparse(parsed)

def employee_count(url):
    """Returns the number of employees from a proff.dk url"""
    r = requests.get(url)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    employees = soup.select_one('li.employees-info > em')
    return int(employees.text) if employees and employees.text != '-' else None

def financial_data(url):
    """Returns the financial data from a proff.dk url"""
    # I could use bs4 to get the table and pass to pandas, but it's easier to just use pandas to find it
    # The match parameter is used to only get the table with the correct header
    # We skip the first row after the header, since it's a string value that will mess up the column type and make it a string.
    # It's given in a list to specify the exact row to skip, and not skip the header row.
    try:
        df = pd.read_html(url, match='RESULTATREGNSKAB', index_col=0, skiprows=[1], thousands='.', decimal=',', encoding='utf-8', na_values='-')[0]
    except ValueError:
        # If no table is found, we return an empty series
        return pd.Series(dtype=float)
    
    # get result row as new series to avoid it being a view
    # I could've not indexed the df or used iloc here, and then the encoding wouldn't have been an issue
    s = pd.Series(df.loc['Årets resultat'])

    # drop last index (the column with a button for a graph)
    s.drop(s.index[-1], inplace=True)
    # remove month from year-month index
    s.rename(lambda i: i.split('-')[0], inplace=True)
    # we could convert years to int here, but it'll get cast to string anyway when converted to json.

    # remove dots and replace commas with dots, then convert to float
    # We don't need to do this if we use the thousands and decimal parameters in read_html
    # s = s.apply(lambda x: x.replace('.', '').replace(',', '.') if isinstance(x, str) else x).astype(float)
    # We also don't to convert to float, since we skip the one row with string values.
    # s = s.astype(float)

    return s

def proff(url):
    """
    Fetches data from proff.dk and returns it as a dict.

    It contains the number of employees and the financial data.
    """
    print(url)
    employees  = employee_count(url)

    url = url_regnskab(url)
    finances = financial_data(url)
    finances['employees'] = employees
    return finances.to_dict()