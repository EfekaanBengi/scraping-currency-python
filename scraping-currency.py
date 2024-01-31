import time
import requests
from bs4 import BeautifulSoup

while True:       # LOOP this code
    url = "https://kur.doviz.com/"                # Website url
    html = requests.get(url).content              # Getting website content with request module
    soup = BeautifulSoup(html, "html.parser")     
    
    table = soup.find("div", {"class": "table sortable"}).find_all("tr", limit=5)    # Choose a block of code that has all the values we need
    
    for item in table:
        currency_name = item.find("div", {"class": "cname"})            # Choose a block of code that has specifically we need
        currency_price = item.find("td",{"data-socket-attr": "ask"})    # Choose a block of code that has specifically we need
        if currency_name and currency_price:
            print(currency_name.text.strip(), currency_price.text.strip())   # Print Values
    time.sleep(60)    # Waits 60 seconds (1 minute) each time the code repeats
