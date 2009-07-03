'''
Created on 29/04/2009

University of Sao Paulo (USP)
Polytechnic School
Department of Computer and Digital Systems Engineering (PCS) 

@author: Charles Boulhosa Rodamilans
'''

'''
So analisa uma lista de symbolos por execucao
Falta implementar o accept == x
'''

from adaptativeTransition import *
from adaptativeFunction import *
from stContext import *
from mecanismForTransitionVisitor import *
from afContext import *
import copy

class AdaptativeAutomaton:
    _id = 0
    _currentState = False
    _symbolsProcess = False 
    _cursor = 0
    _adaptTransitionList = [] #era para ser um map...
    _adapFunctionList = []
    _afContext = []
    _stContext = []
    

    def __init__(self):
         self.__class__._id += 1
         self._afContext = AFContext() 

    def validated(self, allAutomatas):
        for aut in allAutomatas:
            print "#############################"
            print "Checking clone ", aut._id
            if aut.isValid():
                print "Valid"
            else:
                print "Invalid clone "

        
    def start(self, startState, symbolsProcess):
        self._currentState = startState
        self._symbolsProcess = symbolsProcess
        self._stContext = STContext(self._currentState, self._cursor, self._symbolsProcess)
    
    def validateSymbols(self, symbolsProcess):
        for s in symbolsProcess:
            if not validadeSymbol(s):
                print "Symbol " + s + " does not belong to the alphabet."
                return None
        self._symbolsProcess = symbolsProcess
        return True

    def addAdaptativeTransition(self, condition, subjacentTransition, \
                          beforeAdapFunction, afterAdapFunction):
        at = AdaptativeTransition(condition, subjacentTransition, \
                                 beforeAdapFunction, afterAdapFunction)
        self._adaptTransitionList.append(at)
        self._afContext.addAT(at)
        
        #POG
        at.addAFContext(self._afContext)

       
    #duas  funcoes adaptativas nao podem ter o mesmo nome
    # deve procurar mesmo? Ou eh melhor guardar as funcoes em lista?
    def addAdaptativeFunction(self, name, body):
        #for at in self._adaptTransitionList:
        for at in self._afContext._atList:
            baf = at._beforeAdapFunction
            aaf = at._afterAdapFunction
            if baf._name == name:
#                b = Body(body)
#                baf.addBody(b)
                baf.addBody(body)
                baf.addAFContext(self._afContext)
                return True
            
            if aaf._name == name:
#                b = Body(body)
#                aaf.addBody(b)
                aaf.addBody(body)
                aaf.addAFContext(self._afContext)
                return True
            
        print "Name Function does not exist"
        return False
        
        
    def execute(self):
        #visible[adapTran, c]
        generatedAutomatas = [self]
        allAutomatas = [self]
        visibles = self.visiblesCalculate()
        
        #melhor eh update
        for visible in visibles:
                allAutomatas.append(visible[1])
                
        while visibles != [] :
            self.habilitedTransitionsRealize(visibles)
            visibles = self.newVisiblesCalculate(visibles)
            for visible in visibles:
                generatedAutomatas.append(visible[1])
                allAutomatas.append(visible[1])

        self.validated(allAutomatas)
        
        return generatedAutomatas
        
    
                    
    def habilitedTransitionsRealize(self, visibles):
        for visible in visibles:
            hat = visible[0] #habilited Adaptative Transition
            clone = visible[1]
            print "#########################" 
            print "Before"
            clone.printStatus()

            clone.realize2(hat)
                       
            print "After"
            clone.printStatus()
            
    
   
    def realize2(self, adapTransition):
        stc = self._stContext #self.getStContext()
        m = MecanismForTransitionVisitor()
        m.realize(adapTransition, stc)
        self._currentState = stc._currentState
        self._cursor = stc._cursor

    
    #ver isso aqui direito....
    #verificar se o automato foi aceito    
    def realize(self, adapTransition):
#        stc = self.getStContext()
        stc = self._stContext

        t = adapTransition._subjacentTransition
        t.execute(stc)
#        self._currentState = stc._currentState
#        self._cursor = stc._cursor
        
    #diminuir os subspacos
    def newVisiblesCalculate(self, visibles):
        newSubSpace = []
        for visible in visibles :
            clone = visible[1]
            cloneSubSpace = clone.visiblesCalculate()
            if cloneSubSpace != []:
                #newSubSpace.append(cloneSubSpace.values)
                for i in cloneSubSpace:
                    newSubSpace.append(i)
        return newSubSpace
     
    def visiblesCalculate(self):
        subSpaceOfVisiblesAutomatas = []
#        for adapTran in self._adaptTransitionList:
        for adapTran in self._afContext._atList:
            if adapTran.habilited(self):
                c = copy.deepcopy(self)
                c._id += 1
                subSpaceOfVisiblesAutomatas.append([adapTran, c])
        return subSpaceOfVisiblesAutomatas            

    
    def isValid(self):
       
        if self._stContext._cursor  == self._stContext.getTamSymbolProcess(): 
       
            #o ultimo symbolo
#            for t in self._adaptTransitionList:
            for t in self._afContext._atList:
                if self._stContext._currentState == t._subjacentTransition._nextState:
                    if t._subjacentTransition._accept == "v":
                        return True
               
                #verificar o "." da condicao
                #verifica-se a condicao (currentState and Symbol)
                #verifica-se a transicao subjacente
                symbols = self._symbolsProcess[0]
                
                if self._stContext._currentState == t._currentState and \
                t._symbol == self._stContext._symbolsProcess[-1] and \
                t._subjacentTransition._nextState == "." and \
                t._subjacentTransition._accept == "v":
                    return True
                
        return False
    
    
    def getCurrentSymbol(self):
        aux = self._symbolsProcess[0]
        if len(aux) > self._cursor:
            return aux[self._cursor]
        return False
    
    def getTamSymbolProcess(self):
        symbols = self._symbolsProcess[0]
        return len(symbols)
        
    def printStatus(self):
        print "Clone ID: ", self._id
        print "Current State: " + self._currentState
        print "Cursor: ", self._cursor 
        print "Symbol: ", self.getCurrentSymbol()
        print ""
        
    
    def printALL(self):
        print "##############################"
        print "Adaptative Automata"
        print "##############################"
#        for i in self._adaptTransitionList:
        for i in self._afContext._atList:
            i.printALL()
        
