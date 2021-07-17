import serial
import time

ser = serial.Serial("COM3")
ser.timeout = 3

class Scpi_CMD():

    def __init__(self):
        self.current_index = 0
        self.dataDict = {}
        self.numSamples = 10
    
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
            try:
                self.val = float(self.val)
                print(self.val)
                self.current_index += 1
                self.formatDataDict()
                data = self.formatDataDict()
            except:
                pass

    def formatDataDict(self):
        self.dataDict[self.current_index] = self.val
        return self.dataDict
        
    
scpi = Scpi_CMD()
scpi.getInfo()
scpi.mode_volt_dc()

while(scpi.current_index < scpi.numSamples):
    scpi.getScpiData()

print(scpi.dataDict)

