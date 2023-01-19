import speech_recognition as sr
import pyttsx3 as py
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = py.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():

    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'ashley' in command:
            command = command.replace('ashley', '')
            print(command)
        return command


def run_ashley():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.split('play')[-1].strip()
        # song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('the time is ' + time)
    elif 'who is' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'can we go on a date' in command:
        print('i am sorry, you are not my type')
        talk('i am sorry, you are not my type')
    elif 'are you single' in command:
        print('im in a relationship with my creator')
        talk('im in a relationship with my creator')
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif "how are you" in command:
        print('im feeling good today')
        talk('im feeling good today')
    elif "that wasn't funny" in command:
        print('like you can do better')
        talk('like you can do better')
    elif "bro chill" in command:
        print('i am not your bro and dont tell me to chill')
        talk('i am not your bro and dont tell me to chill')
    elif "hello" in command:
        print('hi')
        talk('hi')
    elif 'hey' in command:
        print('hey')
        talk("hey")
    elif "f*** you" in command:
        print('fuck you too, you son of a bitch')
        talk('fuck you too, you son of a bitch')
    elif 'thank you' in command:
        print("youre welcome")
        talk("youre welcome")
    elif 'your name' in command:
        print('my name is ashley')
        talk('my name is ashley')
    elif "bye" in command:
        print('goodbye')
        talk('goodbye')

    else:
        print('please come again')
        talk('please come again')


while True:
    run_ashley()
