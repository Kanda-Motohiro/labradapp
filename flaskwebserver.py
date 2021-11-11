#!/usr/bin/python3
# webserver.py by kanda.motohiro@gmail.com. Released under GPL v3.
# see https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application
from flask import Flask
import os
import client
import webserver


app = Flask(__name__)
# 効かない？
os.environ["LABRADHOST"] = "localhost"
os.environ["LABRADPASSWORD"] = ""


@app.route("/echo/<path>")
def echo(path):
    return webserver.echo(path)


# 非同期。
@app.route("/aecho/<path>")
def async_echo(path):
    return webserver.async_echo(path)


@app.route("/")
def root():
    return webserver.root()


def main():
    webserver.echo_client = client.EchoClient()
    app.run(port=8080, debug=True)


if __name__ == "__main__":
    main()
