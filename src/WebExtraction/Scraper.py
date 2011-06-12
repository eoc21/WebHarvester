'''
Created on Jun 12, 2011

@author: eoc21
'''
import os, sys, urllib.request

class Scraper:
    '''
    Scrapes html articles from online journals.
    '''
    def __init__(self,ifile):
        uriFileHandler = open(ifile,'r')
        self.URIList = uriFileHandler.readlines()
    def getArticles(self):
        for i in range(len(self.URIList)):
            f = urllib.request.urlopen(str(self.URIList[i]))
            article = f.readlines()
            print(article)
s = Scraper(sys.argv[1])
s.getArticles()
