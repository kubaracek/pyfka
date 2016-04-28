import json

def json_encode(msg):
    return str.encode(json.dumps(msg))

def json_decode(msg):
    return json.loads(msg.decode())


def str_decode(msg):
    if msg is None:
        return None

    return msg.decode()

def str_encode(msg):
    if msg is None:
        return None

    return str.encode(msg)
