import pika
import sys

#Método que se conecta con RabbitMQ y envía datos a la cola
def publisher():

    server, port = serverPort()

    print('Usuario de RabbitMQ: ')
    userRabbitMQ = input(" >")
    print('Contraseña de RabbitMQ: ')
    passRabbitMQ = input(" >")

    #Conexión con RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(server, port, '/', 
    pika.PlainCredentials(userRabbitMQ, passRabbitMQ)))
    channel = connection.channel()

    print('------ Runnning Publisher Application ------')

    print('\n [x] Escriba su nombre de usuario: ')
    username = input(" >")
    print('\n [x] Escriba su email: ')
    email = input(" >")

    print('\n [x] Las respuestas serán enviadas a su correo...')
    
    print('\n [x] ¿Qué tarea desea ejecutar? (Escriba únicamente el número)')
    print('      1. Saludar \n      2. Sumar \n      3. Restar \n      4. Multiplicar \n      5. Felicitar \n      6. Salir de la aplicación')
    tarea = input(" >")

    #Guarda la cadena que va a ser enviada al servidor
    mensaje = ""

    while True:
        #Selecciona la tarea que será enviada a la cola para que sea tomada por un servidor y la ejecute
        if tarea == "1": #Tarea 1: Saludar
            print('\n [x] Se envió la tarea 1')
            #Se concatenan los datos para enviar un único mensaje al servidor el cual será desconcatenado
            mensaje = '1' + '.' + username + ',' + email + '-'

        elif tarea == "2": #Tarea 2: Sumar
            print('\n [x] Escriba los números que desea sumar: ')
            numero1 = input(" >")
            numero2 = input(" >")
            print('\n [x] Se envió la tarea 2')
            mensaje = '2' + '.' + username + ',' + email + '-' + numero1 + '_' + numero2

        elif tarea == "3": #Tarea 3: Restar
            print('\n [x] Escriba los números que desea restar: ')
            numero1 = input(" >")
            numero2 = input(" >")
            print('\n [x] Se envió la tarea 3')
            mensaje = '3' + '.' + username + ',' + email + '-' + numero1 + '_' + numero2

        elif tarea == "4": #Tarea 4: Multiplicar
            print('\n [x] Escriba los números que desea multiplicar: ')
            numero1 = input(" >")
            numero2 = input(" >")
            print('\n [x] Se envió la tarea 4')
            mensaje = '4' + '.' + username + ',' + email + '-' + numero1 + '_' + numero2

        elif tarea == "5": #Tarea 5: Felicitar
            print('\n [x] Se envió la tarea 5')
            mensaje = '5' + '.' + username + ',' + email + '-'

        elif tarea == "6": #Tarea 6: Salir de la aplicación
            print('\n [x] Hasta luego...')
            break

        else:
            mensaje = '7' + '.' + username + ',' + email + '-'

        #Envía el mensaje a la cola
        channel.basic_publish(exchange='my_exchange', routing_key='test', body=mensaje)

        print('\n [x] ¿Qué tarea desea ejecutar? (Escriba únicamente el número)')
        tarea = input(" >")

    connection.close()
     

#Método para identificar los parámetros de servidor y puerto
def serverPort():

    if len(sys.argv) == 3:
        server = sys.argv[1]
        port = sys.argv[2]
        print(' [x] Server:', server,'\n [x] Port:', port)
        
    else:
        print(' [x] Recuerde ingresar: $python3 publisher.py ip-sever port')
        print(' [x] Ejemplo: $python3 publisher.py 34.226.36.159 5672\n')

    return server, port

if __name__ == '__main__':
    publisher()
