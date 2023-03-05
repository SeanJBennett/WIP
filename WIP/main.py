# Sean J Bennett
# WIP - Desktop Assistant
# Reference - https://www.youtube.com/watch?v=4k9CphTdnWE - ProgrammingWithHarry - Project1

import pyttsx3 #pip install pyttsx3
import speech_recognition as sprec #pip install speechRecognition
import datetime
import calendar
from num2words import num2words #pip install num2words
import wikipedia #pip install wikipedia
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(textToSpeech):
    engine.say(textToSpeech)
    engine.runAndWait()

def dailyIntro():
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    textToSpeech = "Hello, the current date is " + calendar.day_name[date] + calendar.month_name[month] + num2words(date, ordinal=True)

    engine.say(textToSpeech)
    engine.runAndWait()

def main():
    dailyIntro()

if __name__=="__main__":
    main()