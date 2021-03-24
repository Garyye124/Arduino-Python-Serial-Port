import serial
import numpy as np
import time

#UART CONFIG
BAUD = 2000000 
PORT = '/dev/ttyUSB0'

#Open Serial port
ser = serial.Serial(port = PORT , baudrate = BAUD)
time.sleep(3)

#Get Data
while True:
    Nbytes = 0
    DataValue = 0
    Nerrors =0
    ser.reset_input_buffer()
    while(ser.in_waiting > 0):
        pass
    LastTick = time.time()
    while ((time.time() - LastTick) < 0.5):
        NBuffBytes = ser.in_waiting
        if(NBuffBytes > 0):
            LastTick = time.time()
            Nbytes = Nbytes + NBuffBytes
            #get serial data
            Data = np.frombuffer(ser.read(NBuffBytes),dtype=np.uint8)
            #check data
            for DataIdx in range(0,Data.size):
                if(Data[DataIdx] != DataValue):
                    Nerrors = Nerrors+1
                DataValue = DataValue +1
                if(DataValue>255):
                    DataValue = 0
            #print results
    print('Valid Bytes Received :', round(((Nbytes-Nerrors)/4000)*100),'%')
ser.close()       
