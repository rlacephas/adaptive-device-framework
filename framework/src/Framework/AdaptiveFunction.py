'''
Created on 02/07/2009

@author: Guilherme
'''

import Device
import Transitions

class AdaptiveFunction:
    name = ""
    
    def __init__(self, name):
        self.name = name
        
        
    def PlusPrimitive(self, src, symbol, dest, transitions):
        transitions.addTransition(src, symbol, dest)
    
    def MinusPrimitive(self, src, symbol, dest, transitions):
        transitions.delTransition(src, symbol, dest)
        
    def QuestionPrimitive(self, variables, transition): 
        abstract
        
    def execute(self, transition): abstract