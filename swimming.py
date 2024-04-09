from classes.token import Token
from classes.location import Location

# Function definitions here
def cry(arg):
    """Works similarly to "print" in Python"""
    if isinstance(arg, list) and len(arg) > 0:
        return print(*[str(a) for a in arg])
    elif isinstance(arg, list):
        return print()
    return print(arg)

def kind(lit):
    """Gets the type of a literal"""
    if isinstance(lit, bool):
        return "booboo"
    elif isinstance(lit, int):
        return "num"
    elif isinstance(lit, float):
        return "mathynum"
    elif isinstance(lit, str):
        return "blah"
    elif isinstance(lit, type(cry)):
        return "weapon"
    else:
        raise ValueError("Invalid type!")

def tellme(prompt=None):
    """Similar to Python's input() with an optional prompt"""
    if prompt is not None:
        print(prompt)
    return input()

def counter(string):
    """Takes an input string and returns it reversed"""
    return string[::-1]

def again(string, count):
    """Takes an input string and returns it repeated 'count' times"""
    return string * count

def blah(lit):
    """Casts a literal to the 'blah' data type"""
    return str(lit)

def num(lit):
    """Casts a literal to the 'num' data type"""
    return int(lit)

def mathynum(lit):
    """Casts a literal to the 'mathynum' data type"""
    return float(lit)

def by(arg1, arg2):
    """Multiplies two terms together"""
    return arg1 * arg2
