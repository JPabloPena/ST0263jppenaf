# Título
Laboratorio 4

# Autor
Juan Pablo Peña F.

# Software
App2-colas: _RabbitMQ, Python, AWS Educate_

# Descripción
Simulación de un gestor de tareas para procesamiento distribuido.

Se tiene una aplicación _publisher.py_ la cual envía tareas al middleware que las almacena en una cola para después ser tomadas y realizadas por múltiples servidores.

Se tiene una aplicación _subscriber.py_ la cual recibe y ejecuta las múltiples tareas que se encuentran en la cola del middleware.

Es posible tener múltiples clientes enviando tareas al middleware y múltiples servidores ejecutandolas. Si un servidor se encuentra ocupado con alguna tarea otro servidor toma la tarea siguiente y la ejecuta. Para este caso, al ser las tareas tan sencillas el primer servidor las ejecuta muy rápidamente por lo cual no necesita de otro, sin embargo, se probó utilizando múltiples servidores y funciona correctamente.

# Detalles del diseño
Se desarrolló una aplicación cliente-servidor la cual usa un middleware llamado _RabbitMQ_. La aplicación fue desarrollada en python y se necesitó usar el módulo _pika_ para conectarse con _RabbitMQ_. Fue desplegada en _AWS Educate_. 

# Instalación
Es necesario tener _python3_.

Para instalar la aplicación:
Clonar el repositorio. Para hacerlo se debe instalar git en su máquina de esta manera:
```
$ sudo yum install git
```
Ya para clonarlo debe usar:
```
$ git clone https://github.com/JPabloPena/ST0263jppenaf.git
```
Luego, debe instalar el módulo _pika_, para hacerlo, primero debe instalar pip:
```
$ sudo yum install pip
```
Finalmente, instala el módulo _pika_ de este modo:
```
$ pip3 install pika
```

# Ejecución
## Cliente (_publisher.py_)
Para ejecutar el cliente debe:
```
$ python3 publisher.py <ip-server> <port>
```
Ejemplo:
```
$ python3 publisher.py 34.226.36.159 5672
```
Luego, al ejecutar se le pedirá el usuario y contraseña de RabbitMQ, que para el laboratorio 4 son _user_ y _password_ respectivamente:
```
Usuario de RabbitMQ:
 >user
Contraseña de RabbitMQ:
 >password
```
Después, se le pedirá un usuario y un email en los cuales puede poner lo que desee:
```
 [x] Escriba su nombre de usuario:
 >prueba123
 
 [x] Escriba su email:
 >prueba@prueba.com
```
Finalmente podrá enviar tareas a la cola escribiendo únicamente un número como se indica en la aplicación.

## Servidor (_subscriber.py_)
Para ejecutar el servidor debe:
```
$ python3 subscriber.py <ip-server> <port>
```
Ejemplo:
```
$ python3 subscriber.py 34.226.36.159 5672
```
Luego, al ejecutar se le pedirá el usuario y contraseña de RabbitMQ, que para el laboratorio 4 son _user_ y _password_ respectivamente:
```
Usuario de RabbitMQ:
 >user
Contraseña de RabbitMQ:
 >password
```
Finalmente, el servidor ejecutará automáticamente todas las tareas que se encuentren en la cola.
