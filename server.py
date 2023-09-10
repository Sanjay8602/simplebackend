from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query = parse_qs(parsed_url.query)

        if 'param1' not in query or 'param2' not in query:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Both param1 and param2 are required"}).encode('utf-8'))
            return

        param1 = query['param1'][0]
        param2 = query['param2'][0]

        result = {
            "param1": param1,
            "param2": param2,
            "info": f"Info for {param1} and {param2}",
        }

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode('utf-8'))

def run():
    port = 3000  # You can change the port as needed
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print(f"Server is running on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
