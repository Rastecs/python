##function that draws a grid line
#def twice(f):
#    """ runs the function twice with one argument
#    f: function object
#    """
#    f()
#    f()
#def print_twice():
#    """prints argument twice passed in it """
#    print('spam')
#twice(print_twice)#print twice function called by twice function
"""
# --------second function----------
#modification of the above function  with two arguments in the function
def twice(func, value):
    \"""function with two arguments
    func: function object
    value: argument passed to the function\"""
    func(value)
    func(value)

def print_twice(value):
    \"""function prints twice
    value: anything printable\"""
    print(value)
    #print(value)
#twice(print_twice, 'sam')

def print_four(func, value):
    \"""gunction to print four times
    func: function object
    value: argument to the function\"""
    twice(func, value)
    twice(func, value)

twice(print_twice, 'Rastecs')
print_four(print, 'rastecs')
"""
# ----------third part of code -----------
# creating a grid
def plas_minus(f, v):
    f(v)
    f(v)
def print_out(value):
    i=1
    while (i<=11):
        if (i==1)and(i==6)and(i==11):
            print ('+')
        else:
            print('-')
    print(i, end="")
plas_minus(print_out)