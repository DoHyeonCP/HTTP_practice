# wav -> mp3(BytesIO)
from pydub import AudioSegment
from pydub.playback import play
import io
import requests

with open('text.wav', 'rb') as f:
	wavMem = io.BytesIO(f.read())

mp3Mem = io.BytesIO()
sound = AudioSegment.from_file(wavMem, format = "wav")
sound.export(mp3Mem, format = "mp3", codec = "libmp3lame")

print (mp3Mem.tell()) # 파일크기 출력
mp3Mem.seek(0)

song = AudioSegment.from_mp3(mp3Mem)
play(song)