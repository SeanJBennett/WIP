# Sean J Bennett
# WIP - Desktop Assistant
# Reference - https://www.youtube.com/watch?v=4k9CphTdnWE - ProgrammingWithHarry - Project1

import pyttsx3 # pip install pyttsx3
import speech_recognition as sprec # pip install speechRecognition
import datetime
import calendar
from num2words import num2words # pip install num2words
import wikipedia # pip install wikipedia
import os
import smtplib
from config import config
from newsapi import NewsApiClient # pip install newsapi-python
from urllib import request
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(textToSpeech):
    engine.say(textToSpeech)
    engine.runAndWait()

def listen():
    takenSpeech = sprec.Recognizer()
    with sprec.Microphone() as source:
        speak("What would you like to know?")
        audio = takenSpeech.listen(source)

    try:
        speak("Give me one moment.")
        query = takenSpeech.recognize_google(audio, language='en-us')
        #print(f"user said: {query} \n")

    except Exception as e:
        speak("Say that again please.")
        query = None

    return query

def searchWikipedia(query):
    query = query.replace('Wikipedia', "")
    result = wikipedia.summary(query, sentences = 2)
    speak("According to Wikipedia: " + result)

def dailyIntro():
    # Setting up TTS to say current date, month and ordinal calendar number
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    day = datetime.datetime.now().weekday()
    textToSpeech = "Hello, the current date is " + calendar.day_name[day] + calendar.month_name[month] + num2words(date, ordinal=True)

    # Setting up TTS to add on the current top news articles I am getting from this request
    textToSpeech = textToSpeech + ". The top news articles in the US are: "
    newsUrl = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + config.api_key
    
    with request.urlopen(newsUrl) as response:
        body = response.read()

    newsItems = json.loads(body)

    articles = newsItems['articles']
    for title in range(0, 1):
        titles = articles[title]
        textToSpeech += "\n" + titles['title']

    engine.say(textToSpeech)
    engine.runAndWait()

def main():
    dailyIntro()
    query = listen()
    if 'Wikipedia' in query:
        searchWikipedia(query)

if __name__=="__main__":
    main()