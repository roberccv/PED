import socket, sys, os

puerto = int(sys.argv[1])

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.connect(('localhost', puerto))

    funcion = input("Ingrese la funcion a realizar: ")
    s.send(funcion.encode())

    sig =s.recv(1024)
    print(sig)
    if b'Siguiente' == sig:
        X_max = input("Ingrese el valor de X_max: ")
        s.send(X_max.encode())
    sig2 =s.recv(1024)
    if b'Siguiente' == sig2:
        X_min = input("Ingrese el valor de X_min: ")
        s.send(X_min.encode())
    sig3 =s.recv(1024)
    if b'Siguiente' == sig3:
        Y_max = input("Ingrese el valor de Y_max: ")
        s.send(Y_max.encode())
    if b'Siguiente' == s.recv(1024):
        Y_min = input("Ingrese el valor de Y_min: ")
        s.send(Y_min.encode())

    solucion = s.recv(1024).decode()
    print(solucion)

if __name__ == '__main__':
    main()