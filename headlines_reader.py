#pip install newsapi-python
from newsapi import NewsApiClient

def read_api():
    with open("Api_key.txt", "r") as apikey:
       file = apikey.read()
       print(file)

# Init
newsapi = NewsApiClient(api_key=read_api())

# /v2/top-headlines
""" top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us') """


# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()

""" for items in all_articles['sources']:
    print(items['name']) """