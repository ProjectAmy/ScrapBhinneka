import scrapy
from ..items import TerlarisItem

class TerlarisSpider(scrapy.Spider):
    name = "terlaris"
    allowed_domains = ["bhinneka.com"]
    start_urls = ["https://bhinneka.com/promo/bhinneka-top-sale"]

    def parse(self, response):

        # Mengambil semua link di halaman produk
        urls = response.css("a.product-wrapper ::attr(href)").getall()

        # Link dibuka satu per satu
        for url in urls:

            # jika url nya relatif
            if "bhinneka.com" not in url:
                url =response.urljoin(url)

            # mencari detail
            yield scrapy.Request(url, callback=self.find_detail, dont_filter=True) # Tanpa filter url

    def find_detail(self, response):
        pass