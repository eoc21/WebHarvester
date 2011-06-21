'''
Created on Jun 12, 2011
Identifies tokens through a lookup.
@author: eoc21
'''
import os, sys
class ChebiDictionary():
    def __init__(self):
        self.dictionaryEntries=[]
    def initializeDictionary(self):
        path = os.path.expanduser('../../ChebiNames.txt')
        dictF = open(path,'r')
        dictValues = dictF.readlines()
        for x in dictValues: self.dictionaryEntries.append(str(x).strip())
    def IsPresent(self,name):
        if name in self.dictionaryEntries:
            return True
        else:
            return False
    def getDictionaryEntry(self,name):
        if name in self.dictionaryEntries:
            return name
        else:
            return "Not found!"
        
#c = ChebiDictionary()
#c.initializeDictionary()