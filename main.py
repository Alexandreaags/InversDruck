#InversDruck Project. Fraunhofer IPK
#By Tássio Neves and Alexandre Adonai

from machine import Pin, ADC
from utime import sleep

p_Vel = Pin(16, Pin.OUT)
p_Dir = Pin(17, Pin.OUT)

p_Vel = 0
p_Dir = 0

p_force = Pin(26, Pin.IN)



while 1:
    val = adc.read_u16()
    val = 3.3/65535*val
    val = val/3.3*100
    print(val)
    sleep(.1)