from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import requests
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url = 'https://www.nseindia.com/market-data/currency-derivatives#derivwatch-currDeriv.html'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

table_one = driver.find_elements('/html/body/div[7]/div/section/div/div/div/div/div/div/div/div/div[4]')
for table in table_one :
    print(table.text)
    symbol = driver.find_elements('/html/body/div[7]/div/section/div/div/div/div/div/div/div/div/div[4]/div[1]/table/tbody/tr[3]/td[2]')
    expiry_date = driver.find_elements('/html/body/div[7]/div/section/div/div/div/div/div/div/div/div/div[4]/div[1]/table/tbody/tr[3]/td[3]')
    last_price = driver.find_elements('/html/body/div[7]/div/section/div/div/div/div/div/div/div/div/div[4]/div[1]/table/tbody/tr[3]/td[7]')

symbol_result = []
for i in range(len(symbol)):
    tem_data = {'Symbol' : symbol[i].text,'Expiry_date' : expiry_date[i].text,'Last_price' : last_price[i].text}
    symbol_result.append(tem_data)

df_data = pd.DataFrame(symbol_result)
print(df_data)