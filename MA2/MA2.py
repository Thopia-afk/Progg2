"""
Solutions to module 2 - A calculator
Student: Karl Johansson
Mail:achates02@hotmail.com
Reviewed by: Olle Virding
Reviewed date:2023-05-02
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""




from MA2tokenizer import TokenizeWrapper
import math
from tokenize import TokenError

class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

def log(val):
    if val <= 0:
        raise EvaluationError("Logarithm of non-positive value is not defined")

    result = math.log(float(val))
    return result

def mean(args):
    result = sum(args) / len(args)
    return result

def fib(val, cache = {0: 0, 1: 1}):
    if val < 0 or val % 1 != 0: 
        raise EvaluationError("Only positive integer values allowed")   
    elif val in cache:
        return cache.get(val)
    else:
        cache[val] = fib(val - 1, cache) + fib(val - 2, cache)
        return cache[val]

def fac(val):
    if val < 0:
        return EvaluationError("Negative numbers not allowed")
    elif val % 1:
        raise EvaluationError("Not integer")
    elif val == 0:
        return 1
    else:
        result = math.factorial(val)
    return result

def statement(wtok, variables):
    """ See syntax chart for statement"""
    if wtok.is_at_end() == False:
        result = assignment(wtok, variables)
    else:
        raise SyntaxError("EOL error")
    return result

def assignment(wtok, variables):
    """ See syntax chart for assignment"""

    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
            mem = wtok.is_at_end()
            wtok.next()
            if wtok.is_at_end():
                pass
            elif wtok.get_current() not in [')', '=']:
                raise SyntaxError('Cannot solve equations')
        else:
            raise SyntaxError("Expected variable name")
    return result

def arglist(wtok, variables):
    result = []
    def _arglist(wtok, variables):
        if wtok.get_current() == "(":
            wtok.next()
            result.append(assignment(wtok, variables))
            _arglist(wtok, variables)
        
        elif wtok.get_current() == ",":
            wtok.next()
            result.append(assignment(wtok, variables))
            _arglist(wtok, variables)
            
        elif wtok.get_current() == ")":
            return result

        else:
            raise SyntaxError("Expected ',' or ')'")

    _arglist(wtok, variables)
    return result

def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    
    while wtok.get_current() == '-' or wtok.get_current() == '+':
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
            
        elif wtok.get_current() == '-':
            wtok.next()
            result = result - term(wtok, variables)
            
    return result
    
def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == '*' or wtok.get_current() == '/':
        wtok.next()
        if wtok.get_previous() == '*':
            result = result * factor(wtok, variables)
            
        else:
            factor_ = factor(wtok, variables)                   #try:
            if factor_ == 0:                                    #   result = result / factor(wtok, variables)
                raise EvaluationError("Division by zero")       #except ZerodivisionError as ze
            else:                                               #   raise EvaluationError("Division by zero")
                result = result / factor_         
    return result

FUNCTIONS_1 = {'sin':math.sin, 'cos':math.cos, 'exp':math.exp, 'log':log, 'fib': fib, 'fac':fac, 'tan':math.tan}
FUNCTIONS_N = {'min':min, 'max':max, 'mean':mean, 'sum':sum}

def factor(wtok, variables):
    """ See syntax chart for factor
        Follow the syntax chart as closely as possible!
        Check only for syntax error error - not for evaluation errors!
    """
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_previous() != ')':
            SyntaxError("Expected ')'")
        wtok.next()
                
    elif wtok.get_current() in FUNCTIONS_1:
        wtok.next()

        if wtok.get_current() != '(':
            raise SyntaxError("Expected '('")
        
        else:
            func = FUNCTIONS_1[wtok.get_previous()]
            wtok.next()
            result = func(assignment(wtok, variables))
            wtok.next()
                
    elif wtok.get_current() in FUNCTIONS_N:
        wtok.next()
        result = FUNCTIONS_N[wtok.get_previous()](arglist(wtok, variables))
        wtok.next()
            
    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok, variables)

    elif wtok.is_number():
        wtok.next()
        if wtok.is_number():
            raise SyntaxError("Missing operator")
        else:
            result = float(wtok.get_previous())
    
    elif wtok.is_name():
        if wtok.get_current() not in variables:
            raise EvaluationError("Variable has no value")
        else:
            result = float(variables[wtok.get_current()])
            wtok.next()
        
    else:
        raise SyntaxError(
            "Expected number or '('")
    return result

def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file.

    You need to add handling of EvaluationError in this function!
    """

    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0] == '#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == 'vars':
            for i in variables.keys():
                print(f"{i} = {variables.get(i)}")
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                    f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')

            except EvaluationError as ee:
                print('Evaluation error')
        
if __name__ == "__main__":
    main()
