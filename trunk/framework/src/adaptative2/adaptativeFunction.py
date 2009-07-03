'''
Created on 29/04/2009

University of Sao Paulo (USP)
Polytechnic School
Department of Computer and Digital Systems Engineering (PCS) 

@author: Charles Boulhosa Rodamilans
'''

from afContext import  *
from body import *
import  adaptativeTransition

class AdaptativeFunction:
    _name = ""
    _condition = []
    _afContext = False
    _body = False
    _afContext = False
    
    def __init__(self, adaptativeFunction):
        if len(adaptativeFunction) == 2:
            self._name = adaptativeFunction[0]
            self._condition = adaptativeFunction[1]

            self._afContext = AFContext()
#            self._body = Body()
       
    
    def call(self):
        print self._name
        print self._condition 
        print self._afContext 
        print self._body 
        print self._afContext 
        print ""
        self._body.call()
        
    
    def add(self, condition, st, beforeAdaptativeFunction, afterAdaptativeFunction):
        self._afContext.add(condition, st, beforeAdaptativeFunction, afterAdaptativeFunction)
        
    def remove(self, condition, st, beforeAdaptativeFunction, afterAdaptativeFunction):
        self._afContext.add(condition, st)
        
    def addBody(self, body):
        self._body = Body(body, self._afContext)
#        self._body = body
    
    def addAFContext(self, afContext):
        self._afContext = afContext
        
    def printALL(self):  
        if self._name != "" and self._condition != []:
            print "Function [id] "+ self._name + " [condition] " 
            for i in self._condition: 
                print i
        else:
            print "Function []"
            
        
    