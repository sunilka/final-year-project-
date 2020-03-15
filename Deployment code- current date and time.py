import cv2 
import time
import os
import pytesseract  
import pyttsx3   
from PIL import Image              
from googletrans import Translator       
from gtts import gTTS 
from playsound import playsound
from datetime import datetime
from datetime import date

def speech(msg):
    mytext = msg
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("welcome.mp3") 
    playsound("C:\\Users\\Shruthi\\welcome.mp3")
    os.remove("C:\\Users\\Shruthi\\welcome.mp3")

from datetime import date
today = date.today()
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)
t = time.localtime()
current_time = time.strftime("%H:%M:%S",t)
speech("Today's date is "+d2+"Present time is "+current_time+"       , , , ,  Have a nice day")

