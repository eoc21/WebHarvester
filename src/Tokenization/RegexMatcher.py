'''
Created on Jun 12, 2011
Identifies tokens through regular expressions.
@author: eoc21
'''
import os, re
class ChemicalRegexMatcher():
    def __init__(self):
        self.found = False
        self.names = []
    def ElementMatch(self,token):
        path = os.path.expanduser('../resources/ChemicalElementList.txt')
        chemicalElementFile = open(path,'r')
        chemicalElements = chemicalElementFile.readlines()
        for i in range(len(chemicalElements)):
            if token == str(chemicalElements[i]).strip():
                self.names.append(token)
    def PrefixMatch(self,token):
        path = os.path.expanduser('../resources/Regex/Prefixes')
        prefixRegexFile = open(path,'r')
        prefixRegexes = prefixRegexFile.readlines()
        for i in range(len(prefixRegexes)):
            m = re.search(str(prefixRegexes[i]),token)
            print(m.group(0))
    def SuffixMatch(self,token):
        pass
    
    def IsPresent(self,name):
        pass
    def getNames(self):
        pass

