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

# --------second function----------
#modification of the above function  with two arguments in the function
def twice(func, value):
    """function with two arguments
    func: function object
    value: argument passed to the function"""
    func(value)
    func(value)
def print_twice(value):
    """function prints twice
    value: anything printable"""
    print(value)
    print(value)
twice(print_twice, 'sam')
def print_four(func, value):
    """gunction to print four times
    func: function object
    value: argument to the function"""
    