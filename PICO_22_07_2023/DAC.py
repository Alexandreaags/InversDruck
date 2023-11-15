from machine import I2C, Pin
from mcp4725 import MCP4725, BUS_ADDRESS
from time import sleep 
#create a I2C bus
i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=100000) 
#sleep(.5)
#create the MCP4725 driver
dac=MCP4725(i2c,BUS_ADDRESS[0])
sleep(.5)
dac.write(1000)
sleep(2)
x = dac.read()
print(x)