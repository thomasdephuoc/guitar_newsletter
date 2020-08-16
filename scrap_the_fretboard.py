import scrapy


class GuitarSpider(scrapy.Spider):
    name = 'guitars_the_fretboard'
    start_urls = [
        'https://www.thefretboard.co.uk/categories/guitars-for-sale',
    ]

    def parse(self, response):
        for DiscussionName in response.css('div.DiscussionName'):
            yield {
                'Title': quote.xpath('span.Title::text').get(),

            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)