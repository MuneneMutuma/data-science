import scrapy


class w3resource(scrapy.Spider):

    start_urls = [
        "https://www.w3resource.com/python-exercises/numpy/basic/numpy-basic-exercise-2.php"
    ]

    def parse(self, response):
        heading = response.css("#h_one")
        question = response.css("body > div > div > main > div > div > div.mdl-cell.mdl-card.mdl-shadow--2dp.through.mdl-shadow--6dp.mdl-cell--9-col > article > p:nth-child(6)")

        solution = response