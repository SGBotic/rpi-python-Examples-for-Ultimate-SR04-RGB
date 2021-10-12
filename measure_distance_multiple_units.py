# example code for SGBotic Ultimate SR04 RGB
# this code is to use three sensors to measure 
# distance of the obstacles

# run on Raspberry Pi, Python3

from smbus import SMBus
import time

# Create a new I2C bus
i2cbus = SMBus(1)

#define I2C address of the sensors
i2cAddr1 = 0x59
i2cAddr2 = 0x60
i2cAddr3 = 0x61

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
    #trigger sensor 1 to 3
    i2cbus.write_byte_data(i2cAddr1, triggerRegister, triggerCmd)
    i2cbus.write_byte_data(i2cAddr2, triggerRegister, triggerCmd)
    i2cbus.write_byte_data(i2cAddr3, triggerRegister, triggerCmd)
    
    # wait for sound wave to return
    time.sleep(1/100000)
    
    #read back measured distance of sensor 1
    data = i2cbus.read_i2c_block_data(i2cAddr1, result_cm_register, 2)
    #convert returned data from byte array to integer
    dist1 = bytes_to_int(data)
    
    #read back measured distance of sensor 2
    data = i2cbus.read_i2c_block_data(i2cAddr2, result_cm_register, 2)
    dist2 = bytes_to_int(data)
    
    #read back measured distance of sensor 3
    data = i2cbus.read_i2c_block_data(i2cAddr3, result_cm_register, 2)
    dist3 = bytes_to_int(data)
    
    #print to serial
    print("cm #1: %s  cm #2: %s  cm #3: %s" % (dist1,  dist2,  dist3))
    time.sleep(1)
