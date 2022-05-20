# from multiprocessing.dummy import current_process
# from re import search
import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import pywhatkit as pwk
#from googlesearch import search

name = 'Leo'                                                                                            #Default name of the Virtual Assistant
current_time = datetime.datetime.now()                                                                  #Current date and time
browser_path = wb.Mozilla('C:\\Program Files\\Mozilla Firefox\\firefox.exe')                            #Defualt browser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',voices[0].id)

#Wishes Good morning, good afternoon and good evening according to the time
def WishMe():
    hour = int(current_time.hour)

    #speak("Hey! I'm Leo...")
    #speak(f"{WishMe()}! How can I help you?")
    if hour>0 and hour<12:
        speak("Good Morning! How can I help you?")
    elif hour>12 and hour<16:
        speak("Good Afternoon! How can I help you?")
    else:
        speak("Good Evening! How can I help you?")

#Converts text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Take commands from the user
def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 100
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print(f"User said: {query}")
        speak(f"User said: {query}")

    except Exception as e:
        print("Can't recognize! Please say again...")
        return 'None'
    return query

#Selects users favourite browser
def browser():

    print("Which browser do you want to use?")
    speak("Which browser do you want to use?")
    speak("Chrome or firefox")

    opt = TakeCommand().lower()

    if 'chrome' in opt:
        browser_path = wb.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
        # browser_path.open_new_tab('youtube.com')

    elif 'firefox' in opt:
        browser_path = wb.Mozilla('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
        # browser_path.open_new_tab('youtube.com')

    else:
        speak("Browser not found!!!")
        exit()

    return browser_path

#Tells the current time
def Time():
        
    # hour = datetime.datetime.now().hour
    # min = datetime.datetime.now().min
    # sec = datetime.datetime.now().second
    # speak(f"{hour} hour, {min} minutes, {sec} seconds")
    # current_time = datetime.datetime.now()
    # speak(f"{current_time.time()}")
    # print(current_time.strftime('%I:%M:%S'))

    hour = int(current_time.hour)
    if hour>0 and hour<12:
        print(f"{current_time.strftime('%I:%M:%S')} AM")
        speak(f"{current_time.strftime('%I:%M:%S')} AM")
    else:
        print(f"{current_time.strftime('%I:%M:%S')} PM")
        speak(f"{current_time.strftime('%I:%M:%S')} PM")

#Tells the current date
def Date():     
    # current_time = datetime.datetime.now()
    print(f"{current_time.date()}")
    speak(f"{current_time.date()}")

# Checks queries of the user and process accordingly
# def Check_Queries(query):



#Main function
if __name__ == "__main__":
    WishMe()
    while True: 
        query = TakeCommand().lower()
        # Check_Queries(query)

        #---------- IF condition starts -----------
        #Finds info from wikipedia
        if 'wikipedia' in query:
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)
            continue

        #Opens YouTube
        elif 'open youtube' in query:
            browser_path = browser()
            speak("Opening youtube...")
            print("Opening youtube...")
            browser_path.open_new_tab('youtube.com')
            continue

        #Opens Google
        elif 'open google' in query:
            browser_path = browser()
            speak("Opening google...")
            print("Opening google...")
            browser_path.open_new_tab('www.google.com')
            continue

        #Opens Spotify
        elif 'open spotify' in query:
            browser_path = browser()
            speak("Opening spotify")
            browser_path.open_new_tab('https://open.spotify.com/')

        #Change Virtual Assistant's name
        elif 'change your name' in query:
            speak("Sure sir")
            speak("Give me a new name...")
            name = TakeCommand()
            speak("Name changed...")
            continue

        #Gives Intro
        elif 'tell me about yourself' in query:
            speak(f"Hello Everyone! I'm {name}")
            speak("I'm a python bot created by Sandip Ash for voice recognition purpose...")
            continue

        #Tells current time
        elif 'time' in query:
            Time()

        #Tells current date
        elif 'date' in query:
            Date()
        #----------- IF condition ends ----------------
        #Send WhatsApp message
        Message = ['open whatsapp', 'message']
        for i in Message:
            if i in query:
        
                while True:
                    speak("Do you want to send message to anyone")
                    opt = TakeCommand().lower()
                    if 'yes' in opt:
                        while True:
                            print("Please tell the contact number you want to message")
                            speak("Please tell the contact number you want to message")
                            
                            num = TakeCommand()
                            # if isinstance(num, int) == True: 
                            num = '+91'+num
                            print("What do you want to send?")
                            speak("What do you want to send?")
                            msg = TakeCommand().lower
                            
                            #Time()
                            pwk.sendwhatmsg(f"{num}",f"{msg}", current_time.hour, (current_time.minute + 3))
                            break
                            # else:
                            #     print("Number is not valid!!")
                            #     speak("Number is not valid!!")
                            #     continue
                        break
                    elif 'no' in opt:
                        browser_path.open_new_tab('https://web.whatsapp.com/')
                        break
                    elif 'exit' in opt:
                        exit()
                    else:
                        speak("Can't recognize! Please tell again")
                        continue

        #Intro
        Intro = ['your name', 'who are you']
        for i in Intro:
            if i in query:
                speak(f"My name is {name}")
                speak("Nice to meet you")
        
        #Execute
        Stop = ["exit", "quit", "stop"]
        for i in Stop:
            if i in query:
                speak("Thank you")
                exit()

        