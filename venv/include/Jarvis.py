import os
import time
# Google API для распознование речи
import speech_recognition as sr
# модуль для нечеткого сравнения
import fuzzywuzzy as fuzz
# преобразование текста в речь
import pyttsx3
import datetime

# engine = pyttsx3.init()
# engine.say("Hey you! I am Jarvis")
# engine.runAndWait()

# определение индекса микрофона
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

opts = {
    "alias": ('джарвис', 'джар', 'джа-джа', 'джо'),
    "tbr": (),
    "cmds": ()
}

r = sr.Recognizer()

with sr.Microphone(device_index=0) as source:
    print("Say some thing...")
    audio = r.listen(source)

query = r.recognize_google(audio, language="ru-RU")
print("Ты сказал: " + query.lower())