#!/bin/python36
import fileinput
from deviceservice.processor import DeviceService
import configparser

def finalizeServiceCall():
    global service
    #print("#### FINALIZE service for {}###".format(inputFileName))
    service.process(lockSet, unlockSet)
    service = None
    lockSet.clear()
    unlockSet.clear()
    doneFileName = inputFileName.replace("Inbound", "Outbound")
    import shutil
    shutil.move(inputFileName, doneFileName)  # use copy for local, use move in dev/qa/prod

parser = configparser.ConfigParser()
parser.read('/apps/Unlock/Source/app.conf')
# parser.read('app.conf')
wsdlUrl = parser.get(parser.get('DEFAULT','DEPLOY_ENV'), 'soapUrl');
with fileinput.input() as pipeInput:
    lockSet = [] #set() # changing to list - will have duplicates, as requested by Alison.
    unlockSet = [] #set()
    service = None
    inputFileName = None
    logFileName = None
    for streamToken in pipeInput:
        #print(streamToken.strip())
        (key,value) = streamToken.strip().split('||')
        #print("kv:({},{}):".format(key,value))

        if('FILE' in key):
            if service != None :
                #action = Inbound("About to run service, Press ENTER").upper()
                finalizeServiceCall()

            inputFileName = value
            logFileName = inputFileName.replace("Inbound", "logs")+".log"
            #print("#### INTIALIZE service for {}###".format(logFileName))
            #print("initalize DeviceService(path)")
            service = DeviceService(wsdlUrl, inputFileName, logFileName)
        elif ('UNLOCK' in key and service != None):
            #unlockSet.add(value)
            unlockSet.append(value)
            if len(unlockSet)== 100:
                #print("calling unlockMax:{} - intermediate".format(len(unlockSet)))
                service.unLock(unlockSet)
                unlockSet.clear()
        elif ('LOCK' in key and service != None):
            # lockSet.add(value)
            lockSet.append(value)
            if len(lockSet)== 100:
                #print("calling lockMax:{} - intermediate".format(len(lockSet)))
                service.lock(lockSet)
                lockSet.clear()
        else:
            print("Invalid state. Likely attempt to stream without file. Only streaming of File-Paths in a directory is allowed")
            continue
if service != None: # The last service
    finalizeServiceCall()
