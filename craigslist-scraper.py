# Updated Craigslist scraper - current selectors (Nov 2026)
# scrapy runspider craigslist-scraper.py -O out.csv

import scrapy

class CraigslistSpider(scrapy.Spider):
    name = 'craigslist_apa'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://pittsburgh.craigslist.org/search/apa']

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'DOWNLOAD_DELAY': 1.5,
        'ROBOTSTXT_OBEY': False,
    }

    def parse(self, response):
        for row in response.css('div.cl-search-result'):
            item = {
                'title': row.attrib.get('title', '').strip() or row.css('a::text').get(default='').strip(),
                'price': row.css('.priceinfo::text').get(default='').strip(),
                'location': ' '.join(row.css('.meta::text').getall()).strip(),
                'pid': row.attrib.get('data-pid', ''),
                'url': response.urljoin(row.css('a::attr(href)').get(default='')),
            }
            if item['title']:
                yield item
