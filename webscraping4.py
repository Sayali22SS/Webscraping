# importing the libraries
from bs4 import BeautifulSoup
import requests
import csv
import urllib.request
from urllib.request import urlopen

url = 'https://www.nseindia.com/market-data/currency-derivatives#derivwatch-currDeriv'
Page = urlopen(url)

soup = BeautifulSoup(Page)
table = soup.find_all("table", { "id" : "currencyDerTable" })
#print(table)
for mytable in table:
    table_body = mytable.find('tbody')
    try:
        rows = table_body.find_all('tr')
        for tr in rows:
            cols = tr.find_all('td')
            for td in cols:
                print(td.text)
            for td in cols:
                cols1 = td.find_all(href)
    except:
        print("no tbody")