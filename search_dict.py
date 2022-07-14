# import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

import requests_html


from lxml import etree


# def scraper(word):
word = 'apple'
all_pages_reviews = []
#            https://en.dict.naver.com/#/search?range=meaning&page=4&query=apple&autoConvert=
base_url1 = "https://en.dict.naver.com/#/search?range=meaning&page="
base_url2 = "&query="
base_url3 = "&autoConvert="
for i in range(1,2):
    s = requests_html.HTMLSession()

    # query_parameter = "?page="+str(i) # i represents the page number
    pagewise_reviews = []
    url = base_url1 + str(i) + base_url2 + str(word) + base_url3
    # response = requests.get(url)
    page = s.get(url)
    soup=bs(page.text,'lxml')
    print(soup)
    # print(response)
    # soup = bs(response.content, 'html.parser')
    # print(soup)
    # print(soup.prettify())
    # rev_div = soup.findAll("div",attrs={"class","row"}) # /html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div[1] # xpath
    print(soup.get_text())

    # dom = etree.HTML(str(soup))
    # print(dom)
    # print(dom.xpath('/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]'))
    # print(dom.xpath('/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]')[0].text)
    # print(rev_div)
# if __name__=='__main__':
#     word = input('Type some thong : ')
#     scraper(word)