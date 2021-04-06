#Constants
Digits='0123456789'
#Tokens in the language
tokenDict={
'KEYWORD':'KEYWORD',
'ID':'IDENTIFIER',
'INT':'INT',
'FLOAT':'FLOAT',
'STRING':'STRING',
'*':'MUL',
'+':'PLUS',
'-':'MINUS',
'/':'DIV',
'=':'EQU',
'(':'LPAREN',
')':'RPAREN',
}
class Token:
    def __init__(self,tokenType,value=None):
        self.tokenType=tokenType
        self.value=value
    def __repr__(self):
        if self.value:
            return f'{self.tokenType}:{self.value}'
        return f'{self.tokenType}'
#ERROR HANDLING
class Error:
    def __init__(self,pos_start,pos_end,errorName, details):
        self.errorName=errorName
        self.details=details
        self.pos_start= pos_start
        self.pos_end=pos_end
    def as_string(self):
        result=f'{self.errorName}:{self.details}'
        result+=f'\nFile {self.pos_start.fn},line{self.pos_start.ln+1}'
        return result
class IllegalCharError(Error):
    def __init__(self,pos_start,pos_end,details):
        super().__init__(pos_start,pos_end,'Illegal Character',details)
#FILEHANDLING
class Position:
    def __init__(self,idx,ln,col,fn,ftext):
        self.idx=idx
        self.ln=ln
        self.col=col
        self.fn=fn
        self.ftext=ftext
    def advance(self,current_char):
        self.idx+=1
        self.col+=1

        if current_char=='\n':
            self.ln+=1
            self.col=0

        return self
    def copy(self):
        return Position(self.idx,self.ln,self.col,self.fn,self.ftext)


#LEXER
class Lexer:
    def __init__(self,fn,text):
        self.fn=fn
        self.text=text
        self.pos=Position(-1,0,-1,fn,text)
        self.current_char=None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char=self.text[self.pos.idx] if self.pos.idx<len(self.text) else None

    def make_tokens(self):
        tokens=[]
        while self.current_char!=None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in Digits:
                tokens.append(self.checkTypeOfNumber())

            else:
                if self.current_char in tokenDict:

                    tokens.append(Token(tokenDict[self.current_char]))
                    self.advance()
                else:
                    pos_start=self.pos.copy()
                    char=self.current_char
                    self.advance()
                    return [],IllegalCharError(pos_start,self.pos,"'"+char+"'")
        return tokens,None
    def checkTypeOfNumber(self):
        num_String =''
        dotsInString=0
        while self.current_char !=None and  self.current_char in Digits+'.':
            if self.current_char=='.':
                if dotsInString==1:
                    break
                dotsInString+=1
            num_String+=self.current_char
            self.advance()
        if num_String.isdigit():
            return Token(tokenDict['INT'],int(num_String))
        else:
            return Token(tokenDict['FLOAT'],float(num_String))
def run(fn,text):
    lexer=Lexer(fn,text)
    tokens,errors=lexer.make_tokens()

    return tokens,errors
