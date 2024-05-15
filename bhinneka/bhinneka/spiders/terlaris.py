import scrapy
from ..items import TerlarisItem

class TerlarisSpider(scrapy.Spider):
    name = "terlaris"
    allowed_domains = ["bhinneka.com"]
    start_urls = ["https://bhinneka.com/promo/bhinneka-top-sale"]

    custom_settings = {
        "ITEM_PIPELINES": {"bhinneka.pipelines.TerlarisPipeline": 300},
    }

    def parse(self, response):

        # Mengambil semua link di halaman produk
        urls = response.css("a.product-wrapper ::attr(href)").getall()

        # Link dibuka satu per satu
        for url in urls:

            # jika url nya relatif
            if "bhinneka.com" not in url:
                url =response.urljoin(url)

            # mencari detail
            yield scrapy.Request(url, callback=self.detail, dont_filter=True) # Tanpa filter url

    def detail(self, response):
        item = TerlarisItem()
        item['nama'] = response.css("#product_details > h1::text").get()
        item['harga'] = response.css("span.oe_currency_value::text").get()
        item['cicilan'] = response.css("span.installments-data > strong > span.oe_currency_value::text").get()
        item['link'] = response.url

        yield item # Menghasilkan list