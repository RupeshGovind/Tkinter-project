from tkinter import *
import time
root = Tk()
root.geometry("1280x720")
def update_clock():
    current_time = time.strftime("%I:%M:%S:%p")
    label.config(text=current_time)
    root.after(1000,update_clock)

label = Label(root,text="Digital Clock",font="century 200",bg="black",fg="white")
label.pack()
update_clock()
root.mainloop()