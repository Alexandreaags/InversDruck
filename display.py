# Code used to display some Raspberry Pi Pico data on PC

import serial
import time
import numpy as np
import matplotlib.pyplot as plt

az = []

samples = 1000

### open a serial connection
pico = serial.Serial("COM6", 115200)

tempo_inicial = time.time()

### get Acceleration array
for i in range(0,samples):
    inst_acc_z = str(pico.readline())
    inst_acc_z = float(inst_acc_z[2:-6])
    print(inst_acc_z)
    az.append(inst_acc_z)

tempo_final = time.time()

np_az = np.array(az)

print(1000/(tempo_final - tempo_inicial))

plt.plot(range(len(np_az)), np_az)
plt.xlabel('Samples')
plt.ylabel('Acceleretion on Z [g]')
plt.ylim(-5, 5)

plt.show()