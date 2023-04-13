import io
import queue
import sounddevice as sd
import soundfile as sf
import sys

samplerate = 44100
channels = 1
sd.default.sampleraute = samplerate
sd.default.channels = channels

q = queue.Queue()
recMem = io.ButesIO()

#���� �����尡 �ϴ� ��
def callback(indata, frames, time, status):
	if status:
		print(status, file = sys.stderr)
	q.put(indata.copy()) # ���� ������ ť�� �߰�

try:
	with sf.SoundFile(recMem, mode = 'x', format = 'wav',
										samplerate = samplerate, channels = channels) as file:
		with sd.InputStream(callback=callback):
			print('#' * 80)
			print('press Ctrl+C to stop the recording')
			print('#' * 80)
			while True:
				# ť�� ���� �����Ͱ� �ִٸ� �����Ͽ� ���Ͽ� ���
				file.write(q.get())

except KeyboardInterrupt:
	print(recMem.tell())
	# �Ϸ� ó��
	print('\nRecording finished: ')
except Exception as e:
	print(e)