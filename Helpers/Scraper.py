<<<<<<< HEAD
from bs4 import BeautifulSoup
# import sys
from urllib.request import urlopen, Request
import requests
import os
import re  # for regex
import time  # for sleeping , so don't get blocked again

# from unidecode import unidecode
# -*- coding: utf-8 -*-


# import pdb
# pdb.set_trace()


# create this class's object to scrape
class Scraper:

  def __init__(self, url):
    self.url = url
    self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Connection': 'keep-alive'}  # to emulate a browser
    self.seriesName = "The Simpsons"
    self.episodeName = "0"

  def cleanString(self):
    self.seriesName = re.sub('\W+', ' ', self.seriesName)
    self.seriesName = self.seriesName.rstrip()

    self.episodeName = re.sub('\W+', ' ', self.episodeName)

  def scrapeTheEpisodeScript(self, reg_url):  # this function gets script of an episode given its url
    print('jayant class came ')
    req = Request(url=reg_url, headers=self.headers)
    sauce = urlopen(req).read()  # reading html page

    soup = BeautifulSoup(sauce, 'lxml')  # parse the html
    body = soup.body  # take the body part of the page only

    self.cleanString()

    filePath = "./Newdata/" + self.seriesName
    if not os.path.isdir(filePath):
      os.makedirs(filePath)

    f = open(filePath + "/" + self.seriesName + " - " + self.episodeName + ".txt", "w", encoding="utf - 8")  # this is where a temporary file is created which stores the script of that particular episode

    for div in body.find_all('div', class_='postbody'):  # all the content is present in the class caleed postbody. Select and scrape it
      for para in div.find_all('p'):  # take all the paragraph tags
        para.encode(encoding="utf-8").strip()  # the text is in unicode
        para = para.text.encode('utf-8')
        para = para.decode("utf-8", "ignore")
        para = para + '\n'
        f.write(para)
    f.close()

  def scappingSinglePageSeries(self, url):
    req_url = url

    try:
      source = requests.get(url=req_url, headers=self.headers).text  # headr to make it look real , site is not allowing it wihtout it
    except requests.ConnectionError as e:
      print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
      print(str(e))
    except requests.Timeout as e:
      print("OOPS!! Timeout Error")
      print(str(e))
    except requests.RequestException as e:
      print("OOPS!! General Error")
      print(str(e))
    except KeyboardInterrupt:
      print("Someone closed the program")
    except AttributeError:
      print("attrubute error aaya")
    except:
      print("pta nhi kuch error aaya ,but pakada gya")

    soup = BeautifulSoup(source, 'lxml')

    for link in soup.find_all('td', class_='topic-titles row2'):
      for temp in link.find_all('a', class_='topictitle'):
        self.episodeName = temp.text
        url = temp['href']
        url = 'http://transcripts.foreverdreaming.org' + url[1:]
        self.scrapeTheEpisodeScript(url)

  def scrapeSeries(self, url):  # this one scare is used to scarpe one tv series
    req_url = url

    try:
      source = requests.get(url=req_url, headers=self.headers).text  # headr to make it look real , site is not allowing it wihtout it
    except requests.ConnectionError as e:
      print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
      print(str(e))
    except requests.Timeout as e:
      print("OOPS!! Timeout Error")
      print(str(e))
    except requests.RequestException as e:
      print("OOPS!! General Error")
      print(str(e))
    except KeyboardInterrupt:
      print("Someone closed the program")
    except AttributeError:
      print("attrubute error aaya")
    except:
      print("pta nhi kuch error aaya ,but pakada gya")

    soup = BeautifulSoup(source, 'lxml')

    self.scappingSinglePageSeries(req_url)  # scrapping one single episode

    for link in soup.find_all('div', class_='box extra-content control-box top'):
      link = link.find('b', class_='pagination')
      try:
        for temp in link.find_all('a'):
          if temp.text == '»':
            url = temp['href']
            url = 'http://transcripts.foreverdreaming.org' + url[1:]
            self.scrapeSeries(url)
          else:
            pass
      except requests.ConnectionError as e:
        print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
        print(str(e))
      except requests.Timeout as e:
        print("OOPS!! Timeout Error")
        print(str(e))
      except requests.RequestException as e:
        print("OOPS!! General Error")
        print(str(e))
      except KeyboardInterrupt:
        print("Someone closed the program")
      except AttributeError:
        print("attrubute error aaya")

  def noReduntantOperation(self):
    self.cleanString()

    filePath = "./data/" + self.seriesName
    if os.path.isdir(filePath):
      return True

  def scrapeWebsite(self):  # this one gets TV series list and their urls and calls scrapeSeries method. Mr. Yash Gupta, please implement this also
    req_url = self.url

    try:
      source = requests.get(url=req_url, headers=self.headers).text  # header to make it look real , site is not allowing it wihtout it
    except requests.ConnectionError as e:
      print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
      print(str(e))
    except requests.Timeout as e:
      print("OOPS!! Timeout Error")
      print(str(e))
    except requests.RequestException as e:
      print("OOPS!! General Error")
      print(str(e))
    except KeyboardInterrupt:
      print("Someone closed the program")
    except AttributeError:
      print("attrubute error aaya")
    except:
      print("pta nhi kuch error aaya ,but pakada gya")

    soup = BeautifulSoup(source, 'lxml')

    for link in soup.find_all('p', class_='forumdesc subforums'):
      for temp in link.find_all('a', class_='subforum'):
        self.seriesName = temp.text

        if self.noReduntantOperation() is True:
          continue

        time.sleep(5)
        print(self.seriesName)
        print()

        url = temp['href']  # taking the href part of a
        url = 'http://transcripts.foreverdreaming.org' + url[1:]
        self.scrapeSeries(url)



# just a demo-main script
main_url = 'http://transcripts.foreverdreaming.org'
s = Scraper(main_url)
# s.scrapeWebsite()
# s.scrapeSeries("http://transcripts.foreverdreaming.org/viewforum.php?f=51")
# s.scrapeSeries("http://transcripts.foreverdreaming.org/viewforum.php?f=165")
s.scrapeSeries("http://transcripts.foreverdreaming.org/viewforum.php?f=431")
=======
import bs4 as bs
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
>>>>>>> eee7e39e2c0f24970eb4d6a76a00983d028e4259
