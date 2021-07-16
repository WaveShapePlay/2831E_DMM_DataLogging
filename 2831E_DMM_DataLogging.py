import serial
import time

ser = serial.Serial("COM3")
ser.timeout = 3

class Scpi_CMD():

    def __init__(self):
        self.current_index = 0
        self.dataDict = {}
        
    def getInfo(self):
        ser.write(b'*idn?\n')
        print(ser.readline())

    def mode_volt_dc(self): 
        ser.write(b'func volt:dc\n')
        ser.write(b'volt:dc:rang:auto 1\n')
        time.sleep(1)
        ser.write(b'fetch?\n')
        print(ser.readline())
        ser.write(b'fetch?\n')
        print(ser.readline())

    def getScpiData(self):
        ser.write(b'fetch?\n')
        self.val = ser.readline()
        if self.val != b'fetch?\n':
            self.val = self.val.decode()
            self.val = str(self.val)
            self.val = self.val[0:-3]
            self.current_index += 1
            self.formatDataDict()
            data = self.formatDataDict()
            #print(data)

    def formatDataDict(self):
        self.dataDict[self.current_index] = self.val
        return self.dataDict
        
    
scpi = Scpi_CMD()
scpi.getInfo()
scpi.mode_volt_dc()
numSamples = 20

for i in range(0,numSamples):
    scpi.getScpiData()

print(scpi.dataDict)

