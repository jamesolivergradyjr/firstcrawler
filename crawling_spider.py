#Web Scraping : Extract data from a website

#Web crawling: find links, find urls, find branches off that website | urls with specific patterns

# inherit from CrawlSpider class | rule class to specify site crawl rules
from scrapy.spiders import CrawlSpider, Rule
# linkextracter
from scrapy.linkextractors import LinkExtractor

# creating a custom spider class (global naming limitation)
class CrawlingSpider(CrawlSpider):
    name = "mycrawler" #assigning name to this spider (programs used for crawling)
    allowed_domains = ["toscrape.com"] #list only the urls targetted for scraping/crawling
    start_urls = ["http://books.toscrape.com/"] #base-point to start the scraping/crawling process

    
    rules = (
        # Rules to define the links (in site) we will be looking for | this limits the crawling to these link types
        Rule(LinkExtractor(allow="catalogue/category")),
        # crawler finds all links that fit this rule
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")

    )
    # the parse_item function called in the rules
    # extracts title, price, availability using the css language based on 'inspect' feature in chrome
    def parse_item(self, response):
        # yield keyword (generator, not a return) not return, as we want the printout on the screen
        yield {
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
            "availability": response.css(".availability::text")[2].get()
        }