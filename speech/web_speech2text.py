import speech_recognition as sr
import webbrowser
#import speak

"""
from gtts import gTTS
import pyglet
import time, os


def tts(text, lang):
    file = gTTS(text = text, lang = lang)
    filename = '/tmp/temp.mp3'
    file.save(filename)

    music = pyglet.media.load(filename, streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(filename)"""



chrome_path = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --kiosk %s'

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
    print ('We reconiging your voice...!')
 
try:
    text = r.recognize_google(audio)
    print('Google thinks you said:\n' + text)
    lang = 'en'


    f_text = 'https://www.google.pl/search?q=' + text
    webbrowser.get(chrome_path).open(f_text)



 
except Exception as e:
    print (e)
