import pyaudio
import wave

# Set the recording parameters
chunk = 1024  # number of samples per frame
format = pyaudio.paInt16  # audio format
channels = 1  # mono
rate = 44100  # sample rate
record_seconds = 5  # duration of the recording in seconds
filename = "output.wav"  # name of the output file

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open the microphone for recording
stream = audio.open(format=format, channels=channels, rate=rate,
                    input=True, frames_per_buffer=chunk)

# Create a buffer to store the recorded data
frames = []

# Record audio for the specified duration
for i in range(0, int(rate / chunk * record_seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop the recording
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(audio.get_sample_size(format))
wf.setframerate(rate)
wf.writeframes(b''.join(frames))
wf.close()
