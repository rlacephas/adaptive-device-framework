'''
Created on 20/05/2009

University of Sao Paulo (USP)
Polytechnic School
Department of Computer and Digital Systems Engineering (PCS) 

@author: Charles Boulhosa Rodamilans
'''

import adaptativeTransition 


class AFContext:
    _atList = False
    _generator = False
    
    def __init__(self):
        self._atList = []
        self._generator = []
    
    #pode adicionar qualquer coisa :(
    def addAT(self, at):        
        self._atList.append(at)
    
    def g(self):
        if self._generator == []:
            g = "1"
            self._generator.append(g)
        else :
            g = self._generator[-1]
            g = g + 1
            self._generator.append(g)
            
         
    def add(self, condition, subjacentTransition, beforeAdapFunction, afterAdapFunction):
        at = adaptativeTransition.AdaptativeTransition(condition, subjacentTransition, beforeAdapFunction, afterAdapFunction)

        self._atList.append(at)
        
    def remove(self, condition, subjacentTransition, beforeAdapFunction, afterAdapFunction):
        for at in self._atList:
            if at.getCondition() == condition and \
            at._subjacentTransition == subjacentTransition:
                self._atList.remove(at)
                
        
#    def __init__(self, atList):
#        self._atList = atList
        
     
        
    
    