#!usr/bin/python3
# pip install newsapi-python
# documentation https://newsapi.org/docs
import csv
from newsapi import NewsApiClient


def api_key():
    with open('Api_key.txt', 'r') as key:
        read = key.read()
        return read

print(api_key())

# Init
newsapi = NewsApiClient(api_key = api_key())

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          language='en',
                                          )

print(top_headlines)

headlines = ""

for items in top_headlines['articles']:
    headlines += items['title'] + items['url'] + '\n' +'\n'

print(headlines)

with open('top.headlines.docx', 'w') as file:
    for items in headlines:
        file.writelines(items) 