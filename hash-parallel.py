import threading
import time
from Crypto.Cipher import DES
import re
import os


class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print ("Starting " + self.name)
        # zlapanie zamka - synchronizacja
        threadLock.acquire()
        #
        # TU SB ROBIMY
        #print_time(self.name, 3)
        hashing()
        reduction()
        #KONIEC WATKU
        # wypuszczenie zamka - dla innych watkow
        threadLock.release()

def print_time(threadName, counter):
    while counter:
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

### WKLEJONE



def hashing(counter):
    key = b'key12345'
    iv = b"\0\0\0\0\0\0\0\0"
    if os.path.getsize("/home/piotr/PycharmProjects/rt/plaintextes.txt") ==0:
        plain_text=b'cokolwiek_co_ma_24_znaki'
    else:
        with open('plaintextes.txt', 'rb') as file:
            plain_text=file.read()[-8:]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    encrypted = cipher.encrypt(plain_text)
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
        reduced="".join(re.findall("[a-zA-Z0-9]+", str(hash)))[1:4]
        #print(reduced)
    with open('plaintextes.txt', 'ab') as passes:
        passes.write(bytes(reduced, 'utf8'))





#####




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
print ("Exiting Main Thread")
