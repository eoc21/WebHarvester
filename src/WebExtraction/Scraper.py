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
    