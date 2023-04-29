import wikipedia

# import wikipediaapi

# wiki_wiki = wikipediaapi.Wikipedia('da')
wikipedia.set_lang('da')

def wikipedia_page(company):
    try:
        page = wikipedia.page(company)
        print(company, page.url)
        return page.content
    except wikipedia.exceptions.DisambiguationError as e:
        print(company, e.options)
    except wikipedia.exceptions.PageError as e:
        print(company, e)