import RPi.GPIO as GPIO
import time
import serial
import sys
GPIO.setwarnings(False)

class SerialPass:
    
    def __init__(self,portname='/dev/ttyAMA0',baudrate = 115200, relay_0=21,relay_1=22,relay_2=23,relay_3=24,opto_0=17,opto_1=18,opto_2=19,opto_3=20):
        self.portname=portname
        self.baudrate=baudrate
        self.ser=serial.Serial(port = portname,baudrate = baudrate,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
        self.relay_0 = relay_0
        self.relay_1 = relay_1
        self.relay_2 = relay_2
        self.relay_3 = relay_3
        self.opto_0 = opto_0
        self.opto_1 = opto_1
        self.opto_2 = opto_2
        self.opto_3 = opto_3
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(relay_0,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(relay_1,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(relay_2,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(relay_3,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(opto_0,GPIO.IN)
        GPIO.setup(opto_1,GPIO.IN)
        GPIO.setup(opto_2,GPIO.IN)
        GPIO.setup(opto_3,GPIO.IN)
        
    def relay_set(self , pin , value):
        if(pin == 0):
            GPIO.output(self.relay_0,value)
        elif(pin == 1):
            GPIO.output(self.relay_1,value)
        elif(pin == 2):
            GPIO.output(self.relay_2,value)
        elif(pin == 3):
            GPIO.output(self.relay_3,value)
            
    
    def opto_status(self,pin):
        if(pin == 0):
            if(GPIO.input(self.opto_0) == 0):
                return 1
            else:
                return 0
        elif(pin == 1):
            if(GPIO.input(self.opto_1) == 0):
                return 1
            else:
                return 0
        elif(pin == 2):
            if(GPIO.input(self.opto_2) == 0):
                return 1
            else:
                return 0
        elif(pin == 3):
            if(GPIO.input(self.opto_3) == 0):
                return 1
            else:
                return 0
            
    def serial_write(self,data):
        
        self.ser.write(data)
    def serial_read(self): 
        rx_data = self.ser.read()
        data_left = self.ser.inWaiting()
        if data_left > 0:
            rx_data += self.ser.read(data_left)
        return rx_data

try:     
    obj=SerialPass()
    obj.relay_set(0,0)
    print(obj.opto_status(3))
    obj.serial_write(b'hello')
    print(obj.serial_read())

except Exception as e:
    print(e)