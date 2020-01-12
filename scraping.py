#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import os

class Scraping():
    def __init__(self, url):
       self.url = url

    def getLinks(self, download=False):
        request = requests.get(self.url)
        soup = BeautifulSoup(request.content, 'html.parser')   
        if download:
            with open("dataExport.txt", mode="w") as fs:
                for link in soup.find_all('a'):
                    line = str(link.get('href')) + "\n"
                    fs.write(line)
        else:
             for link in soup.find_all('a'):
                    print(link.get('href'))

obj = Scraping("http://gnula.nu/")
obj.getLinks(download=True)
