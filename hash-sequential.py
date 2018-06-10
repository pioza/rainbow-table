from Crypto.Cipher import DES
import re

def hashing(plain_text):
    key = b'key12345' #wymyslamy klucz- musi miec 8 znakow
    iv = b"\0\0\0\0\0\0\0\0"#tu 8 bajtow
    cipher1 = DES.new(key, DES.MODE_CBC, iv)
    cipher2 = DES.new(key, DES.MODE_CBC, iv)
    #plain_text = b'cokolwiek_co_ma_24_znaki'#wymyslamy co ma byc zaszyfrowane

    encrypted = cipher1.encrypt(plain_text) #zaszyforwane
    decrypted = cipher2.decrypt(encrypted)#rozszyfrowane

    print(encrypted)
    print(decrypted)
    with open('hashes.txt', 'ab') as hashfile:
        hashfile.write(encrypted)
    with open('plaintextes.txt', 'a') as passes:
        passes.write(str(decrypted)[2:-1]+'\n')



def reduction(hash):
    hash = "A1s2xc3cccBF23FFseF"
    word1 = "".join(re.findall("[a-z]+", hash)) #tylko znaki male
    #word1 = "".join(re.findall("[a-zA-Z]+", hash)) #dla znakow duzych i malych
    word2 = word1[:5]
    print(word1, word2)
    return word2

hashing(b'cokolwiek_co_ma_24_znaki')
