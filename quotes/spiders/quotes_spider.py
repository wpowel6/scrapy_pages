import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'

    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('div.quote')

        for quote in quotes:
            yield {
                'author': quote.css('small.author::text').get(),
                'text': quote.css('span.text::text').get().replace('“','').replace('”','')
            }

        next_page = response.css('li.next a').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
