'''
Created on 26/04/2009

@author: Guilherme
'''

import AdaptiveFunction
import Device

class A( AdaptiveFunction.AdaptiveFunction ):
    
    def execute(self, transitions):
        self.PlusPrimitive('0', 'b', '1', transitions)
        
class Automata ( Device.AdaptiveDevice ):
    
    def __init__(self, initial):
        self.current = initial
        


test = Automata('0')
a = A("n")

test.transitions.addTransition('0', 'a', '0')
test.transitions.includeAdaptiveFunction('0', 'a', '0', a, "before")  

test.processInput('ab')

