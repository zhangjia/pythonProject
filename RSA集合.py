# encoding: utf-8
# RSA集合
from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime, isPrime
import primefac
import gmpy2
import libnum
import random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def modinv(a, n):
    return primefac.modinv(a, n) % n


# 知道p和q，求N
def getN(p, q):
    return p * q


# 知道m，e，n,求C
def getC(m, e, n):
    return pow(m, e, n)


# 知道c,d,n，求M
def getM(c, d, n):
    return pow(c, d, n)


# 知道c、p、q、dq、dp，求M
def getMByDQDP(dp, dq, p, q, c):
    InvQ = gmpy2.invert(q, p)
    mp = pow(c, dp, p)
    mq = pow(c, dq, q)
    m = (((mp - mq) * InvQ) % p) * q + mq
    return libnum.n2s(int(m)).decode()


# 知道m1, m2, p, q，求M，m1和m2需要先调用getM1OrMP计算
def getMBYM1M2(m1, m2, p, q):
    return ((m1 - m2) * modinv(p, q) % p) * q + m2


# 知道n，c,npp，求M
def getMByNPP(n, c, npp):
    x1 = gmpy2.mpz(1)
    x2 = gmpy2.mpz(-((npp - n - 4) // 2))
    x3 = gmpy2.mpz(n)
    i = gmpy2.mpz(gmpy2.iroot(x2 * x2 - 4 * x1 * x3, 2)[0])
    p1 = (-x2 - i) // 2
    q1 = (-x2 + i) // 2
    p2 = p1 + 2
    q2 = q1 + 2
    d2 = modinv(65537, (p2 - 1) * (q2 - 1))
    m2 = pow(c, d2, npp)
    d1 = modinv(65537, (p1 - 1) * (q1 - 1))
    m1 = pow(m2, d1, n)
    return long_to_bytes(m1)


def getD(e, p, q):
    return modinv(e, (p - 1) * (q - 1))


def getM1OrMP(c, dp, p):
    return pow(c, dp, p)


def getM2OrMQ(c, dq, q):
    return pow(c, dq, q)


def getStr(num):
    return libnum.n2s(int(num)).decode()


def getP(n1, n2):
    return primefac.gcd(n1, n2)


# 知道p，q，求NPP
def getNPP(p, q):
    return (p + 2) * (q + 2)


def getDP(d, p):
    return d % (p - 1)


def getDQ(d, q):
    return d % (q - 1)


# 当e特别小的时候，用这个
def samllE(c, n):
    i = 0
    while 1:
        if (gmpy2.iroot(c + i * n, 3)[1] == 1):
            print(long_to_bytes(gmpy2.iroot(c + i * n, 3)[0]))
            break
        i = i + 1


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


# 当知道ned，求p和q
def getpq(n, e, d):
    p = 1
    q = 1
    while p == 1 and q == 1:
        k = d * e - 1
        g = random.randint(0, n)
        while p == 1 and q == 1 and k % 2 == 0:
            k = int(k // 2)
            y = pow(g, k, n)
            if y != 1 and gcd(y - 1, n) > 1:
                p = gcd(y - 1, n)
                q = n // p
    return p, q


# 知道dp，e，n，求P和Q
def getPAndQByDP(dp, e, n):
    temp = dp * e
    for i in range(1, e):
        if (temp - 1) % i == 0:
            x = (temp - 1) // i + 1
            y = n % x
            if y == 0:
                return x, n // x


def get10ToStr(x):
    return long_to_bytes(x)


def same_n_sttack(n, e1, e2, c1, c2):
    def egcd(a, b):
        x, lastX = 0, 1
        y, lastY = 1, 0
        while (b != 0):
            q = a // b
            a, b = b, a % b
            x, lastX = lastX - q * x, x
            y, lastY = lastY - q * y, y
        return (lastX, lastY)

    s = egcd(e1, e2)
    s1 = s[0]
    s2 = s[1]
    if s1 < 0:
        s1 = - s1
        c1 = primefac.modinv(c1, n)
        if c1 < 0:
            c1 += n
    elif s2 < 0:
        s2 = - s2
        c2 = primefac.modinv(c2, n)
        if c2 < 0:
            c2 += n
    m = (pow(c1, s1, n) * pow(c2, s2, n)) % n
    return m


# 有key或者pem后缀的文件，求E和N
def getEAndNByPem(ad):
    with open(ad, "rb") as f:
        key = RSA.import_key(f.read())
        return key.e, key.n


def createPrivatePem(e, p, q, ad):
    rsa_components = (p * q, e, getD(e, p, q), p, q)
    keypair = RSA.construct(rsa_components)
    with open(ad, 'wb') as f:
        f.write(keypair.exportKey())
        return keypair.exportKey()


# def getFlagByEnc(ad1,ad2):
#     with open(ad1, "rb") as f:
#         private_key = RSA.importKey(f.read())
#         pk = PKCS1_v1_5.new(private_key)
#         with open(ad2, "rb") as f2:
#             msg = pk.decrypt(f2.read(),0)
#             print(msg)
# 知道e，p，q,密闻，求私钥D，明文
def getFlagByEnc(e, p, q, ad1):
    private_key = RSA.importKey(RSA.construct((p * q, e, getD(e, p, q), p, q)).exportKey())
    pk = PKCS1_v1_5.new(private_key)
    with open(ad1, "rb") as f2:
        msg = pk.decrypt(f2.read(), 0) #对秘文解密
        print(msg)


def getMByCArray(c, e, p, q):
    res = ""
    for i in c:
        res += long_to_bytes(getM(i, getD(e, p, q), p * q)).decode('unicode_escape')
    return res


# 知道p + q ,知道（p + 1）（q+1）,知道e，d，c
def getMByPAddQANDPAadd1QAdd1(pAq, pA1qA1, c, d):
    return long_to_bytes(getM(c, d, pA1qA1 - 1 - pAq))

n=41376961156168948196303384218941117367850019509202049026037168194982219784159
e=65537
c=4161293100530874836836422603625206824589693933040432789074054165274087272587


getM()
'''
1. 知道n，用yafu分解出：p和q2. 知道p，q，相乘得出：n
3. 知道e，p，q，通过欧几里得算法得出：d 
4. 知道c，d，n，通过pow方法算出：m
5. 知道m，e，n，通过pow可以得出: c        
6. 多组加密，e为65537，n很大，可以采用公约数模数分解 
7. 知道e是3，密文前面的的问候语众所周知，或者p和q知道了一部分，或者知道一部分明文: https://cocalc.com/projects?session=1635902259454
8. 果e很大，远远超过65537，那么基本就可以确定是Wiener :Durfee Attack.py
9. 有两组及以上的RSA加密过程，而且其中两次的m和n都是相同的（或者说是已知1个n，但是有多个c、e对），那么same_n_sttack方法可以通过计算直接计算出m :共模攻击      
10. 多次选择的加密指数较低（这里可以取3也可以取其他较小的素数），而且这几次加密过程，加密的信息都是相同的 : 广播攻击      
11. 当使用同一公钥对两个具有某种线性关系的消息M1和M2进行加密，并将加密后的消息C1、C2发送时，我们就可以获得对应的消息M1与M2：消息攻击
12. 使用相同的k，即r也相同，如果知道两个不同的消息利用相同的r，就可以进行攻击了
13. secret+message为明文的情况下，可以进行哈希长度扩展攻击    
14. 可以直接使用CTF-RSA-tool计算
其他：
ab = 1 mod n：a乘以b的积除以n余数为1 称a和b是关于n的乘法逆元
扩展欧几里得算法：给予二整数 a 与 b, 必存在有整数 x 与 y 使得ax + by = gcd(a,b)，比如gcd(42,98) = 14 ，那么存在gcd(3 * 42 ， 5 * 98）= 14 ，
'''
