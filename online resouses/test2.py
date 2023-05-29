import pyaudio
import time
import numpy as np
import scipy.signal as signal
WIDTH = 2
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()
b,a=signal.iirdesign(0.03,0.07,5,40)
fulldata = np.array([])

def callback(in_data, frame_count, time_info, flag):
    global b,a,fulldata 
    audio_data = np.fromstring(in_data, dtype=np.float32)
    audio_data = signal.filtfilt(b,a,audio_data,padlen=200).astype(np.float32).tostring()
    fulldata = np.append(fulldata,audio_data)
    return (audio_data, pyaudio.paContinue)

stream = p.open(format=pyaudio.paFloat32,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                input=True,
                stream_callback=callback)

stream.start_stream()

while stream.is_active():
    time.sleep(5)
    stream.stop_stream()
stream.close()

p.terminate()