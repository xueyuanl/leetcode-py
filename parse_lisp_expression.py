import re

"""
Grammar (LL(2))
expr          := let_expr | add_expr | mult_expr | var | int
let_expr      := '(' 'let' var_expr_list expr ')'
var_expr_list := var expr var_expr_list | var expr
add_expr      := '(' 'add' expr expr ')'
mult_expr     := '(' 'mult' expr expr ')'
var           := [a-z]([a-zA-Z]|\d)*
int           := \d+
"""


class Number(object):
    def __init__(self, val): self.val = int(val)

    def eval(self, var_map): return self.val


class Variable(object):
    def __init__(self, id): self.id = id

    def eval(self, var_map): return var_map[self.id]

    def __hash__(self): return hash(self.id)

    def __repr__(self): return self.id


class Let(object):
    def __init__(self, var_list, sub_expr):
        self.var_list = var_list
        self.sub_expr = sub_expr

    def eval(self, var_map):
        new_map = dict(var_map)
        for var, expr in self.var_list:
            new_map[var.id] = expr.eval(new_map)

        return self.sub_expr.eval(new_map)


class Add(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def eval(self, var_map): return self.a.eval(var_map) + self.b.eval(var_map)


class Mult(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def eval(self, var_map): return self.a.eval(var_map) * self.b.eval(var_map)


class LispParser(object):
    def __init__(self):
        self.tokens = None
        self.index = None

    def lookahead(self, offset=0):
        return self.tokens[self.index + offset]

    def consume(self):
        token = self.lookahead()
        self.index += 1
        return token

    def parse(self, tokens):
        self.tokens = tokens
        self.index = 0
        return self.parse_expr()

    def parse_expr(self):
        lookahead = self.lookahead()

        if lookahead == '(':
            secondlook = self.lookahead(offset=1)

            if secondlook == 'let':
                return self.parse_let_expr()
            elif secondlook == 'add':
                return self.parse_add_expr()
            elif secondlook == 'mult':
                return self.parse_mult_expr()
            else:
                print 'ERROR'
        elif lookahead[0].isalpha():
            return Variable(self.consume())
        else:
            return Number(self.consume())

    def parse_let_expr(self):
        self.consume()  # '('
        self.consume()  # 'let'

        var_map = self.parse_var_expr_list()
        sub_expr = self.parse_expr()

        self.consume()  # ')'
        return Let(var_map, sub_expr)

    def parse_var_expr_list(self):
        vars = []
        while self.lookahead() != '(' and (self.index + 1 < len(self.tokens)) and self.lookahead(offset=1) != ')':
            var = Variable(self.consume())
            expr = self.parse_expr()
            vars.append([var, expr])
        return vars

    def parse_add_expr(self):
        self.consume()  # '('
        self.consume()  # 'add'

        a, b = self.parse_expr(), self.parse_expr()
        self.consume()  # ')'

        return Add(a, b)

    def parse_mult_expr(self):
        self.consume()  # '('
        self.consume()  # 'mult'
        a, b = self.parse_expr(), self.parse_expr()
        self.consume()  # ')'
        return Mult(a, b)


class Solution(object):
    def evaluate(self, expression):
        token_classes = [
            '\(',
            '\)',
            'let',
            'add',
            'mult',
            '[a-z][a-z0-9]*',  # var
            '\d+|\-\d+'
        ]

        def scan(): return re.findall('|'.join(token_classes), expression)

        parser = LispParser()
        tokens = scan()
        return parser.parse(tokens).eval({})


if __name__ == '__main__':
    s = Solution()
    result = s.evaluate('(let x 1 x)')
    print result
