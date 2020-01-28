from http.server import HTTPServer, BaseHTTPRequestHandler
import custom_calc

class calculationHandler(BaseHTTPRequestHandler):
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

  def do_POST(self):
    content_len = int(self.headers.get('Content-Length'))
    post_body = self.rfile.read(content_len)
    response_data = custom_calc.test_function(post_body)
    self.send_response(200)
    self.send_header('content-type', 'json/application')
    self.send_header('Access-Control-Allow-Origin', '*')
    self.end_headers()
    self.wfile.write(response_data.encode())

def run(server_class=HTTPServer, handler_class=calculationHandler):
    server_address = ('127.0.0.1', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

#Clever trick in a lot of python scripts, figure it out yourself ;)
if __name__ == '__main__':
  run()

#TEST