'''
Created on 29/04/2009

University of Sao Paulo (USP)
Polytechnic School
Department of Computer and Digital Systems Engineering (PCS) 

@author: Charles Boulhosa Rodamilans
'''
from adaptativeFunction import *
from subjacentTransition import*
from stContext import *

class AdaptativeTransition:
    #condition(actualState, symbol)    
    _currentState = False
    _symbol = False
    
    
    _subjacentTransition = False
    _beforeAdapFunction = False
    _afterAdapFunction = False
    
    _afContext = False
    
    def __init__(self, condition, subjacentTransition, \
                 beforeAdapFunction, afterAdapFunction):
        #Fazer a critica dos elementos
        if len(condition) == 2 and len(subjacentTransition) == 3:
            self._currentState = condition[0]
            self._symbol = condition[1]
            self._subjacentTransition = SubjacentTransition(subjacentTransition[0],
                                                            subjacentTransition[1],
                                                            subjacentTransition[2])
            
            self._beforeAdapFunction = AdaptativeFunction(beforeAdapFunction)
           
            self._afterAdapFunction = AdaptativeFunction(afterAdapFunction)
            self._afContext = []
        
    def addAFContext(self, afContext):
        self._afContext = afContext
    
    def realize(self, m, stContext):
        if self.habilited2(stContext):
            #atList = [self._subjacentTransition,self._beforeAdapFunction, self._afterAdapFunction]
#            atList = []
#            
#            if self._beforeAdapFunction._name != "":
#                atList.append(self._beforeAdapFunction._afContext._atList)
#                
#            if self._afterAdapFunction._name != "":
#                atList.append(self._afterAdapFunction._afContext._atList)
            
            atList = self._afContext._atList
            
            m.atRealize(self, atList, stContext)
        
    def stRealize(self, stContext):
        self._subjacentTransition.execute(stContext)
    
    
    #before Adaptative Function
    def beforeAFApply(self): 
        if self._beforeAdapFunction._name != "":
            self._beforeAdapFunction.call()
    
    #after Adaptative Function
    def afterAFApply(self):
        implement = 0
#        if self._afterAdapFunction._name != "":
#            self._afterAdapFunction.call()
        
        
    
    def habilited2(self, stContext):
        #estou passando o valor ou uma referencia???
        current = stContext._currentState
        symbol = stContext._cursor
        if (stContext._currentState == self._currentState) and \
        (stContext.getCurrentSymbol() == self._symbol):
            return True
        return False
    
   
    
    def habilited(self, automata):
        current = automata._currentState
        symbol = automata.getCurrentSymbol()
        if (current == self._currentState) and \
        (symbol == self._symbol):
            return True
        return False
    
    def getCondition(self):
        condition = [self._currentState, self._symbol]
        return condition
    
    def printALL(self):
        print "AdaptativeTransition"
        print "Actual State: " + self._currentState
        print "Symbol: " + self._symbol
        self._subjacentTransition.printALL()
        print "Before " 
        self._beforeAdapFunction.printALL()
        print "After " 
        self._afterAdapFunction.printALL()
        print "##############################"
        
        
        
        
        