from socket import socket
import sys

#Método que posee toda la lógica de negocio
def Main():

    #Condicional que determina los parámetros iniciales al ejecutar la apliación
    if len(sys.argv) == 3:
        server = sys.argv[1]
        port = sys.argv[2]
        print('Server:', server,'\nPort:', port)
    else:
        print("Recuerde ingresar: $python3 client.py ip-sever port")
        print("Ejemplo: $python3 client.py 34.226.36.159 3000")
    

    mySocket = socket() #Se llama al método sockect
    mySocket.connect( (server, int(port)) ) #Se establece una conexión con el servidor mediante el método socket recibiendo un servidor y puerto
    #mySocket.connect( ('localhost', 8000) )
    #mySocket.connect( ('35.153.31.234', 3000) )

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

            #La variable mensaje concatena la operación y los números recibidos para poder enviar un único dato al servidor. A modo de ejemplo quedaría: SUMAR15.20
            mensaje = "SUMAR" + numero1 + "." + numero2
            mySocket.send(mensaje.encode()) #Codifica el mensaje para que pueda ser enviado al servidor y lo envía
            datos = mySocket.recv(1024).decode() #Recibe la respuesta del servidor y la descodifica para podersela mostrar al cliente
            print('El resultado es: ' + datos)
        
        #Lo anteriormente explicada se aplica de forma similar para todas las condiciones

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

    mySocket.close() #Se termina la conexión con el servidor

if __name__ == '__main__':
    Main()
    
