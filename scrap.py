#from bs4 import BeautifulSoup
#import requests
#from requests_html import HTMLSession
import time
#import os


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


#import os
import csv

def url_build(name):
    url = "https://www.tcgplayer.com/search/magic/product?Language=English&productLineName=magic"
    url += "&Condition=Near+Mint|Lightly+Played"
    url += "&printing=Foil|Normal"
    name= name.lower()
    name = name.replace(" ", "+")

    url +=" &q=" + name + "&view=grid&page=1"
    return url

def input_cvs(file):
    cards = []
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            cards.append(row)
    
    print(cards)
    return cards

def main():
    cards = input_cvs("input.csv")

    driver = webdriver.Firefox()
    """ driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    time.sleep(2)"""
    for card in cards[:2]:
        url = url_build(card[0])
        driver.get(url)
        time.sleep(3)
        price = driver.find_elements(By.CLASS_NAME, "inventory__price-with-shipping")
        print(price.text)
        

    driver.close()

    exit()

"""    url = "https://www.tcgplayer.com/search/magic/product?productLineName=magic&q=Llanowar+Elves&view=grid"
    session = HTMLSession()
    r = session.get(url)
    r.html.render()
    page = requests.get(url)
    soup  = BeautifulSoup(r.content, "html.parser")
    #print(soup.prettify())
    #print(soup.find_all("span"))
    #print(soup.find_all("span", {"class": "inventory__price"}))"""




if __name__ == "__main__":
    main()