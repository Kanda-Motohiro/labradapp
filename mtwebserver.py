#!/usr/bin/python3
# mtwebserver.py by kanda.motohiro@gmail.com. Released under GPL v3.
import os
import time
import http.server
import client

echo_client = None

def echo(path):
    out = echo_client.echo(path)
    out = "<br />".join(out)
    return out


# 非同期。
def async_echo(path):
    out = echo_client.async_echo(path)
    out = "<br />".join(out)
    return out

def root():
    return """
<!DOCTYPE html>
<html>
<header>
<script src="static/app.js"></script>
</header>
<body>
<h1>Toy LabRAD echo client</h1>

<input id="input0">
<button type="button" onclick="button0()">
echo
</button>
<br />
<label id="label0">output</label>
<br />

<input id="input1">
<button type="button" onclick="button1()">
echo async
</button>
<br />
<label id="label1">output</label>
<br />

</body>
</html>"""

class EchoHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        self.send_response(200)
        self.end_headers()

        if self.path == "/":
            buf = root()
        elif self.path.startswith("/echo/"):
            path = self.path.replace("/echo/", "")
            buf = echo(path)
        elif self.path.startswith("/aecho/"):
            path = self.path.replace("/aecho/", "")
            buf = async_echo(path)
        else:
            path = self.path[1:]
            with open(path) as f:
                buf = f.read()

        self.wfile.write(buf.encode("utf-8"))


def main():
    global echo_client
    echo_client = client.EchoClient()
    server_address = ("", 8080)
    print("serving at {}".format(server_address))
    httpd = http.server.ThreadingHTTPServer(server_address, EchoHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    main()
