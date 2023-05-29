import pyaudio
import numpy as np

# Define the phase shift in radians
phase_shift = np.pi / 2

# Define the audio stream parameters
sample_rate = 44100
buffer_size = 1024

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open a stream with the specified parameters
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=sample_rate,
                input=True,
                output=True,
                frames_per_buffer=buffer_size)

# Start the stream
stream.start_stream()

# Loop infinitely, processing audio data as it arrives
while True:
    # Read audio data from the stream
    data = stream.read(buffer_size)

    # Convert the audio data to a numpy array
    audio = np.frombuffer(data, dtype=np.float32)

    # Apply the phase shift to the audio signal
    audio = np.roll(audio, int(phase_shift * sample_rate / (2 * np.pi)))

    # Convert the audio signal back to bytes
    data = audio.tobytes()

    # Write the audio data to the output stream
    stream.write(data)
