import pyaudio
import numpy as np

# Define stream parameters
CHUNK = 102 # Number of samples in each chunk
FORMAT = pyaudio.paFloat32
CHANNELS = 1 # Mono audio input
RATE = 44100 # Sample rate of the input audio

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open input and output streams
stream_in = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
stream_out = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)


# Loop continuously, processing audio data in chunks
while True:
    # Read a chunk of audio data from the input stream
    chunk_in = stream_in.read(CHUNK)

    # Convert the audio data to a numpy array
    audio_data = np.frombuffer(chunk_in, dtype=np.float32)

    # Compute the root mean square (RMS) of the audio signal
    rms = np.sqrt(np.mean(np.square(audio_data)))

    # Convert the processed audio data back to bytes
    chunk_out = audio_data.tobytes()

    # Write the processed audio data to the output stream
    stream_out.write(chunk_out)
