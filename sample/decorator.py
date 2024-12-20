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
    return 'hello, ' + name

greet = hello

print('print hello:', hello)
print('print hello():', hello())

print('print greet', greet)
print('print greet()', greet())