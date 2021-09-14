from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

#Arreglo donde se guardarán las tareas
tasklist = ['Task 1', 'Task 2', 'Task 3']

class requestHandler(BaseHTTPRequestHandler):
    
    #Método GET
    def do_GET(self):
        
        #Vista inicial (index)
        if self.path.endswith('/tasklist'):
            #Headers
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            #self.wfile.write('Hello!'.encode())
            
            #HTML para la vista del cliente 
            output = ''
            output += '<html><body>'
            output += '<h1>Task List</h1>'
            output += '<h3><a href="/tasklist/new">Add New Task</a></h3>'
            for task in tasklist:
                output += task
                output += '<a href="/tasklist/%s/remove">X</a>' % task
                output += '</br>'

            output += '</body></html>'
            
            self.wfile.write(output.encode()) #Envía la vista al navegador
        
        #Vista donde se crean nuevas tareas
        if self.path.endswith('/new'):
            #Headers
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            #HTML para la vista del cliente 
            output = ''
            output += '<html><body>'
            output += '<h1>Add New Task</h1>'

            output += '<form method="POST" enctype="multipart/form-data" action="/tasklist/new">'
            output += '<input name="task" type="text" placeholder="Add new task">'
            output += '<input type="submit" value="Add">'
            output += '</form>'
            
            output += '</body></html>'

            self.wfile.write(output.encode()) #Envía la vista al navegador

        #Ruta que elimina las tareas
        if self.path.endswith('/remove'):
            listIDPath = self.path.split('/')[2]
            #Headers
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            
            #HTML que ejecuta el método POST para eliminar la tarea
            output = ''
            output += '<html><body>'
            output += '<h1>Remove task: %s</h1>' % listIDPath.replace('%20', ' ')
            output += '<form method="POST" enctype="multipart/form-data" action="/tasklist/%s/remove">' % listIDPath
            output += '<input type="submit" value="Remove"></form>'
            output += '<a href=/tasklist>Cancel</a>'
            output += '</body></html>'
            
            self.wfile.write(output.encode()) #Envía la vista al navegador

    #Método POST
    def do_POST(self):
        
        #Condición que permite crear una tarea
        if self.path.endswith('/new'):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                new_task = fields.get('task')
                tasklist.append(new_task[0])
            
            #Headers
            self.send_response(301)
            self.send_header('content-type', 'text/html')
            self.send_header('Location', '/tasklist')
            self.end_headers()
        
        #Condición que permite eliminar una tarea
        if self.path.endswith('/remove'):
            listIDPath = self.path.split('/')[2]
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            if ctype == 'multipart/form-data':
                list_item = listIDPath.replace('%20', ' ')
                tasklist.remove(list_item)
            
            #Headers
            self.send_response(301)
            self.send_header('content-type', 'text/html')
            self.send_header('Location', '/tasklist')
            self.end_headers()

#Método que inicia la conexión del servidor
def main():
    PORT = 8000
    server = HTTPServer(('', PORT), requestHandler)
    print('Server running on port', PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
