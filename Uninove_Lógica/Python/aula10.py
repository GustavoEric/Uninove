#Utilização de Break

import os
import speech_recognition as sr
rec = sr.Recognizer()
print(sr.Microphone().list_microphone_names())
i = 10
while True:
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print('Diga algo')
        audio = rec.listen(mic)
        try:
            for x in range(60,0,-1):
                texto = rec.recognize_google(audio,language="pt-BR")
                print(x)
                print(texto)
        except sr.UnknownValueError:
            print('Não Entendi')