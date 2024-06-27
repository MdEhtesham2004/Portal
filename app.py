from tkinter import *
from main_frame import MainFrame
from login_frame import LoginFrame
from signup_frame import SignupFrame

FONT = ("Courier", 22, "bold")


class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.login_frame = LoginFrame(master, self)  # Pass the App instance to LoginFrame
        self.signup_frame = SignupFrame(master, self)  # Pass the App instance to SignupFrame
        self.main_frame = MainFrame(master, self)
        self.current_frame = None

    def show_login_frame(self):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.login_frame
        self.login_frame.pack()

    def show_signup_frame(self):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.signup_frame
        self.signup_frame.pack()

    def switch_frame(self):
        if self.current_frame == self.login_frame:
            self.show_signup_frame()
        else:
            self.show_login_frame()

    def show_mainframe(self):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.main_frame
        self.main_frame.pack()
