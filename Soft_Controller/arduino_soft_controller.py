from time import sleep
from machine import Pin, I2C
from scales import Scales
from mcp4725 import MCP4725, BUS_ADDRESS

#Setting up load cell
load_cell = Scales(d_out=3, pd_sck=2)

#Setting up DAC
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)
dac = MCP4725(i2c,BUS_ADDRESS[0])
dac.write(0)

#Force Parameters
lowest_force = 20
target_force_lower_limit = 40
target_force_higher_limit = 60
highest_force = 100

#Output Bits Parameters
idle_bit = 0
fastest_down_bit = 400
middle_bit = 2200
fastest_up_bit = 4000

#Taring the load cell
load_cell.tare()

#########################################################################
# Bits Mapping
# MCP4725 DAC works with 12 bits, so 4096 bits
# 0 for idle -------------------------------- 0V
# 400 for fastest velocity down ------------- 0,488V
# From 400 to 2200 for variable speed down -- 0,488V to 2,929V
# From 2200 to 4000 for variable speed up --- 2,929V to 4,882V
# 4000 for fastest velocity up -------------- 4,882V
#########################################################################

while True:
    load_cell.measure_force()
    
    #Go down at the fastest velocity
    if load_cell.force <= lowest_force:
        output = fastest_down_bit
        dac.write(output)

    #Go down at a variable speed based on the force input
    elif load_cell.force > lowest_force and load_cell.force <= target_force_lower_limit:
        
        #Percentage of velocity to be applied
        output =  (load_cell.force - lowest_force)/(target_force_lower_limit - lowest_force)

        #Velocity bit to be outputed  
        output = output * (middle_bit - fastest_down_bit) + fastest_down_bit

        dac.write(int(output))

    #Stay stopped in the idle
    elif load_cell.force > target_force_lower_limit and load_cell.force <= target_force_higher_limit:
        output = idle_bit
        dac.write(output)

    #Go up at a variable speed based on the force input
    elif load_cell.force > target_force_higher_limit and load_cell.force <= highest_force:
        
        #Percentage of velocity to be applied
        output = (load_cell.force - target_force_lower_limit)/(target_force_higher_limit - target_force_lower_limit)
        
        output = output * (fastest_up_bit - middle_bit) + middle_bit

        dac.write(int(output))

    #Go up at the fastest velocity
    elif load_cell.force > highest_force:
        output = fastest_up_bit
        dac.write(output)

    print(load_cell.force, '  ', output)
