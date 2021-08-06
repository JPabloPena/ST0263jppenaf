#import socket
from socket import socket, error
from threading import Thread
import os
from shutil import rmtree
import shutil
class Client(Thread):

    def __init__(self, conn, addr):

        Thread.__init__(self)

        self.conn = conn
        self.addr = addr
    
    def run(self):
        while True:
            try:
                datos = self.conn.recv(1024).decode()
            except error:
                print("[%s] Error de lectura." % self.name)
                break
            
            if datos.startswith("SUMAR"):
                print(str(self.addr), "envía: " + str(datos))
                indice = datos.find(".")
                numero1 = datos[5:indice]
                numero2 = datos[indice+1:len(datos)]
                suma = int(numero1) + int(numero2)
                datos = str(suma)
                print("SUMA: " + str(datos))
                self.conn.send(datos.encode())

            elif datos.startswith("RESTAR"):
                print(str(self.addr), "envía: " + str(datos))
                indice = datos.find(".")
                numero1 = datos[6:indice]
                numero2 = datos[indice+1:len(datos)]
                resta = int(numero1) - int(numero2)
                datos = str(resta)
                print("RESTA: " + str(datos))
                self.conn.send(datos.encode())

            elif datos.startswith("MULTIPLICAR"):
                print(str(self.addr), "envía: " + str(datos))
                indice = datos.find(".")
                numero1 = datos[11:indice]
                numero2 = datos[indice+1:len(datos)]
                mul = int(numero1) * int(numero2)
                datos = str(mul)
                print("MULTIPLICACIÓN: " + str(datos))
                self.conn.send(datos.encode())

            elif datos.startswith("DIVIDIR"):
                print(str(self.addr), "envía: " + str(datos))
                indice = datos.find(".")
                numero1 = datos[7:indice]
                numero2 = datos[indice+1:len(datos)]
                div = int(numero1) / int(numero2)
                datos = str(div)
                print("DIVIDIR: " + str(datos))
                self.conn.send(datos.encode())

            elif datos == 'EXIT':
                print(str(self.addr), "envía: " + str(datos))
                datos = "Hasta luego..."
                print("Enviando: " + str(datos))
                self.conn.send(datos.encode())
                break

            else:
                print(str(self.addr), "envía: " + str(datos))
                datos = "Operación no válida..."
                print("Enviando: " + str(datos))
                self.conn.send(datos.encode())
        
        self.conn.close()
        
def Main():

    mySocket = socket()
    #mySocket.bind( ('localhost', 8000) )
    mySocket.bind( ('172.31.15.122', 3000) )
    mySocket.listen(5)

    while True:
        conn, addr = mySocket.accept()
        print("Conexión desde: " + str(addr))

        c = Client(conn, addr)
        c.start()

if __name__ == '__main__':
    Main()