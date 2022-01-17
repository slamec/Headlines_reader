#!usr/bin/python3
# pip install newsapi-python
# https://newsapi.org/docs
import csv
from newsapi import NewsApiClient


def api_key():
    with open('Api_key.txt', 'r') as key:
        read = key.read()
        return read

print(api_key())

# Init
newsapi = NewsApiClient(api_key = api_key())

""" # /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
 """
# /v2/top-headlines/sources
sources = newsapi.get_sources()

# print(sources)

sources_list = []

for items in sources['sources']:
    sources_list.append(items['name'])

with open('sources_list.csv', 'w', newline= '') as file:
    for items in sources_list:
        write = csv.writer(file)
        write.writerow([items])