import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule



class CoinrrencySpider(CrawlSpider):
    name = "coinrrency"
    allowed_domains = ["web.archive.org"]
    start_urls = ["https://web.archive.org/web/20190101085451/https://coinmarketcap.com"]

    rules = (Rule(LinkExtractor(restrict_xpaths=("//a[@class='currency-name-container link-secondary']")), callback="parse_item", follow=True),)

    def parse_item(self, response):
        coin_name = response.xpath("(normalize-space(//h1[@class='details-panel-item--name']/text()[2]))").get()
        abbreviation = response.xpath("normalize-space(//h1[@class='details-panel-item--name']/span/text())").get()
        amount = response.xpath("normalize-space(//span[@class='h2 text-semi-bold details-panel-item--price__value']/text())").get()
        difference = response.xpath("normalize-space(//span[@class='h2 text-semi-bold negative_change']/span/text())").get()
        value = response.xpath("normalize-space(//span[@class='text-gray']/span/text())").get()
        rank = response.xpath("normalize-space(//span[@class='label label-success']/text())").get()

        yield {
            'coin_name': coin_name,
            'abbreviated_name': abbreviation,
            'amount': amount,
            'difference': difference,
            'value': value,
            'rank': rank
        }

    