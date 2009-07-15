# -*- coding: iso-8859-1 -*-
'''
Created on 29/04/2009

University of Sao Paulo (USP)
Polytechnic School
Department of Computer and Digital Systems Engineering (PCS) 

@author: Charles Boulhosa Rodamilans
'''





from adaptativeAutomaton import *
from test import *
import functools

if __name__ =='__main__':
    
    
    
    aut =AdaptativeAutomaton() 
    
#    testWithoutAdaptative(aut)
    testWithAdaptative(aut)
    
#    startState = "I"
#    symbolsProcess = ["ba"]
#    aut.start(startState, symbolsProcess)

     
    aut.printALL()
    aut.execute()
    

    
    