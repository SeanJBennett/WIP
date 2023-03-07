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

def dailyIntro():
    # Setting up TTS to say current date, month and ordinal calendar number
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    textToSpeech = "Hello, the current date is " + calendar.day_name[date] + calendar.month_name[month] + num2words(date, ordinal=True)

    # Setting up TTS to add on the current top news articles I am getting from this request
    textToSpeech = textToSpeech + ". The top news articles in the US are: "
    newsUrl = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + config.api_key
    
    with request.urlopen(newsUrl) as response:
        body = response.read()

    newsItems = json.loads(body)

    articles = newsItems['articles']
    for title in range(0, 3):
        titles = articles[title]
        textToSpeech += "\n" + titles['title']

    engine.say(textToSpeech)
    engine.runAndWait()

def main():
    dailyIntro()

if __name__=="__main__":
    main()