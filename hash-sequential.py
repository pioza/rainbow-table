from Crypto.Cipher import DES
import re
import threading
import time



def hashing(plain_text,threadName, counter):
    while counter:
        if exitFlag:
            threadName.exit()
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
        #print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


def reduction(hash):
    hash = "A1s2xc3cccBF23FFseF"
    word1 = "".join(re.findall("[a-z]+", hash)) #tylko znaki male
    #word1 = "".join(re.findall("[a-zA-Z]+", hash)) #dla znakow duzych i malych
    word2 = word1[:5]
    print(word1, word2)
    return word2



exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      hashing(b'cokolwiek_co_ma_24_znaki', self.name, 5)
      print ("Exiting " + self.name)




# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)


# Start new Threads
thread1.start()
thread2.start()

print ("Exiting Main Thread")
