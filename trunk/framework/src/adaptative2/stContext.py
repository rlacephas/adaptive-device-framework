'''
Created on 29/04/2009

University of Sao Paulo (USP)
Polytechnic School
Department of Computer and Digital Systems Engineering (PCS) 

@author: Charles Boulhosa Rodamilans
'''
class STContext:
    _currentState = False
    _cursor = False
    _symbolsProcess = False
    
    def __init__(self, currentState, cursor, symbols):
        self._currentState = currentState
        self._cursor = cursor 
        self._symbolsProcess = symbols
    
    def execute(self, cursorMoviment):
        if cursorMoviment != ".":
            self._cursor += 1
    
    def getCurrentSymbol(self):
        aux = self._symbolsProcess[0]
        if len(aux) > self._cursor:
            return aux[self._cursor]
        return False
    
    def getTamSymbolProcess(self):
        symbols = self._symbolsProcess[0]
        return len(symbols)
    
        