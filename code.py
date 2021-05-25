import pyttsx3 
import datetime
import speech_recognition as sr 
import PIL
from PIL import Image

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
    

if _name_ == "_main_":
    Greetings()
    while True :
    
        query = takeCommand().lower()
        
        if 'on air conditioner' in query:
            speak("Showing Switched On Air Conditioner.")
            im = Image.open(r"C:\Users\panis\Downloads\AC.jpg")
            im.show()
        
        
        elif 'off air conditioner' in query:
            speak("Showing Switched Off Air Conditioner.")
            im = Image.open(r"C:\Users\panis\Downloads\AC_OFF.jpg")
            im.show()

        
        elif 'on television' in query:
            speak("Showing Switched On Television.")
            im = Image.open(r"C:\Users\panis\Downloads\TV.jpeg")
            im.show()

        
        elif 'off television' in query:
            speak("Showing Switched Off Television.")
            im = Image.open(r"C:\Users\panis\Downloads\TV_OFF.jpg")
            im.show()

            
        elif 'on ceiling fan' in query:
            speak("Showing Switched On Ceiling Fan.")
            im = Image.open(r"C:\Users\panis\Downloads\FAN_ON.jpg")
            im.show()
            
            
        elif 'off ceiling fan' in query:
            speak("Showing Switched Off Ceiling Fan.")
            im = Image.open(r"C:\Users\panis\Downloads\FAN.jpg")
            im.show()


        elif 'on light' in query:
            speak("Showing Switched On Lights.")
            im = Image.open(r"C:\Users\panis\Downloads\LIGHT.jpg")
            im.show()
            
        elif 'off light' in query:
            speak("Showing Switched Off Lights.")
            im = Image.open(r"C:\Users\panis\Downloads\LIGHT_OFF.jpg")
            im.show()

                
        elif 'bye' in query or 'quit' in query :
            speak("Thank you. Have a nice day!")
            break
