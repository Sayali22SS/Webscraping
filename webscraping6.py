from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
URL = ("https://www.nseindia.com/market-data/currency-derivatives#derivwatch-currDeriv")
r = requests.get(URL)
htmlContent = r.content
#print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')


product=[]
symbol=[]
Ltp=[]
product=soup.find('div',attrs={'class':'nav-item nav-link active show'})
print(product.text)

for a in soup.find_all('a',href=True,attrs={'class':'nav-item nav-link active show'}):
    symbol=a.find('div',attrs={'href':'/currency-getquote?identifier=FUTCURUSDINR27-10-2021XX0.0000'})
    Ltp=a.find('div',attrs={'href':'bold text-right>74.8550'})

    products.append(symbol.text)
    product.append(Ltp.text)

    df = pd.DataFrame({'Product Name':product,'Symbol':symbol,'LTP':Ltp})
    df.head()
