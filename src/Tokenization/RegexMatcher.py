'''
Created on Jun 12, 2011
Identifies tokens through regular expressions.
@author: eoc21
'''
import os
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
            
    def IsPresent(self,name):
        pass
    def getNames(self):
        pass
