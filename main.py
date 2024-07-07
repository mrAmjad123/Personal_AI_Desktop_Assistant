import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import os
import smtplib

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

# engine.say('Hello I am Jarvis')
# engine.say('what can i do for you')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning sir.")

    elif hour >= 12 and hour < 18:
        talk('Good Afternoon sir.')

    else:
        talk('Good Evening sir.')
    talk("I am Jarvis, please tell me How may I help you")
WishMe()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print("User said:", command)
            command = command.lower()
            if 'Jarvis' in command:
                command = command.replace('Jarvis', '')
            # engine.say(command)
            # print(command)
            # talk((command))
    except:
        return 'None'
    return command

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('raazs0062@gmail.com', 'Mr_raaz0062')
    server.sendmail('raazs0062@gmail.com',to , content)
    server.close()


def run_amjad():
    command = take_command()
    # print(command)
    if 'hello jarvis' in command:
        talk('Helllllooo')
    elif 'play' in command:
        song = command.replace('play', '')
        print('playing' + song)
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 5)
        print('Searching Wikipedia Please Wait...')
        talk('Searching Wikipedia Please Wait...')
        print('Accoring to Wikipedia', info)
        talk('Accoring to Wikipedia')
        talk(info)

    elif 'thank you' in command:
        talk('you are welcome')

    elif 'love' in command:
        talk('Sorry I have Girlfriend')

    elif 'what is' in command:
        answer = command.replace('what is', '')
        ans = wikipedia.summary(answer, 2)
        print('Searhing wikipedia plaese wait...')
        talk('Searching wikipedia please wait..')
        print('According to wikipedia:', ans)
        talk('According to wikipwdia')
        talk(ans)

    elif 'open youtube' in command:
        webbrowser.open('youtube.com')

    elif 'open google' in command:
        webbrowser.open('google.com')

    elif 'open project' in command:
        path = 'C:\\Users\\amjad\\Desktop\\4t semester\\INT 404 AI\\AI Project'
        os.startfile(path)

    elif 'start music' in command:
        path1 = 'C:\\Entertainment\\music'
        songs = os.listdir(path1)
        print(songs)
        os.startfile(os.path.join(path1, songs[1]))

    elif 'about you' in command:
        talk('My name is Jarvis I am your personal assistant I can help you to make your life easier')

    elif 'send email to sam' in command:
        try:
            talk('what do you want to send')
            content = take_command()
            to = 'sam271272@gmail.com'
            sendEmail(to, content)
            talk('email has been sent')
        except Exception as e:
            print(e)
            talk('sorry, I am not able to send this email')
    
    elif 'for whom do you work' in command:
        talk('I am Jarvis and I work for Mr Amjad Ansari')
            
    

    else:
        print('sorry i did not understand, please say again')
        talk('sorry i did not understand, please say again')
        
    # while True():
    #     run_amjad()

def Start_Conversation():

    command1 = take_command()
    if 'what are you doing' in command1:
        talk('Nothing')
        
    elif 'Can you work for me' in command1:
        talk('No sorry I work for Mr Amjad only')
        talk('Better I will suggest you to design your own Assistant')
        

run_amjad()           
Start_Conversation()
        
    
    













