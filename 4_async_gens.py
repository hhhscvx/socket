import socket
from select import select

tasks = []

to_read = {}
to_write = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:

        yield ('read', server_socket)  # ready to read
        client_socket, addr = server_socket.accept()  # read

        print('Connection from', addr)
        tasks.append(client(client_socket))


def client(client_socket):
    while True:

        yield ('read', client_socket)  # ready to read
        request = client_socket.recv(1024)  # read

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()

            yield ('write', client_socket)  # ready to write
            client_socket.send(response)  # write


def event_loop():

    while any([tasks, to_read, to_write]):

        while not tasks: # 2
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try: # 1
            task = tasks.pop(0)

            reason, sock = next(task)
            if reason == 'read':
                to_read[sock] = task
            elif reason == 'write':
                to_write[sock] = task

        except StopIteration:
            print('done')


tasks.append(server())
event_loop()
