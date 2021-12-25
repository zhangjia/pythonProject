# coding=utf-8
import base64

# 无论是单一base64循环解密还是base16、base32、base64混合解密都可以解出来
def getFlag(s):
    while '{' not in s:
        try:
            s = base64.b16decode(s)
        except Exception as e:
            try:
                s = base64.b32decode(s)
            except Exception as e:
                try:
                    s = base64.b64decode(s)
                except Exception as e:
                    print(e)
        finally:
            s = str(s, encoding="utf8")
    return s


if __name__ == "__main__":
    s = '7Dafajno3nKyZtujtxiF49QzL3Ad76yUzDBCJePBbxd4CPyZ8C17enZJB24fRTTFb7diodhPYPa64Jo1u6RhLG5segvLBE4ZhYDu1KXPcc72sUE2ULFCT1XNyBfbE2JHPh1Mr5eqfT6Y7UyvzLqWsqaqMjPgjRn6tBTCzjbpH1JK68RnEuZedaiXSWgvdASy2Rkzf17vzLrjFwaZodUAzUtBJmnan1wzFQQZGmeeok2'
    print(getFlag(s))
