import socket
import sys
import thread
import math
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9096))
s.listen(10)

def conecOP(sc,addr):
    cadena="ok"
    ope=sc.recv(1024)
    time.sleep(int(ope))
    sc.send(cadena)

print "respondiendo..."

while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(conecOP,(sc,addr))
    
sc.close()
s.close()