def universal_func(func):

    def wrapper(*args):
        func(*args)
        print('finished')

    return wrapper


@universal_func
def some_text(text):
    print(text)


some_text('print me')
