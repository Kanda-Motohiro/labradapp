#!/usr/bin/python3
# mtwebserver.py by kanda.motohiro@gmail.com. Released under GPL v3.
import time
import http.server
import client
import webserver


class EchoHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)

        status = 200
        buf = ""
        if self.path == "/":
            buf = webserver.root()
        elif self.path.startswith("/echo/"):
            path = self.path.replace("/echo/", "")
            buf = webserver.echo(path)
        elif self.path.startswith("/aecho/"):
            path = self.path.replace("/aecho/", "")
            buf = webserver.async_echo(path)
        else:
            path = self.path[1:]
            try:
                with open(path) as f:
                    buf = f.read()
            except OSError as e:
                self.log_error("path=%s error=%s %s", path, type(e), str(e))
                status = 404

        if status == 200:
            self.send_response(status)
            self.end_headers()
            self.wfile.write(buf.encode("utf-8"))
        else:
            self.send_error(status)


def main():
    webserver.echo_client = client.EchoClient()
    server_address = ("", 8080)
    print("serving at {}".format(server_address))
    httpd = http.server.ThreadingHTTPServer(server_address, EchoHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
