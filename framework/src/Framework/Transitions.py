'''
Created on 02/07/2009

@author: Guilherme
'''

class SubTransition:
    
    transitions = {}
    
    def __init__(self):
        None
    
    def addTransition(self, src, symbol, dest):
        if(self.transitions.__len__() > 0):
           self.transitions[src][symbol] = dest
        else:
            self.transitions = {src : {symbol : dest}}
        
    def delTranstion(self, src, symbol, dest):
        if(self.transitions[src][symbol] == dest):
            del(self.transitions[src][symbol])
            
    def realize(self, src, symbol): 
        raise NotImplementedError
    
class AdaptiveTransition( SubTransition ):
    
    def includeAdaptiveFunction(self, src, symbol, dest, function, type):

        if(type == "before"):            
            originaldest = self.transitions[src][symbol]
            
            if(not (isinstance(originaldest, list))):
                   self.transitions[src][symbol] = [function, dest, '']
            
            else:
                originaldest[0] = function
                self.transitions[src][symbol] = originaldest
                            
        if(type == "after"):
            originaldest = self.transitions[src][symbol]
            
            if(not (isinstance(originaldest, list))):
                   self.transitions[src][symbol] = ['', dest, function]
            
            else:
                originaldest[2] = function
                self.transitions[src][symbol] = originaldest
                   
    def realize(self, src, symbol):
        print self.transitions
                      
        dest = self.transitions[src][symbol]       
                      
        if(not isinstance(dest, list)):
           return dest
        
        else:
            if(dest[0] != ''):
                dest[0].execute(self)
            
            rtrn = dest[1]
                        
            if(dest[2] != ''):
                dest[2].execute(self)
        
        return rtrn