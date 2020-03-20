from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

path = '/Users/Jovan/Desktop/EbayBot/chromedriver'
chrome_options = Options()
chrome_options.add_argument("- incognito")
driver = webdriver.Chrome(path, options=chrome_options)

# ================================================================================================
url = 'https://offer.ebay.com/ws/eBayISAPI.dll?ViewBidsLogin&item=362771938372&rt=nc&_trksid=p2047675.l2564'
driver.get(url)
# ================================================================================================

# ================================================================================================

# element = driver.find_element_by_css_selector("div.BHbidSecBorderGrey")
# element = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/table[2]/tbody/tr/td[1]/div[3]/div/div[2]/table[2]/tbody").text.split('\n')
element = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/table[2]/tbody/tr/td[1]/div[3]/div[1]/div[2]/table[3]").text.split('\n')

# dop = i.find_element_by_xpath("/html/body/div[2]/div/div/div/table[2]/tbody/tr/td[1]/div[3]/div/div[2]/table[2]/tbody/tr[2]/td[5]").text
# add 9 strating from 13
count = 1
while count < 10:
    print(element[count])
    count += 1
    

# print(element[1].split()
# ================================================================================================
''' This piece of code will list out all the items in the list and number them '''
# count = 0
# for i in element:
#     print(str(count) + '  ' + i )
#     count += 1
# ================================================================================================

# print(elem[22])
# print(elem[31])
# print(elem[40])
# for i in range(20):
#     print(elem[i])

