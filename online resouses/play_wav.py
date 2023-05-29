from pydub import AudioSegment
from pydub.playback import play

audio = AudioSegment.from_file_using_temporary_files()

play(audio)