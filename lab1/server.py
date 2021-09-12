import sys
from socket import socket, error
from threading import Thread

#Clase para conectarse con múltiples clientes al tiempo
class Client(Thread):

    #Método para indentificar cada cliente que se conecta al servidor
    def __init__(self, conn, addr):

        Thread.__init__(self) #Crea el hilo para el cliente

        self.conn = conn #Guarda la conexión
        self.addr = addr #Guarda la dirección de la conexión
    
    #Método que posee toda la lógica de negocio
    def run(self):

        while True:
            try:
                #Recibe los datos enviados del cliente y los descodifica
                datos = self.conn.recv(1024).decode()
            except error:
                print("[%s] Error de lectura." % self.name)
                break
            
            #Como en la variable datos se recibe una cadena, cada condición verifica que fue lo que envió el usuario. 
            #En caso de que quiera sumar la variable datos recibiría una cadena como esta: SUMAR15.20
            #Entonces la condición lo que hace es identificar la operación (SUMAR) y luego separar los números en diferentes variables.
            #Esto mismo sucede para todas las condiciones.
            if datos.startswith("SUMAR"): 
                print(str(self.addr), "envía: " + str(datos))
                indice = datos.find(".")
                numero1 = datos[5:indice] #Según el ejemplo: 15
                numero2 = datos[indice+1:len(datos)] #Según el ejemplo: 20
                suma = int(numero1) + int(numero2) #Realiza la operación
                datos = str(suma) #Lo convierte en una cadena
                print("SUMA: " + str(datos))
                self.conn.send(datos.encode()) #Lo codifica para poder enviarselo al cliente

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
        
        self.conn.close() #Termina la conexión con el cliente
        
#Método que establece la conexión con múltiples clientes y determina de donde se conectan
def Main():
    
    mySocket = socket() #Se llama al método socket
    host = '0.0.0.0'
    port = int(parameters())
    #mySocket.bind( ('localhost', 8000) )
    #mySocket.bind( ('172.31.15.122', 3000) )
    mySocket.bind( (host, port) ) #Escucha la conexión con el cliente
    mySocket.listen(5) #Define cuantos clientes se pueden conectar al servidor al mismo tiempo

    while True:
        conn, addr = mySocket.accept()
        print("Conexión desde: " + str(addr))

        c = Client(conn, addr) #Crea el hilo con el cliente
        c.start() #Empieza la conexión con el cliente

def parameters():
    if len(sys.argv) == 2:
        port = sys.argv[1]
        print('Port:', port)
        return port
    else:
        port = '3000'
        print('Se estableción el puerto 3000 por defecto. Si desea usar otro puerto cierre la aplicación y recuerde ingresar:')
        print('$python3 server.py port')
        print("Ejemplo: $python3 server.py 3000")
        return port
    

if __name__ == '__main__':
    Main()
