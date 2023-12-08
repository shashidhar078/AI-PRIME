import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        print("Good Morning,sir")
        print("Test case passed")
        speak("Good Morning,sir")
    elif hour >12 and hour<=15:
        print("Good Afternoon ,sir")
        print("Test case passed")
        speak("Good Afternoon ,sir")

    else:
        print("Good Evening,sir")
        print("Test case passed")
        speak("Good Evening,sir")

    print("Please tell me, How can I help you ?")
    speak("Please tell me, How can I help you ?")

speak("Hello Sir")
