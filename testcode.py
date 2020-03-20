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
print('Enter URL')
url = input()
# url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=Apple+AirPods+with+Charging+Case+%28Latest+Model%29&_sacat=0'
def open_driver(url):
    driver.get(url)
open_driver(url)
# ================================================================================================

# ================================================================================================
# element = driver.find_element_by_id("mainContent")
element = driver.find_element_by_css_selector("ul.srp-results")    # will grab them all
# ebay_list = element.find_element_by_id('srp-river-results-listing{}'.format(count))
# ================================================================================================

# ================================================================================================
''' This piece of code is looping through the 'id' to find all listings. It then saves to the list of links so that I can access them one by one '''
links = []
for i in range(1, 10):
    ebay_list = element.find_element_by_id('srp-river-results-listing{}'.format(i))
    ebay_link = ebay_list.find_element_by_css_selector('li.s-item div.s-item__info a.s-item__link').get_attribute('href')
    links.append(ebay_link)


''' This piece of code is gathering the information that I want from the detail/product page '''
wait_time = 2.3
sold_links = []
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
        print(views_per_hour[0] + ' vpr')
    except NoSuchElementException:
        views_per_hour = 0
        print(str(views_per_hour) + ' vpr')

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
                # time.sleep(0.5)

                # sold_links.remove(sold_page)
            else:
                print('No element')

            # if driver.find_element_by_xpath("/html/body/div[2]/div/div/div/table[2]/tbody/tr/td[1]/div[3]/div[1]/div[2]/table[3]"):
            #     elem2 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/table[2]/tbody/tr/td[1]/div[3]/div[1]/div[2]/table[3]").text.split('\n')
            #     print(elem2[1])
            #     time.sleep(0.5)
            #     # sold_links.remove(sold_page)
            # else:
            #     print('No element')

            sold_links.remove(sold_page)

        # sold_list = driver.get(sold_links)
        # time.sleep(wait_time)
        # sold_detail = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/table[2]/tbody/tr/td[1]/div[3]/div/div[2]/table[2]/tbody").text.split()
        # print(sold_detail)
    except NoSuchElementException:
        sold = '0 sold'
        print(sold)

    # for s in sold_links:
    #     sold_link_list = driver.get(s)

    print('=' * 100)
    print('')

# ================================================================================================
# print(links[0])

# count = 0
# while count < 3:
#     print(links[count])
#     print('=' * 100)
#     count += 1

    



    # ebay_link = ebay_list.find_element_by_css_selector('li.s-item div.s-item__info a.s-item__link')
    # time.sleep(2)
    # ebay_link.click()
    # time.sleep(2)
    # driver.get(back_url)
    # driver.back()
    # time.sleep(3)
# ================================================================================================

# ================================================================================================
# count = 1
# while count < 5:
#     ebay_list = element.find_element_by_id('srp-river-results-listing{}'.format(count))
#     ebay_link = ebay_list.find_element_by_css_selector('li.s-item div.s-item__info a.s-item__link')
#     time.sleep(2)
#     ebay_link.click()
#     time.sleep(2)
#     driver.get(url)
#     driver.back()
#     time.sleep(3)
#     count += 1
    
# ================================================================================================

# ================================================================================================
''' This piece of code works for getting the 'title' 'price' 'links' using the 'for loop' '''
# for i in range(1,21):
#     ebay_list = element.find_element_by_id('srp-river-results-listing{}'.format(i))
#     title = ebay_list.find_element_by_css_selector('li.s-item div.s-item__info h3.s-item__title').text
#     price = ebay_list.find_element_by_css_selector('li.s-item div.s-item__info div.s-item__details span.s-item__price').text
#     ebay_link = ebay_list.find_element_by_css_selector('li.s-item div.s-item__info a.s-item__link').get_attribute('href')
#     print(title)
#     print(price)
#     print(ebay_link)
#     print('')
#     print('=' * 100)
# ================================================================================================


# ================================================================================================
''' This piece of code works for getting the 'title' 'price' 'links' using the 'while loop' '''
# count = 1
# while count < 50:
#     ebay_list = element.find_element_by_id('srp-river-results-listing{}'.format(count))
#     title = ebay_list.find_element_by_css_selector('li.s-item div.s-item__info h3.s-item__title').text
#     price = ebay_list.find_element_by_css_selector('li.s-item div.s-item__info div.s-item__details span.s-item__price').text
#     ebay_link = ebay_list.find_element_by_css_selector('li.s-item div.s-item__info a.s-item__link').get_attribute('href')
#     print(title)
#     print(price)
#     print(ebay_link)
#     print('')
#     print('=' * 100)
#     count += 1
# ================================================================================================



# ================================================================================================
# element = driver.find_element_by_css_selector("ul.srp-results li.s-item")    # will grab 1
# element = driver.find_element_by_id("srp-river-results-listing1")
# element = driver.find_element_by_xpath("//*[@id='mainContent']")
# elem = element.find_element_by_css_selector('li.s-item')
# link = element.find_element_by_css_selector('li.s-item div.s-item__info a.s-item__link').get_attribute('href')
# title = element.find_element_by_css_selector('li.s-item div.s-item__info h3.s-item__title')
# elem = element.find_element_by_css_selector('li.s-item').get_attribute('s-item__title')

# print(elem.text)
    # print(i.text)



# print(element.get_attribute('href'))

# title = driver.find_element.by_xpath('//*[@id="srp-river-results-listing1"]/div/div[2]/a/h3')


# print(ebay_listings)
# driver.close()

# 'https://stackoverflow.com/questions/21898567/how-to-click-on-all-links-in-web-page-in-selenium-webdriver'
# 'https://stackoverflow.com/questions/24775988/how-to-navigate-to-a-new-webpage-in-selenium'