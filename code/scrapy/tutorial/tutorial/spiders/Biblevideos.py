import scrapy

class VideosSpider(scrapy.Spider):
    # name of the spider
    name = "videos"

    # a list of starting urls
    start_urls = [
        "https://www.churchofjesuschrist.org/media/collection/bible-videos-the-life-of-jesus-christ?lang=eng"
    ]

    # default parsing method
    def parse(self, response):
        # extracts links to different folders eg Nativity, Miracles, Teachings into a list using css parsing
        links = response.css("#__next > churchofjesuschrist-eden-normalize > div:nth-child(3) > div > div >div > div >a ::attr(href)").extract()
        """        
        # parsing using xpath, it is equivalent to the css example above
        divs = response.xpath("//*[@id=\"__next\"]/churchofjesuschrist-eden-normalize/div[3]/div/div")
        for div in divs:
            href = div.xpath("div/a/@href").extract()
        """

        for link in links:
            # creates a full link from a relative link
            full_link = response.urljoin(link)
            
            # follows the full_link and parses the response as callback using parse_download link
            yield scrapy.Request(full_link, callback=self.parse_download_link)

    # This method parses each video site and extracts the download link into a dictionary
    # with the title as key and link as value 
    # It is the callback method for the parse_download_link method
    def get_download_link(self, response):
        # extract download link
        # using css 
        download_link = response.css("#__next > churchofjesuschrist-eden-normalize > div > div > section > div > div > section > div.sc-1kxk49n-1.jsHngM > div:nth-child(3) > section.sc-1dbjm18-7.dJyqAY > div > a ::attr(href)").getall()

        # using xpath
        # download_link = response.css("//*[@id=\"__next\"]/churchofjesuschrist-eden-normalize/div/div/section/div/div/section/div[1]/div[2]/section[2]/div[1]/a/@href").extract()
        
        # extracts the title using css
        video_title = response.css("#__next > churchofjesuschrist-eden-normalize > div > div > section > div > div > section > div.sc-1kxk49n-1.jsHngM > h2::text").get()

        # yields a dictionary with video title as key and download link as value
        yield {
            video_title:download_link
        }       

    # This parsing method gets all the links for videos in a given folder
    # It is the callback method of parse() method

    def parse_download_link(self,response):
        # extract the links for download sites
        download_site_links = response.css("#__next > churchofjesuschrist-eden-normalize > div:nth-child(3) > div > div > div > div > a ::attr(href)").getall()

        # loop that goes through each link in download_site_links
        for link in download_site_links:

            # gets the full link from the relative link
            link=response.urljoin(link)

            # follows the download_site_link
            # and does the callback using the get_download_link method as the parsing method for the link
            yield response.follow(link, callback=self.get_download_link)

    

        

    
     
