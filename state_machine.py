# from imu import MPU6050
from time import sleep
from machine import Pin, I2C
from scales import Scales
from mcp4725 import MCP4725, BUS_ADDRESS

balanca = Scales(d_out=3, pd_sck=2)

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)

dac=MCP4725(i2c,BUS_ADDRESS[0])


dac.write(0)

step_1 = 50 #idle
step_2 = 70 #idle
step_3 = 80
step_4 = 90
step_5 = 100
step_6 = 110
step_7 = 120
step_8 = 130
step_9 = 90
step_10 = 85
step_11 = 90




balanca.tare()
# threshold = 0.10

while True:
    #az = 0
    #for i in range(50):
    balanca.measure_force()
   
    
    if balanca.force <= step_1:
        output = 400
        dac.write(output)  # goes down fast

    if balanca.force > step_1 and balanca.force <= step_2:
        output = 0
        dac.write(output) # idle

    if balanca.force > step_2 and balanca.force <= step_3:
        output = 1120
        dac.write(output) # goes up slower

    if balanca.force > step_3 and balanca.force <= step_4:
        output = 1330
        dac.write(output) # goes up slower

    if balanca.force > step_4 and balanca.force <= step_5:
        output = 1540
        dac.write(output) # goes up slower

    if balanca.force > step_5 and balanca.force <= step_6:
        output = 1750
        dac.write(output) # goes up slower

    if balanca.force > step_7 and balanca.force <= step_8:
        output = 1960
        dac.write(output) # goes up slow

    if balanca.force > step_8:
        output = 2070
        dac.write(output)  # goes up fast
    
        # sleep(1.5)
        # dac.write(0)
    # az = imu.accel.z
    # az = abs(az)#/50
    # az = az - 1.13 
    

    print(balanca.force, '  ', output)
