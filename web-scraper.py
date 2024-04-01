from bs4 import BeautifulSoup
from selenium import webdriver

website_to_scrape = 'http://books.toscrape.com/'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome()
driver.get(website_to_scrape)

def main():
    while True:
      pass

if __name__ == "__main__":
  main()
