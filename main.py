import requests
from bs4 import BeautifulSoup

url = "https://www.buckedup.com/shop/men-bottoms/bucked-up-liner-shorts"
url2 = "https://www.google.com/"

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    

def main():
   print("testing")

   req = requests.get(url)
   soup = BeautifulSoup(req.content, 'html.parser')
#    print(soup.prettify())
#    print(soup.find_all("div", "container-fluid"))
# TODO not working because items are not selected which dynamically update the page. Not all information is stored individually. use XML? to force render page and grab info?
#use selenium to modifyy web page before grabbing. Fast way by modifying using API?
   print(soup.find_all("div", {"class": "quantity-container add-to-cart-container"}))

#    {"class": "tablebox"}


if __name__ == "__main__":
    main()