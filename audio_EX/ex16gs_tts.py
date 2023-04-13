#tts01.py
from gtts import gTTS
text = "Hello, æ»≥Á«œººø‰."

tts = gTTS(text=text, lang='ko')
tts.save('hi.mp3')