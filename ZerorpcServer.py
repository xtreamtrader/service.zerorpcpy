import zerorpc
import spacy
import json
from NlpService import ProcessText


class RpcServer(object):
    def textProcessor(self, text):
        spacyed = ProcessText("en_core_web_sm", text)
        return spacyed


s = zerorpc.Server(RpcServer())
port = "tcp://0.0.0.0:5828"
s.bind(port)
print("zerorpc server is running @ port:5828")
s.run()

