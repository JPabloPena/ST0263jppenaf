#import socket
from socket import socket
import sys

def Main():

    if len(sys.argv) == 3:
        server = sys.argv[1]
        port = sys.argv[2]
        print('Server:', server,'\nPort:', port)
    else:
        print("Recuerde ingresar: client.py 'ip sever' port")
    

    mySocket = socket()
    #mySocket.connect( ('localhost', 8000) )
    #mySocket.connect( ('35.153.31.234', 3000) )
    mySocket.connect( (server, int(port)) )

    print("")
    print("• Primero elija la operación que desea realizar y luego digíte los dos números •")
    print("============|| OPERACIONES ||============")
    print("• Para sumar:         SUMAR")
    print("• Para restar:        RESTAR")
    print("• Para multiplicar:   MULTIPLICAR")
    print("• Para dividir:       DIVIDIR")
    print("=========================================")
    print("• Para salir escriba: EXIT")
    print("")

    operacion = input(">")
    numero1 = input(">")
    numero2 = input(">")
    mensaje = ""

    while True:
        
        if operacion == "SUMAR":
            print("Enviando:", numero1, "+", numero2)
            mensaje = "SUMAR" + numero1 + "." + numero2
            mySocket.send(mensaje.encode())
            datos = mySocket.recv(1024).decode()
            print('El resultado es: ' + datos)

        elif operacion == "RESTAR":
            print("Enviando:", numero1, "-", numero2)
            mensaje = "RESTAR" + numero1 + "." + numero2
            mySocket.send(mensaje.encode())
            datos = mySocket.recv(1024).decode()
            print('El resultado es: ' + datos)

        elif operacion == "MULTIPLICAR":
            print("Enviando:", numero1, "*", numero2)
            mensaje = "MULTIPLICAR" + numero1 + "." + numero2
            mySocket.send(mensaje.encode())
            datos = mySocket.recv(1024).decode()
            print('El resultado es: ' + datos)

        elif operacion == "DIVIDIR":
            print("Enviando:", numero1, "/", numero2)
            mensaje = "DIVIDIR" + numero1 + "." + numero2
            mySocket.send(mensaje.encode())
            datos = mySocket.recv(1024).decode()
            print('El resultado es: ' + datos)

        else:
            mySocket.send(operacion.encode())
            datos = mySocket.recv(1024).decode()

            print(datos)
            #print('Recibido desde el servidor: ' + datos)

        operacion = input(">")
        if operacion == 'EXIT':
            mySocket.send(operacion.encode())
            datos = mySocket.recv(1024).decode()
            #print('Recibido desde el servidor: ' + datos)
            print(datos)
            break

        numero1 = input(">")
        numero2 = input(">")

    mySocket.close()

if __name__ == '__main__':
    Main()
