# Decorator
def my_decorator(func):
    def wrap_func():
        print('*'*80)
        func()
        print('*' * 80)
    return wrap_func


@my_decorator
def hello():
    print('hello')


hello()
