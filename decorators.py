


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def my_first_decorator(function):

    # * args is a variable recognised tby the ide to mean 'any positional argument' such as any iterable type (0,1,2,3,4)
    # **kwargs is a variable recognised tby the ide to mean 'any names argument' such as named variables passed in
    # *args and **kwargs can be used as arguments with standard arguments  but should be passed in the following order
    # both are used to make a function more flexible so that you want a function to execute..
    #  in the case that any number or type of argument is passed into it
    # function(standard arguments, * args , **kwargs)

    # unpacking operator (* ):iterates over a sequence in a list or tuple -
    # * is to indicate that this variable should be a list containing the elements from the iterable that weren't
    # a, *b, c = [1, 2, 3, 4, 5]
    # print(b)
    # results in  2, 3, 4
    # explicitly assigned to another variable.
    # library unpacking operator (**)

    # tuples are like lists but tuples are immutable and lists are mutable: values of tuples cannot be changed once
    # assigned
     # comma (,) next to variable indicates a single value tiple
    # if you want to unpack a single value tuple such as *variable, = "hello"
    # this will give you list of single value tuples variable=[h,e,l,l,o]

    def wrapper(*args, **kwargs):

        ret_val = function
        print(f"i have decorated the function")

        return ret_val(*args, **kwargs)

    return wrapper


@my_first_decorator
def hello(person):
    print(f"hello {person}")
    return f"hello {person}"


if __name__ == '__main__':

    # hello("person") is a decorated function as indicated but the "@ decoratorname" flag above it
    # when hello("person") is run
    # The @my_first_decorator flag tells the ide that hello(person) is decorated with my_first_decorator(function)
    # the @my_first_decorator is a flag that runs the 1) decorator function and 2) the return of the decorator function
    # the return of my_first_decorator(function) is wrapper(*args, **kwargs)
    # therefore  wrapper(*args, **kwargs) is also executed and thus runs the print function and original function.
    # you can do many things from within the wrapper and don't need to call the original function, although this...
    # is NOT GOOD PRACTICE and makes for unreadable code as your the original function you decorated wont run...
    # so why use a decorator in the first place.
    hello("houcine")
