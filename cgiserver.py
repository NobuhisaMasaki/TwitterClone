import http.server

server_address = ("", 8000)
handler_class = http.server.CGIHTTPRequestHandler
cgi_server = http.server.HTTPServer(server_address, handler_class)
cgi_server.serve_forever()
