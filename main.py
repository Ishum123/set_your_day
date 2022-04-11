import time
from time import sleep
from plyer import notification
import random
import credentials
from win32com.client import Dispatch
from datetime import datetime


def speak(str):
    speak= Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)
    
    
date= datetime.now()
hour=time.strftime("%I")
min=time.strftime("%M")


ans=date.weekday()


""" get time feature"""
""" Week day: 1 2 3 4 5 6 7"""
""" printing quotes acc to weekdays"""
""" motivating reminder each time you run the code"""

d2={0:"You are a rockstar", 1:"Believe you can and you will",2:"Try until you don't see test case accepted", 3: "If you feel like giving up, just remember why you started", 4: "Stars can't shine without nights", 5:"When you were born, this world recieved a gem", 6:"Be you because that's your power!!"}


if hour=="04" and min=="24" or hour=="01" and min=="00" or hour=="09"and min=="00":
    speak(d2[ans])
 		
   
if hour=="03" and min=="22" or hour=="12" and min=="00" or hour=="08"and min=="00":
    speak("**Please Drink Water, Dear little superstar!!")
    
    
    
while True:
    notification.notify(
        title= "Check your to do once",
        message= "Start, grind, don't give up!",
        timeout=12
    )
    time.sleep(60*60)


