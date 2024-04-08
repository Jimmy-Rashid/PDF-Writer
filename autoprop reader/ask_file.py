from tkinter import *
from tkinter import ttk
from tkinter import filedialog

window = Tk()
window.title("File Input Test")

mainframe = ttk.Frame(window, padding="5 5 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

file = filedialog.askopenfile(mode='r')
print(file.name)

window.mainloop()