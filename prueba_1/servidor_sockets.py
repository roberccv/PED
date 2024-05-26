import socket
from respuesta import Respuesta

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 8001))
    s.listen(2)
    respuesta_servidor = Respuesta()
    
    ns, _ = s.accept()
    mensaje_1 = ns.recv(1024)
    
    ns.send(respuesta_servidor.respuesta_del_servidor(mensaje_1).encode())
    mensaje_2 = ns.recv(1024)
    ns.send(respuesta_servidor.respuesta_del_servidor(mensaje_2).encode())
    mensaje_3 = ns.recv(1024)
    ns.send(respuesta_servidor.respuesta_del_servidor(mensaje_3).encode())
    Cierre = ns.recv(1024)
    if Cierre == b"":
        ns.close()

if __name__ == "__main__":
    main()
