from lxml import html #pip install lxml
import requests #pip install requests

# url = "https://www.leroymerlin.pl/zabezpieczenie-domu/systemy-smart-home,a3358.html"
url = "https://www.leroymerlin.pl/zabezpieczenie-domu/systemy-smart-home,a3358,strona-2.html"
page = requests.get(url)
tree = html.fromstring(page.content)
xpath_selector='//*[@id="product-listing"]/div/a/h3/text()'
products = tree.xpath(xpath_selector)
for product in products:
    print(product.strip())

