import socket, sys

#puerto = int(sys.argv[1])

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('localhost', 5001))

    s.sendto('Hola, servidor'.encode(), ('localhost', 5000))
    s.sendto('Hola, servidor'.encode(), ('localhost', 5000))
    s.sendto('Hola, servidor'.encode(), ('localhost', 5000))
    s.sendto('Hola, servidor'.encode(), ('localhost', 5000))
    s.sendto('Hola, servidor'.encode(), ('localhost', 5000))
    s.sendto('Exit'.encode(), ('localhost', 5000))


if __name__ == '__main__':
    main()