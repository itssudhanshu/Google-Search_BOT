# First Initializez these packages
# pip install numpy==1.19.3 for pandas
# pip install google for search
from time import sleep
import pandas as pd
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
# try: 
    # from googlesearch import search 
# except ImportError:  
#     print("No module named 'google' found") 
  
# to search 
query = "Sudhanshu"
result = []
  
# for j in search(query,user_agent='your bot 0.1'): 
#     result.append(j)
# browser = webdriver.Chrome('chromedriver')
options = Options()
options.headless = True
driver = webdriver.Chrome("chromedriver", chrome_options=options) 

href = []

for i in range(1): 
    driver.get("https://www.google.com/search?q=" +
                                     query + "&start=" + str(i)) 
    results = driver.find_elements_by_css_selector('div.g> div > div.yuRUbf')
    # print(len(results))
    for l in range(len(results)):
        link = results[l].find_element_by_tag_name("a")
        href.append(link.get_attribute("href"))
    
    print(href)
    # link = results[1].find_element_by_tag_name("a")
    # href = link.get_attribute("href")
    # print(href)


# sleep(20)

df = pd.DataFrame() 

# print(len(result))
# # print(result)
df[query] = len(href)
df[query] = href[0:]
df.to_excel('result.xlsx', index = False) 

driver.quit()
