# client.py for labrad echoserver by kanda.motohiro@gmail.com
# Released under GPL v3. Based on code on https://github.com/labrad/pylabrad.
import labrad
import os
from typing import List

os.environ["LABRADHOST"] = "localhost"
os.environ["LABRADPASSWORD"] = ""

class EchoClient:
    def __init__(self):
        self.cxn = labrad.connect('localhost')
        servers = self.cxn.manager.servers()
        # echoserver プロセス一覧を得る。
        self.echoServers = []
        for server in servers:
            name = server[1]
            if name.startswith("EchoServer"):
                self.echoServers.append(self.cxn[name])

    def echo(self, data: str) -> List[str]:
        out = []
        for sv in self.echoServers:
            # これは、同期で返る。
            resp = sv.echo(data)
            # print(resp)
            out.append(resp)

        return out

    def async_echo(self, data: str) -> List[str]:
        out = []
        responses = []
        for sv in self.echoServers:
            # 非同期で呼ぶにはこうする。
            p = sv.packet()
            p.delayed_echo(data)
            response = p.send_future()
            responses.append(response)

        for response in responses:
            result = response.result()
            # print(result.delayed_echo)
            out.append(result.delayed_echo)

        return out

def main():
    client = EchoClient()
    out = client.echo("Hello")
    print("\n".join(out))
    out = client.async_echo("Hello again")
    print("\n".join(out))
        
if __name__ == '__main__':
    main()
