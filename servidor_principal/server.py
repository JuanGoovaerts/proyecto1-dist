from socket import socket, error
from threading import Thread

lista=[]
class Client(Thread):
    """
    Servidor eco - reenvía todo lo recibido.
    """
    
    def __init__(self,puerto,host):
        # Inicializar clase padre.
        Thread.__init__(self)
        
        
        
        
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
    
    def __init__(self,host,puerto):
        # Inicializar clase padre.
        Thread.__init__(self)
        self.s = socket()
        self.host=host 
        self.port=puerto
    def run(self):
        print ('Server started!')
        print ('Waiting for clients...')

        self.s.bind((self.host, self.port))       
        self.s.listen(5)   
        conn, addr = self.s.accept() 
        print ('Got connection from', addr )             
        while True:
               
            try:
                # Recibir datos del cliente.
                input_data = conn.recv(1024)
            except error:
                print("[%s] Error de lectura." % self.name)
                break
            else:
                # Reenviar la información recibida.
                if input_data:
                    conn.send(input_data)
            
            
def main():
     
    c1 = Servidor("localhost",8888)
    c1.start()
if __name__ == "__main__":
    main()

    

    