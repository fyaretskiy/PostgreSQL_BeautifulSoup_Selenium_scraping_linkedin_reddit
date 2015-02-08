import re
import requests
from bs4 import BeautifulSoup

"""Should be renamed for specificity to reddit"""

# url = 'http://www.reddit.com/r/worldnews'
def get_data(url):
    """receives URL and returns a list of list."""
    a = requests.get(url)
    name = url #the title of the table will be the url
    soup = BeautifulSoup(a.text)
    top = soup.find("div", id="siteTable", class_="sitetable linklisting")

    entry_list = []
    entry = []
    for i in top.findAll(onclick="click_thing(this)"):
        title = i.find("p", class_="title").get_text()
        link = i.find("p", class_="title").find('a')['href']
        votes = i.find("div", class_="midcol unvoted").find(class_="likes").get_text()
        #sometimes a votes number is not given
        if votes.isdigit() is False:
            votes = None
        comment = str(i.find("li", class_="first").get_text())
        comments = re.sub('[a-zA-Z]+', "", comment).replace(" ", "")  # removed the 'comments'/'comment'
        if comments.isdigit() is False:
            comments = None
        entry.extend((title, link, votes, comments))

        entry_list.append(entry)
        entry = []

    return entry_list

#for testing:

# url = 'http://www.reddit.com/r/worldnews'
# get_data(url)
    #



