from tkinter import *
import connect as con
import time
from mail import Mail
import hashlib


def hashed(value):
    input_password = value
    h1 = hashlib.sha256()
    h1.update(input_password.encode())
    input_password_hash = h1.hexdigest()
    return input_password_hash


FONT = ("Courier", 22, "bold")

mail = Mail()


class SignupFrame(Frame):
    def __init__(self, master, app_instance):
        super().__init__(master, bg="purple")
        self.master = master
        self.app_instance = app_instance  # Store the instance of the App class

        self.signup_label = Label(self, text="Sign up:", bg="purple", fg="white", font=FONT)
        self.signup_label.grid(row=0, column=0, pady=30)

        self.name = Entry(self, width=30, border=5, borderwidth=5)
        self.name.insert(END, "What's your name?")
        self.name.grid(row=1, column=0, pady=10)

        self.Email_input_signup = Entry(self, width=30, border=5, borderwidth=5)
        self.Email_input_signup.insert(END, "Enter your Email")
        self.Email_input_signup.grid(row=2, column=0, pady=10)

        self.password_input_signup = Entry(self, width=30, border=5, borderwidth=5)
        self.password_input_signup.insert(END, "Enter your password")
        self.password_input_signup.grid(row=3, column=0, pady=10)

        self.confirm_password_input_signup = Entry(self, width=30, border=5, borderwidth=5)
        self.confirm_password_input_signup.insert(END, "Confirm password")
        self.confirm_password_input_signup.grid(row=4, column=0, pady=10)

        self.submit_button_signup = Button(self, text="Submit", border=5, borderwidth=5,
                                           command=self.submit_entry)
        self.submit_button_signup.grid(row=5, column=0, pady=10)

        self.reset_button_signup = Button(self, text="Reset", border=5, borderwidth=5,
                                          command=self.reset_entries)
        self.reset_button_signup.grid(row=6, column=0, pady=10)

        self.switch_login = Button(self, text="Switch to login?", bg="purple", fg="white",
                                   command=self.app_instance.switch_frame)
        self.switch_login.grid(row=7, column=0)

        self.signup_successful = Label(self, text="Signup successful!", bg="purple", font=FONT, fg="white")

        self.password_mismatch = Label(self, text="Password Mismatch!", bg="purple", font=FONT, fg="white")

        self.credentials_exists = Label(self, text="Credentials already exists!", bg="purple", font=FONT, fg="white")

        self.wrong_email = Label(self, text="Wrong Email!", bg="purple", font=FONT, fg="white")

    def submit_entry(self):
        if self.check_password():
            name = self.name.get()
            email = self.Email_input_signup.get()
            password = self.password_input_signup.get()

            if not con.check_credentials(email, password):
                if mail.check(str(email)):
                    con.insert_entry(name, email, hashed(password))
                    self.signup_successful.grid(row=0, column=0)
                    self.update_idletasks()
                    time.sleep(1)
                    self.app_instance.show_login_frame()
                else:
                    print("Wrong Email")
                    self.wrong_email.grid(row=0, column=0)
            else:
                print("Credentials already exist!!")
                self.credentials_exists.grid(row=0, column=0)
        else:
            print("Password and confirm password do not match!")
            self.password_mismatch.grid(row=0, column=0)

    def reset_entries(self):
        self.name.delete(0, END)
        self.Email_input_signup.delete(0, END)
        self.password_input_signup.delete(0, END)
        self.confirm_password_input_signup.delete(0, END)

    def check_password(self):
        return self.password_input_signup.get() == self.confirm_password_input_signup.get()
