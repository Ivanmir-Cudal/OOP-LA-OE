print("OE#8")
import tkinter as tk

name = "Ivanmir Pogi"

root = tk.Tk()
root.title(f"Task management ni {name}")
root.geometry("500x500")

count = 1
def display():
    global count
    task = entry.get()
    print(f"{count}. {task}")
    count+=1
    

entry = tk.Entry(root)
entry.grid(row = 0, column=1)
button = tk.Button(text = "TAP", command = display)
button.grid(row = 0, column=6)
root.mainloop()
