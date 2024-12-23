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

def a_new_decorator(func):
    def wrapTheFunction():
        print("I am doing some bullshit before executing %s()" % func.__name__)

        func()

        print("I am doing some bullshit after executing %s()" % func.__name__)

    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the bullshit function which needs some decoration")

print('デコレータをつける前：')
a_function_requiring_decoration()

# デコレータをつけている
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

print('\nデコレータをつけた後：')
a_function_requiring_decoration()