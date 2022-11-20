from lxml import html #pip install lxml
import requests #pip install requests
from requests import get

siteNumber = 1
url = "https://www.leroymerlin.pl/zabezpieczenie-domu/systemy-smart-home,a3358,strona-" + str(siteNumber) +".html"
# urlCheck = get(url)

while get(url).ok:#urlCheck.ok
    url = "https://www.leroymerlin.pl/zabezpieczenie-domu/systemy-smart-home,a3358,strona-" + str(siteNumber) +".html"
    page = requests.get(url)
    tree = html.fromstring(page.content)
    xpath_noResults = '//*[@id="right-content"]/div[2]/text()'
    noResultsSite = tree.xpath(xpath_noResults)
    if "W chwili obecnej trwają prace nad zaprezentowaniem w serwisie produktów z wybranej kategorii" in noResultsSite[1]:
        print("Nie ma strony.")
        exit()
    else:
        xpath_selector='//*[@id="product-listing"]/div/a/h3/text()'
        products = tree.xpath(xpath_selector)
        print("\nStrona: " + str(siteNumber))
        # print(url)
        for product in products:
            print(product.strip())
        siteNumber+=1

