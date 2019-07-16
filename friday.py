import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour <18:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak("i am friday sir. please tell me how may i help you ")

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening .....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("say that again please....")
        return "None"
    return query

if __name__=="__main__":
    wishme()
    takeCommand()
