from tkinter import *
import connect as con
import time
from signup_frame import hashed
FONT = ("Courier", 22, "bold")


class LoginFrame(Frame):
    def __init__(self, master, app_instance):
        super().__init__(master, bg="purple")
        self.master = master
        self.app_instance = app_instance  # Store the instance of the App class
        self.label_Email = Label(self, text="Login:", bg="purple", fg="white", font=FONT)
        self.label_Email.grid(row=0, column=5, pady=30)

        self.Email_input = Entry(self, width=30, border=5, borderwidth=5)
        self.Email_input.insert(END, "Enter your Email")
        self.Email_input.grid(row=1, column=5, pady=5)

        self.password_input = Entry(self, width=30, border=5, borderwidth=5)
        self.password_input.insert(END, "Enter your password")
        self.password_input.grid(row=2, column=5, pady=10)

        self.submit_button = Button(self, text="Submit", border=5, borderwidth=5,
                                    command=self.login)
        self.submit_button.grid(row=3, column=5, pady=5)

        self.reset_button = Button(self, text="Reset", border=5, borderwidth=5,
                                   command=self.reset_entries)
        self.reset_button.grid(row=4, column=5, pady=10)

        self.switch_signup = Button(self, text="Sign up?", fg="white",
                                    bg="purple", command=self.app_instance.switch_frame)
        self.switch_signup.grid(row=5, column=5, pady=10)

        self.login_successful = Label(self, text="Login Successful!", bg="purple", font=FONT, fg="white")

        self.credentials_mismatch = Label(self, text="Credentials does not match!",  bg="purple", font=FONT, fg="white")

    def login(self):
        email = self.Email_input.get()
        password = self.password_input.get()
        if con.check_credentials(email, hashed(password)):
            print("Login successful!")
            self.login_successful.grid(row=0, column=5)
            self.update_idletasks()
            time.sleep(1)
            self.app_instance.show_mainframe()
        else:
            print("Credentials do not match!")
            self.credentials_mismatch.grid(row=0, column=5)

    def reset_entries(self):
        self.Email_input.delete(0, END)
        self.password_input.delete(0, END)
