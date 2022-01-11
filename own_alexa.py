import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    import pdb;pdb.set_trace()
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        import pdb;pdb.set_trace()

        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except Exception as e:
        print(e)
    # return command

def run_alexa():
    import pdb;pdb.set_trace()
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace("play","")
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("Current time is " + time)
    elif 'who the heck is' in command:
        person = command.replace("who the heck is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk("sorry, I have a headache")
    elif 'are you single' in command:
        talk("I am in a relationship with wifi")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("please say the command again")


while True:
    run_alexa()