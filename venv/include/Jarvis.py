import os
import time

# Google API для распознование речи
import speech_recognition as sr

# Модуль для нечеткого сравнения
import fuzzywuzzy as fuzz

# Преобразование текста в речь
import pyttsx3
import datetime

# engine = pyttsx3.init()
# engine.say("Hey you! I am Jarvis")
# engine.runAndWait()

# Определение индекса микрофона
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

opts = {
    "alias": ('джарвис', 'джар', 'джа-джа', 'джо'),
    "tbr": ('открой', 'серия', 'серию', 'сезон'),
    "cmds": {
        "films": ('включи', 'запусти', 'открой', 'найди')
    }
}

def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    pass

def recognized_cmd(cmd):
    pass

def execute_cmd(cmd):
    pass

# Запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=0)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

# Если установлены голоса для синтеза речи
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[4].id)

speak("Привет, я тебя слушаю")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)