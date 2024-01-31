import time
import requests
from bs4 import BeautifulSoup

while True:
    url = "https://kur.doviz.com/"
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    
    table = soup.find("div", {"class": "table sortable"}).find_all("tr", limit=5)
    
    for item in table:
        currency_name = item.find("div", {"class": "cname"})
        currency_price = item.find("td",{"data-socket-attr": "ask"})
        if currency_name and currency_price:
            print(currency_name.text.strip(), currency_price.text.strip())
    time.sleep(60)
