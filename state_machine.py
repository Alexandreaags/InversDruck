# from imu import MPU6050
from time import sleep
from machine import Pin, I2C
from scales import Scales
from mcp4725 import MCP4725, BUS_ADDRESS

balanca = Scales(d_out=3, pd_sck=2)

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)

dac=MCP4725(i2c,BUS_ADDRESS[0])


dac.write(0)


balanca.tare()
# threshold = 0.10

while True:
    #az = 0
    #for i in range(50):
    balanca.measure_force()
    # if balanca.force >= -1 and balanca.force <= 10:
    #     dac.write(2048)  # goes down fast

    # if balanca.force > 10 and balanca.force <= 20:
    #     dac.write(1536)  # goes down slower

    # if balanca.force > 20 and balanca.force <= 40:
    #     dac.write(1024)  # goes down slow 


    # if balanca.force > 40 and balanca.force <= 70:
    #     dac.write(0) # idle

    # if balanca.force > 70 and balanca.force <= 85:
    #     dac.write(2400) # goes up slower

    # if balanca.force > 85 and balanca.force <= 100:
    #     dac.write(3248) # goes up slow


    # if balanca.force > 100:
    #     dac.write(4095)  # goes up fast
    
    if balanca.force <= 40:
        dac.write(400)  # goes down fast

    if balanca.force > 40 and balanca.force <= 70:
        dac.write(0) # idle

    if balanca.force > 70 and balanca.force <= 85:
        dac.write(1120) # goes up slower

    if balanca.force > 85 and balanca.force <= 100:
        dac.write(1330) # goes up slow


    if balanca.force > 100:
        dac.write(1540)  # goes up fast
    
        # sleep(1.5)
        # dac.write(0)
    # az = imu.accel.z
    # az = abs(az)#/50
    # az = az - 1.13 
    

    print(balanca.force)
