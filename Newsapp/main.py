from tkinter import *
from PIL import ImageTk, Image
import time 
import textwrap

def wrap_text(text, width=50):
    wrapped_text = textwrap.fill(text, width)
    return wrapped_text

def on_configure(event):
    # Update scroll region to fit the size of the inner frame
    canvas.configure(scrollregion=canvas.bbox("all")) 

def update_clock():
    current_time = time.strftime("%d-%m-%y %H:%M:%S")
    l1.config(text=f"Breaking News\n{current_time}")
    root.after(1000, update_clock)

root = Tk()
root.title("News")
root.maxsize(800,800)
root.geometry("800x800")

texts = []
photos = []

for i in range(0, 3):
    with open(f"text{i+1}.txt") as f:
        text = f.read()
        texts.append(wrap_text(text))  # Wrap the text
    image = Image.open(f"news{i+1}.jpg")
    image = image.resize((225, 400))
    photos.append(ImageTk.PhotoImage(image))

# Create a canvas and scrollbar
canvas = Canvas(root)
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

# Bind the function to the canvas' configuration
scrollable_frame.bind("<Configure>", on_configure)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Adding content to the scrollable frame
f0 = Frame(scrollable_frame, width=800, height=70)
f0.pack(fill="both")
l1 = Label(f0, text="Breaking News", font="lucida 33 bold")
l1.pack(fill=BOTH)

f1 = Frame(scrollable_frame, width=900, height=200,relief="groove",borderwidth=3)
f1.pack(pady=30,fill=BOTH)
Label(f1, image=photos[0]).pack(side="right", anchor="n")
Label(f1, text=texts[0], padx=88, pady=22, font="helvetica 10 bold").pack()

f2 = Frame(scrollable_frame, width=900, height=200,relief="groove",borderwidth=3)
f2.pack(fill="both")
Label(f2, image=photos[1]).pack(side="right", anchor="n")
Label(f2, text=texts[1], padx=22, pady=22, font="helvetica 10 bold").pack(side=LEFT, anchor="n")

f3 = Frame(scrollable_frame, width=900, height=200,relief="groove",borderwidth=3)
f3.pack(pady=30,fill=BOTH)
Label(f3, image=photos[2]).pack(side="right", anchor="n",fill=BOTH)
Label(f3, text=texts[2], padx=22, pady=22, font="helvetica 10 bold").pack(fill=BOTH)

# Start the clock
update_clock()

root.mainloop()
