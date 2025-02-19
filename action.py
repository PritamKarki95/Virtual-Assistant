import webbrowser

import text_to_speech
import speech
import datetime
import os

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data or "your introduction" in user_data or "what are you" in user_data:
        text_to_speech.text_to_speech("I am your Virtual Assistant")
        return 'I am your Virtual Assistant'

    elif "open notepad" in user_data:
        os.startfile("notepad.exe")
        text_to_speech.text_to_speech("opening notepad")
        return 'Opening Notepad'

    elif "open browser" in user_data or "open microsoft edge" in user_data or "open ms edge" in user_data:
        os.startfile("msedge.exe")
        text_to_speech.text_to_speech("opening Microsoft Edge")
        return 'opening Microsoft Edge'

    elif "open outlook" in user_data:
        os.startfile("Outlook.exe")
        text_to_speech.text_to_speech("opening this pc")
        return 'Opening Outlook'

    elif "open ms word" in user_data:
        os.startfile("Winword.exe")
        text_to_speech.text_to_speech("opening microsoft word")
        return 'Opening MS Word'

    elif "hello" in user_data:
        text_to_speech.text_to_speech("Welcome How can I assist you today")
        return 'Welcome How can I assist you today'

    elif "erase the text" in user_data or "delete" in user_data:
        text_to_speech.text_to_speech("You can simply do that by using the erase button on your right")
        return 'You can simply do that by using the erase button on your right'

    elif "who created you" in user_data or "who is your creator" in user_data:
        text_to_speech.text_to_speech("I was created by a Computer Science student named Pritam Karki,                                            here is his linkedin profile")
        webbrowser.open("https://www.linkedin.com/in/pritam-karki-826b36257/")
        return 'Opening Linkedin profile'

    elif "what can you do" in user_data or "what are you capable of" in user_data:
        text_to_speech.text_to_speech("I can open applications and websites for you, I can also tell time")
        return 'I can open websites for you, I can also tell time'

    elif "are you original" in user_data:
        text_to_speech.text_to_speech("In a sense I am but technically I am inspired by different projects")
        return 'In a sense I am but technically I am inspired by different projects'

    elif "how are you" in user_data or "how you doing" in user_data or "how are you doing" in user_data:
        text_to_speech.text_to_speech("I was just missing you                       Good thing youre back               how can i help you")
        return 'I am fine, How can I help you'

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Morning What can I help you with")
        return 'Morning What can I help you with'

    elif "good evening" in user_data:
        text_to_speech.text_to_speech("Evening What can I help you with")
        return 'Evening What can I help you with'

    elif "good afternoon" in user_data:
        text_to_speech.text_to_speech("Afternoon What can I help you with")
        return 'Afternoon What can I help you with'

    elif "time" in user_data:
        current_time = datetime.datetime.now()
        Time = current_time.strftime("%H hours %M minutes %S seconds")
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shut down" in user_data or "shut it" in user_data:
        text_to_speech.text_to_speech("shutting down")
        return 'shutting down'

    elif "play music" in user_data or "play songs" in user_data or "play some tunes" in user_data:
        webbrowser.open("https://spotify.com/")
        text_to_speech.text_to_speech("opening spotify")
        return 'Opening spotify'

    elif "open reddit" in user_data:
        webbrowser.open("https://reddit.com/")
        text_to_speech.text_to_speech("opening reddit")
        return 'Opening reddit'

    elif "open twitter" in user_data:
        webbrowser.open("https://x.com/")
        text_to_speech.text_to_speech("opening reddit")
        return 'Opening x'

    elif "open threads" in user_data:
        webbrowser.open("https://threads.com/")
        text_to_speech.text_to_speech("opening threads by meta")
        return 'Opening threads'

    elif "open games" in user_data:
        webbrowser.open("https://poki.com/")
        text_to_speech.text_to_speech("opening poki for game")
        return 'Opening poki'

    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("opening youtube")
        return 'opening youtube'

    elif "open facebook" in user_data:
        webbrowser.open("https://facebook.com/")
        text_to_speech.text_to_speech("opening fresh feed for you")
        return 'opening fresh feed for you'

    elif "open instagram" in user_data:
        webbrowser.open("https://instagram.com/")
        text_to_speech.text_to_speech("opening instagram")
        return 'opening instagram'

    else:
        text_to_speech.text_to_speech("I am not capable of doing that                               Sorry")
        return 'I am not capable of doing that sorry'



