import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
# https://linuxhint.com/chrome_selenium_headless_running/#:~:text=So%2C%20Selenium%20can%20do%20web,web%20browser%20in%20headless%20mode.
# https://medium.com/ymedialabs-innovation/web-scraping-using-beautiful-soup-and-selenium-for-dynamic-page-2f8ad15efe25
url = "https://www.buckedup.com/shop/men-bottoms/bucked-up-liner-shorts"
url2 = "https://www.google.com/"

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


def configureDriver():
   options = webdriver.ChromeOptions()
   options.add_argument('--ignore-certificate-errors')
   options.add_argument('--incognito')
   # options.add_argument('--headless')
   driver = webdriver.Chrome("/chromedriver", chrome_options=options)
   return driver

def selectItem(driver):
   #Clicks drop down menu for color
   print('clicks drop down menu for colors')
   driver.find_element(By.XPATH, '//*[@id="product-page"]/div/div[1]/div[2]/div[3]/div[1]/select').click()
   # selects dark gray
   print('selects gray/white')
   driver.find_element(By.XPATH, '//*[@id="product-page"]/div/div[1]/div[2]/div[3]/div[1]/select/option[5]').click()

def selectSize(driver):
   print('select the drop down for size')
   driver.find_element(By.XPATH, '//*[@id="product-page"]/div/div[1]/div[2]/div[3]/div[2]/select').click()
   print('select size large')
   driver.find_element(By.XPATH, '//*[@id="product-page"]/div/div[1]/div[2]/div[3]/div[2]/select/option[4]').click()


def main():
   print("testing")
   driver = configureDriver()
   driver.get("https://www.buckedup.com/shop/men-bottoms/bucked-up-liner-shorts")
   selectItem(driver)
   selectSize(driver)
   driver.save_screenshot('ss.png')
   screenshot = Image.open('ss.png')
   screenshot.show()

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