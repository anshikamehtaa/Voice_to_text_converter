from tkinter import *
from tkinter.messagebox import showinfo
import speech_recognition as sr
import os

mainwindow = Tk()
mainwindow.title('Voice Based Text Input System')
mainwindow.geometry('500x500')
mainwindow.resizable(0, 0)
mainwindow.configure(bg='white')


def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="en-IN")
            except:
                pass
            return text


def SpeechToText():
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('Voice Based Text Input System')
    speechtotextwindow.geometry("500x500")
    speechtotextwindow.configure(bg='pink')

    Label(speechtotextwindow, text='Voice Based Text Input System', font=("Comic Sans MS", 15),
          bg='IndianRed').place(x=100)

    text = Text(speechtotextwindow, font=10, height=2, width=30)
    text.place(x=90, y=100)

    recordbutton = Button(speechtotextwindow, text='Click to Record', bg='Sienna',
                          command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=200, y=50)


Label(mainwindow, text='Voice Based Text Input System',
      font=('Times New Roman', 16), bg='red', wrap=True, wraplength=450).place(x=130, y=10)

speechtotextbutton = Button(mainwindow, text='Click to start speech Recognition!', font=('Times New Roman', 16), bg='Purple',
                            command=SpeechToText)
speechtotextbutton.place(x=100, y=250)

mainwindow.update()
mainwindow.mainloop()