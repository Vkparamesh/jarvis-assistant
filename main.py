import cv2
import pyttsx3
import webbrowser
import os
import pyautogui
import random
import speech_recognition as sr
import wikipedia
import datetime
import pyjokes
import subprocess

from playsound import playsound
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from assist import Ui_Ruby

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExection()

    def commands(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 2
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source,phrase_time_limit=3)
        try:
            print("Wait for few moments...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You Just Said: {query}\n")
        except Exception as e:
            print(e)
            print('Sorry sir! I didn\'t get that! Try typing the command!')
            query = str(input('Command: '))


        return query

    def wishings(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            print('Good morning ')
            speak('Good morning')
        elif hour >= 12 and hour < 17:
            print("Good Afternoon ")
            speak("Good Afternoon ")
        elif hour >= 17 and hour < 21:
            print("Good Evening ")
            speak("Good Evening ")
        else:
            print("Good Night ")
            speak("Good Night ")

    def TaskExection(self):
        self.wishings()
        while True:

            self.query = self.commands().lower()
            if 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak("Sir, The time is: " + strTime)
                print(strTime)


            elif 'wikipedia' in self.query:
                speak("Searching in wikipedia")
                try:
                    self.query = self.query.replace("wikipedia", '')
                    results = wikipedia.summary(self.query, sentences=1)
                    speak("According to Wikipedia..")
                    print(results)
                    speak(results)
                except:
                    print("No results found..")
                    speak("no results found")

            elif'joke' in self.query:
                joke = pyjokes.get_joke('en','all')
                print(joke)
                speak(joke)

            elif 'weather' in self.query:
                webbrowser.open_new_tab('https://www.google.co.in/search?q=' + self.query)
            elif 'open youtube' in self.query:
                speak('okay')
                webbrowser.open('www.youtube.com')

            elif 'video' in self.query:
                webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + self.query)

            elif 'my computer'  in self.query:
                subprocess.Popen('explorer.exe')


            elif 'song' in self.query:
                webbrowser.open_new_tab('https://music.youtube.com/search?q=' + self.query)

            elif 'play music' in self.query  or'play song'in self.query :
                webbrowser.open_new_tab('https://music.youtube.com/watch?v=a4peeMf9lvs&list=RDAMVMa4peeMf9lvs')

            elif 'open google' in self.query:
                speak('okay')
                webbrowser.open('www.google.co.in')



            elif 'notepad' in self.query:
                cmd = "notepad"
                os.system(cmd)

            elif 'whatsapp' in self.query:
                webbrowser.open('https://web.whatsapp.com/')

            elif 'camera' in self.query:
                cam = cv2.VideoCapture(0)

                cv2.namedWindow("camera")

                img_counter = 0

                while True:
                    ret, frame = cam.read()
                    if not ret:
                        print("failed to grab frame")
                        break
                    cv2.imshow("camera", frame)

                    k = cv2.waitKey(1)
                    if k % 256 == 27:
                        # ESC pressed
                        print("Escape hit, closing...")
                        break
                    elif k % 256 == 32:
                        # SPACE pressed
                        img_name = "opencv_frame_{}.png".format(img_counter)
                        cv2.imwrite (img_name, frame)
                        print("{} written!".format(img_name))
                        img_counter += 1

                cam.release()

                cv2.destroyAllWindows();




            elif 'gmail' in self.query:
                speak('okay')
                webbrowser.open('www.gmail.com')

            elif "what\'s up" in self.query or 'how are you' in self.query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
                speak(random.choice(stMsgs))

            elif 'hello' in self.query:
                speak('Hello Sir how may i help you')

            elif 'bye'in self.query or'stop'in self.query or 'end' in self.query:
                speak('Bye Sir, have a good day.')
                sys.exit()
            else:
                speak('Searching...')
                webbrowser.open_new_tab('https://www.google.co.in/search?q=' + self.query)


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Ruby()
        self.ui.setupUi(self)

        self.ui.start.clicked.connect(self.startTask)
        self.ui.quit.clicked.connect(self.close)

    def startTask(self):
        # Jarvis GUI
        self.ui.movie = QtGui.QMovie("image_processing20210913-12239-1ov2meu.gif")
        self.ui.ani1.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())