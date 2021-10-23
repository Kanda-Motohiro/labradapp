# client.py for labrad echoserver by kanda.motohiro@gmail.com
# Released under GPL v3. Based on code on https://github.com/labrad/pylabrad.
import labrad
import os

#os.environ["LABRADHOST"] = "localhost"
#os.environ["LABRADPASSWORD"] = ""

cxn = labrad.connect('localhost')
servers = cxn.manager.servers()

# echoserver プロセス一覧を得る。
echoServers = []
for server in servers:
    name = server[1]
    if name.startswith("EchoServer"):
        echoServers.append(cxn[name])

responses = []
for sv in echoServers:
    # これは、同期で返る。
    resp = sv.echo("hello")
    print(resp)

    # 非同期で呼ぶにはこうする。
    p = sv.packet()
    p.delayed_echo("world")
    response = p.send_future()
    responses.append(response)

for response in responses:
    result = response.result()
    print(result.delayed_echo)
