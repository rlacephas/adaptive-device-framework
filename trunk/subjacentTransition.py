'''
Created on 29/04/2009

University of Sao Paulo (USP)
Polytechnic School
Department of Computer and Digital Systems Engineering (PCS) 

@author: Charles Boulhosa Rodamilans
'''
from abstractTransition import*
from stContext import *

class SubjacentTransition (AbstractTransition):
    _nextState = ""
    _get = ""
    _accept = ""
    
    def __init__(self, nextState, get , accept):
        self._nextState = nextState
        self._get = get
        self._accept = accept

    def printALL(self):
        print "Subjacent Transition [nextState]: " + self._nextState + \
        " [get]: " + self._get + " [accept]: " + self._accept
    
    def execute(self, stContext):
        self.subjacentTransitionRealize(stContext)
    
    def realize(self, m, stContext): 
        m.realize(self, stContext)
        m.realizeAT(self)
    
    def subjacentTransitionRealize(self, stContext): 
        if self._nextState != "." :
            stContext._currentState = self._nextState
        if self._get != ".":
            stContext.execute("next")
        
        
        
        
