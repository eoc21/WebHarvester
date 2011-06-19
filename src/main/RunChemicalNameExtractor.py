'''
Created on Jun 18, 2011
Example usage.
@author: eoc21
'''
from WebExtraction.Scraper import *
from Tokenization.Tokenizer import * 
import os, sys

s = Scraper(sys.argv[1])
articles = s.getArticles()

p = ParagraphTokenizer()
p.splitText2Paragraphs(articles)