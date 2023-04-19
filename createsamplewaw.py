import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

sr = 44100
freq = 200
length = 1.0

t = np.arange(0,length, 1.0/sr) 
x = np.pi*2*freq*t 

#sin wave
#signal = np.sin(x)

#triangle wave
#signal = np.abs((x/np.pi-0.5)%2-1)*2-1

#square wave
#signal = np.where(x/np.pi%2>1,-1,1)

#sawtooth wave
#signal = -((x/np.pi)%2)+1

#noice
def norm(data):
    min_v = min(data)
    max_v = max(data)
    offset = min_v+max_v
    data = data + (offset/2)
    data = np.array([((x-min_v)/(max_v-min_v))for x in data])*2.0-1
    return data*((max_v/min_v)*-1)

signal = norm(np.random.random(int(length*sr))) 

signal *= 32767  
signal = np.int16(signal)
wavfile.write("file.wav",sr,signal)