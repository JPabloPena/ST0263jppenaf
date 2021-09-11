import pika
import sys

#Método que se conecta con RabbitMQ
def subscriber():

    server, port = serverPort()

    print('Usuario de RabbitMQ: ')
    userRabbitMQ = input(" >")
    print('Contraseña de RabbitMQ: ')
    passRabbitMQ = input(" >")

    #Conexión con RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(server, port, '/', 
    pika.PlainCredentials(userRabbitMQ, passRabbitMQ)))
    channel = connection.channel()

    print('------ Runnning Subscriber Application ------')

    #Toma la tarea de la cola
    channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


#Método que identifica y ejecuta las tareas tomadas de la cola
def callback(ch, method, properties, body):
    
    #Se descodifica el mensaje enviado en la cola
    body = body.decode()

    #Variables para separar la cadena obtenida de body
    indicePunto = body.find(".")
    indiceComa = body.find(",")
    indiceGuion = body.find("-")
    indiceGuionB = body.find("_")

    username = body[indicePunto + 1: indiceComa]
    email = body[indiceComa + 1: indiceGuion]
    num1 = body[indiceGuion + 1: indiceGuionB]
    num2 = body[indiceGuionB + 1: len(body)]

    if body.startswith("1"): #Tarea 1: Saludar
    
        print('\n [x] Tarea: 1 -> Saludar \n [x] Buen día señor(a) ' + username)
    
    elif body.startswith("2"): #Tarea 2: Sumar

        suma = int(num1) + int(num2)
        body = suma
        print('\n [x] Tarea: 2 -> Sumar \n [x] El resultado de la suma es: ' + str(body))
    
    elif body.startswith("3"): #Tarea 3: Restar

        resta = int(num1) - int(num2)
        body = resta
        print('\n [x] Tarea: 3 -> Restar \n [x] El resultado de la resta es: ' + str(body))

    elif body.startswith("4"): #Tarea 4: Multiplicar

        mult = int(num1) * int(num2)
        body = mult
        print('\n [x] Tarea: 4 -> Multiplicar \n [x] El resultado de la multiplicación es: ' + str(body))

    elif body.startswith("5"): #Tarea 5: Felicitar
        
        print('\n [x] Tarea: 5 -> Felicitar \n [x] Felicitaciones señor(a) ' + username)
    
    else:
        print('\n [x] La tarea no ha sido identificada...')
    
    print(' [x] Enviando respuesta al correo de ' + username + ': ' + email)


#Método para identificar los parámetros de servidor y puerto
def serverPort():
    if len(sys.argv) == 3:
        server = sys.argv[1]
        port = sys.argv[2]
        print(' [x] Host:', server,'\n [x] Port:', port)
        
    else:
        print(' [x] Recuerde ingresar: $python3 subscriber.py ip-sever port')
        print(' [x] Ejemplo: $python3 subscriber.py 34.226.36.159 5672\n')
        
    return server, port

if __name__ == '__main__':
    subscriber()