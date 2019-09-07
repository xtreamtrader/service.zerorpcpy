import zerorpc
import spacy
import json
from NlpService import ProcessText


class RpcServer(object):
    def textProcessor(self, text):
        spacyed = ProcessText("en_core_web_sm", text)
        return spacyed


s = zerorpc.Server(RpcServer())
s.bind("tcp://127.0.0.1:5828")
s.run()
