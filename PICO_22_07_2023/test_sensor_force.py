#InversDruck Project. Fraunhofer IPK
#By Tássio Neves and Alexandre Adonai

from machine import Pin, ADC
from utime import sleep

p_Vel = Pin(16, Pin.OUT)
p_Dir = Pin(17, Pin.OUT)

p_Vel = 0
p_Dir = 0

p_force = Pin(26, Pin.IN)
adc = ADC(p_force)

x=0
val_t=0


while 1:
    for x in range(0,10):
        val = adc.read_u16()
        val = 3.3/65535*val
#        val = val/3.3*100
        val_t = val_t + val
    val_t = val_t / 10
    print(val_t)
    val_t = 0
    sleep(.1)