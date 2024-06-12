

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g) # доходим в функции до первого yield и сразу оттуда начинаем работу
        return g
    return inner


def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen received:', message)


@coroutine
def average():
    count = 0
    sum = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        else:
            count += 1
            sum += x
            average = round(sum / count, 2)

    return average # return в генераторе вернется только в экземпляре ошибки StopIteration.value
