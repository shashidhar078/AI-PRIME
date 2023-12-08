import pywifi
import pyautogui
import time
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170) 


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

def turn_off_wifi():    #on_wifi
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  

    iface.disconnect()  



def turn_on_bluetooth_windows():   #bluetooth_on
   
    pyautogui.press('win')
    time.sleep(1)  

    
    pyautogui.write('Bluetooth')
    pyautogui.press('enter')
    time.sleep(1) 

   
    pyautogui.press('tab', presses=3)  
    pyautogui.press('space') 

    
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')



def turn_off_bluetooth_windows():           #bluetooth_off
    
    pyautogui.press('win')
    time.sleep(1) 

    
    pyautogui.write('Bluetooth')
    pyautogui.press('enter')
    time.sleep(1) 

    
    pyautogui.press('tab', presses=3)  
    pyautogui.press('space')  

    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')





