# -*- coding: utf-8 -*-
class Buffer(object):
    def __init__(self, data):
        self.data = data
        self.offset = 0

    def peek(self):
        if self.offset >= len(self.data):
            return None
        return self.data[self.offset]
    
    def advance(self):
        self.offset += 1

class Token(object):
    def consume(self,b_uffer):
        pass

class IntToken(Token):
    def consume(self, b_uffer):
        accum = ""
        while True:
            ch = b_uffer.peek()
            if ch is None or ch not in '0123456789':
                break
            else:
                accum += ch
                b_uffer.advance()
        if accum != "":
            return ("int", int(accum))
        else:
            return None

class OperatorToken(Token):
    def consume(self, b_uffer):
        ch = b_uffer.peek()
        if ch is not None and ch in '+-':
            b_uffer.advance()
            return ("ope", ch)
        return None

def tokenize(string):
    b_uffer = Buffer(string)
    tk_int = IntToken()
    tk_op = OperatorToken()
    tokens = []

    while b_uffer.peek():
        token = None
        for tk in (tk_int, tk_op):
            token = tk.consume(b_uffer)
            if token:
                tokens.append(token)
                break
        if not token:
            raise ValueError("Error in Syntax")
    return tokens 		

class Node(object):
    pass

class IntNode(Node):
    def __init__(self, value):
        self.value = value

class BinaryOpNode(Node):
    def __init__(self, kind):
        self.kind = kind
        self.left = None
        self.right = None

def parse(tokens):
    if tokens[0][0] != 'int':
        raise ValueError("Must start with an int")
    node = IntNode(tokens[0][1])
    nbo = None
    last = tokens[0][0]
    for token in tokens[1:]:
        if token[0] == last:
            raise ValueError("Error in Syntax")
        last = token[0]
        if token[0] == 'ope':
            nbo = BinaryOpNode(token[1])
            nbo.left = node
        if token[0] == 'int':
            nbo.right = IntNode(token[1])
            node = nbo
    return node

def calculate(nbo):
    if isinstance(nbo.left, BinaryOpNode):
        leftval = calculate(nbo.left)
    else:
        leftval = nbo.left.value
    if nbo.kind == '-':
        return leftval - nbo.right.value
    elif nbo.kind == '+':
        return leftval + nbo.right.value
    else:
        raise ValueError("Wrong operator")

def evaluate(node):
    if isinstance(node, IntNode):
        return node.value
    else:
        return calculate(node)

if __name__ == '__main__':
    input = input('Input:')
    tokens = tokenize(input)
    node = parse(tokens)
    print("Result:"+str(evaluate(node)))
