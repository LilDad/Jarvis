import os
import time
import speech_recognition as sr
import fuzzywuzzy as fuzz
# преобразование текста в речь
import pyttsx3
import datetime

engine = pyttsx3.init()
engine.say("Hey you! I am Jarvis")
engine.runAndWait()

