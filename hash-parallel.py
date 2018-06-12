import threading
from Crypto.Cipher import DES
import re
import os


class myThread (threading.Thread): #nadpisanie klasy Thread - potrzebne do watkow
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        # zlapanie zamka - synchronizacja
        threadLock.acquire()
        hashing()
        reduction()
        # wypuszczenie zamka - dla innych watkow
        threadLock.release()

def hashing():
    if os.path.getsize("/home/piotr/PycharmProjects/rt/plaintextes.txt") ==0: # sprawdzenie czy plik jest pusty
        plain_text=b'cokolwiek_co_ma_24_znaki'
    else:
        with open('plaintextes.txt', 'rb') as file:
            plain_text=file.read()[-8:]
    c=0
    while c<5: #hashowanie i redukcja - tutaj przyjete 5 razy
        my_hash=minihash(plain_text)
        minireduction(my_hash)
        c+=1
    encrypted=my_hash
    with open('hashes.txt', 'ab') as hashfile: #zapis do pliku z hashami
        hashfile.write(encrypted)
    with open('plaintextes.txt', 'ab') as passes: #zapis do pliku z haslami
        passes.write(plain_text)

def reduction():
    if os.path.getsize("/home/piotr/PycharmProjects/rt/hashes.txt") ==0: #sprawdzenie czy plik nie jest pusty
        reduced="sth"
    else:
        with open('hashes.txt', 'rb') as hashfile: #pobieramy hash do redukcji
            hash=hashfile.read()[-8:]
        reduced=minireduction(hash)
    with open('plaintextes.txt', 'ab') as passes: # dodajemy nowye tekst do zahashowania
        passes.write(bytes(reduced, 'utf8'))

def minihash(plain_text): #jej jedynym zadaniem jest wykonywanie hashy
    key = b'key12345'
    iv = b"\0\0\0\0\0\0\0\0"
    cipher = DES.new(key, DES.MODE_CBC, iv)
    encrypted = cipher.encrypt(plain_text)
    return encrypted

def minireduction(hash): ##jej jedynym zadaniem jest redukcja
    return "".join(re.findall("[a-zA-Z0-9]+", str(hash)))[1:4]

threadLock = threading.Lock()
threads = []

# tworzenie nowych watkow
thread1 = myThread(1, "Thread-1")
thread2 = myThread(2, "Thread-2")
thread3 = myThread(3, "Thread-3")
thread4 = myThread(4, "Thread-4")
thread5 = myThread(5, "Thread-5")
# zaczynanie watkow
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

# dodanie watkow do listy
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)
threads.append(thread5)

# czekanie na zakonczenie watkow
for t in threads:
    t.join()
print ("Program finished")
