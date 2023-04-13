# wav -> mp3
from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file('text.wav', format="wav")
sound.export('converted.mp3', format="mp3", codec="libmp3lame")