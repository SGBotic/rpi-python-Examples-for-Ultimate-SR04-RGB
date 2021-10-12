# python code for SGBotic Ultimate SR04 RGB
# This code is to set the RGB inside the transducers 
# to red -> green -> blue, then repeat

# run on Raspberry Pi, Python3

from smbus import SMBus
import time

# Create a new I2C bus
i2cbus = SMBus(1)

i2cAddr = 0x60

redRegister = 0x02
greeRegister = 0x03
blueRegister = 0x04

light_intensity_full = 0xFF
light_intensity_zero = 0x00

#turns off LEDs
def ledOff():
    i2cbus.write_byte_data(i2cAddr, redRegister,light_intensity_zero)
    i2cbus.write_byte_data(i2cAddr, greeRegister,light_intensity_zero)
    i2cbus.write_byte_data(i2cAddr, blueRegister,light_intensity_zero)
    
while True:
    ledOff()
    #red led on
    i2cbus.write_byte_data(i2cAddr, redRegister,light_intensity_full)
    #Pause 1s
    time.sleep(1)
    
    ledOff()
    # green led on
    i2cbus.write_byte_data(i2cAddr, greeRegister,light_intensity_full)
    time.sleep(1)
    
    ledOff()
    #blue led on
    i2cbus.write_byte_data(i2cAddr, blueRegister,light_intensity_full)
    time.sleep(1)
