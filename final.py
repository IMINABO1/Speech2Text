from time import sleep
import playsound as ps
import speech_recognition as sr
from gtts import gTTS

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said=""
        try:
            said=r.recognize_google(audio)
            print(said)
        except Exception as e:
            return "Exception: "+str(e)

    return said.lower()

def ready():
    return "Ready \nProcessing"
aza=None
a=True
while a==True:
    print(ready())
    liste=get_audio()
    aza=liste
    if aza=="quit"or"stop"or"terminate program"or"kill"or"close":
        print(aza)
        a=False
    else:
        continue
        print(liste)
sleep(10)
