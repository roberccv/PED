import socket, sys, os
from figura import Figura

puerto = int(sys.argv[1])
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    s.bind(('localhost', puerto ))

    s.listen(2)

    while True:
        ns, _ = s.accept()

        atender_cliente(ns)

    
def atender_cliente(ns):
    pid = os.fork()
    if pid == 0:
        while True:
            calculo = ns.recv(1024).decode()
            ns.send(b'Siguiente')
            X_max = int(ns.recv(1024).decode())
            ns.send(b"Siguiente")
            X_min = int(ns.recv(1024).decode())
            ns.send(b"Siguiente")
            Y_max = int(ns.recv(1024).decode())
            ns.send(b"Siguiente")
            Y_min = int(ns.recv(1024).decode())

            fig = Figura()
            if calculo == "area":
                respuesta = fig.area(X_max, X_min, Y_max, Y_min)
            elif calculo == "perimetro":
                respuesta = fig.perimetro(X_max, X_min, Y_max, Y_min)
            elif calculo == "punto_medio":
                respuesta = fig.punto_medio(X_max, X_min, Y_max, Y_min)
            else:
                respuesta = "Error"
            ns.send(str(respuesta).encode())
            ns.close()
            break
if __name__ == '__main__':
    main()