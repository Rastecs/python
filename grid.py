#function that draws a grid line
def twice(f):
    """ runs the function twice with one argument
    f: function object
    """
    f()
    f()
def print_twice():
    """prints argument twice passed in it """
    print('spam')
twice(print_twice)#print twice function called by twice function