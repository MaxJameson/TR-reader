import threading
from queue import Queue
import record
import json

class createThread(threading.Thread):
    def __init__(self,rList,rLock,file):
        threading.Thread.__init__(self)
        self.file = file
        self.list = rList
        self.lock = rLock

    def run(self):
        try:
            with open (self.file) as TR:
                data = json.load(TR)
                try:
                    recordObj = record.testRecord(data)
                    with self.lock:
                        self.list.append(recordObj)
                except Exception as e:
                    with self.lock:
                        self.list.append([self.file.split('\\')[1],e])

        except Exception as e:
                with self.lock:
                    self.list.append([self.file.split('\\')[1],e])