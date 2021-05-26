#Creating GUI with tkinter
import tkinter
from tkinter import *


def send():

    msg = EntryBox.get("1.0",'end-1c').strip()
    
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#000402", font=("Verdana", 12 ))
    
        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
 

base = Tk()
base.title("Pillai Hoc College Bot")
base.geometry("400x465")

base.resizable(width=FALSE, height=FALSE)

#Create Chat window

ChatLog = Text(base, bd=2, bg="#D5F5E3", height="12", width="120", font="Arial",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="8", height=5,
                    bd=4, bg="#186A3B", activebackground="#58D68D",fg='#ffffff',
                    command=send )

#Create the box to enter message
EntryBox = Text(base, bd=4, bg="white",width="110", height="10", font="Verdana")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=120, y=401, height=50, width=256)
SendButton.place(x=6, y=401, height=50)

base.mainloop()
