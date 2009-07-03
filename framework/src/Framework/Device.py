'''
Created on 08/05/2009

@author: Guilherme
'''

import Transitions

class Device( object ):

    transitions = Transitions.SubTransition()
    current = ''
    
    def __init__(self, inital):
        abstract        
    
    def realize(self, symbol):
        return self.transitions.realize(current, symbol)
        
    def processInput(self, input):
        for symbol in input:
            self.current = self.realize(symbol)
                   
        return self.current
  
class AdaptiveDevice( Device ):
    
    transitions = Transitions.AdaptiveTransition()
    
    def realize(self, symbol):
        return self.transitions.realize(self.current, symbol)
    
        