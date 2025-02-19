from tkinter import*
from PIL import Image , ImageTk
import speech
import action

admin = Tk()
admin.title("Virtual Assistant")
admin.geometry("500x600")
admin.resizable(False, False)
admin.config(bg="#adc8ec")


#functions
def ask():
    user_val = speech.speech()
    bot_val = action.Action(user_val)
    text.insert(END, 'User: '+user_val+"\n")
    if bot_val is not None:
        text.insert(END,'Assistant: '+str(bot_val)+"\n")
    if bot_val == "shutting down":
        admin.destroy()


def send():
    send = area.get()
    bot = action.Action(send)
    text.insert(END,'User: '+send+"\n")
    if bot is not None:
        text.insert(END,'Assistant: '+str(bot)+"\n")
    if bot == "shutting down":
        admin.destroy()

def erase():
    text.delete("1.0", "end")

#sections
section = LabelFrame(admin, padx=58, pady=8, borderwidth=0, relief="sunken")
section.config(bg="#adc8ec")
section.grid(row=1, column=0, padx=67, pady=10)


#text
text = Label(section, text="Virtual Assistant", font=("Impact", "24"), bg="#adc8ec")
text.grid(row=0, column=0, padx=20, pady=10)

#image
image = ImageTk.PhotoImage(Image.open("image/ai1.jpg"))
image_label= Label(section, image= image)
image_label.grid(row=1, column=0, pady=20)

#text_area
text = Text(admin, font=("Arial", "10"), bg="#FFFFFF", borderwidth=1.0, highlightcolor="#fcf1d7")
text.grid(row=2, column=0)
text.place(x=76, y=370, width=360, height=100)

#widget
area = Entry(admin, justify="center", relief="groove", borderwidth=0.5, highlightcolor="#fcf1d7")
area.place(x=76, y=480, width=360, height=40)

#buttons
button1 = Button(admin, text="VOICE", font=("Arial","9"), bg="#fcf1d7", padx=16, pady=35, borderwidth=1.0, relief="groove", highlightcolor="#00FFFF", command=ask)
button1.place(x=76, y=540, width=90, height=50)

button2 = Button(admin, text="SEND", font=("Arial","9"), bg="#fcf1d7", padx=16, pady=35, borderwidth=1.0, relief="groove", highlightcolor="#00FFFF", command=send)
button2.place(x=225, y=540, width=70, height=50)

button3 = Button(admin, text="ERASE", font=("Arial","9"), bg="#fcf1d7", padx=16, pady=35, borderwidth=1.0, relief="groove", highlightcolor="#00FFFF", command=erase)
button3.place(x=364, y=540, width=70, height=50)

line_frame = LabelFrame(admin, height=3, width=508, borderwidth=3.5, relief="sunken")
line_frame.config(bg="#adc8ec")
line_frame.grid(row=2, column=0, padx=1, pady=5)

admin.mainloop()