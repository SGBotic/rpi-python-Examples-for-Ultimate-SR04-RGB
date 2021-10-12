# example code for SGBotic Ultimate SR04 RGB
# this code is to measure distance of an obstacle

# run on Raspberry Pi, Python3

from smbus import SMBus
import time

# Create a new I2C bus
i2cbus = SMBus(1)

#define I2C address of the sensor
i2cAddr = 0x60

triggerRegister = 0x01
triggerCmd = 0x01
result_cm_register = 0x0A

#convert byte array to integer
def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result
    
data = bytes([2])

while True:
    #trigger the measurement
    i2cbus.write_byte_data(i2cAddr, triggerRegister, triggerCmd)
    
    #wait for sound wave to return
    time.sleep(1/100000)
    
    #read back measured distance
    data = i2cbus.read_i2c_block_data(i2cAddr, result_cm_register, 2)
    
    #convert returned data from byte array to integer
    dist = bytes_to_int(data)
    
    #print to serial
    print("distance in cm: %s" % dist)
    
    #wait for 100ms before repeat next cycle
    time.sleep(1)
