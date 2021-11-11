#!/usr/bin/python3
# echoserver.py for labrad by kanda.motohiro@gmail.com
# Released under GPL v3. Based on code on https://github.com/labrad/pylabrad.
from labrad.server import LabradServer, setting
from twisted.internet.defer import inlineCallbacks, returnValue
from labrad import util
import os
import time

os.environ["LABRADHOST"] = "localhost"
os.environ["LABRADPASSWORD"] = ""


class EchoServer(LabradServer):
    # プロセスごとに別の名前にする。
    name = "EchoServer{}".format(os.getpid())

    @inlineCallbacks
    def initServer(self):
        self.pid = os.getpid()
        print("initServer: pid={}".format(self.pid))
        yield None
        # yeild しないで戻ると、落ちる。

    @setting(1, data='s', returns='s')
    def echo(self, c, data):
        print("echo:" + data)
        out = data + " from {} at {}".format(self.pid, time.ctime())
        return out

    @setting(2, data='s', returns='s')
    def delayed_echo(self, c, data):
        print("delayed_echo:" + data)

        # １０秒後に非同期で返すには、こうする。
        yield util.wakeupCall(10)
        out = data + " from {} at {}".format(self.pid, time.ctime())
        returnValue(out)


__server__ = EchoServer()

if __name__ == '__main__':
    util.runServer(__server__)
