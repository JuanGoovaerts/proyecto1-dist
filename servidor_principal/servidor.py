from socket import socket, error
from threading import Thread
import threading


lista=[]
class Client(Thread):
    """
    Servidor eco - reenvía todo lo recibido.
    """
    
    def __init__(self, conn, addr):
        # Inicializar clase padre.
        Thread.__init__(self)
        
        self.conn = conn
        self.addr = addr
        
    def run(self):
        while True:
            try:
                # Recibir datos del cliente.
                input_data = self.conn.recv(1024)
                lista.append(input_data)
            except error:
                print("[%s] Error de lectura." % self.name)
                break
            else:
                # Reenviar la información recibida.
                if input_data:
                    self.conn.send(input_data)
            print(lista)
class Servidor(Thread):
    """
    Servidor eco - reenvía todo lo recibido.
    """
    
    def __init__(self, conn, addr):
        # Inicializar clase padre.
        Thread.__init__(self)
        
        self.conn = conn
        self.addr = addr
        
    def run(self):
        while True:
            try:
                # Recibir datos del cliente.
                input_data = self.conn.recv(1024)
            except error:
                print("[%s] Error de lectura." % self.name)
                break
            else:
                # Reenviar la información recibida.
                if input_data:
                    self.conn.send(input_data)
            
            
def cliente():
    s = socket()
    # Escuchar peticiones en el puerto 6030.
    s.bind(("localhost", 6030))
    s.listen(0)
    
    while True:
        conn, addr = s.accept()
        c = Client(conn, addr)
        c.start()
        print("%s:%d se ha conectado al servidor de clientes." % addr)
def servidor():
    s = socket()
    # Escuchar peticiones en el puerto 6030.
    s.bind(("localhost", 6031))
    s.listen(0)
    
    while True:
        conn, addr = s.accept()
        c = Servidor(conn, addr)
        c.start()
        print("%s:%d se ha conectado al servidor de miniservidores." % addr)
       
if __name__ == "__main__":
    hilo_cliente = threading.Thread(target=cliente)
    hilo_servidor = threading.Thread(target=servidor)
    hilo_cliente.start()
    hilo_servidor.start()
    

    