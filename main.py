# show a GUI windows with text input and a button
import downloader as dl
import analyzer as ay

import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()
root.geometry('500x300')
root.title('Lightsaber')
root.grid()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

text_box = tk.Entry(root)
# make the text box fill the window

# add text
tk.Label(root, text="Enter a song name to analyze:").grid(row=0, column=0)
text_box.insert(0, 'Enter your search query here...')
text_box.grid(column=0, row=1, columnspan=2, sticky='we', padx=10, pady=20)

pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=280
)
# place the progressbar
pb.grid(column=0, row=2, columnspan=2, padx=10, pady=20)
  
#---------------------------------------
# handle the events:
#---------------------------------------

def on_click(event):
    if text_box.get() == 'Enter your search query here...':
        text_box.delete(0, "end")
        text_box.insert(0, '')
        text_box.config(fg = 'black')

def start():
    query = text_box.get()
    pb.start
    path = dl.download(query)
    pb.stop
    tempo, beats = ay.get_beats(path)
    print(tempo)
        
clicked = text_box.bind('<Button-1>', on_click)

# start button
start_button = tk.Button(root, text="Start", command=lambda: start())
start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

root.mainloop()