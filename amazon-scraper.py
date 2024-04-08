from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

website_to_scrape = 'http://books.toscrape.com/'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
options.page_load_strategy = 'normal'
driver = webdriver.Chrome()
driver.get(website_to_scrape)
page = driver.page_source
soup = BeautifulSoup(page)
print(soup)
def main():
    while True:
      pass

if __name__ == '__main__':
  main()
