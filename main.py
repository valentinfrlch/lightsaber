# show a GUI windows with text input and a button
import downloader as dl
import analyzer as ay



import tkinter as tk

def main():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    # set the window size to 300x300
    root.geometry("500x300")

    label = tk.Label(frame, text="Search query")
    label.pack()

    entry = tk.Entry(frame)
    entry.pack()

    button = tk.Button(frame, text="Submit", command=lambda: print(entry.get()))
    button.pack()
    root.mainloop()
    
    # once the user clicks the button, print the text from the entry
    print(entry.get())
    # once the user clicks the button, download the first result from youtube
    
    
    
if __name__ == "__main__":
    main()