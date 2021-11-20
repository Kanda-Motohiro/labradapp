#!/usr/bin/python3
# webserver.py by kanda.motohiro@gmail.com. Released under GPL v3.
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
<script type="module" src="static/app.js"></script>
</header>
<body>
<h1>Toy LabRAD echo client</h1>

<input id="input0">
<button type="button" id="button0">
echo
</button>
<br />
<label id="label0">output</label>
<br />

<input id="input1">
<button type="button" id="button1">
echo async
</button>
<br />
<label id="label1">output</label>
<br />

</body>
</html>"""
