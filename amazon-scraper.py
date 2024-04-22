import pandas as pd
import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import random

async def request_with_retry(page, url):
  MAX_RETRIES = 5
  curr_retries = 0
  while curr_retries < MAX_RETRIES:
    try:
      await page.goto(url)
      break
    except:
      curr_retries += 1
      if curr_retries == MAX_RETRIES:
        raise Exception('Request timed out')
      await asyncio.sleep(random.uniform(1, 5))

# Takes amazon product url as input and returns a list of results
async def scrape_amazon(product_url):
  async with async_playwright() as pw:
    # Launch new browser
    browser = await pw.chromium.launch(headless=True)
    page = await browser.new_page()

    current_url = product_url
    # Crawl and scrape through product pages until there is no longer a 'next page'
    # Need to consider edge cases here so that does not loop indefinitely. Could make it a function and add a max_iterations argument
    while current_url != 'N/A':
      print('Scraping product url:', current_url)
      # Go to Amazon product URL and parse html
      await request_with_retry(page, current_url)

      html = await page.content()
      soup = BeautifulSoup(html,'html.parser')
      # Extract information from all listings on product page
      results = []
      listings = soup.find_all('div', class_='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20')

      for listing in listings:
        result = {}

        product_name = listing.find('span', class_='a-size-base-plus a-color-base a-text-normal').text if listing.find('span', class_='a-size-base-plus a-color-base a-text-normal') else 'N/A'
        result['product_name'] = product_name

        product_rating = listing.find('span', class_='a-icon-alt').text[0:3] if listing.find('span', class_='a-icon-alt') else 'N/A'
        result['product_rating'] = product_rating

        product_limited_deal = True if listing.find('span', id=lambda x:x and x.startswith('BEST_DEAL')) else False
        result['product_is_limited_deal'] = product_limited_deal

        product_url = 'https://www.amazon.com' + listing.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')['href'] if listing.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')['href'] else 'N/A'
        result['product_url'] = product_url

        results.append(result)
      next_page_url = 'https://www.amazon.com' + soup.find('a', class_='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator')['href'] if soup.find('a', class_='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator')['href'] else 'N/A'
      current_url = next_page_url
    await browser.close()
    return results

def main():
  amazon_search_url = 'https://www.amazon.com/s?k=technology&crid=397VY8LH02RMK&sprefix=technology%2Caps%2C332&ref=nb_sb_noss_2'
  results = asyncio.run(scrape_amazon(amazon_search_url))
  df = pd.DataFrame(results)
  df.to_csv('amazon_products_listings.csv', index=False)

if __name__ == '__main__':
  main()
