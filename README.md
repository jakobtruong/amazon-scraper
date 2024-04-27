# Amazon Product Web Scraper
This web scraper utilizes Playwright, BeautifulSoup4, and pandas to scrape and crawl through Amazon product search pages given a valid url as an input to extract relevant purchase information such as product name, product rating, image url, product url, and if the product is currently on sale. This has potential applications for Machine Learning projects where one would need various image urls for specific products. This web scraper could potentially act as a way to get all of the product urls to potentially scrape for user review information for a potential future sentiment analysis project.

## Installation
Navigate to the desired file directory location and clone the repository.
```bash
git clone https://github.com/jakobtruong/amazon-scraper.git
```

---
### Setting Up Virtual Environment (Optional)
In case any readers of this are unfamiliar with virtual environments, it is generally recommended to set up virtual environments for each project to create an isolated python environment. Virtual environments are stable, reproducible, and portable while leaving just the necessary dependencies for the project to execute successfully. This can help avoid various environment and dependency conflicts that can vary from developer to developer.

To create the virtual environment, use the following command. The last argument (ex: '.venv') can be freely renamed to anything the user decides to name the virtual environment folder.

```bash
python3 -m venv .venv
```

To activate the virtual environment, use the following command.
```bash
source .venv/bin/activate
```

To deactivate the virtual environment, use `deactivate` in the terminal.

Using `which python3` can be useful for identifying and confirming where your current Python3 path is pointing to.

---
Finally, install necessary dependencies using the following command.
```bash
pip install -r requirements.txt
```

## Usage
1. In a terminal, execute the amazon-scraper.py by using the following `python3 amazon-scraper.py`.
2. The program will prompt the user to enter a url. An example url can be found [here](https://www.amazon.com/s?k=technology&crid=25DJB16HLDJQB&sprefix=technology%2Caps%2C136&ref=nb_sb_noss_1).
3. The program will then prompt the user to enter an integer representing how many pages starting from the url given in the previous step as a starting point to web crawl and scrape.
4. The program will then output a .csv named amazon_products_listings.csv in the project's root directory.
![usage_example_gif](./usage_example.gif)

## Design Decisions
During the planning stage of this project, I contemplated on which libraries to use and which websites to potentially scrape. Being brand new to web scraping, I began researching and looking into the documentation of BeautifulSoup4 - a popular and powerful python library to extract information from HTML and XML. This library also seemed to have a strong community backing with easy to use documentation. From this point, I decided to use Requests, a HTTP python library, and BeautifulSoup4 to extract all the relevant HTML information coming back from the GET request.

Unfortunately, Amazon does restrict and limit users from web scraping to prevent overloading on their servers. This barrier led me to look for another solution to bypass many of the restrictions that Amazon places on web scrapers. This led to me to look into what goes into an HTTP request and what types of information in it would Amazon use to determine if the request came from a normal user browsing the site vs. a program used for web scraping. After looking into the network requests, I found that HTTP headers such as User-Agent and Accept-Language could be used to differentiate a normal user and a web scraper. This led me to look into web automation libraries such as Selenium and Playwright. These libraries work as general purpose browser automation tools allowing it to act as a real user. This would be particularly useful for automating page loading and scrolling through the whole page to expose dynamically rendered HTML. Upon reading some blogs comparing the two, I decided to use playwright for its newer, more advanced tool designed for modern web applications although either library would have sufficed for this project.

Finally, I needed a way to convert the data scraped from the program to a .csv file to be imported into databases for future projects. Although there are many libraries to do this, I wanted to get familiar with and use a popular Python library, pandas. After processing the data, the data was transformed to a [dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) which then had its own to_csv method to get the desired output.
## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
