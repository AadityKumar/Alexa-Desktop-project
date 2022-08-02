import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

res=True
listener = sr.Recognizer()
engine = pyttsx3.init()
# voices = engine.getProperty('voices')  # for female
# engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
         # main function
def take_command():
    try:
        with sr.Microphone(device_index=1) as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bharat' in command:
                command = command.replace('bharat')
                print(command)
    except:
       pass
    return command

def run_command():
    command = take_command()
    print(command)
    if 'hello' in command:
        talk('hello aaditya !!. what can i do for you')
    elif 'play' in command:
        song = command.replace('play','')
        talk('playing....'+ song)
        pywhatkit.playonyt(song)
    elif 'send' in command:
        pywhatkit.sendwhatmsg('+919006330203','good night',22,1)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is'+ time)
        print(time)
    elif 'question' in command:
        person = command.replace('person','')
        info = wikipedia.summary(person,1)
        talk(info)
        # print(info)
    elif 'joke' in command:
        talk(pyjokes.get_jokes())
        
    elif 'call' in command:
        talk('i did not have number list provided by you')
    elif 'down' in command:
        print('program shutting down')
        res=False
    elif 'laugh' in command:
        talk('hahahahhahahaha hihihihihiihi hohohoohohoho hehehhehhehehehee')
   
    else:
        talk('please say this again....')

while True:
    run_command()
        







