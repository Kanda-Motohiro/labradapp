# webserver.py by kanda.motohiro@gmail.com
# Released under GPL v3.
# https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application
from flask import Flask
from markupsafe import escape
import os
import client

app = Flask(__name__)
echo_client = None
# 効かない？
os.environ["LABRADHOST"] = "localhost"
os.environ["LABRADPASSWORD"] = ""

@app.route("/echo/<path>")
def echo(path):
    out = echo_client.echo(path)
    out = "<br />".join(out)
    return out


@app.route("/aecho/<path>")
def async_echo(path):
    out = echo_client.async_echo(path)
    out = "<br />".join(out)
    return out


@app.route("/")
def root():
    return """
<html>
<header>
<script src="static/app.js"></script>
</header>
<body>
<h1>Toy LabRAD echo client</h1>
<button type="button" onclick="button0()">
button0
</button>
<br />
<label id="label0"></label>
<br />
</body>
</html>"""

def main():
    global echo_client
    echo_client = client.EchoClient()
    app.run(port=8080, debug=True)

if __name__ == "__main__":
    main()
