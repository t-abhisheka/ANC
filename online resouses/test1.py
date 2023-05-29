import time
import sys
import numpy as np

import pyaudio

DURATION = 5  # seconds

def callback(in_data, frame_count, time_info, status):
    data = np.frombuffer(in_data, dtype=np.float32)
    processed_data = data * 0.5
    out_data = processed_data.tobytes()
    return (out_data, pyaudio.paContinue)

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(2),
                channels=1 if sys.platform == 'darwin' else 2,
                rate=44100,
                input=True,
                output=True,
                stream_callback=callback)

start = time.time()
while stream.is_active() and (time.time() - start) < DURATION:
    time.sleep(0.1)

stream.close()
p.terminate()