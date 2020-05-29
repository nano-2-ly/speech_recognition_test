import pyaudio
from pygame import mixer
import wave
import json
import STT
import socket

class IOT():
    def __init__(self):
        self.HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
        self.PORT = 8005           # Arbitrary non-privileged port
        
    def turn_on_light(self, light_ID):
        if light_ID == 'room':
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.HOST,self.PORT))
            s.sendall('room_light_on'.encode('utf-8'))
            s.close()
            
    
    def turn_off_light(self, light_ID):
        if light_ID == 'room':
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.HOST,self.PORT))
            s.sendall('room_light_off'.encode('utf-8'))
            s.close()
            

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "./sounds/output.wav"


p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


mixer.init()




print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

command = json.loads(STT.naver_STT('./sounds/output.wav'))['text']
print(command)

if '불 켜' in command : 
    IOT().turn_on_light('room')

elif '불 꺼' in command : 
    IOT().turn_off_light('room')
