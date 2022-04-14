
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import wolframalpha
import requests
import os
from selenium_web import *
from youtube import *

print('Loading your AI personal assistant - Jarvin')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening... ")
        r.adjust_for_ambient_noise(source,duration=1)
        audio= r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant Jarvin")
wishMe()

    
if __name__=='__main__':


    while True:
        
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            break

        if "search" or "wikipedia" in statement:
            speak("you need information related to which topic?")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                r.energy_threshold=1000
                r.adjust_for_ambient_noise(source, 1.2)
                print("listening...")
                audio = r.listen(source)
                infor = r.recognize_google(audio) 
            speak("searching {} in wikipedia".format(infor))
            print("searching {} in wikipedia".format(infor))    
            
            assist = infow()
            assist.get_info(infor)

        if "play" or "video" in statement:
            speak("you want me to play which video??")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                r.energy_threshold=1000
                r.adjust_for_ambient_noise(source, 1.2)
                print("listening...")
                audio = r.listen(source)
                vid = r.recognize_google(audio) 
            print("playing {} on youtube".format(vid)) 
            speak("playing {} on youtube".format(vid))
            assist = music()
            assist.play(vid)  

        if 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")

        if 'who are you' in statement or 'what can you do' in statement:
            speak('I am Siri version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')    

        if "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Kadir")
            print("I was built by Kadir")   


        if 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")


        if "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak(" City Not Found ")          

        if 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        if 'news' in statement:
            news = webbrowser.open_new_tab("https://www.haberler.com/")
            speak('Here are some headlines from the Times of turkey,Happy reading')
        
        if 'feel' in statement:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print('Clearing background noise...')
                recognizer.adjust_for_ambient_noise(source,duration=1)
                print('Waiting for your message...')
                recordaudio = recognizer.listen(source)
                print('Done recording...')

            try:
                print('Printing the message...')
                text=recognizer.recognize_google(recordaudio,language='en-in')
                print(f"user said:{text}\n")

            except Exception as ex:
                print(ex)
            
            sentence =[str(text)]
            recognizer = SentimentIntensityAnalyzer()
            for i in sentence:
                v=recognizer.polarity_scores(i)
                print(v)
       















 