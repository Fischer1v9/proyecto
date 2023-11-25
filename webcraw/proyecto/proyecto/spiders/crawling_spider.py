from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item"),
    )

    def parse_item(self, response):
        yield {
            "Titulo": response.css(".product_main h1::text").get(),
            "Precio": response.css(".price_color::text").get().replace("£",""),
            "Disponibilidad": response.css(".availability::text")[1].get().replace("\n","").replace(" ","").replace("Instock", "").replace("(","").replace(")","").replace("available",""),
            "Enlace": response.url
        }