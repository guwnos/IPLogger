import webbrowser
import tkinter as tki

root = tki.Tk()
root.title("SNIFFIP by Guwnos")
root.geometry("300x45")
root.iconbitmap(r"resources\v1.ico")

def funkcja():
    i = 0

    while i < 30:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

url = tki.Entry(root, width=40)
url.pack()

gener = tki.Button(root, text="Generate", bg="#91ffaf", command=funkcja)
gener.pack()


root.mainloop()