#Module imports
import speech_recognition as sr
import pyaudio
import pyttsx3

import datetime
import time



#Variables
user = '' #Enter your name in the ''

hour = int(datetime.datetime.now().hour)
strTime = datetime.datetime.now().strftime("%H:%M")
date = datetime.datetime.now().strftime("%A:%B:%Y")

r = sr.Recognizer()



#Speech-recognition setup
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
#Taking the command
def command():
	with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            query = r.recognize_google(audio, language='en-gb')
            print(f"{user}: {query}\n")
        
        except Exception as e:
            print("Exception: " + str(e))
        
    return query



#Tells you the time of day (Morning, afternoon, evening, night) - when you open the script
def Welcome():
    if hour>=0 and hour<12:
        speak('Good morning ' + user)
    
    elif hour>=12 and hour<18:
        speak('Good afternoon ' + user)

    elif hour >=18 and hour>0:
        speak('Good evening ' + user)

    else:
        speak("Good night " + user)
		

		
#Main Script
print("[BOT] : Running \n\n")

time.sleep(2)
Welcome()

while True:
    query = Command()
	
    if query == "Hello":
	speak("Hello" + user)
		
	
