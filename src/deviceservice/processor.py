from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport

import copy
import logging.config

LOG_CONFIG = {
    'version': 1,
    'formatters': {
        'detailed': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-15s %(levelname)-8s  %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'detailed',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'default',
            'mode': 'a',
            'formatter': 'detailed',
        },
    },
    'loggers': {
        'zeep.transports': {
            'level': 'DEBUG',
            #'propagate': True,
            'handlers': ['console', 'file'],
        },
        'device': {
            'level': 'INFO',
            #'propagate': True,
            'handlers': ['console', 'file'],
        },
    }
}
REQUEST_TEMPLATE = {
    'submitter': {
        'channel': 'DIGITAL',
    },
    'DeviceList': {},
}

class DeviceService:
    def __init__(self, wsdlUrl,inputFileName, logfileName = 'deviceServiceDefault.log'):
        self.client = self.createClient(wsdlUrl)
        self.logfileName = logfileName #do not append ".log" to inputfilename
        self.inputFileName = inputFileName # THis is just for logging, do not read this file directly.
        log_config = copy.deepcopy(LOG_CONFIG)
        log_config['handlers']['file']['filename'] = logfileName
        logging.config.dictConfig(log_config)
        self.log = logging.getLogger('device')
        logging.getLogger('device').debug("init DeviceService with logfileName:", inputFileName)

    def createClient(self, wsdlurl):
        transport = Transport(cache=SqliteCache())
        client = Client(wsdl=wsdlurl, transport=transport)
        return client

    def lock(self,imeiSet):
        self.log.info("   Inter call LOCK:{},unLOCK:{}   for inputfile {}".format(len(imeiSet),0, self.inputFileName))
        self.processOp(imeiSet,"LockDevice")

    def unLock(self,imeiSet):
        self.log.info("   Inter call LOCK:{},unLOCK:{}   for inputfile {}".format(0,len(imeiSet), self.inputFileName))
        self.processOp(imeiSet,"UnlockDevice")

    def processOp(self,imeiSet, operationName):
        if len(imeiSet) == 0 :
            return
        #if len(imeiSet) == 100 :
         #   self.log.info("   Intermediate call {}:{} for inputfile {}".format(operationName,len(imeiSet),self.inputFileName))
        opFunction = getattr(self.client.service, operationName)
        try:
            response = opFunction(**self.buildDeviceList(imeiSet))
            # response = self.client.service.UnlockDevice(**self.buildDeviceList(imeiSet))
        except Exception as e:
            self.log.error("SOAP Service not reachable :" + str(e))
            exit(-1)
        self.processResponse(response)

    def buildDeviceList(self,imeiSet):
        deviceList = []
        for imei in imeiSet:
            myDevice = {}
            myDevice['imei'] = imei
            deviceList.append(myDevice)
        deviceListDict =  {'Device': deviceList}
        req = copy.deepcopy(REQUEST_TEMPLATE)
        req['DeviceList'] = deviceListDict
        return req

    def process(self, lockSet, unlockSet):
        self.log.info("Finalize call LOCK:{},unLOCK:{}   for inputfile {}".format(len(lockSet),len(unlockSet), self.inputFileName))
        self.processOp(lockSet,"LockDevice")
        self.processOp(unlockSet,"UnlockDevice")

    def processResponse(self, response):
        soapCallStatus = response['result'][ 'status']
        #self.log.info("SOAP Response status " + soapCallStatus)
        if "OK" in soapCallStatus:
            devices = response['DeviceList'][ 'Device']
            #print("IMEI|ISSUCCESS|STATE|DETAIL")
            for device in devices:
                self.log.debug('{}|{}|{}|{}'.format(device['imei'], device['stateUpdateStatus'] == 'Success', device['carrierLockState'], device['description']))
        else:
            self.log.error("Service call failed, check logs")
