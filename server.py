import http.server
import sys

class LoggingHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        client_ip   = self.client_address[0]
        client_port = self.client_address[1]
        self.wfile.write("Roger {}:{}\n"
                         .format(client_ip, client_port)
                         .encode("utf-8"))

    # def log_request(self, code='-', size='-'):
    #     self.log_message(str(self.client_address[1]))
    #     super(LoggingHandler, self).log_request(*args, **kwargs)
    
    def log_message(self, format, *args):
        # Stole this code from https://hg.python.org/cpython/file/3.4/Lib/http/server.py
        sys.stderr.write("%s:%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.client_address[1],
                          self.log_date_time_string(),
                          format%args))




PORT = int(sys.argv[1])

httpd = http.server.HTTPServer(("", PORT), LoggingHandler)
httpd.serve_forever()
