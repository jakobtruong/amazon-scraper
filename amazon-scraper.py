import pandas as pd
import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import random

# Retry requested url a max of 5 times with a random uniform 1-3 second timeout between each retry
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
      await asyncio.sleep(random.uniform(1, 3))

# Takes amazon product url as input and max_pages to crawl through and returns a list of results
async def scrape_amazon(product_url, max_pages = 1):
  async with async_playwright() as pw:
    # Launch new browser - Used firefox since Chromium would sometimes return a error amazon page
    browser = await pw.firefox.launch(headless=True)
    page = await browser.new_page()

    # Crawl and scrape through product pages until there is no longer a 'next page'
    results = []
    current_iterations = 0
    current_url = product_url
    while current_url != 'N/A' and current_iterations < max_pages:
      # Prints current url being scraped for feedback and debugging
      print('Scraping product url:', current_url)

      # Go to Amazon product URL and parse html
      await request_with_retry(page, current_url)
      html = await page.content()
      soup = BeautifulSoup(html,'html.parser')

      # On cases where amazon
      if soup.find('title').text == 'Sorry! Something went wrong!':
        print('Something went wrong with the scraping. Adjust configurations.')
        break

      listings = soup.find_all('div', class_='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20')
      for listing in listings:
        result = {}

        product_name = listing.find('span', class_='a-size-base-plus a-color-base a-text-normal').text if listing.find('span', class_='a-size-base-plus a-color-base a-text-normal') else 'N/A'
        result['product_name'] = product_name

        product_rating = float(listing.find('span', class_='a-icon-alt').text[0:3]) if listing.find('span', class_='a-icon-alt') else 'N/A'
        result['product_rating'] = product_rating

        product_limited_deal = True if listing.find('span', class_='a-badge-text') and listing.find('span', class_='a-badge-text').text == 'Limited time deal' else False
        result['product_is_limited_deal'] = product_limited_deal

        product_url = 'https://www.amazon.com' + listing.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')['href'] if listing.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal') else 'N/A'
        result['product_url'] = product_url

        product_image_url = listing.find('img', class_='s-image')['src'] if listing.find('img', class_='s-image')['src'] else 'N/A'
        result['product_image_url'] = product_image_url

        results.append(result)
      next_page_url = 'https://www.amazon.com' + soup.find('a', class_='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator')['href'] if soup.find('a', class_='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator') else 'N/A'
      current_url = next_page_url
      current_iterations += 1
    await browser.close()
    return results

def main():
  # Base url we are trying to web scrape
  print('Example url: https://www.amazon.com/s?k=technology&crid=25DJB16HLDJQB&sprefix=technology%2Caps%2C136&ref=nb_sb_noss_1')
  user_input_url = input('Enter Amazon product search url to scrape: ')
  max_pages_to_scrape = int(input('Enter maximum number of pages to scrape (int): '))

  # Get the data from url and formats/outputs the data as a csv using pandas
  results = asyncio.run(scrape_amazon(user_input_url, max_pages_to_scrape))
  df = pd.DataFrame(results)
  df.to_csv('amazon_products_listings.csv', index=False)
  print('csv has been written successfully!')

if __name__ == '__main__':
  main()
