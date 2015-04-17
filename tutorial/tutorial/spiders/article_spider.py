# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

class ArticleSpider(scrapy.Spider):
    name = "article_spider"
    allowed_domains = ["nytimes.com","hercampus.com"]
    start_urls = [
        "http://www.nytimes.com/2015/04/17/business/obama-trade-legislation-fast-track-authority-trans-pacific-partnership.html",
        "http://www.hercampus.com/school/u-mass-amherst/fashion-finds-du-bois-vogue-collection"
    ]

    def parse(self, response):
        filename = response.url.split("/")[2]
        with open(filename, 'wb') as f:
            f.write(response.body)
