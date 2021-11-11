# Python program to scrape table from website

# import libraries selenium and time
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

# Create webdriver object
driver = webdriver.Chrome(ChromeDriverManager().install())


# Get the website
driver.get('https://www.nseindia.com/market-data/currency-derivatives#derivwatch-currDeriv')

# Make Python sleep for some time
sleep(1)

# Obtain the number of rows in body
rows = len(driver.find_elements(
	"/html/body/div[3]/div[2]/div/div[1]/div/div/div/article/div[3]/div/table/tbody/tr"))

# Obtain the number of columns in table
cols = len(driver.find_elements(
	"/html/body/div[3]/div[2]/div/div[1]/div/div/div/article/div[3]/div/table/tbody/tr[1]/td"))

# Print rows and columns
print(rows)
print(cols)

# Printing the table headers
print("SYMBOL		 "+"			 LAST PRICE")

# Printing the data of the table
for r in range(2, rows+1):
	for p in range(1, cols+1):
		
		# obtaining the text from each column of the table
		value = driver.find_element(
			"/html/body/div[3]/div[2]/div/div[1]/div/div/div/article/div[3]/div/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
		print(value, end='	 ')
	print()
