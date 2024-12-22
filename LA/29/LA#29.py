import tkinter as tk

name = "Ivanmir Pogi"

root = tk.Tk()
root.title(f"OOP LA29 {name}")
root.geometry("500x500")
#root.configure(bg = "white")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text = "OOP LA29 IVANMIR_CUDALpogi BSIT-2A")
label.grid(row = 0, column = 0, padx=10, pady=10)


root.mainloop()
