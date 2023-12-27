import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")

    elif hour >= 12 and hour < 18:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak("i am your assistant,jarvis. how may i help you?")


def takeCommand():
    # it takes microphone input and gives string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pausethreshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("will you please repeat that?")
        return "none"
    return query


def sendEmail(to, content):
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mabhisheksingh574@gmail.com', 'vtomfnljbubrnqmu')
    server.sendmail('mabhisheksingh574@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    speak("hello everyone. and hello respected H O D sir")
    wishme()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open wikipedia' in query:
            webbrowser.open("wikipedia.com")

        elif 'play music' in query:
            music_dir = "C:\\AC 2001\\Ringtones"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'email to abhi' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mabhisheksingh574@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Abhishek Sir. I am not able to send this email")

        elif 'open chrome' in query:
            codepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(codepath)

        elif 'open code' in query:
            codepath = "C:\\Users\\Abhishek singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open games' in query:
            codepath = "C:\\Users\\Abhishek singh\\OneDrive\\Desktop\\Rockstar Games Launcher.lnk"
            os.startfile(codepath)

        elif 'tell me a joke' in query:
            speak("i dont like stairs. theyre always upto something")

        elif 'tell me another joke' in query:
            speak("i have a joke about pizza. but its too cheesy")