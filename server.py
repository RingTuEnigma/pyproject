from http.server import HTTPServer, BaseHTTPRequestHandler
import custom_calc

#Subclass to handle the HTTP Request
class CalculationHandler(BaseHTTPRequestHandler):
  #Handling the CORS-Policy of the browser
  def do_OPTIONS(self):
    self.send_response(200, "ok")
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, POST')
    self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
    self.send_header("Access-Control-Allow-Headers", "Content-Type")
    self.end_headers()
  
  #def do_GET(self):
    #self.send_response(200)
    #self.send_header('content-type', 'text/html')
    #self.end_headers()
    #self.wfile.write('Hello Test'.encode())

  #Handling the actual request with the client data
  def do_POST(self):
    #Reading the entity-body of the HTTP-Request
    content_len = int(self.headers.get('Content-Length'))
    post_body = self.rfile.read(content_len)
    #custom_calc.test_function(post_body)
    response_data = custom_calc.do_calculation(post_body)
    self.send_response(200)
    self.send_header('content-type', 'json/application')
    self.send_header('Access-Control-Allow-Origin', '*')
    self.end_headers()
    self.wfile.write(response_data.encode())

#Running the HTTP-Server and passing our request handler class
def run(server_class=HTTPServer, handler_class=CalculationHandler):
    server_address = ('127.0.0.1', 8000)
    try:
      httpd = server_class(server_address, handler_class)
      print("Server will be running now!")
      httpd.serve_forever()
    except:
      print("You stopped the server or something went wrong!")

#Making sure it doesnt run if it is imported as a module
if __name__ == '__main__':
  run()