from Crypto.Cipher import DES
import re
import os

def hashing():
    if os.path.getsize("/home/piotr/PycharmProjects/rt/plaintextes.txt") ==0:
        plain_text=b'cokolwiek_co_ma_24_znaki'
    else:
        with open('plaintextes.txt', 'rb') as file:
            plain_text=file.read()[-8:]
    c=0
    while c<5:
        my_hash=minihash(plain_text)
        minireduction(my_hash)
        c+=1
    encrypted=my_hash
    with open('hashes.txt', 'ab') as hashfile:
        hashfile.write(encrypted)
    with open('plaintextes.txt', 'ab') as passes:
        passes.write(plain_text)

def reduction():
    if os.path.getsize("/home/piotr/PycharmProjects/rt/hashes.txt") ==0:
        reduced="sth"
    else:
        with open('hashes.txt', 'rb') as hashfile:
            hash=hashfile.read()[-8:]
        print(hash)
        reduced=minireduction(hash)
    with open('plaintextes.txt', 'ab') as passes:
        passes.write(bytes(reduced, 'utf8'))

def minihash(plain_text):
    key = b'key12345'
    iv = b"\0\0\0\0\0\0\0\0"
    cipher = DES.new(key, DES.MODE_CBC, iv)
    encrypted = cipher.encrypt(plain_text)
    return encrypted

def minireduction(hash):
    return "".join(re.findall("[a-zA-Z0-9]+", str(hash)))[1:4]
