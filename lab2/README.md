# Título
Laboratorio 2

# Autor
Juan Pablo Peña F.

# Software
Calculadora: _Python, AWS Educate_

# Descripción
Calculadora sencilla que permite las operaciones de suma, resta, multiplicación y división utilizando el protocolo HTTP.

Se tiene una aplicación _client.py_ desde la cual se pueden enviar operaciones al servidor para que las realice y entregue su respuesta.

Se tiene una aplicación _server.py_ la cual recibe las peticiones enviadas por el cliente para ser ejecutadas y después devolver su respuesta.

Es posible tener múltiples clientes enviando peticiones al servidor.

# Detalles del diseño
Se desarrolló una aplicación cliente-servidor por medio de _Python_ haciendo uso del protocolo HTTP.

1. Se desplegó una instancia EC2 en AWS Educate.
2. Se creó el cliente (_client.py_) el cual se conecta con el servidor para enviar las peticiones.
3. Se creó el servidor (_server.py_) el cual permite que se conecten múltiples clientes para ejecutar y dar respuesta a sus peticiones.

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
Finalmente, acceda a la carpeta del laboratorio 2.
```
$ cd ST0263jppenaf/lab2/
```

# Ejecución
## Servidor
Para ejecutar el servidor debe:
```
$ python3 server.py <ip-server> <port>
```
Por ejemplo en mi caso fue:
```
$ python3 server.py 172.31.56.16 8000
```

## Cliente
Para ejecutar el cliente debe:
```
$ python3 client.py <ip-server> <port>
```
Por ejemplo en mi caso fue:
```
$ python3 client.py 100.26.225.171 8000
```
Ya para ejecutar las operaciones siga las instrucciones de la aplicación.
