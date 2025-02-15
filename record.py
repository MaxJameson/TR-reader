import json

class testRecord():

    def __init__(self,record):
        self.testName = record['testName'].upper()
        self.stepCount = record['stepCount']
        self.result = record['result'].upper()
        self.checkResult()
        self.runTime = record['runTime']

    def checkResult(self):
        if 'PASS' in self.result:
            self.result = 'PASS'
        elif 'FAIL' in self.result:
            self.result = 'FAIL' 
        elif 'BLOCKED' in self.result:  
            self.result = 'BLOCKED'
        else:
            raise Exception(f"Invalid result type: {self.result}")