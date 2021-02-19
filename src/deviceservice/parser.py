import sys, csv
csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)


def printStream(message):
    sys.stdout.write(str(message)+'\n') # use this for efficiency
    #print(message) # use this for debugging

class B2bRmaParser:
    def parse(self, filePath):
        with open(filePath, 'r') as file:
            for line in file:
                #print("line:",len(line),line)
                if len(line)>=50 and line.startswith('S'):
                    #print(row)
                    operation = 'LOCK'
                    imei = line[30:49]
                    printStream("{}||{}".format(operation, imei))

class InventoryParser:
    def parse(self, filePath):
        with open(filePath, 'r') as file:
            #next(fileName, None)
            csvReader = csv.reader(file, dialect='piper')
            #csvReader.next()
            for row in csvReader:
                if len(row) > 7 and row[0] == 'D' and (row[1] == '32' or row[1] == '42') and row[8] != '':
                    #print(row)
                    #service.log.debug("Is a Device: ",row['0_DEVICE'] == 'D') # DEVICE
                    operationCode = row[1] #Operation 1
                    if (operationCode == '32'):
                        operation = 'UNLOCK'
                    elif (operationCode == '42'):
                        operation = 'LOCK'
                    else :
                        continue
                    #service.log.debug("Operation: " +operation) #32=unlock, 42=lock
                    imei = row[8]
                    printStream("{}||{}".format(operation, imei))

class RmaParser:
    def parse(self, filePath):
        with open(filePath, 'r') as file:
            #next(fileName, None)
            csvReader = csv.reader(file, dialect='piper')
            #csvReader.next()
            for row in csvReader:
                #print(row)
                if len(row) > 4 and row[0] == 'S' and row[4] != '':
                    #print(row)
                    operation = 'LOCK'
                    imei = row[4]
                    printStream("{}||{}".format(operation, imei))


