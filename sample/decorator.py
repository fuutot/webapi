def decorator(func):
    def wrapper(*args, **kwargs):
        print('Do some bullshit BEFORE executing %s' % func.__name__)
        func(*args, **kwargs)
        print('Do some bullshit AFTER executing %s' % func.__name__)

    return wrapper

@decorator
def a_function_requiring_decoration():
    print('I am a bullshit function which needs decoration')

a_function_requiring_decoration()
"""
Do some bullshit BEFORE executing a_function_requiring_decoration
I am a bullshit function which needs decoration
Do some bullshit AFTER executing a_function_requiring_decoration
"""

def hello(name: str = 'sei'):
    def greet():
        return 'now you are in the greet() function'

    def welcome():
        return 'now you are in the welcome() function'

    if name == 'sei':
        return greet
    else:
        return welcome

hello_returned = hello()
hello_deep_returned = hello()()

print('print hello_returned:', hello_returned)
print('print hello_returned():', hello_returned())

print('print hello_deep_returned:', hello_deep_returned)
print('print hello_deep_returned():', hello_deep_returned()) # TypeError: 'str' object is not callable