from lxml import html #pip install lxml
import requests #pip install requests
from requests import get
import os
from datetime import datetime


def data():
    siteNumber = 1
    url = "https://www.leroymerlin.pl/zabezpieczenie-domu/systemy-smart-home,a3358,strona-" + str(siteNumber) +".html"
    lista=""
    
    while get(url).ok:
        page = requests.get(url)
        tree = html.fromstring(page.content)
        xpath_noResults = '//*[@id="right-content"]/div[2]/text()'
        noResultsSite = tree.xpath(xpath_noResults)
        if  "W chwili obecnej trwają prace nad zaprezentowaniem w serwisie produktów z wybranej kategorii" in noResultsSite[1]:
            print("There is no other website in this category.")
            break
        else:
            xpath_selector='//*[@id="product-listing"]/div/a/h3/text()'
            products = tree.xpath(xpath_selector)
            lista =lista + "\nStrona: " + str(siteNumber) +"\n" + url +"\n"
            for product in products:
                lista=lista+product.strip()+"\n"
                # print(product.strip())           
        siteNumber+=1
        url = "https://www.leroymerlin.pl/zabezpieczenie-domu/systemy-smart-home,a3358,strona-" + str(siteNumber) +".html"
        # print(siteNumber)
        # print(url)
    return lista

def saveFile(lista):
    path = os.getcwd() + '\\created_files\\'
    plik = "wynik.txt"
    plikPath = path+plik
    now = datetime.now()
    date = now.strftime("%Y%m%d_%H%M%S")
    
    if os.path.isfile(plikPath):
        plikPath = path + "wynik_"+ date +".txt"
    f = open(plikPath,"w")
    f.write(lista)
    f.close()


def main(args):
    print("ściąganie danych ze strony i zapis do pliku.")
    # ściagniecie danych 
    listaWynik = data()
    # utworzenie pliku i zapisanie go
    saveFile(listaWynik)

if __name__ =='__main__':
    import sys
    sys.exit(main(sys.argv))
