#import socket
from socket import socket

def Main():
    
    mySocket = socket()
    #mySocket.connect( ('localhost', 8000) )
    mySocket.connect( ('172.31.15.122', 3000) )

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
    print("• Primero elija la operación que desea realizar y luego digíte los dos números •")
    print("============|| OPERACIONES ||============")
    print("• Para sumar:         SUMAR")
    print("• Para restar:        RESTAR")
    print("• Para multiplicar:   MULTIPLICAR")
    print("• Para dividir:       DIVIDIR")
    print("=========================================")
    print("• Para salir escriba: EXIT")
    print("")
    Main()
    