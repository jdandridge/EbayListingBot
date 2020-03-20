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
''' Will open a window to the ebay search results '''
print('Enter Ebay Search URL')
url = input()

def open_driver(url):
    driver.get(url)
open_driver(url)
# ================================================================================================

# ================================================================================================
''' This is the base search page selector '''
element = driver.find_element_by_css_selector("ul.srp-results")
# ================================================================================================

# ================================================================================================
links = []
wait_time = 2.3
sold_links = []
# ================================================================================================

# ================================================================================================
''' This piece of code is looping through the 'id' to find all listings. It then saves to the list of links so that I can access them one by one '''

for i in range(1, 10):
    ebay_list = element.find_element_by_id('srp-river-results-listing{}'.format(i))
    ebay_link = ebay_list.find_element_by_css_selector('li.s-item div.s-item__info a.s-item__link').get_attribute('href')
    links.append(ebay_link)


''' This piece of code is gathering the information that I want from the detail/product page '''

for link in links:
    link_list = driver.get(link)
    time.sleep(wait_time)

    if driver.find_element_by_id('itemTitle'):
        title = driver.find_element_by_id('itemTitle').text
        print(title)
    else:
        title = 'N/A'

    try:
        views_per_hour = driver.find_element_by_css_selector('div.vi-notify-new-bg-dBtm span').text.split()
        print(views_per_hour[0] + ' vph')
    except NoSuchElementException:
        views_per_hour = 0
        print(str(views_per_hour) + ' vph')

    try:
        price = driver.find_element_by_id('prcIsum').text.split()
        print(price[1])
    except NoSuchElementException:
        price = 0
        print(price)

    try:
        sold = driver.find_element_by_css_selector('span.vi-qtyS-hot-red a').text
        print(sold)

        sold_page = driver.find_element_by_css_selector('span.vi-qtyS-hot-red a').get_attribute('href')
        sold_links.append(sold_page)
        print(sold_links)


        for s in sold_links:
            element_list = driver.get(s)

            if driver.find_element_by_xpath("/html/body/div[2]/div/div/div/table[2]/tbody/tr/td[1]/div[3]/div/div[2]/table[2]/tbody"):
                try:
                    elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/table[2]/tbody/tr/td[1]/div[3]/div/div[2]/table[2]/tbody").text.split('\n')

                    count = 1
                    while count < 11:
                        print(elem[count])
                        count += 1
                except IndexError:
                    print('Need to Manualy look up')

            else:
                print('No element')


            sold_links.remove(sold_page)

    except NoSuchElementException:
        sold = '0 sold'
        print(sold)

    print('=' * 100)
    print('')

# ================================================================================================
