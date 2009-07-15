'''
Created on 29/04/2009

University of Sao Paulo (USP)
Polytechnic School
Department of Computer and Digital Systems Engineering (PCS) 

@author: Charles Boulhosa Rodamilans
'''

from adaptativeTransition import *

class MecanismForTransitionVisitor:

    def __init__(self):
        implement = 0
        
    def realize(self, adapTransition, stContext):
        adapTransition.realize(self, stContext)
        
    def atRealize(self, t, atList, stContext):
        t.beforeAFApply()
        if self.exist2(t, atList): #mudar o nome desta funcao
           t.stRealize(stContext)
           t.afterAFApply()
            
    def exist2(self, t, atList):
        for at in atList:
            if at._currentState  == t._currentState  and \
            at._symbol == t._symbol:
                return True
        return False
    
    def exist(self,  t, atList):
        if atList == []:
            return False
        
        st = atList[0] #subjacentTransition
        baf = atList[1] #beforeAdapFunction
        aaf = atList[2] #afterAdapFunction
        
        
        if t._subjacentTransition == st and \
        t._beforeAdapFunction == baf and \
        t._afterAdapFunction == aaf:
            return True
        return False
        
        