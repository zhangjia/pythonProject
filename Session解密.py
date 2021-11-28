#!/usr/bin/env python3
#Session解密
import sys
import zlib
from base64 import b64decode
from flask.sessions import session_json_serializer
from itsdangerous import base64_decode

def decryption(payload):
    payload, sig = payload.rsplit(b'.', 1)
    payload, timestamp = payload.rsplit(b'.', 1)

    decompress = False
    if payload.startswith(b'.'):
        payload = payload[1:]
        decompress = True

    try:
        payload = base64_decode(payload)
    except Exception as e:
        raise Exception('Could not base64 decode the payload because of '
                         'an exception')

    if decompress:
        try:
            payload = zlib.decompress(payload)
        except Exception as e:
            raise Exception('Could not zlib decompress the payload before '
                             'decoding the payload')

    return session_json_serializer.loads(payload)

if __name__ == '__main__':
    s = '.eJw9kE2PgjAQhv_KZs4ekI-LiYduCsRNZgxuWdJeDCpSCtUENQs1_vdFs_Ewp2fyvDPvHbbHvrpoWFz7WzWDbXOAxR0-drAA6WJHjgVK7H0ybEBfWWU2Gl3uiLOIRByhyULpPydpMV2NaBNNNmlVmoey-LLkU6fMKiSTaGmyQBrm6OnhdTDxRqXorXk8rnkeSPHZkaAW_diTRTagxUC6zCnTWen2kbLZtMtCsptmcnpTxiidnnLzJTxmsL_0x-313Fan9wvKxL_S1IPi2ZxEZ9Zcdyha_3WSYBEWZKnAUdl4QJ47lW5aYsuXrrFlXb1Nu_nP-fufnEo7AXC6PNWmKWEGt0vVv6qDuQePP-AQbZs.YYzB_Q.MY3LXXV65zC5J5SQSewReaw0DGM'
    print(decryption(s.encode()))