import threading, time,random

count = 0



class MyThread(threading.Thread):
    def __init__(self, threadName):
        super(MyThread, self).__init__(name=threadName)
        self.lock = lock


    def run(self):
        global count
        self.lock.acquire()
        for i in range(100):
            count += 1
            time.sleep(0.3)
            print(self.getName(), count)
        self.lock.release()

lock = threading.Lock()
for i in range(2):
    MyThread("MyThreadName:" + str(i)).start()
