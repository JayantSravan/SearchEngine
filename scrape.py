import bs4 as bs
import codecs
import sys
from urllib.request import urlopen, Request
from unidecode import unidecode
# -*- coding: utf-8 -*-

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

reg_url = 'http://transcripts.foreverdreaming.org/viewtopic.php?f=177&t=11509'
req = Request(url=reg_url, headers=headers)
sauce = urlopen(req).read()

soup = bs.BeautifulSoup(sauce,'lxml')
body = soup.body

f = open("testOutput.txt","w", encoding = "utf-8")
for div in body.find_all('div', class_='postbody'):
    for para in div.find_all('p'):
        para.encode(encoding="utf-8").strip()
        para = para.text.encode('utf-8')
        para = para.decode("utf-8", "ignore")
        para = para + '\n'
        f.write(para)
f.close()
