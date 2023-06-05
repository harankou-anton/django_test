import scrapy


class OmaSpider(scrapy.Spider):
    name = "oma.by"
    allowed_domains = ["www.oma.by"]
    start_urls = ["https://www.oma.by/velosipedy-c"]

    def parse(self, response, **kwargs):
        for product in response.css(".catalog-grid .product-item"):
            data = {
                "external_id": int(product.attrib.get("data-ga-product-id")),
                "name": product.attrib.get("data-ga-product-name").strip(),
                "price": product.attrib.get("data-ga-product-price").strip(),
                "category": product.attrib.get("data-ga-category-last").strip(),
                "link": f"{self.allowed_domains[0]}{product.css('a.area-link::attr(href)').get()}",
                "image": f"https://www.oma.by{product.css('img.catlg_list_img::attr(data-src)').get()}",
            }

            yield data

        next_page = response.css(
            ".page-nav_box .btn-combo .btn__nav-right::attr(href)"
        ).get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
