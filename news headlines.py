import requests      
import os
from gtts import gTTS
import time


def speech(str1):
    mytext = str1
  
    # Language in which you want to convert 
    language = 'en'

    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text=mytext, lang=language, slow=False) 

    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("welcome.mp3") 

    # Playing the converted file 
    os.system("C:\\Users\\Shruthi\\welcome.mp3") 
    
    
def NewsFromBBC(): 
      
    # BBC news api 
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=dc8e4f0486b84d01bf7c18d5d8f06e72"
  
    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open_bbc_page["articles"] 
  
    # empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
    
    f= open("C:\\Users\\Shruthi\\Desktop\\lets.txt","w+")
    for i in range(len(results)): 
          
        # printing all trending news 
        s = "headline "+str(i + 1)+": "+ results[i]
        print(s)
        f.write(s+"\n")
        speech(s)
        time.sleep(1)
    f.close()
    os.remove("C:\\Users\\Shruthi\\welcome.mp3")  
    
  
# Driver Code 
if __name__ == '__main__': 
      
    # function call 
    NewsFromBBC()  