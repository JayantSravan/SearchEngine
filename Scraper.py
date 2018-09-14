import bs4 as bs
import codecs
import sys
from urllib.request import urlopen, Request
from unidecode import unidecode
# -*- coding: utf-8 -*-

#create this class's object to scrape
class Scraper:
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'} #to emulate a browser

    def scrapeTheEpisodeScript(self, reg_url): #this function gets script of an episode given its url
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
        req = Request(url=reg_url, headers=self.headers)
        sauce = urlopen(req).read() #reading html page


        soup = bs.BeautifulSoup(sauce,'lxml') #parse the html
        body = soup.body #take the body part of the page only
        f = open("ScraperOutputs/testOutput.txt","w", encoding = "utf-8") #this is where a temporary file is created which stores the script of that particular episode
        for div in body.find_all('div', class_='postbody'): #all the content is present in the class caleed postbody. Select and scrape it
            for para in div.find_all('p'): #take all the paragraph tags
                para.encode(encoding="utf-8").strip() #the text is in unicode
                para = para.text.encode('utf-8')
                para = para.decode("utf-8", "ignore")
                para = para + '\n'
                f.write(para)
        f.close()

    def scrapeSeries(self, url): #this method takes the url of the particular TV series and finds url of all the episodes and calls scrpaeTheEpisodeScript method Mr.Yash Gupta to implement this
        pass # pass just means you are yet to implement this. Replace it with your implementation.

    def scrapeWebsite(self, url): #this one gets TV series list and their urls and calls scrapeSeries method. Mr. Yash Gupta, please implement this also
        pass # pass just means you are yet to implement this. Replace it with your implementation.


#just a demo script
s = Scraper('http://transcripts.foreverdreaming.org/index.php')
url = 'http://transcripts.foreverdreaming.org/viewtopic.php?f=177&t=11509'
s.scrapeTheEpisodeScript(url)
