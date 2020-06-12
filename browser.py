
import socket 


import urllib.request
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from tkinterhtml import HtmlFrame

root = tk.Tk()

frame = HtmlFrame(root, horizontal_scrollbar="auto")
frame.grid(sticky=tk.NSEW)



def get_html(url):
    """Grab html code of a page given its URL"""
    usock = urllib.request.urlopen(url)
    html = usock.read()
    usock.close()
    return html


frame.set_content(get_html("https://www.google.com/"))
#frame.set_content("<h1>Hello World</h1>")




root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()

