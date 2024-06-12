

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return inner


class AsdException(Exception):
    pass


def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            print('asd Except!')
            break
        else:
            print('.......', message)
    return 'Return from subgen'


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except StopIteration as e:
    #         g.throw(e)
    result = yield from g # берем все yield g yield`ам делегатора
    print(result) # Return from subgen
