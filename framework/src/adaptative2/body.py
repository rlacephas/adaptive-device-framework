'''
Created on 20/05/2009

University of Sao Paulo (USP)
Polytechnic School
Department of Computer and Digital Systems Engineering (PCS) 

@author: Charles Boulhosa Rodamilans
'''

class Body:
    _b = False
    _afContext = False
    
    def __init__(self, body, afContext):
        self._b = body
        self._afContext = afContext
        
    def call(self):
        self._b()
    
