#!/usr/bin/python3

import fileinput
from deviceservice.parser import *
from deviceservice.util import *
import configparser
import os,sys
parser = configparser.ConfigParser()
#parser.read('/apps/Unlock/Source/app.conf')
parser.read('app.conf')
wsdlUrl = parser.get(parser.get('DEFAULT','DEPLOY_ENV'), 'soapUrl');

INVENTORY_PARSER = InventoryParser()
RMA_PARSER =  RmaParser()
B2B_PARSER = B2bRmaParser()

with fileinput.input() as pipeInput:
    #assert isUrlAccessible(wsdlUrl)

    for file2parse in pipeInput:
        file2parse = file2parse.strip()
        assert os.path.exists(file2parse), "Fatal: File does not exist. Make sure the shell script is using:  ls -d <basedir>/inbound/*"
        inputDir = os.path.dirname(file2parse)
        assert inputDir.endswith("Inbound") ,"Input files must be in folder ending with <basedir>/Inbound"
        logDir = inputDir.replace("Inbound", "logs")
        doneDir = inputDir.replace("Inbound", "Outbound")
        if not os.path.exists(logDir):
            os.mkdir(logDir)
        if not os.path.exists(doneDir):
            os.mkdir(doneDir)
        parser = None
        if('INV_TRANSACTION' in file2parse):
            parser = INVENTORY_PARSER
        elif('I020_RMACRT' in file2parse):
            parser = RMA_PARSER
        elif('B2BRMAnotification' in file2parse):
            parser = B2B_PARSER
        else:
            continue
        if(parser != None):
            printStream("FILE||{}".format(file2parse))
            parser.parse(file2parse)
            parser = None
