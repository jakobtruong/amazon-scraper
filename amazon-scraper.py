import pandas as pd
import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from time import sleep

amazon_search_url = 'https://www.amazon.com/s?k=technology&crid=397VY8LH02RMK&sprefix=technology%2Caps%2C332&ref=nb_sb_noss_2'

async def scrape_amazon():
  async with async_playwright() as pw:
    # Launch new browser
    browser = await pw.chromium.launch(headless=False)
    page = await browser.new_page()
    # Go to Amazon product URL and parse html
    await page.goto(amazon_search_url)
    html = await page.content()
    soup = BeautifulSoup(html,'html.parser')
    # Extract information
    results = []
    listing = soup.find('div', class_='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20')
    print(listing)
    product_name = listing.find('span', class_='a-size-base-plus a-color-base a-text-normal').text
    product_rating = listing.find('span[aria-label*="out of 5 stars"] > span.a-size-base')
    print('product name: ', product_name)

    await browser.close()

def main():
  results = asyncio.run(scrape_amazon())


if __name__ == '__main__':
  main()
