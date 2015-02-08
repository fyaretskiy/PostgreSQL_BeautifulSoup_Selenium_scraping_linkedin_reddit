
import re
from selenium import webdriver

def get_data(url):
    """receives URL and returns a list of list."""
    driver = webdriver.Firefox()
    driver.get("https://www.linkedin.com/channels/206")
    elem = driver.find_element_by_xpath('//ul[@id="my-feed-post" and @class="chron katify activities"]')
    elements = elem.find_elements_by_xpath('//li[@class="feed-item"]')
    entry = []

    entry_list = []

    for i in elements:
        entry = []
        title = i.find_element_by_xpath('div//p[@class="share-title"]').text
        summary = i.find_element_by_xpath('div//p[@class="share-desc"]').text
        try:
           like = re.findall('[0-9]+', str(i.find_element_by_xpath('div//li[@class="feed-like"]').text))[0]
        except:
            like = None
        try:
            comment = re.findall('[0-9]+', str(i.find_element_by_xpath('div//li[@class="feed-comment"]').text))[0]
        except:
            comment = None
        try:
            share = re.findall('[0-9]+', str(i.find_element_by_xpath('div//li[@class="feed-share"]').text))[0]
        except:
            share = None
        link = i.find_element_by_xpath('div//p[@class="share-title"]/a').get_attribute("href")
        entry.extend((title, summary, like, comment, share, link))
        entry_list.append(entry)

    driver.close()
    return entry_list

