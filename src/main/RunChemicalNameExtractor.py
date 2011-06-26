'''
Created on Jun 18, 2011
Example usage.
@author: eoc21
'''
from WebExtraction.Scraper import *
from WebExtraction.HTMLCustomParser import *
from Tokenization.Tokenizer import * 
from Tokenization.RegexMatcher import *
import os, sys,io
s = Scraper(sys.argv[1])
articles = s.getArticles()

chp = ChemicalHTMLParser(articles)
paras = chp.getParagraphs()
extractor = ExtractChemicalNames()
extractor.ExtractNames(paras)
regexMatcher = ChemicalRegexMatcher()
regexMatcher.PrefixMatch("abcdef")