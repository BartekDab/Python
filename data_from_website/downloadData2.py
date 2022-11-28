from lxml import html #pip install lxml
import requests #pip install requests
from requests import get

plik = "wynik.txt"

siteNumber = 1
url = "https://www.leroymerlin.pl/zabezpieczenie-domu/systemy-smart-home,a3358,strona-" + str(siteNumber) +".html"
# urlCheck = get(url)
lista = ""

while get(url).ok:#urlCheck.ok
    url = "https://www.leroymerlin.pl/zabezpieczenie-domu/systemy-smart-home,a3358,strona-" + str(siteNumber) +".html"
    page = requests.get(url)
    tree = html.fromstring(page.content)
    xpath_noResults = '//*[@id="right-content"]/div[2]/text()'
    noResultsSite = tree.xpath(xpath_noResults)
    if "W chwili obecnej trwają prace nad zaprezentowaniem w serwisie produktów z wybranej kategorii" in noResultsSite[1]:
        print("Nie ma strony.")
        break
    else:
        xpath_selector='//*[@id="product-listing"]/div/a/h3/text()'
        products = tree.xpath(xpath_selector)
        #print("\nStrona: " + str(siteNumber))
        # print(url)
        lista =lista + "\nStrona: " + str(siteNumber)
        for product in products:
            lista=lista+product.strip()+"\n"
            # print(product.strip())
        siteNumber+=1

f = open(plik,"w")
f.write(lista)
f.close()
