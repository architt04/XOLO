
import os
import pyttsx3
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def command():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening speech...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing speech...")
        qry=r.recognize_google(audio,language='en-in'or 'hi-In')
        print(f"User said: {qry}\n")
    except Exception as e:
        print("Can you repeat please...")
        return "Sorry I didn't get that!"
    return qry
if __name__ == "__main__":
    while True:
        qry= command().lower()
        if 'hey' in qry or 'namaskar' in qry or 'namaskar solo' in qry or 'hey solo' in qry in qry:
            os.startfile(r"C:\Users\r1ash\OneDrive\Desktop\heymain.py")
        else:
            pass



    
