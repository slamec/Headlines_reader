# pip install newsapi-python
# https://newsapi.org/docs
  
import requests
import json

from requests.api import head

def api_key():
    with open('Api_key.txt', 'r') as key:
        key_read =key.read()
        return key_read


def top_headlines_query(keyword):
    url = 'https://newsapi.org/v2/top-headlines?q=' + keyword + '&apiKey=' + api_key()

    return(url) 

response = requests.get(url = top_headlines_query('bitcoin'))

    