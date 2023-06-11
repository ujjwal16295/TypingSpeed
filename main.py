import time
from tkinter import *
from tkinter import  messagebox
import datetime

start_time=0
end_time=0
speed=0
start_check=0

def timer_start():
    global  start_time,start_check
    start_time=time.time()
    print("started")
    text.config(state="normal")
    start_check=1

def timer_end():
    global end_time, speed
    if start_check==1:
        end_time = time.time()
        total_time = datetime.datetime.fromtimestamp(end_time).second - datetime.datetime.fromtimestamp(start_time).second
        print(total_time)
        words = text.get("1.0", 'end-1c')
        speed = len(words) / total_time
        new_text=(f"{speed} words per second")
        speed_label.config(text=new_text)
        label.config(text="")
    else:
        messagebox.showinfo(title="Can not submit",message="please start first")








windows=Tk()

windows.minsize(width=100,height=350)
label=Label(text="Type here")
speed_label=Label(text="0 words per second")

text=Text(height=30,width=80,state="disabled")
# text.insert("type here")
enter_button=Button(text="submit",command=timer_end)
start_button=Button(text="Start",command=timer_start)
label.grid(row=1,column=2)
start_button.grid(row=2,column=2)
text.grid(row=3,column=2)
enter_button.grid(row=4,column=2)
speed_label.grid(row=5,column=2)



windows.mainloop()
