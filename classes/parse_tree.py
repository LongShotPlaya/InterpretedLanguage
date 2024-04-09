from classes.token import Token
from classes.expression import Expression
from classes.variable import Variable

class ParseTree:
    def __init__(self, tokens, errors: list[str]):
        self.tokens = tokens
        self.pointer = 0
        self.variables = {}
        self.errors = errors
        self.root = Expression("execution", "execute", self.variables, [self.parse()])

    def curr_token(self) -> Token:
        return None if self.pointer >= len(self.tokens) else self.tokens[self.pointer]

    def next_token(self) -> Token:
        self.pointer += 1
        return self.curr_token()
    
    def peek(self, amt) -> Token:
        self.pointer += amt
        val = self.curr_token()
        self.pointer -= amt
        return val

    def evaluate(self):
        return self.root.evaluate()

    def parse(self):
        token = self.curr_token()

        if token is None:
            return None

        match token.type:
            case "word":
                if token.content == "swim":
                    if (next_token := self.peek(1)).content == "{":
                        self.next_token()
                        return self.parse_swim_block()
                    else:
                        self.errors.append(f"Unexpected token '{next_token.content}' after 'swim' at {next_token.location}.")
                elif token.content == "exclaim":
                    return self.parse_exclaim()
                elif token.content == "classify":
                    return self.parse_classify()
                elif token.content == "speak":
                    return self.parse_speak()
                elif token.content == "reverse":
                    return self.parse_reverse()
                elif token.content == "repeat":
                    return self.parse_repeat()
                else:
                    self.errors.append(f"Unknown swim stroke '{token.content}' at {token.location}.")
                    return None
            case _:
                self.errors.append(f"Unexpected token '{token.content}' at {token.location}.")
                return None

    def parse_swim_block(self):
        expressions = []

        while self.curr_token() is not None and self.curr_token().content != "}":
            expression = self.parse()
            if expression is not None:
                expressions.append(expression)

        self.next_token()
        return Expression("execution", "execute", self.variables, expressions)

    def parse_exclaim(self):
        token = self.next_token()
        args = []

        while self.curr_token() is not None and self.curr_token().content != ".":
            expression = self.parse()
            if expression is not None:
                args.append(expression)

        return Expression("statement", "exclaim", self.variables, args)

    def parse_classify(self):
        token = self.next_token()
        args = []

        while self.curr_token() is not None and self.curr_token().content != ".":
            expression = self.parse()
            if expression is not None:
                args.append(expression)

        return Expression("statement", "classify", self.variables, args)

    def parse_speak(self):
        token = self.next_token()
        args = []

        while self.curr_token() is not None and self.curr_token().content != ".":
            expression = self.parse()
            if expression is not None:
                args.append(expression)

        return Expression("statement", "speak", self.variables, args)

    def parse_reverse(self):
        token = self.next_token()
        args = []

        while self.curr_token() is not None and self.curr_token().content != ".":
            expression = self.parse()
            if expression is not None:
                args.append(expression)

        return Expression("statement", "reverse", self.variables, args)

    def parse_repeat(self):
        token = self.next_token()
        args = []

        while self.curr_token() is not None and self.curr_token().content != ".":
            expression = self.parse()
            if expression is not None:
                args.append(expression)

        return Expression("statement", "repeat", self.variables, args)
