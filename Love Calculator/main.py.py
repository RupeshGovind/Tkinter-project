
from tkinter import *
import pygame
from PIL import Image,ImageTk
from tkinter import messagebox
import random
pygame.init()
can_width  = 300
can_height = 500
root = Tk()
root.title("Love Calculator")
root.geometry(f"{can_width}x{can_height}")
root.maxsize(can_width,can_height)
root.minsize(can_width,can_height)
photo = PhotoImage(file="lovecalculator icon/relationship.png")
root.iconphoto(FALSE,photo)

# Load and resize the background image
images = Image.open("lovecalculator icon/heartbg.jpg")
resized_image = images.resize((800, 800))
bg_image = ImageTk.PhotoImage(resized_image)

# Create a canvas to hold the background image and other widgets
canvas = Canvas(root, width=can_width, height=can_height)
canvas.pack(fill=BOTH, expand=True)

# Display the background image on the canvas
canvas.create_image(0, 0, image=bg_image, anchor='nw')



def calculate_love():
  name1_val = entry1.get().strip()
  name2_val = entry2.get().strip()
  if not name1_val or not name2_val:
    messagebox.showerror("Error","Please Enter Both Name")
    return

  pygame.mixer.music.load("lovecalculator icon/dice.mp3")
  pygame.mixer.music.play()

  def delent():
   entry1.delete(0, END)
   entry2.delete(0, END)
  
  def show_suspense():
    st = "123456789"
    digit = 2
    temp = "".join(random.sample(st,digit))+"%"
    result.config(text=temp,font="helvitica 30 bold",relief="sunken")
  for i in range(40):
    root.after(i*300,show_suspense)

  root.after(14000,delent)

  

name1 = Label(text="Enter Your Name: ",relief="sunken")
name1.pack()
entry1 = Entry(root,border=5)
entry1.pack()

name2 = Label(root,text="Enter Your Partner Name: ",relief="sunken")
name2.pack()
entry2 = Entry(root,border=5)
entry2.pack()

bt = Button(root,text="Calculate",command=calculate_love)
bt.pack()

result = Label(root,text= "Love Percentage Between Both OF You:")
result.pack()

canvas.create_window(150, 20, window=name1)
canvas.create_window(150, 60, window=entry1)
canvas.create_window(150, 100, window=name2)
canvas.create_window(150, 140, window=entry2)
canvas.create_window(150, 180, window=bt)
canvas.create_window(150, 220, window=result)


root.mainloop()