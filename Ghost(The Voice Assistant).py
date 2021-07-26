import random
import pyttsx3   #text to speech module
import speech_recognition as sr
import pyaudio
import winshell
import subprocess
import time
import datetime
import os
import webbrowser
import wikipedia
import smtplib
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def start():
    hour = int(datetime.datetime.now().hour)        #getting hour in currnet time
    if hour>=0 and hour<12 :
        speak("Very Good Morning!")
    elif hour>12 and hour<18 :
        speak("Good afternoon")
    else:
        speak("Good evening")

    rate = engine.getProperty('rate')               #Get the rate/speed of speech

    engine.setProperty('rate',225)                  #set the rate/speed of speech
    speak("Hey there! I am ghost. How may I assist you sir?")


def takeCommand():
    """This function tekes user input or say command and returns string output"""
    record = sr.Recognizer()                        #Recognizer is a class helps in recognizing audio
    with sr.Microphone() as source:                 #with statement in Python is used in exception handling
        print("Listening...")
        record.energy_threshold = 500
        record.pause_threshold = 0.8                #Time gap for the module not to stop listening
        audio = record.listen(source)

    try:
        print("Recognizing...")
        voice_data = record.recognize_google(audio,language='en-in') # Search Engine
        print(f"user said: {voice_data}\n" )

    except Exception as ex:
        # print(ex)      #print the exception or error
        print("Oops, say that again..")
        speak("Oops, say that again..")
        return "none"
    return voice_data

def sendEmail(sender,receiver,message):
    
    server =smtplib.SMTP('smtp.gmail.com',578)
    server.ehlo()
    server.starttls()
    
    # Low security apps login must be enabled
    server.login('tarunmathur97@gmail.com','TarunHNA')
    server.sendmail(sender, receiver, message)
    server.close()
    


if __name__ == "__main__":
    start()
    # while True:
    if 1:
        voice_data = takeCommand().lower()

        # Logic for executing tasks based on voice_data

        #Some normal questions to be asked
        if 'what is your name' in voice_data:
            speak('My name is Ghost. sir!')

        elif "who are you" in voice_data:
            speak("I am a virtual assistant programmed by Master Tarun")
        
        elif "why you came to the world" in voice_data:
            speak("My master who is Tarun,was bored of just clicking "
                  "buttons and moving mouse pointer here and there for"
                  "such basic operations. So he programmed me to do these tasks.")

        elif "who made you" in voice_data or "who created you" in voice_data or 'who programmed you' in voice_data:
            speak("I am programmed by my master Mr. Tarun mathur.")

        elif "will you be my gf" in voice_data or "will you be my bf" in voice_data:
            speak("I appreciate you proposal but this is not my cup of tea.")

        elif 'love you' in voice_data:
            speak('oops! I can not work properly. these words seem to be bugs.')

        #Some system based tasks
        elif 'the time' in voice_data:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {strTime}")

        elif 'play music' in voice_data or "play song" in voice_data:
            speak("Here you go with music")
            music_dir = "C:\\Users\\tarun\\Desktop\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'open pycharm' in voice_data:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'empty recycle bin' in voice_data:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin is empty now.")

        elif 'hibernate' in voice_data or 'sleep' in voice_data:
            speak('hibernating')
            subprocess.call(["shutdown /h"])

        elif "restart" in voice_data:
            subprocess.call(["shutdown", "/r"])

        elif "log off" in voice_data or "sign out" in voice_data:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])


        #Internet based tasks
        elif 'wikipedia' in voice_data or 'find wikipedia' in voice_data:
            speak('Searching Wikipedia...')
            voice_data = voice_data.replace("wikipedia", "")
            results = wikipedia.summary(voice_data, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in voice_data:
            webbrowser.open("youtube.com")

        elif 'open google' in voice_data:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in voice_data:
            webbrowser.open("stackoverflow.com")

        elif 'search' in voice_data:
            speak('what you want me to search?')
            search = takeCommand()
            url = "https://google.com/search?q=" + search
            webbrowser.get().open(url)
            speak('here is what I found for'+ search)

        elif 'find location' in voice_data or 'find place' in voice_data:
            speak('tell me the location')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            speak('here is location of ' + location)

        elif 'send an email' in voice_data:
            try:
                speak('to whom you want to send the e-mail')
                receiver = takeCommand()
                print(receiver)
                # to.replace(" ","")
                speak("what is the message you want to send")
                message = takeCommand()
                sender = 'tarunmathur97@gmail.com'
                sendEmail(sender,receiver,message)
                speak("Email has been sent successfully.")

            except Exception as ex:
                speak("oops! Could not send the email.")


        elif 'tell me a joke' in voice_data or 'crack a joke' in voice_data:
            speak(pyjokes.get_joke(language='en'))
            

        elif 'exit' in voice_data:
            speak('Hope! I helped you')
            exit()