'''
Created on 25/05/2009

University of Sao Paulo (USP)
Polytechnic School
Department of Computer and Digital Systems Engineering (PCS) 

@author: Charles Boulhosa Rodamilans
'''
from adaptativeFunction import *
from adaptativeTransition import *

def testWithoutAdaptative(aut):
    startState = "I"
    symbolsProcess = ["aaaba"]
    aut.start(startState, symbolsProcess)
    
    #1th adaptative Transition
    #a)
    condition = ["I", "a"]
    
    #b)
    nextState = "J"     # TransicaoSubjacent.seguinte 
    get = "v"        
    accept = "."   
    subjacentTransition = [nextState, get,  accept ]

    #c)
   
    beforeAdaptativeFunction = [[]] # ["", [""] ]
    afterAdaptativeFunction = [[]] #["", [""] ]
    
    aut.addAdaptativeTransition(condition, subjacentTransition, beforeAdaptativeFunction,afterAdaptativeFunction)
    
    #2th adaptative Transition
    #a)
    condition = ["J", "a"]
    
    #b)
    nextState = "J"     # TransicaoSubjacent.seguinte 
    get = "v"        
    accept = "v"   
    subjacentTransition = [nextState, get,  accept ]
    beforeAdaptativeFunction = [[]] # ["", [""] ]
    afterAdaptativeFunction = [[]] #["", [""] ]
    
    aut.addAdaptativeTransition(condition, subjacentTransition, beforeAdaptativeFunction,afterAdaptativeFunction)
    
    #3th adaptative Transition
    #a)
    condition = ["J", "b"]
    
    #b)
    nextState = "L"     # TransicaoSubjacent.seguinte 
    get = "v"        
    accept = "v"   
    subjacentTransition = [nextState, get,  accept ]
    beforeAdaptativeFunction = [[]] # ["", [""] ]
    afterAdaptativeFunction = [[]] #["", [""] ]
    
    aut.addAdaptativeTransition(condition, subjacentTransition, beforeAdaptativeFunction,afterAdaptativeFunction)
 
 
def body(x, args):
        p1 = args[0]
        p2 = args[1]
        g1 = x.g()
  
        #remove Rule h1 (J, b, L)
        condition = [p1,p2]
        st = [p1, "b"] # 
    
        name = "X"
        condition = ["J", "a"]
        
        baf = [name, condition] # ["", [""] ]
        aaf = [[]] #afterAdaptativeFunction 
        x.add(condition, st, baf, aaf)
 
def testWithAdaptative(aut):
    startState = "I"
    symbolsProcess = ["aabb"]
    aut.start(startState, symbolsProcess)
    
    #1th adaptative Transition
    #a)
    condition = ["I", "a"]
    
    #b)
    nextState = "J"     # TransicaoSubjacent.seguinte 
    get = "v"        
    accept = "."   
    subjacentTransition = [nextState, get,  accept ]

    #c)
   
    beforeAdaptativeFunction = [[]] # ["", [""] ]
    afterAdaptativeFunction = [[]] #["", [""] ]
    
    aut.addAdaptativeTransition(condition, subjacentTransition, beforeAdaptativeFunction,afterAdaptativeFunction)
    
    
    
    #2th adaptative Transition
    #a)
    condition = ["J", "b"]
    
    #b)
    nextState = "L"     # TransicaoSubjacent.seguinte 
    get = "v"        
    accept = "v"   
    subjacentTransition = [nextState, get,  accept ]
    beforeAdaptativeFunction = [[]] # ["", [""] ]
    afterAdaptativeFunction = [[]] #["", [""] ]
    
    aut.addAdaptativeTransition(condition, subjacentTransition, beforeAdaptativeFunction,afterAdaptativeFunction)

    #3th adaptative Transition
    #a)
    condition = ["J", "a"]
    
    #b)
    nextState = "J"     # TransicaoSubjacent.seguinte 
    get = "v"        
    accept = "."   
    subjacentTransition = [nextState, get,  accept ]
    
    #c) 
    name = "X"
    condition = ["J", "a"]
    beforeAdaptativeFunction = [name, condition] # ["", [""] ]
    afterAdaptativeFunction = [[]] #["", [""] ]
    
    aut.addAdaptativeTransition(condition, subjacentTransition, beforeAdaptativeFunction,afterAdaptativeFunction)
    
    #d) Body
    #testando....    
    b = body
#    condition = ["I", "J"]
#    af = AdaptativeFunction(["J", "a"])
    
    
    aut.addAdaptativeFunction("X", b)
    
  
#        #add Rule h2 (J, b, #1)
#        condition = [p1,g1]
#        st = [p1, "b"] # 
#    
#        name = "X"
#        condition = ["J", "a"]
#        
#        baf = [name, condition] # ["", [""] ]
#        aaf = [[]] #afterAdaptativeFunction 
#        x.add(condition, st, baf, aaf)
#        
#        #add Rule h3 (#1, b#, L)
#        condition = [g1,p2]
#        st = [p1, "b"] # 
#        
#        baf = [[]] # ["", [""] ]
#        aaf = [[]] #afterAdaptativeFunction 
#        x.add(condition, st, baf, aaf)
#    
