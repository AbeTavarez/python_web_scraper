import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        # urlopen() makes a request to the site and
        # returns a responce object
        # with html from the site we passed in.
        res = urllib.request\
            .urlopen(self.site)
        html = res.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        # finding the target
        for tag in sp.find_all("a"):
            url = tag.get("href")
            # print("\n" + url)
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)


url_to_scrape = 'http://econpy.pythonanywhere.com/ex/001.html'
scraper_results = Scraper(url_to_scrape)
scraper_results.scrape()
