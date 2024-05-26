import socket, os, sys

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    s.connect(('localhost', 8001))

    i = 0
    while i < 3: 
        peticion = input("\n Ingrese la: ")
        s.send(peticion.encode())
        respuesta = s.recv(1024)
        os.write(1, respuesta)
        i += 1
    s.close()

if __name__ == '__main__':
    main()
   