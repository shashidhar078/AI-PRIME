import pyttsx3
import speech_recognition 
import requests
import datetime
import pyautogui
import webbrowser
import os
from plyer import notification
from pygame import mixer
from bs4 import BeautifulSoup


for i in range(3):
    a = input("Enter Password to open Prime :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170) 

from Intro import play_gif
play_gif
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up prime" in query:
            from Response import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    print("Ok sir , You can  call me anytime")
                    speak("Ok sir , You can  call me anytime")
                    break
                elif "change password" in query:
                    print("What's the new password")
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    print("Done sir")
                    speak("Done sir")
                    print(new_pw)
                    speak(f"Your new password is{new_pw}")
                
                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("Prime","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")  
                elif  "visit" in query:
                    Nameofweb = query.replace("visit ","")
                    link = f"http://www.{Nameofweb}.com"
                    webbrowser.open(link)
                    speak("opened")
                elif "launch" in query:
                    Nameofweb = query.replace("launch ","")
                    link = f"http://www.{Nameofweb}.com"
                    webbrowser.open(link)
                    speak("opened")
                elif "hello" in query:
                    print("Hello sir, how are you ?")
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    print("that's great, sir")
                    speak("that's great, sir")
                elif "how are you" in query:
                    print("Perfect, sir")
                    speak("Perfect, sir")
                elif "thank you" in query:
                    print("Perfect, sir")
                    speak("you are welcome, sir")
                elif "what is your name" in query:
                    print("my name is Prime")
                    speak("my name is Prime")
                elif "open" in query:
                      from Dictapp import openappweb
                      openappweb(query)
                elif "close" in query:
                     from Dictapp import closeappweb
                     closeappweb(query)
                elif "google" in query:
                    from search import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from search import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from search import searchWikipedia
                    searchWikipedia(query)
                elif "temperature" in query:
                        search = "temperature in hyderabad"
                        url = f"https://www.google.com/search?q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        print(temp)
                        speak(f"current{search} is {temp}")
                elif "weather" in query:
                        search = "temperature in hyderabad"
                        url = f"https://www.google.com/search?q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        print(temp)
                        speak(f"current{search} is {temp}")
                elif "the time" in query:
                        strTime = datetime.datetime.now().strftime("%H:%M")
                        print(strTime)
                        speak(f"Sir , the time is {strTime}")
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("prime remember that","")
                    print(rememberMessage)
                    speak("You told me"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me" + remember.read())
                elif "news" in query:
                    from NewsRead  import latestnews
                    latestnews()
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    print("Do you want to clear old tasks (Plz speak YES or NO)")
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.wav")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                        )
                elif "shutdown the system" in query:
                    print("Are You sure you want to shutdown")
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break
                elif "turn off wi-fi" in query:
                   from taskwb import turn_off_wifi
                   turn_off_wifi()
                
                elif "turn on bluetooth" in query:
                    from taskwb import turn_on_bluetooth_windows
                    turn_on_bluetooth_windows()

                elif "turn off bluetooth" in query:
                    from taskwb import turn_off_bluetooth_windows
                    turn_off_bluetooth_windows()
                            
                elif "finally sleep" in query:
                        print("Going to sleep,sir")
                        speak("Going to sleep,sir")
                        exit()