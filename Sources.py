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

# /v2/top-headlines/sources
sources = newsapi.get_sources()

#print(sources)

sources_list = []

for items in sources['sources']:
    sources_list.append(items['name'])

print(sources_list)    