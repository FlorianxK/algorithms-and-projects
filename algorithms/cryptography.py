from typing import *
from ctypes import *

class Encrypt:

    def caesarEncrypt(text:str,steps:int) -> str:
        res = ""
        c:str
        for c in text:
            if c.isupper():
                res += chr( (ord(c)+steps-65)%26+65 )
            else:
                res += chr( (ord(c)+steps-97)%26+97 )
        return res

    def teaEncrypt(number:int,key:int):
        y = c_uint32(number[0])
        z = c_uint32(number[1])
        sum = c_uint32(0)
        delta = 0x9e3779b9
        n = 32
        w = [0,0]

        while n > 0:
            sum.value += delta
            y.value += (z.value << 4) + key[0]^z.value + sum.value^(z.value >> 5) + key[1]
            z.value += (y.value << 4) + key[2]^y.value + sum.value^(y.value >> 5) + key[3]
            n -= 1

        w[0] = y.value
        w[1] = z.value
        return w

class Decrypt:

    def caesarDecrypt(text:str,steps:int) -> str:
        res = ""
        c:str
        for c in text:
            if c.isupper():
                res += chr( (ord(c)-steps-65)%26+65 )
            else:
                res += chr( (ord(c)-steps-97)%26+97 )
        return res

    def teaDecrypt(number:int,key:int):
        y = c_uint32(number[0])
        z = c_uint32(number[1])
        sum = c_uint32(0xc6ef3720)
        delta = 0x9e3779b9
        n = 32
        w = [0,0]

        while n > 0:
            z.value -= (y.value << 4) + key[2]^y.value + sum.value^(y.value >> 5) + key[3]
            y.value -= (z.value << 4) + key[0]^z.value + sum.value^(z.value >> 5) + key[1]
            sum.value -= delta
            n -= 1

        w[0] = y.value
        w[1] = z.value
        return w

def main():
    text = "ATTACKATONCE"
    e = Encrypt.caesarEncrypt(text,4)
    print(e)
    d = Decrypt.caesarDecrypt(e,4)
    print(d)

    key = [1,2,3,4]
    values = [1385482522,639876499]
    e = Encrypt.teaEncrypt(values,key)
    print(e)
    d = Decrypt.teaDecrypt(e,key)
    print(d)
    
if __name__ == "__main__":
    main()