#tts01.py
from gtts import gTTS
text = "Hello, �ȳ��ϼ���."

tts = gTTS(text=text, lang='ko')
tts.save('hi.mp3')