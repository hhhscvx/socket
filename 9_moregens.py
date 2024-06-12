import time
queue = []


def counter():
    counter = 0
    while True:
        print(f'counter: {counter}')
        counter += 1
        yield


def printer():
    secs = 0
    while True:
        if secs % 3 == 0:
            print('Bang!')
        secs += 1
        yield


def main():
    while True:
        g = queue.pop(0)
        next(g)
        queue.append(g)
        time.sleep(0.5)


if __name__ == "__main__":
    g1 = counter()
    queue.append(g1)
    g2 = printer()
    queue.append(g2)
    main()
