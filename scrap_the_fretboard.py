import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'guitars_the_fretboard'
    start_urls = [
        'https://www.thefretboard.co.uk/categories/guitars-for-sale',
    ]

    def parse(self, response):
        for guitar in response.css('div.Wrap'):
            yield {
                'Title': quote.css('span.Title::').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)