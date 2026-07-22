def universal_func(func):

        def wrapper(*args, **kwargs):
            number = kwargs.get('count', 0)
            while number > 0:
                func(*args)
                number -= 1

        return wrapper


@universal_func
def some_text(text):
    print(text)


some_text('print me', count = 2)
