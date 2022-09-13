# show a GUI windows with text input and a button
import downloader as dl
import analyzer as ay
import threading

import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('500x300')
root.title('Lightsaber')
root.grid()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
text_box = ttk.Entry(root)
# make the text box fill the window
# add text
label = ttk.Label(root, text="Enter a song name to analyze:")
label.grid(row=0, column=0)
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
# --------------backend-----------------
#---------------------------------------

def on_click(event):
    if text_box.get() == 'Enter your search query here...':
        text_box.delete(0, "end")
        text_box.insert(0, '')
        text_box.config(fg = 'black')


def check(t, mode):
    if t.is_alive():
        root.after(100, check, t, mode)
    else:
        t.join()
        pb.stop()
        if mode == "download":
            from downloader import cache_location
            print(cache_location)
            s = threading.Thread(target=ay.get_beats, args=(cache_location,))
            s.start()
            pb.start()
            root.after(100, check, s, "analyze")
        elif mode == "analyze":
            from analyzer import tempo, beats
            pb.stop()
            pb.grid_remove()
            print(tempo, beats)

def start():
    query = text_box.get()
    # run in a separate thread
    query = text_box.get()
    # run in a separate thread
    t = threading.Thread(target=dl.download, args=(query,))
    # change the label text
    label.config(text="Downloading " + query)
    t.start()
    pb.start()
    # check periodically if the thread is still alive
    root.after(100, check, t, "download")
        
clicked = text_box.bind('<Button-1>', on_click)

# start button

start_button = ttk.Button(root, text="Start", command=start)
start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)


root.mainloop()