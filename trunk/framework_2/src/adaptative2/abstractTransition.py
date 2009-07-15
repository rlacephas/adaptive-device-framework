'''
Created on 29/04/2009

University of Sao Paulo (USP)
Polytechnic School
Department of Computer and Digital Systems Engineering (PCS) 

@author: Charles Boulhosa Rodamilans
'''
class AbstractTransition:
    
    def realize(self, m, stContext): abstract
    
    def subjacentTransitionRealize(self, stContext): abstract
        