import cv2 
import time
import os
import pytesseract  
import pyttsx3   
from PIL import Image              
from googletrans import Translator       
from gtts import gTTS 
from playsound import playsound
 

def speech(msg):
    os.remove("C:\\Users\\Shruthi\\welcome.mp3")
    mytext = msg
    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("welcome.mp3") 
    playsound("C:\\Users\\Shruthi\\welcome.mp3")

    
#function to capture the image and convert it into speech 
def convert_img_to_speech():
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(1)
    while True:
        try:
            check, frame = webcam.read()
            print(check) #prints true as long as the webcam is running
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                cv2.imwrite(filename='saved_img.jpg', img=frame)
                webcam.release()
                img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                img_new = cv2.imshow("Captured Image", img_new)
                cv2.destroyAllWindows()
                img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                speech("Image captured, converting the image to text, please wait")
                img = Image.open('saved_img-final.jpg')      

                print(img)                           
                pytesseract.pytesseract.tesseract_cmd ='C:\\Users\\Shruthi\\Desktop\\TesseractOCR\\tesseract.exe'   
                result = pytesseract.image_to_string(img)      
                with open('abc.txt',mode ='w') as file:      
                                 file.write(result) 
                                 print(result)
                p = Translator() 
                k = p.translate(result,dest='english')       
                engine = pyttsx3.init() 
                engine.say(k)                              
                engine.runAndWait() 
                speech('Program complete...')
                break
            elif key == ord('q'):
                speech("Turning off camera.")
                webcam.release()
                cv2.destroyAllWindows()
                break
        except(KeyboardInterrupt):
            webcam.release()
            cv2.destroyAllWindows()
            break

speech('Hello,,,,, You have choosen the option to convert the image to text. Please hold the image in front and wait. After few seconds tap key to capture the image')
convert_img_to_speech()
