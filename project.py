import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(" I am  Vision sir !!! Your desktop assistant !!! Please tell me how may I help you")       

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source) #reduce noise
        audio = r.listen(source)
        print("Sucessfully Listen")

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User : {query}\n")

    except Exception as e:
          
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching on Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "Who are you" in query:
            speak("I am Vision. Your desktop Assistant")
        
        elif "competitors" in query:
            speak(" They are Amazon's Alexa, Google Assistant, and Apple's Siri")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif ' joke please' in query:
            speak(pyjokes.get_joke())

        elif 'play music' in query:
            music_dir = "C:\\Users\\Desktop\\music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #here you can add the path of the file which you want to open
            os.startfile(codePath)   

        elif 'open telegram' in query:
            telegrampath = "C:\\Users\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe" #here you can add the path of the file which you want to open
            os.startfile(telegrampath)   

        elif "quit" in query:
                speak("Quitting , Sir !  See You soon")
                exit()