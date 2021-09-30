import socket
import sys
from _thread import *
from http.server import BaseHTTPRequestHandler, HTTPServer

mySocket = socket.socket()

#Clase que maneja las peticiones enviadas por los clientes
class HandlerConection(BaseHTTPRequestHandler):
    def _set_response(self): #Método de los HEADERS
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', '/results')
        self.end_headers()

    def do_GET(self): #Método GET
        if self.path.endswith('/results'):
            conn, addr = mySocket.accept()
            connection(conn)
            self._set_response()
            self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self): #Método POST
        content_length = int(self.headers['Content-Length']) 
        post_data = self.rfile.read(content_length) 
        post_data = str(post_data.decode('utf-8'))
        dataArray = post_data.split('|')

        if dataArray[0] == '1':
            result = int(dataArray[1]) + int(dataArray[2])

        elif dataArray[0] == '2':
            result = int(dataArray[1]) - int(dataArray[2])
        
        elif dataArray[0] == '3':
            result = int(dataArray[1]) * int(dataArray[2])

        elif dataArray[0] == '4':
            result = int(dataArray[1]) / int(dataArray[2])
        
        print(result)
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def connection(conn):
    while True:
        
        data = conn.recv(1024).decode()
        dataArray = data.split('|')

        if dataArray[0] == '1':
            result = int(dataArray[1]) + int(dataArray[2])
            msg = ' [x] El resultado es ' + str(result)
            conn.send(msg.encode())
        
        elif dataArray[0] == '2':
            result = int(dataArray[1]) - int(dataArray[2])
            msg = ' [x] El resultado es ' + str(result)
            conn.send(msg.encode())
        
        elif dataArray[0] == '3':
            result = int(dataArray[1]) * int(dataArray[2])
            msg = ' [x] El resultado es ' + str(result)
            conn.send(msg.encode())
        
        elif dataArray[0] == '4':
            result = int(dataArray[1]) / int(dataArray[2])
            msg = ' [x] El resultado es ' + str(result)
            conn.send(msg.encode())
        
        elif dataArray[0] == '5':
            msg = ' [x] Hasta luego...'
            conn.send(msg.encode())
            break
    conn.close()

#Método que recibe los parámetros iniciales (ip-servidor y puerto)
def parameters():
    if len(sys.argv) == 3:
        server = sys.argv[1]
        port = sys.argv[2]
        print(' [x] Server:', server,'\n [x] Port:', port)
        
    else:
        print(' [x] Recuerde ingresar: $python3 server.py ip-sever port')
        print(' [x] Ejemplo: $python3 server.py 172.31.56.16 8000\n')

    return server, port

def main():
    try:
        server, port = parameters()
        server = HTTPServer((server, int(port)), HandlerConection) #Establece la conexión del servidor
        print('------ Runnning Server Application ------')
        server.serve_forever()
    except Exception as error:
        print("Server error")
        print(error)

if __name__ == '__main__':
    main()