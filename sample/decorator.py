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

# Pythonにおいてすべてがオブジェクトである

# int型のオブジェクトである
x = 10
print(type(x))
print(x.bit_length())

# str型のオブジェクトである
s = "hoge"
print(type(s))
print(s.capitalize())

# function型のオブジェクトである

def hoge():
    """hoge関数"""
    return "hoge"
print(type(hoge))
print(hoge.__doc__)