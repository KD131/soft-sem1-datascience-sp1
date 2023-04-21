import requests

def cvrapi(company):
    # Specifically uses the company name search of the API, not the general search.
    r = requests.get('https://cvrapi.dk/api', params={
        'name': company,
        'country': 'dk',
        'format': 'json'
    })
    return r.json()