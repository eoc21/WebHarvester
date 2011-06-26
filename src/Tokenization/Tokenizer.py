'''
Created on Jun 12, 2011
General module for tokenization / identification of 
chemicals in text.
@author: eoc21
'''
import os, sys, re
from Tokenization import DictionaryLookup
class ExtractChemicalNames:
    def __init__(self):
        self.chemicalNames = []
    def ExtractNames(self,processedArticles):
        javascriptString = 'function doi(ref)'
        javascriptString1 = 'frames.length'
        javascriptString2 = 'var'
        javascriptString3 = 'document.write'
        googleAd = 'google_ad_client'
        c = DictionaryLookup.ChebiDictionary()
        c.initializeDictionary()
        for i in range(len(processedArticles)):
            if processedArticles[i] == ' ':
                pass
            elif javascriptString in processedArticles[i]:
                pass
            elif javascriptString1 in processedArticles[i]:
                pass
            elif javascriptString2 in processedArticles[i]:
                pass
            elif javascriptString3 in processedArticles[i]:
                pass
            elif googleAd in processedArticles[i]:
                pass
            else:
                for j in range(len(c.dictionaryEntries)):
                    if c.dictionaryEntries[j] in processedArticles[i] and len(c.dictionaryEntries[j]) >= 3:
                        print(c.dictionaryEntries[j])
            
            

         
