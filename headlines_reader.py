# pip install newsapi-python
# https://newsapi.org/docs 
from newsapi import NewsApiClient
import os 

cwd = os.getcwd()
print(cwd)

def read_api():
    with open('Api_key.txt', 'r') as apikey:
        file = apikey.read()
        return file

# Init
newsapi = NewsApiClient(api_key=read_api())


# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge'
                                                                    )

with open('test_file.txt', 'w') as file:
    for items in top_headlines['articles']:
        file.write(items['source']['name'] + '\n')
        file.write(items['title'])