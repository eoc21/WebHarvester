'''
Created on Jun 18, 2011

@author: eoc21
'''
from html.parser import HTMLParser
class ChemicalHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.paragraphs =[]
    def handle_data(self,data):
        self.paragraphs.append(data)
    def getParagraphs(self):
        return self.paragraphs
