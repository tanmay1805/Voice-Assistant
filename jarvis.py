import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
       speak("        Good Morning sire!")
    elif hour >=12 and hour < 18:
        speak("       Good Afternoon sire!")
    else :
        speak("       Good Evening sire!")
    
    speak("        Hello sire I am Natalie your virtual assistant. How may i help you today?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("       Sorry I am unable to understand")
        print("Say that again please......")
        return "None"
    return query

def sendEmail(to , content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(" ....  your email ....","... your passord ....")
    server.sendmail("....  your email ....",to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        
        query=takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia..........")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"  Sir the time is {strTime}")
        
        elif "date" in query:
            strDate=datetime.date.today()
            speak(f"  Sir the date is {strDate}")
        
        elif "open vs code" in query:
            codepath="... path to vs code exe file ..."
            os.startfile(codepath)
        
        elif "play song" or "play music" in query:
            music_dir = '... path to music playlist folder ...'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))


        elif "send email" in query:
        
            try:
                speak("   What should i send?")
                content=takeCommand()
                to ="... email id of the reciever ..."
                sendEmail(to,content)
                speak("   Email has been sent !!")
        
            except Exception as e:
                print(e)
                speak("   Sorry I was unable to send the email!!")
        
        elif "quit" in query:
            speak("Thank you sir have a nice day ahead!")
            exit()