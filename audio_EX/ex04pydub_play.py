from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_file('text.wav', format = "wav")
# song = Audiosegment.from_wav('text.wav')

play(song)