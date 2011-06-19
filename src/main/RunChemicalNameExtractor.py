'''
Created on Jun 18, 2011
Example usage.
@author: eoc21
'''
from WebExtraction.Scraper import *
from WebExtraction.HTMLCustomParser import *
from Tokenization.Tokenizer import * 
import os, sys,io
s = Scraper(sys.argv[1])
articles = s.getArticles()

#p = ParagraphTokenizer()
#p.splitText2Paragraphs(articles)
chp = ChemicalHTMLParser()
val1 = str(articles).replace('[', '')
val2 = val1.replace(']','')
val3 = val2.replace('b\'','')
val4 = val3.replace('\\n\',','')
chp.feed(val4)
paras = chp.getParagraphs()
print(paras)
