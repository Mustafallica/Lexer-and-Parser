from parser1 import Parser
from lexer import Lexer, TokenKind
import unittest



class Test(unittest.TestCase):
    
   def test1(self):
       l = Lexer('Q').tokenize()
       #self.assertEqual(l.kind, [TokenKind.ID])

   def test2(self):
        tokelist = Lexer('(P /\ Q)').tokenize()
        #parse_tree = Parser().parse(tokelist)
        # some assertion goes here


   if __name__ == '__main__':
      
       
        #Reading input file         
        input_file=open('input.txt','r')
        #Spliting file based on new line
        data=input_file.read().splitlines()
        i=1
        for line in data:
            #printing current line
            print 'Input #'+`i`+':'
            print '---------\n'
            print 'Proposition : '+line
            #Getting tokens
            l=Lexer(line).tokenize()
            lexerOutPut=l.kind
            print 'Lexer       : '+`lexerOutPut`
            #Getting parse tree from input passed
            parse_tree=Parser(i).parse(l)
            if parse_tree !=None:
               
               print 'Parser      : '+`parse_tree`
            i =i+1
            print '\n'
   

    
    
    
    
    
