import numpy as np
import pyaudio 

class callBacking:
    

    def callback(in_data, frame_count, time_info, status):
        data = stream.read(BUFFER_SIZE)
        audio = np.frombuffer(data, dtype=np.float32)
        audio = np.roll(audio, int(PHASESHIFT * SAMPLE_RATE / (2 * np.pi)))
        data = audio.tobytes()
        return (in_data, pyaudio.paContinue)