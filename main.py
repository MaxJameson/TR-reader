import record
import threading
import os
import json
import createrThread as CT
from datetime import datetime, timedelta

threads = []
recordList = []
recordLock = threading.Lock()

timeFormat = "%H:%M:%S"
testTimes = []

errors = {}

results={
    "PASS" : 0,
    "FAIL" : 0,
    "BLOCKED" : 0,
}

files = os.listdir('records')


for i in os.listdir('records'):
    thread = CT.createThread(recordList,recordLock,f"Records\\{i}")
    thread.start()
    threads.append(thread)

for i in threads:
    i.join()

for i in recordList:
    if type(i) == record.testRecord:
        results[i.result] += 1
        hms = i.runTime.split(':')
        testTimes.append(timedelta(hours=int(hms[0]),minutes=int(hms[1]),seconds=int(hms[2])))
    else:
        errors[i[0]] = i[1]

    

averageTime = sum(testTimes,timedelta())/len(testTimes)

print(f"Results: \n {results}\n")


print(f"Average Time: \n {averageTime}\n")

print("Errors:")
for i in errors:
    print(f"File: {i}, Error: {errors[i]}")

