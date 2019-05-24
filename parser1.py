from lexer import Location, Lexer
import sys
class VariableType:
    PROPOSITIONS = 0
    PROPOSITION  = 1
    ATOMIC       = 2
    MOREPROPOSITIONS = 3
    COMPOUND = 4
    CONNECTIVE = 5
class Parser:
    #Input list tokens
    inputList=None
    #Look a head pointer
    look_a_headPtr=0
    #Parse tree set
    parseTreeList=list()
    parseTreePtr=0
    line=0
    #initialization
    def __init__(self,lineNo):
        self.loc = Location(0, 0)
        self.line=lineNo
        del self.parseTreeList[:]
    #RDP parsing function
    def parse(self, tokenList):
        #input tokens recieved
        self.inputList=tokenList
        #starting with start symbol
        self.propositions()
        if self.look_a_headPtr==len(self.inputList.kind):
            return self.parseTreeList
        else:
            print 'Parser      : Syntax Error at line '+`self.line`+' column '+`self.look_a_headPtr+1`
        #raise NotImplementedError

    def match(self, token):
        #print token
        #raise NotImplementedError
        if self.inputList.kind[self.look_a_headPtr]==token:
            self.look_a_headPtr=self.look_a_headPtr+1
        else:
             print 'Match failed'

    def propositions(self):
        #print sys._getframe().f_code.co_name
        #raise NotImplementedError
        #Appending symbol to parse tree
        self.parseTreeList.append('propositions')
        #if a input list of tokens have parse tree return true else false
        if self.proposition() and self.more_propositions():
            return True
        return False
       

    def  more_propositions(self):
        #print sys._getframe().f_code.co_name
        #raise NotImplementedError
        #Appending symbol to parse tree
        self.parseTreeList.append('more_propositions')
        #checking a comma is encountered that we use ,propositions production
        if self.look_a_headPtr<len(self.inputList.kind) and self.inputList.kind[self.look_a_headPtr]=='COMMA' :
            self.match('COMMA')
            #Appending symbol to parse tree
            self.parseTreeList.append('COMMA')
            #if a correct input is parsed using grammer return true
            if self.propositions():
                return True
            else:
                return False
            
        #At last appending epsilon to each successfully parsed input.    
        else:
             self.parseTreeList.append('epsilon')
            # self.parseTreePtr=parseTreePtr+1
             return True
    def proposition(self):
        #print sys._getframe().f_code.co_name
        #raise NotImplementedError
        #Appending symbol to parse tree 
        self.parseTreeList.append('proposition')
        #Checking if the input is derived from compound non terminal
        if self.compound():
            return True
        #Checking if the input is derived from automic non terminal   
        if self.atomic():
            return True
        return False
            

    def atomic(self):
        #print sys._getframe().f_code.co_name
        #raise NotImplementedError
        #Checking look a head pointer to determine if backtracking is needed or not and also if current input symbol is 0
        if self.look_a_headPtr<len(self.inputList.kind) and self.inputList.kind[self.look_a_headPtr]=='0':
            #matching symbol for lookAhead ptr to move next or not
            self.match('0')
            #Appending Symbol to parse tree
            self.parseTreeList.append('atomic')
            self.parseTreeList.append('0')
            
            return True
        #Checking look a head pointer to determine if backtracking is needed or not and also if current input symbol is 1
        elif self.look_a_headPtr<len(self.inputList.kind) and self.inputList.kind[self.look_a_headPtr]=='1':
            #matching symbol for lookAhead ptr to move next or not
            self.match('1')
            #Appending Symbol to parse tree
            self.parseTreeList.append('atomic')
            self.parseTreeList.append('1')
            return True
        #Checking look a head pointer to determine if backtracking is needed or not and also if current input symbol is ID
        elif self.look_a_headPtr<len(self.inputList.kind) and self.inputList.kind[self.look_a_headPtr]=='ID':
            #matching symbol for lookAhead ptr to move next or not
            self.match('ID')
            #Appending Symbol to parse tree
            self.parseTreeList.append('atomic')
            self.parseTreeList.append('ID')
            return True
        else:
            return False
    def compound(self):
        #print sys._getframe().f_code.co_name
        #raise NotImplementedError
     #Appending Symbol to parse tree   
     self.parseTreeList.append('compound')
     #Backing tracking ptr 'to' some non terminal if needed to check its next production
     i=len(self.parseTreeList)
     #Reset pointer for lookAhead pointer if wrong production is used
     prev_lookAHead=self.look_a_headPtr
     #checking the first production if it derives the parse tree for input
     if self.atomic()and self.connective() and self.proposition():
         return True
     #if production choosen was not correct for input tokenlist remove path  
     j=len(self.parseTreeList)-1
     while j>=i:
         self.parseTreeList.pop(j)
         j=j-1
     #Resetting lookAhead ptr.    
     self.look_a_headPtr=prev_lookAHead
     i=len(self.parseTreeList)
     #checking the second production if it derives the parse tree for input
     if self.look_a_headPtr<len(self.inputList.kind) and self.inputList.kind[self.look_a_headPtr]=='LPAR':
         self.match('LPAR')
         self.parseTreeList.append('LPAR')
         if self.proposition() and self.look_a_headPtr<len(self.inputList.kind) and  self.inputList.kind[self.look_a_headPtr]=='RPAR':
             self.match('RPAR')
             
             self.parseTreeList.append('RPAR')
             return True
    #if production choosen was not correct for input tokenlist remove path      
     j=len(self.parseTreeList)-1
     while j>=i:
         self.parseTreeList.pop(j)
         j=j-1
     #Resetting lookAhead ptr.    
     self.look_a_headPtr=prev_lookAHead 
     i=len(self.parseTreeList)
     #checking the third production if it derives the parse tree for input
     if self.look_a_headPtr<len(self.inputList.kind) and self.inputList.kind[self.look_a_headPtr]=='NOT':
         self.match('NOT')
         
         self.parseTreeList.append('NOT')
         if self.proposition():
             return True
     #if production choosen was not correct for input tokenlist remove path        
     j=len(self.parseTreeList)-1
     if self.parseTreeList[len(self.parseTreeList)-1]=='compound':
         
         self.parseTreeList.pop(len(self.parseTreeList)-1)
     else:  
       while j>=i:
           self.parseTreeList.pop(j)
           j=j-1
     #Input cannot be generated from this non terminal      
     return False
        
    def connective(self):
        #print sys._getframe().f_code.co_name
        #raise NotImplementedError
        #Checking look a head pointer to determine if backtracking is needed or not and also if current input symbol is And
        if self.look_a_headPtr<len(self.inputList.kind) and self.inputList.kind[self.look_a_headPtr]=='AND':
            #matching symbol for lookAhead ptr to move next or not
            self.match('AND')
            #Appending Symbol to parse tree
            self.parseTreeList.append('connective')
            self.parseTreeList.append('AND')
            return True
        #Checking look a head pointer to determine if backtracking is needed or not and also if current input symbol is Or    
        elif self.look_a_headPtr<len(self.inputList.kind) and self.inputList.kind[self.look_a_headPtr]=='OR':
            #matching symbol for lookAhead ptr to move next or not
            self.match('OR')
            #Appending Symbol to parse tree
            self.parseTreeList.append('connective')
            self.parseTreeList.append('OR')
            return True
        #Checking look a head pointer to determine if backtracking is needed or not and also if current input symbol is Implies
        elif self.look_a_headPtr<len(self.inputList.kind) and self.inputList.kind[self.look_a_headPtr]=='IMPLIES':
            #matching symbol for lookAhead ptr to move next or not
            self.match('IMPLIES')
            #Appending Symbol to parse tree
            self.parseTreeList.append('connective')
            self.parseTreeList.append('IMPLIES')
            return True
        #Checking look a head pointer to determine if backtracking is needed or not and also if current input symbol is iff
        elif self.look_a_headPtr<len(self.inputList.kind) and self.inputList.kind[self.look_a_headPtr]=='IFF':
            #matching symbol for lookAhead ptr to move next or not
            self.match('IFF')
            #Appending Symbol to parse tree
            self.parseTreeList.append('connective')
            self.parseTreeList.append('IFF')
            return True
        else:
            return False
