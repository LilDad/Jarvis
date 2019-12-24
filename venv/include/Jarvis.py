import os
import time
import speech_recognition as sr
import fuzzywuzzy as fuzz
# преобразование текста в речь
import pyttsx3
import datetime

# engine = pyttsx3.init()
# engine.say("Hey you! I am Jarvis")
# engine.runAndWait()

# определение индекса микрофона
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
