'''
Created on Jun 12, 2011
General module for tokenization, html clean up
paragraph identification and sentence splitting.
@author: eoc21
'''
import os, sys, re
class ParagraphTokenizer():
    def __init__(self):
        self.paragraphs =[]
    def splitText2Paragraphs(self,articles):
        for i in range(len(articles)):
            print(articles[i])
    
class SentenceTokenizer():
    def __init__(self):
        pass
    
p = ParagraphTokenizer()
p.splitText2Paragraphs()