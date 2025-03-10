class Expression:
    def __init__(self, type: str, operation: str, vars: dict, args: list):
        self.type = type
        self.operation = operation
        self.vars = vars
        self.args = unpack_expression_chain(args)

    def evaluate(self):
        args = evaluate_children(self.args)

        match self.type:
            case "literal":
                return self.args[0]
            case "statement":
                return execute_swim_stroke(self.operation, args)
            case "parentheses":
                result = []
                for arg in args:
                    result.append(arg)
                return purge_nones(result)
            case "contents":
                pass
            case "indexer":
                pass
            case "variable":
                pass 
            case "expression":
                match self.operation:
                    case "+":
                        total = 0
                        for arg in args:
                            total += arg
                        return total
                    case "-":
                        total = 0
                        for arg in args:
                            total -= arg
                        return total
                    case "*":
                        total = 1
                        for arg in args:
                            total *= arg
                        return total
                    case "/":
                        total = args[0] ** 2
                        for arg in args:
                            total /= arg
                        return total
            case "invalid":
                pass
            case "empty":
                # Just evaluates to None
                return None
            case "execution":
                # Should just run code
                return None
            case _:
                raise "Invalid expression type!"
            
def unpack_expression_chain(chain):
    chain = unpack_list(chain)
    if type(chain) == list:
        for i, elem in enumerate(chain):
            chain[i] = unpack_expression_chain(elem)
    elif type(chain) == Expression:
        unpack_expression_chain(chain.args)
        return chain
    return purge_nones(unpack_list(chain))

def evaluate_children(args):
    args = unpack_list(args)
    if type(args) == list:
        for i, arg in enumerate(args):
            args[i] = evaluate_children(arg)
        return purge_nones(unpack_list(args))
    elif type(args) == Expression:
        return args.evaluate()
    return purge_nones(unpack_list(args))
            
def unpack_list(packed_list):
    if type(packed_list) == list:
        while len(packed_list) == 1 and type(packed_list[0]) == list:
            packed_list = packed_list[0]
        for i in packed_list:
            unpack_list(i)
    return packed_list

def purge_nones(packed_list):
    if (type(packed_list) == list):
        return [purge_nones(i) for i in packed_list if purge_nones(i) != None]
    return packed_list

def execute_swim_stroke(swim_stroke, args):
    match swim_stroke:
        case "exclaim":
            if type(args) == list and len(args) > 0:
                return print(*[str(arg) for arg in args])
            elif type(args) == list:
                return print()
            return print(args)
        case "classify":
            if type(args) == bool:
                return "brave"
            elif type(args) == int:
                return "number"
            elif type(args) == float:
                return "mathynum"
            elif type(args) == str:
                return "words"
            elif type(args) == type(execute_swim_stroke):
                return "arsenal"
            else:
                raise "Invalid type!"
        case "speak":
            if args != None and type(args) == list and len(args) > 0:
                print(args[0])
            return input()
        case "reverse":
            args = str(args[0])
            result = ""
            for i in args[::-1]:
                result += i
            return result
        case "repeat":
            return args[0] * args[1]
        case "words":
            return str(args[0])
        case "number":
            return int(args[0])
        case "mathynum":
            return float(args[0])
        case "multiply":
            return args[0] * args[1]
