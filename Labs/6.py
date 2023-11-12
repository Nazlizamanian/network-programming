import http.server

class CustomRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Set the response status, headers, and content type
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Generate the HTML content with <pre> tag to preserve formatting
        response_html = """
<html>
<body>  
<h1>Your browser made the following request: </h1>
<pre>
{request_line}
{headers}
</pre>
</body>
</html>
""".format(
            request_line=self.requestline,
            headers=str(self.headers)
        )

        self.wfile.write(response_html.encode('utf-8')) # Send the HTML content as bytes

def run_server():
    server_address = ('', 8080)  
    httpd = http.server.HTTPServer(server_address, CustomRequestHandler)
    print("Serving on port 8080...")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
