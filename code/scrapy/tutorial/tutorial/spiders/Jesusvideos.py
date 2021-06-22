import scrapy

class VideosSpider(scrapy.Spider):
    name = "videos"
    start_urls = [
        "https://www.churchofjesuschrist.org/media/collection/bible-videos-the-life-of-jesus-christ?lang=eng"
    ]

    def parse(self, response):
        links = list()
        links = response.css("#__next > churchofjesuschrist-eden-normalize > div:nth-child(3) > div > div >div > div >a ::attr(href)").extract()
        """        
        # parsing using xpath, it is equivalent to the css example above
        divs = response.xpath("//*[@id=\"__next\"]/churchofjesuschrist-eden-normalize/div[3]/div/div")
        for div in divs:
            href = div.xpath("div/a/@href").extract()
        """
        # print(links)
        i =1
        for link in links:
            print(link)
            yield {
                i : link
            }
            i+=1





        