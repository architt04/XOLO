import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import subprocess
import operator
import pyjokes
import pywhatkit
import ctypes
import os
import time
import requests
import json
import sys

from bs4 import BeautifulSoup
from datetime import date
from urllib.request import urlopen
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

from PySide import QtCore,QtGui
from PySide import QtUiTools
import os, sys
from kicad_board import KicadBoard

def load_ui(file_name, where=None):
    """
    Loads a .UI file into the corresponding Qt Python object
    :param file_name: UI file path
    :param where: Use this parameter to load the UI into an existing class (i.e. to override methods)
    :return: loaded UI
    """
    # Create a QtLoader
    loader = QtUiTools.QUiLoader()

    # Open the UI file
    ui_file = QtCore.QFile(file_name)
    ui_file.open(QtCore.QFile.ReadOnly)

    # Load the contents of the file
    ui = loader.load(ui_file, where)

    # Close the file
    ui_file.close()

    return ui

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_XoloUi(object):
    def setupUi(self, XoloUi):
        XoloUi.setObjectName("XoloUi")
        XoloUi.resize(1366, 720)
        self.centralwidget = QtWidgets.QWidget(XoloUi)
        self.centralwidget.setObjectName("centralwidget")
        self.bg_1 = QtWidgets.QLabel(self.centralwidget)
        self.bg_1.setGeometry(QtCore.QRect(-70, -20, 1531, 841))
        self.bg_1.setText("")
        self.bg_1.setPixmap(QtGui.QPixmap("../GUI/bg/vecteezy_abstract-blue-circuit-digital-background_6736873.jpg"))
        self.bg_1.setScaledContents(True)
        self.bg_1.setObjectName("bg_1")
        self.bg_2 = QtWidgets.QLabel(self.centralwidget)
        self.bg_2.setGeometry(QtCore.QRect(610, 240, 111, 101))
        self.bg_2.setText("")
        self.bg_2.setPixmap(QtGui.QPixmap("../GUI/bg/Screenshot_20230423_000708_Microsoft 365 (Office) (2).png"))
        self.bg_2.setScaledContents(True)
        self.bg_2.setObjectName("bg_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(510, 410, 111, 41))
        self.pushButton_1.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(226, 226, 218);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 410, 111, 41))
        self.pushButton_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(226, 226, 218);")
        self.pushButton_2.setObjectName("pushButton_2")
        XoloUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(XoloUi)
        QtCore.QMetaObject.connectSlotsByName(XoloUi)

    def retranslateUi(self, XoloUi):
        _translate = QtCore.QCoreApplication.translate
        XoloUi.setWindowTitle(_translate("XoloUi", "MainWindow"))
        self.pushButton_1.setText(_translate("XoloUi", "START"))
        self.pushButton_2.setText(_translate("XoloUi", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    XoloUi = QtWidgets.QMainWindow()
    ui = Ui_XoloUi()
    ui.setupUi(XoloUi)
    XoloUi.show()
    sys.exit(app.exec_())

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    h=int (datetime.datetime.now().hour)
    if h>=0 and h<12:
       speak("Good Morning!")

    elif h>=12 and h<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello I am Zolo. How can I assist you?")

def command():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening speech...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing speech...")
        qry=r.recognize_google(audio,language='en-in'or 'hi-In')
        print(f"User said: {qry}\n")
    except Exception as e:
        print("Can you repeat please...")
        return "Sorry I didn't get that!"
    return qry
if __name__ == "__main__":
    wish()
    while True:
        qry= command().lower()
        if "how are you"in qry or'tum kaise ho' in qry:
            speak("I'm fine sir, how may i help you ?")

        elif "university name"in qry or 'tum kahan se ho' in qry:
            speak("Jaypee institute of information technology")

        elif "names of group members" in qry or 'who made you'in qry or 'tumhen kisne banaya hai' in qry:
            speak("I was made by Mohit, Ashwin and Archit")

        elif "what can you do" in qry or 'tum kya kar sakte ho' in qry:
            speak('''i can tell time,i can inform you about anything,
                  i can open applications,i can open websites,i can play music''')

        elif "who are you" in qry or 'tum kaun ho' in qry:
            speak("Sir I am your personal assistant Xolo")

        elif 'who is' in qry or 'what is' in qry or 'wikipedia' in qry:
            speak('Searching...please wait')
            qry = qry.replace("wikipedia", "")
            results =  wikipedia.summary(qry, sentences = 2)
            speak("Accoroding to google")
            print(results)
            speak(results)

        elif'open youtube' in qry or 'youtube kholo' in qry:
            webbrowser.open("youtube.com")
            
        elif 'play' in qry or 'bajao' in qry:
            song=qry.replace('play',"")
            speak('playing')
            pywhatkit.playonyt(song)
            

        elif 'open google' in qry or 'google kholo' in qry:
            webbrowser.open('https://www.google.co.in/')

        elif 'what is the time' in qry or 'can you tell the time' in qry or 'time batao' in qry or 'kya time' in qry or 'time batao' in qry:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'what is the date' in qry or 'can you tell the date' in qry or 'kya din' in qry:
            strdate = date.today()
            speak(f"Sir, the date is {strdate}")

        elif 'search' in qry :
            qry = qry.replace("search", "")
            webbrowser.open(qry)

        elif 'why were you made' in qry or 'reason for your existence' in qry:
            speak("I was created as a project for hackstreet ")

        elif '143' in qry:
            speak("I Love You ")

        elif '5401314' in qry:
            speak("I will Love You for a lifetime. i will love you forever")
        

        elif 'lock window' in qry or 'lock system' in qry or 'system lock kar do' in qry:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in qry or 'computer band kar do' in qry:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                os.system('shutdown /s /t 1')
                
        elif "temperature" in qry or "weather forecast" in qry:
            search = "temperature  is"
            url  = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"Current {search} is {temp}")

        elif "Weather" in qry :
            city_name = input("Enter the name of the City : ")
            def Gen_report(C):
                url = 'https://wttr.in/{}'.format(C)
                data = requests.get(url)
                T = data.text
                Gen_report(city_name)

        elif "do some calculations" in qry or "can you calculate" in qry:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("say what you want to calculate, example: 3 plus 3")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided': operator.__truediv__,
                    }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split())))
            

        elif "hibernate" in qry or "sleep" in qry or 'sleep mode me jaao'in qry:
            speak("Hibernating")
            os.system(r'rundll32.exe powrprof.dll,SetSuspendState Hibernate')

        elif "joke sunao" in qry or 'tell jokes' in qry or 'joke' in qry :
            speak(pyjokes.get_joke())

        elif "log of" in qry or "sign out" in qry:
            speak("Make sure all the application are closed before sign-out")
            subprocess.call(["shutdown", "/l"])
        elif 'Xolo shutdown' in qry or 'close yourself' in qry or'bye xolo' in qry or 'bye solo' in qry:
            speak("it was nice serving you but it's time to say good bye")
            exit()
