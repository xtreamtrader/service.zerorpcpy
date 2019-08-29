import zerorpc
import spacy
import json
from SpacyService import ProcessText


class HelloRPC(object):
    def nlpProcessText(self, text):
        spacyed = ProcessText("en_core_web_sm", text)
        tokens = spacyed["tokens"]
        str_tokens = json.dumps(tokens)
        print(tokens)
        return "Hello, %s" % str_tokens


s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
