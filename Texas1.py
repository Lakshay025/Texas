import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as ktt

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello, I am Texas. How may i help you ?")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Yes i am listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognize...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('akashkryadav786@gmail.com', 'akashmanju143')
    server.sendmail('harshchauhan0297@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")

            print(results)
            speak(results)

        elif 'texas please open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'texas i am getting bored' in query:
            speak(f"ok, i have something for you")
            webbrowser.open("https://www.voot.com/")

        elif 'texas please open google' in query:
            webbrowser.open("google.com")

        elif 'texas what are the latest news' in query:
            speak(f"here's the latest news")
            webbrowser.open("https://www.indiatoday.in/news.html")

        elif 'home location' in query:
            webbrowser.open(
                "https://www.google.com/maps/@28.7245635,77.1663171,16z")

        elif 'texas what is my wifi speed' in query:
            webbrowser.open("https://www.speedtest.net/")

        elif 'texas please open facebook' in query:
            webbrowser.open("https://www.facebook.com/")

        elif 'texas can you please suggest some hotels' in query:
            webbrowser.open("https://www.trivago.in/?__wr=21&tc=102&themeId=280&sem_keyword=trivago&sem_creativeid=598703244717&sem_matchtype=e&sem_network=g&sem_device=c&sem_placement=&sem_target=&sem_adposition=&sem_param1=&sem_param2=&sem_campaignid=12420208030&sem_adgroupid=126823053308&sem_targetid=kwd-5593367084&sem_location=9050497&cipc=br&cip=9119000005&gclid=Cj0KCQjw1tGUBhDXARIsAIJx01nY8ptAI03SsXaWlx2oHQmeRgcQ1iE-wbwxdj-JBxCTjPAqI27rzW4aAuZSEALw_wcB")

        elif 'texas suggest some places to visit' in query:
            webbrowser.open(
                "https://www.trawell.in/india/best#:~:text=Varanasi&text=It%20is%20one%20among%20the,of%20learning%20in%20the%20past.")

        elif 'texas i want to search' in query:
            speak(" {MASTER} what do you want to search")
            query2 = None
            while query2 is None:
                r2 = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    audio2 = r2.listen(source)

                try:
                    print("Recognising...")
                    query2 = r2.recognize_google(audio2, language='en-us')
                    print(f"user said: {query2}\n")
                    print(query2)
                    break

                except Exception:
                    print("Say that again please...")
                    speak("Say that again please...")
                    query2 = None

            query2 = query2.replace(" ", "+")
            webbrowser.open("https://www.google.com/search?q="+query2+"&rlz=1C1YTUH_enIN1008IN1008&oq="+query2 +
                            "&aqs=chrome..69i57j46i433i512j0i433i512j0i131i433i512j0i433i512j0i131i433i512j46i433i512j0i131i433i512j0i433i512j0i131i433i512.1046j0j15&sourceid=chrome&ie=UTF-8")

        elif 'texas i want to play music' in query:
            speak(" {MASTER} which music do you want to play")
            query1 = None
            while query1 is None:
                r2 = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    audio2 = r2.listen(source)

                try:
                    print("Recognising...")
                    query1 = r2.recognize_google(audio2, language='en-us')
                    print(f"user said: {query1}\n")
                    print(query1)
                    break

                except Exception:
                    print("Say that again please...")
                    speak("Say that again please...")
                    query1 = None

            query1 = query1.replace(" ", "+")
            ktt.playonyt(query1)

        elif 'what is the time going on texas' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'texas tell about yourself' in query:
            speak(f"hello, i am texas, a voice assistant, i can look up answers for you or help you with find the quickest way home. If you need anything just ask, your wish is my command. I am developed by Lakshay, akash and harsh.")

        elif 'send email to akash' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "akashkryadav786@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry sir i am not able to sent the email.")

        elif 'i have to do shopping' in query:
            speak(" {MASTER} which product do you want to search")
            query3 = None
            while query3 is None:
                r2 = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    audio2 = r2.listen(source)

                try:
                    print("Recognising...")
                    query3 = r2.recognize_google(audio2, language='en-us')
                    print(f"user said: {query3}\n")
                    print(query3)
                    break

                except Exception:
                    print("Say that again please...")
                    speak("Say that again please...")
                    query3 = None

            query3 = query3.replace(" ", "+")
            webbrowser.open("https://www.amazon.in/s?k="+query3 +
                            "&crid=2TUHA2OHT5Q5E&sprefix=%2Caps%2C1023&ref=nb_sb_ss_recent_1_0_recent")
