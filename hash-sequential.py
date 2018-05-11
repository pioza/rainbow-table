import pyDes
import re

def from_bytes (data, big_endian = False):
    if isinstance(data, str):
        data = bytearray(data)
    if big_endian:
        data = reversed(data)
    num = 0
    for offset, byte in enumerate(data):
        num += byte << (offset * 8)
    return num


def hash(plain_text):
    k = pyDes.des(b"DESCRYPT", pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    d = k.encrypt(plain_text)
    print ("Encrypted: %r" % d)
    print ("Decrypted: %r" % k.decrypt(d))
    #assert k.decrypt(d) == plain_text
    d_str=str(d)
    print(from_bytes(d))
    print("nr 1")
    for e in from_bytes(d):
        print(chr(e), end=' ')
    print("\nnr 2")
    for e in d:
        print(e, end=' ')
    print("\nnr 3")
    for e in d:
        print(chr(e), end=' ')
    #with open('dictionary.txt', 'a') as dict:
        #dict.write(plain_text+'   '+str(from_bytes(k.decrypt(d)))+'\n')


def reduction(hash):
    hash="A123BF23FFsF"
    word1 = "".join(re.findall("[a-zA-Z]+", hash))
    word2 = word1[:3]
    print(word1, word2)
    return word2


hash("elo")
'''
data = b"pozdro"
k = pyDes.des("aaaaaaaa", pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
d = k.encrypt(data)
print ("Encrypted: %r" % d)
print ("Decrypted: %r" % k.decrypt(d))
assert k.decrypt(d) == data
'''


