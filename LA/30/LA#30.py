import tkinter as tk

name = "Ivanmir Pogi"

root = tk.Tk()
root.title(f"OOP LA30 {name}")
root.geometry("500x500")
#root.configure(bg = "white")

frame = tk.Frame(root)
frame.pack(pady=20)

fav = "Irregular at Magic HighSchool"
count = 0
def display():
    global count
    global fav
    print(f"{count} My favorite anime is {fav}")
    count+=1

button = tk.Button(frame, text = "TAP", command = display)
button.pack(pady=10)
root.mainloop()
