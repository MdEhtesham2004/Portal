from tkinter import *
from app import App

FONT = ("Courier", 22, "bold")


window = Tk()
window.title("Portal")
window.geometry("550x500")
window.config(bg="purple")


app = App(window)
app.pack(fill="both", expand=True)
app.show_login_frame()

window.mainloop()

