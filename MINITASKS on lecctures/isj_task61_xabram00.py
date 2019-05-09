#minitask 6.1
def deprecated(func):
    def some_new_function(x, y):
        print("Call to deprecated function: {}".format(func.__name__))
        return func(x,y)
    return some_new_function


@deprecated
def some_old_function(x, y):
    return x + y

some_old_function(1,2)
