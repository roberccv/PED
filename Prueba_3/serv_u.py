import socket, sys,os, select

#puerto = int(sys.argv[1])

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('localhost', 5000))

    #a , _ = s.recvfrom(1024)
    #os.write(1, a)
    #b , _ = s.recvfrom(1024)
    #os.write(1, b)

    lista = [s]
    i = 0
    while True:
        nueva_lista = select.select(lista.copy(), [], [])
        if nueva_lista[0]:
            i  += 1
            a , _ = s.recvfrom(1024)
        if a == b'Exit': 
            print(i - 1)
            break
        else: os.write(1, a)
if __name__ == '__main__':
    main()