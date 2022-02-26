#!usr/bin/python3
# pip install newsapi-python
# documentation https://newsapi.org/docs
from asyncore import write
import csv
from newsapi import NewsApiClient


def api_key():
    with open('Api_key.txt', 'r') as key:
        read = key.read()
        return read

print(api_key())

#Init
newsapi = NewsApiClient(api_key = api_key())

#get information about all sources 
sources = newsapi.get_sources()

print(sources)

#sources to list
sources_list = []

#append sources list (id)
for items in sources['sources']:
    sources_list.append(items['id'])

#write all the sources to a csv file  
with open('sources_list.csv', 'w', newline= '') as file:
    for items in sources_list:
        write = csv.writer(file)
        write.writerow([items])
    
    