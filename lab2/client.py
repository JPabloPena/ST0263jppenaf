import socket		 	 
import requests
import http.client
import sys

mySocket = socket.socket()

#Método que ejecuta toda la lógica del negocio
def client():
    server, port = parameters() #Valores de la IP y puerto por donde accede el cliente al servidor
    serverPort = server + ':' + port

    print('------ Runnning Client Application ------')
    print(' [x] ¿Qué operación desea realizar? Escriba únicamente el número: ')
    print('      1. Sumar \n      2. Restar \n      3. Multiplicar \n      4. Dividir \n      5. Salir de la aplicación')

    try:
        while(True):
            operation = input(' >')
            msg = ""

            if operation == '1': #Suma
                num1 = input(' [Num 1] >')
                num2 = input(' [Num 2] >')
                msg = operation + '|' + num1 + '|' + num2
                print(' [x] Enviando: ', num1, '+', num2)

            elif operation == '2': #Resta
                num1 = input(' [Num 1] >')
                num2 = input(' [Num 2] >')
                msg = operation + '|' + num1 + '|' + num2
                print(' [x] Enviando: ', num1, '-', num2)

            elif operation == '3': #Multiplicación
                num1 = input(' [Num 1] >')
                num2 = input(' [Num 2] >')
                msg = operation + '|' + num1 + '|' + num2
                print(' [x] Enviando: ', num1, 'x', num2)

            elif operation == '4': #División
                num1 = input(' [Num 1] >')
                num2 = input(' [Num 2] >')
                msg = operation + '|' + num1 + '|' + num2
                print(' [x] Enviando: ', num1, '/', num2)

            elif operation == '5': #Salir de la aplicación
                msg = operation
                break

            mySocket = requests.post(serverPort, msg) #Envía la petición POST al servidor
            print(' [x] La respuesta es: ', mySocket)
            
        if mySocket != "":
            
            connection = http.client.HTTPConnection(server, int(port)) #Conexión con el servidor
            #connection = http.client.HTTPConnection("http://localhost", 8000)
            connection.request("GET", '/')
            response = connection.getresponse()
            print("Status: {} and reason: {}".format(response.status, response.reason))
            connection.close()

    except (IndexError, ValueError):
        print('No especificaste una dirección IP y número del puerto!')

#Método que recibe los parámetros iniciales (ip-servidor y puerto)
def parameters():
    if len(sys.argv) == 3:
        server = 'http://' + sys.argv[1]
        port = sys.argv[2]
        print(' [x] Server:', server,'\n [x] Port:', port)
        
    else:
        print(' [x] Recuerde ingresar: $python3 client.py ip-sever port')
        print(' [x] Ejemplo: $python3 client.py 100.26.225.171 8000\n')

    return server, port

if __name__ == '__main__':
    client()
    