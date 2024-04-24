# Amazon Product Web Scraper
This web scraper utilizes Playwright, BeautifulSoup4, and pandas to scrape and crawl through Amazon product search pages given a valid url as an input to extract relevant purchase information such as product name, product rating, image url, product url, and if the product is currently on sale.
## Installation
Navigate to the desired file directory location and clone the repository.
```bash
git clone https://github.com/jakobtruong/amazon-scraper.git
```

### Setting Up Virtual Environment (Optional)
In case any readers of this are unfamiliar with virtual environments, it is generally recommended to set up virtual environments for each project to create an isolated python environment. Virtual environments are stable, reproducable, and portable while leaving just the necessary dependencies for the project to execute successfully.

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
Simply execute the amazon-scraper.py by using the folowing:
```bash
python3 amazone-scraper.py
```

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
