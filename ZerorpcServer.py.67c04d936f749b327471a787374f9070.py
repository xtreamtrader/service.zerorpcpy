import zerorpc
import spacy
import json
from NlpService import ProcessText


class NlpRpcServer(object):
    def textProcessor(self, text):
        spacyed = ProcessText("en_core_web_sm", text)
        tokens = spacyed["tokens"]
        str_tokens = json.dumps(tokens)
        return str_tokens


s = zerorpc.Server(NlpRpcServer())
s.bind("tcp://127.0.0.1:5828")
s.run()