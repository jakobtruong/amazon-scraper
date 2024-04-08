import requests
from bs4 import BeautifulSoup

# HEADERS = {
#   'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'),
#   'Accept-Language': 'en-US, en;q=0.9'
# }
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.9'})
product_url = 'https://www.amazon.com/s?k=computer+stand&crid=160JN6TSDRUXD&sprefix=computer%2Caps%2C172&ref=nb_sb_ss_ts-doa-p_8_8'

def get_data(url, custom_headers):
  page = requests.get(url, custom_headers)
  if page.status_code != 200:
    print('The product url provided does not return a 200 status code')

  soup = BeautifulSoup(page.text,'html.parser').prettify
  print(soup)
  return

def main():
  getdata(product_url, HEADERS)
  return

if __name__ == '__main__':
  main()
