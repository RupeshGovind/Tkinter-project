from tkinter import *
root = Tk()
root.geometry("1280x720")
def update_label():
    label.config(text="Button Clicked By Rupesh")
root.title("Tkinter Project")
label= Label(root,text="Hello Tkinter!",fg="blue",font="Ariel 20 bold")
label.pack()
button = Button(root,text="click me",bg="blue",command=update_label,font="Ariel 20 bold")
button.pack(pady=20)
root.mainloop()



