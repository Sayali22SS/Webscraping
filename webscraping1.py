#importing necessary packages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

element_list = [] 
for page in range(1, 3, 1):
    page_url = 'https://www.nseindia.com/market-data/currency-derivatives#derivwatch-currDeriv'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(page_url)
    new = {'by' : By.ID, 'value' : 'table-currency' }
    table1 = driver.find_elements(new).click()
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(table1).click(table1).perform()
    new1 = {'by' : By.ID, 'value' : 'crrencyDerTable'}
    table = driver.find_elements(new1).click()
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(table).click(table).perform()

    for mytable in table:
        table_body = mytable.find('tbody')
        try:
            rows = table_body.find_all('tr')
            for tr in rows:
                cols = tr.find_all('td')
                for td in cols:
                    print(td.text)
        except NoSuchElementException as e:
            print(e)

    for i in range(len(table)):
        element_list.append(td[i].text)
    
print(element_list)
  
#closing the driver
driver.close()