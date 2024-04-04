# Web Scraping CoinMarketCap Website Using Wayback Machine

This project aims to extract data from the CoinMarketCap website using the Wayback Machine and Scrapy. The data includes information such as the coin name, abbreviated name, amount, difference, value, and rank. The scraped data is then saved as a CSV file for further analysis.

## Overview

CoinMarketCap is a popular website for tracking cryptocurrency prices and market capitalization. However, due to changes in website structure or policies, it may be necessary to retrieve historical data using web archives such as the Wayback Machine.

## Requirements

- Python
- Scrapy
- Wayback Machine API (optional)

## Installation

1. Clone this repository:

```
git clone https://github.com/your_username/coinmarketcap-webscraper.git
```

2. Install dependencies:

```
pip install scrapy
```

3. Run the scraper:

```
scrapy crawl coinmarketcap -o data.csv
```

## Process

1. **Identifying Target Data**: The first step is to determine the specific data fields to be scraped from the CoinMarketCap website. This includes the coin name, abbreviated name, amount, difference, value, and rank.

2. **Configuring Scrapy Spider**: A Scrapy spider is created to navigate the CoinMarketCap website's archived pages on the Wayback Machine. The spider is configured to extract the desired data fields from each page.

3. **Navigating Archived Pages**: The Wayback Machine API (optional) can be utilized to programmatically retrieve archived URLs for CoinMarketCap. Alternatively, archived URLs can be manually collected and provided to the Scrapy spider.

4. **Extracting Data**: Using XPath or CSS selectors, the Scrapy spider extracts the relevant data from each archived page. This data is then processed and cleaned as necessary.

5. **Saving Data**: The scraped data is saved to a CSV file using Scrapy's built-in functionality. This CSV file serves as the output for further analysis or visualization.

## Usage

To use this scraper, simply run the Scrapy spider with the appropriate command-line arguments. Specify the output file where the scraped data will be saved.

```
scrapy crawl coinmarketcap -o data.csv
```

## Conclusion

By utilizing the Wayback Machine and Scrapy, it is possible to retrieve historical data from the CoinMarketCap website. This data can provide valuable insights into past cryptocurrency trends and market movements. The resulting CSV file can be further analyzed or integrated into other data pipelines as needed.

### website view

![image](https://github.com/FaeyO/webscrapping-coinmarketcap-website/assets/118575325/98f2f5f8-11ac-4a5c-8737-10f1bc5ec579)
