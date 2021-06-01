import pyttsx3 
import datetime
import os
import speech_recognition as sr 
import RPi.GPIO as GPIO

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT) # light
GPIO.setup(3, GPIO.OUT) # fan

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Processing")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query)

    except Exception as e:
         
        print("Say that again please...")  
        return "None"
    return query


def Greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    
    speak("I am Friday. Please, tell me how may I help you today?")       
    

if __name__ == "__main__":
    Greetings()
    while True :
    
        query = takeCommand().lower()
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)

        
        if 'on ceiling fan' in query:
            GPIO.output(3, GPIO.LOW)
            speak("Switched On Ceiling Fan.")
            
            
        elif 'off ceiling fan' in query:
            GPIO.output(3, GPIO.HIGH)
            speak("Switched Off Ceiling Fan.")


        elif 'on light' in query:
            GPIO.output(2, GPIO.LOW)
            speak("Switched On Lights.")
            
            
        elif 'off light' in query:
            GPIO.output(2, GPIO.HIGH)
            speak("Switched Off Lights.")
        
        
        elif 'on all appliances' in query:
            GPIO.output(2, GPIO.LOW)
            GPIO.output(3, GPIO.LOW)
            speak("Switched On All Appliances.")
        
        
        elif 'off all appliances' in query:
            GPIO.output(2, GPIO.HIGH)
            GPIO.output(3, GPIO.HIGH)
            speak("Switched Off All Appliances.")
            

        elif 'bye' in query or 'quit' in query :
            speak("Thank you. Have a nice day!")
            break 

GPIO.cleanup() 
