from socket import socket, error
from threading import Thread
import threading
import socket

def sock(ip,tiempo):
    # array con  ip y puerto
    conexion=ip.split(':')
    direccion=conexion[0]
    puerto=int(conexion[1])
    cadena=str(tiempo)
    print direccion,":",puerto,",","tiempo",":",cadena
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((direccion,puerto))
    s.send(cadena)
    recibido = s.recv(1024)
    print "---------------------------------"
    print "resultado recibido del  servidor = " ,recibido
    print "---------------------------------"
    print ""
    s.close()
    return recibido

def server_sol(nombre, estado):
    servers[nombre]['libre'] = estado;

def client_res(cpu, ram):
    while True:
        for ser in servers:
            if(servers[ser]['libre'] and servers[ser]['ram'] >= ram and  servers[ser]['cpu'] >= cpu):
                print servers[ser]
                return [servers[ser]['host'], ser]

servers =   {
  "ser1": {"host": 'localhost:9091', "libre": 1, "ram": 500, "cpu": 500  },
  "ser2": {"host": 'localhost:9092', "libre": 1, "ram": 1000, "cpu": 2000  },
  "ser3": {"host": 'localhost:9093', "libre": 1, "ram": 1500, "cpu": 500  },
  "ser4": {"host": 'localhost:9094', "libre": 1, "ram": 2000, "cpu": 1000  },
  "ser5": {"host": 'localhost:9095', "libre": 1, "ram": 3000, "cpu": 800  },
  "ser6": {"host": 'localhost:9096', "libre": 1, "ram": 500, "cpu": 1000  },
  "ser7": {"host": 'localhost:9097', "libre": 1, "ram": 3500, "cpu": 2000  },
}

lista=[]
class Client(Thread):

    def __init__(self, conn, addr):
        Thread.__init__(self)

        self.conn = conn
        self.addr = addr

    def run(self):
        while True:
            try:
                # Recibir datos del cliente.
                input_data = self.conn.recv(1024)
                cpu_ram = input_data.split(',')
                cpu = int(cpu_ram[0])
                ram = int(cpu_ram[1])
                tiempo = int(cpu_ram[2])
                #lista.append(input_data)
                response = client_res(cpu, ram)
                host = response[0]
                nombre_server = response[1]
                print "Voy a usar ", response[0], " nombre: ", response[1]
                server_sol(nombre_server, 0)
                #ahora me conector al servidor
                respuesta=sock(host,tiempo)

                #una vez tengo la respuesta
                server_sol(nombre_server, 1)


                self.conn.send(respuesta)
            except error:
                print "[%s] Error de lectura." % self.name
                self.conn.send('error')
                break
           # print lista
class Servidor(Thread):


    def __init__(self, conn, addr):
        Thread.__init__(self)

        self.conn = conn
        self.addr = addr

    def run(self):
        while True:
            try:
                # Recibir datos del cliente.
                input_data = self.conn.recv(1024)
                #ej: ser1,0
                ser_estado = input_data.split(',')
                server = ser_estado[0]
                estado = int(ser_estado[1])
                server_sol(server, estado)
                print servers
                self.conn.send('ok')
            except error:
                print "[%s] Error de lectura." % self.name
                self.con.send('error')
                break
            else:
                # Reenviar la informacion recibida.
                if input_data:
                    self.conn.send(input_data)


def cliente():
    s = socket.socket()    
    # Escuchar peticiones en el puerto 6030.
    s.bind(("localhost", 6030))
    s.listen(0)
    
    while True:
        conn, addr = s.accept()
        c = Client(conn, addr)
        c.start()
        print "%s:%d se ha conectado al servidor de clientes." % addr

    
def servidor():
    s = socket.socket()    
    # Escuchar peticiones en el puerto 6031.
    s.bind(("localhost", 6031))
    s.listen(0)

    while True:
        conn, addr = s.accept()
        c = Servidor(conn, addr)
        c.start()
        print "%s:%d se ha conectado al servidor de miniservidores." % addr

if __name__ == "__main__":
    hilo_cliente = threading.Thread(target=cliente)
    hilo_servidor = threading.Thread(target=servidor)
    hilo_cliente.start()
    hilo_servidor.start()
