# =============================== Number functions ===============================

def zero(func=None): 
    if func == None:
        return 0
    else:
        return func(0)
def one(func=None): 
    if func == None:
        return 1
    else:
        return func(1)
def two(func=None): 
    if func == None:
        return 2
    else:
        return func(2)
def three(func=None): 
    if func == None:
        return 3
    else:
        return func(3)
def four(func=None): 
    if func == None:
        return 4
    else:
        return func(4)
def five(func=None): 
    if func == None:
        return 5
    else:
        return func(5)
def six(func=None): 
    if func == None:
        return 6
    else:
        return func(6)
def seven(func=None): 
    if func == None:
        return 7
    else:
        return func(7)
def eight(func=None): 
    if func == None:
        return 8
    else:
        return func(8)
def nine(func=None): 
    if func == None:
        return 9
    else:
        return func(9)

# =============================== Calculation functions ===============================

def plus(y): 
    def operation(x):
        calc = x + y
        return calc
    return operation
def minus(y): 
    def operation(x):
        calc = x - y
        return calc
    return operation
def times(y): 
    def operation(x):
        calc = x * y
        return calc
    return operation
def divided_by(y): 
    def operation(x):
        calc = x // y
        return calc
    return operation
    
print(eight(divided_by(three())))

# How it works: E.g. eight(divided_by(three())) -> 3 is returned, divide_by creates the function, eight() uses it.