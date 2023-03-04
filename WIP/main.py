# Sean J Bennett
# WIP - Desktop Assistant
# Reference - https://www.youtube.com/watch?v=4k9CphTdnWE - ProgrammingWithHarry - Project1

import pyttsx3 #pip install pyttsx3
import speech_recognition as sprec #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(textToSpeech):
    engine.say(textToSpeech)
    engine.runAndWait()

def main():
    speak("Hello, this is a test")

if __name__=="__main__":
    main()