import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
website = 'https://pmgkhulna.bdpost.gov.bd/site/page/fe0acce7-2037-4883-b954-6bb2edce53c5/%E0%A6%AA%E0%A7%8B%E0%A6%B8%E0%A7%8D%E0%A6%9F%E0%A6%95%E0%A7%8B%E0%A6%A1-%E0%A6%85%E0%A6%A8%E0%A7%81%E0%A6%B8%E0%A6%A8%E0%A7%8D%E0%A6%A7%E0%A6%BE%E0%A6%A8'

driver.get(website)
#driver.maximize_window()

#dhakaButton = driver.find_element("xpath", "/html/body/div[5]/div[5]/div[2]/div[4]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/a")
#narayonganjButton = driver.find_element("xpath", "/html/body/div[5]/div[5]/div[2]/div[4]/div/table/tbody/tr/td/table/tbody/tr[1]/td[2]/a")

#narsingdiButton = driver.find_element("xpath", "/html/body/div[5]/div[5]/div[2]/div[4]/div/table/tbody/tr/td/table/tbody/tr[1]/td[4]/a")
#gazipurButton = driver.find_element("xpath", "/html/body/div[5]/div[5]/div[2]/div[4]/div/table/tbody/tr/td/table/tbody/tr[2]/td[1]/a")
#columns = ['District', 'Serial', 'Upozila', 'Post Office', 'Post Office Bangla', 'PostCode']
main = pd.DataFrame()

for row_num in range(1,17):
    for col_num in range(1,5):
        xpath = "/html/body/div[5]/div[5]/div[2]/div[4]/div/table/tbody/tr/td/table/tbody/tr["+ str(row_num)+"]/td["+str(col_num)+"]/a"
        button  = driver.find_element("xpath", xpath)
        title = str(button.get_attribute("title"))
        button.click()
        table_data = driver.find_elements("xpath", "/html/body/div[5]/div[5]/div[2]/div[4]/div/table//td")
        rows=[]
        row=[]
        for i, cell in enumerate(table_data):
            row.append(cell.text)
            if (i+1)%5==0:
               rows.append(row)
               row = []
        df = pd.DataFrame(rows)
        df.drop(index=df.index[0], axis=0, inplace=True)
        df['District'] = title
        main = pd.concat([main, df], ignore_index=True)

        driver.back()

main.to_csv('allPostalCode.csv', index=False)

#title = str(narayonganjButton.get_attribute("title"))
#print(title)
#narayonganjButton.click()
#table_data = driver.find_elements("xpath", "/html/body/div[5]/div[5]/div[2]/div[4]/div/table//td")

#rows = []
#row = []
'''
for i, cell in enumerate(table_data):
    row.append(cell.text)
    if (i + 1) % 5 == 0:
        rows.append(row)
        row = []

df = pd.DataFrame(rows)
df.insert(0, "Post Code", title)
df.to_csv('data_pandas.csv', index=False)

print(df.head(10))

ndf = pd.read_csv('data_pandas.csv')
print(ndf.head(10))
#driver.close()
'''