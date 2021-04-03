TokenKeyword='KEYWORD'
TokenId='IDENTIFIER'
TokenInt='INT'
TokenFloat='FLOAT'
TokenString='STRING'
TokenMul='MUL'
TokenAdd='ADD'
TokenSub='SUB'
TokenDiv='DIV'
TokenEq='EQU'
TokenLParen='LEFT PARANTHESIS'
TokenRParen='RIGHT PARANTHESIS'
class Token:
    def __init__(self,argType,value):
        self.argType=argType
        self.value=value
    def __repr__(self):
        if self.value:
            return f'{self.argType}:{self.value}'
        return f'{self.argType}'


class Lexer:
    def __init__(self,text):
        self.text=text
        self.pos=-1
        self.current_char=None
        self.advance()
    def advance(self):
        self.pos+=1
        self.current_char=self.text[pos] if self.pos<len(self.text) else None
