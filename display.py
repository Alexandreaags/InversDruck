# Code used to display some Raspberry Pi Pico data on PC

import serial
import time
import numpy as np
import matplotlib.pyplot as plt

az = []

samples = 5000
samples_array = []

### open a serial connection
pico = serial.Serial("COM6", 115200)

tempo_inicial = time.time()

### get Acceleration array
for i in range(0,samples):
    inst_acc_z = str(pico.readline())
    inst_acc_z = float(inst_acc_z[2:-6])
    print(inst_acc_z)
    az.append(inst_acc_z)
    samples_array.append(i)

tempo_final = time.time()

np_az = np.array(az)


print(len(samples_array))
print(5000/(tempo_final - tempo_inicial))

plt.plot(samples_array, np_az)
plt.xlabel('Samples')
plt.ylabel('Acceleretion on Z [g]')

plt.show()