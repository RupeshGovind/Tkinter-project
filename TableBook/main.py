import tkinter  as tk
import time
import random



def enter_pressed():
    table_value = table_entry.get()
    if table_value.isdigit():
        table_value = int(table_value)
        table_label.config(text=f"Table of {table_value}",background="grey")

        for i in range(1, 11):
            result_label.config(text=result_label.cget("text") + f"{table_value} x {i} = {table_value * i}\n",background="light grey")
            table_entry.delete(0, tk.END)
            root.update()
            time.sleep(0.05)
    else:
        result_label.config(text="Please enter a valid number!")
   
        

root = tk.Tk()
root.title("Table Book")
root.maxsize(200,425)


table_entry = tk.Entry(root, font=('Arial', 14))
table_entry.pack(pady=10)

enter_button = tk.Button(root, text="Enter", command=enter_pressed)
enter_button.pack(pady=10)

table_label = tk.Label(root, text="Find Table", font=('Arial', 20))
table_label.pack(pady=20)

result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.pack(pady=10)


root.mainloop()