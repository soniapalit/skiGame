import re
from math import pi

def safe_float(x):
    try:
        return float(x)
    except ValueError:
        return x
    
def eval_op(op_str, op_func, tokens):
    while op_str in tokens:
        i = tokens.index(op_str)
        ans = op_func(tokens[i-1], tokens[i+1])
        tokens[i-1:i+2] = [ans]
    return tokens

def get_value(math_expr):
    # does not support subtraction
    tokens = re.findall("(\\*|/|\\+|-?\\d+\\.\\d+|-?\\d+|pi)", math_expr)
    tokens = [pi if t == "pi" else safe_float(t) for t in tokens]
    tokens = eval_op("*", lambda a, b: a * b, tokens)
    tokens = eval_op("/", lambda a, b: a / b, tokens)
    tokens = eval_op("+", lambda a, b: a + b, tokens)
    
    # should be completely evaluated
    return tokens[0]



if __name__ == "__main__":
    print(get_value("2.54*pi/-133+45.987"))
