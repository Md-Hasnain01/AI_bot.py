import datetime
import os
import webbrowser
import wikipedia
import pyttsx3
import speech_recognition as sr
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your AI Sir.")
    print("How may I assist you?")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.record(source, duration=10)
    print("Recognizing...")

    query = r.recognize_google(audio, language='en-in')
    return query

def checkOurcondition():
    if 'tell me' in query:
        # speak('Searching Wikipedia...')
        person = query.replace("tell me", "")
        results = wikipedia.summary(query)
        # speak("According to Wikipedia")
        # print(results)
        speak(results)
    elif 'who is' in query:
        people = query.replace('who is', '')
        result = wikipedia.summary(query)
        speak(people)
    elif 'what is' in query:
        substance = query.replace('what is', '')
        result = wikipedia.summary(query)
        speak(substance)
    elif 'play' in query:
        song = query.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)
    elif 'open youtube' in query:
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
    elif 'open google' in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com/")
    elif 'open brave' in query:
        speak("Opening Brave")
        webbrowser.open("brave.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
        speak(f"It {strTime}")
    elif 'open pycham' in query:
        codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.3.2\\bin\\pycharm64.exe"
        os.startfile(codePath)
    elif ' open intellij idea' in query:
        codePath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2022.3.1\\bin\\idea64.exe"
        os.startfile(codePath)
    elif 'open android studio' in query:
        speak("Opening Android studio")
        codePath = "C:\\Program Files\\Android\\Android Studio2\\bin\\studio64.exe"
        os.startfile(codePath)
    elif 'open ms word' in query:
        codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        os.startfile(codePath)
    elif 'open excel' in query:
        codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        os.startfile(codePath)
    elif 'open powerpoint' in query:
        codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        os.startfile(codePath)
    elif 'open onenote' in query:
        codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
        os.startfile(codePath)
    elif 'open epic games' in query:
        codePath = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
        os.startfile(codePath)
    elif 'open steam' in query:
        codePath = "C:\\Program Files (x86)\\Steam\\Steam.exe"
        os.startfile(codePath)


while True:

    if __name__ == "__main__":
        query = wishMe()
        query = query.lower()
        checkOurcondition()