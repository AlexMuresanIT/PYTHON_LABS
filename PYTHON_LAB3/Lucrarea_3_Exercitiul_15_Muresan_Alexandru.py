import os
from gtts import gTTS
from playsound import playsound
import pygame

cod_morse={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.",
           "H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.",
           "O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-",
           "V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----",
           "2":"..---","3":"...--","4":"....-","5":"......","6":"-....","7":"--...",
           "8":"---..","9":"----.",".":".-.-.-",",":"--..--"," ":"..--.."}


def cod_Morse(text):
    Morse=" "
    for i in text:
        Morse+=cod_morse[i]
    return Morse


text=input("Introdu textul care vrei sa fie convertit in cod Morse:")
text=text.upper()
print("Codul morse este: ",cod_Morse(text))

a=gTTS(text)
a.save("morse.mp3")
playsound("morse.mp3",True)





