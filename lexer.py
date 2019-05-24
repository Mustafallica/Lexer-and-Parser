import string
import re
UPPER_CASE = set(string.ascii_uppercase)

class Location:
    def __init__(self, line, col):
        self.col = col
        self.line = line


class TokenKind:
    ID = 0   # identifier
    LPAR = 1 # (
    RPAR = 2 # )
    NOT = 3  # !
    AND = 4  # /\
    OR = 5   # \/
    IMPLIES = 6  # =>
    IFF = 7  # <=>
    COMMA = 8 # ,



class Token:
    #Initialization
    def __init__(self, loc, kind):
        self.loc = loc
        self.kind = kind

    def __str__(self):
        return str(self.kind)


class Lexer:
    #Initialization
    def __init__(self, text):
        self.text = text
        self.line = 1
        self.col = 1
    #This function is use to make tokens of input propositional logic
    def tokenize(self):
        current_match = None
        #list of tokens
        tokens_list=list()
        #Column list
        col_list=list()
        #the following assignment and if statement are only to allow the test pass. they need to be removed
        #c = self.text[0]
        #if c == 'Q':
         #   return Token(Location(1, 1), [TokenKind.ID])

        #used for holding current id's 
        current_string=''
        i=1
        #scanning each character
        for c in self.text:
            #appending current column index
            col_list.append(i)
            i=i+1
           # raise NotImplementedError
           #if we encounter space just leave and proceed to next 
            if c==' ':
                    current_string=''
           #if if we encounter Lpar        
            elif c=='(':
                #adding lpar to token resultset
                tokens_list.append('LPAR')
                #just removing current_string to remove any wrong collection of tokens
                current_string=''
                
            elif c==')':
                #adding Rpar to token resultset
                tokens_list.append('RPAR')
                #just removing current_string to remove any wrong collection of tokens
                current_string=''
                
            elif c=='!':
                #adding Not operator to token resultset
                tokens_list.append('NOT')
                #just removing current_string to remove any wrong collection of tokens
                current_string=''
            elif c==',':
                #adding comma to token resultset
                tokens_list.append('COMMA')
                #just removing current_string to remove any wrong collection of tokens
                current_string=''
                
            elif  re.search('[A-Z]+',c)!=None:
                #adding Id to token resultset
                tokens_list.append('ID')
                #just removing current_string to remove any wrong collection of tokens
                current_string=''
            else:
                #As operator like <=>, =>, /\, \/ uses more that one character so we append multi character to see if we get an operator
                if c in ('<','>','=','/','\\'):
                    #getting the current character and concatinating it to current string
                    current_string=current_string+c
                    #if we encounter and operator
                    if current_string=="/\\":
                        tokens_list.append('AND')
                        current_string=''
                    #if we encounter or operator    
                    elif current_string=="\/":
                        tokens_list.append('OR')
                        current_string=''
                    #if we encounter implies operator     
                    elif current_string=="=>":
                        tokens_list.append('IMPLIES')
                        current_string=''
                    #if we encounter IFF operator     
                    elif current_string=="<=>":
                        tokens_list.append('IFF')
                        current_string=''
                
        #Return the toke back to caller   
        return Token(Location(0,col_list),tokens_list)         
                
            
