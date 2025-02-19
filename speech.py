import speech_recognition as sr

def speech():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)
    try:
        voice =r.recognize_google(audio)
        print(voice)
        return voice
    except sr.UnknownValueError:
        print("no input   error")
    except sr.RequestError:
        print("Audio not heard   error")


speech()