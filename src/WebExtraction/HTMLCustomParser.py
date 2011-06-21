'''
Created on Jun 18, 2011

@author: eoc21
'''
from html.parser import HTMLParser
class ChemicalHTMLParser(HTMLParser):
    def __init__(self,articles):
        HTMLParser.__init__(self)
        self.paragraphs =[]
        self.cleanArticles(articles)
    def handle_data(self,data):
        self.paragraphs.append(data)
    def getParagraphs(self):
        return self.paragraphs
    def cleanArticles(self,articles):
        partialClean = str(articles).replace('[', '')
        cleaner = partialClean.replace(']','')
        cleanerStill = cleaner.replace('b\'','')
        cleaned = cleanerStill.replace('\\n\',','')
        self.feed(cleaned)


