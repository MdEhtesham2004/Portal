from tkinter import *
from cgpa import CGPACalculatorApp
FONT = ("Courier", 22, "bold")


class MainFrame(Frame):
    def __init__(self, master, app_instance):
        super().__init__(master, bg="purple")
        self.cal = None
        self.master = master
        self.app_instance = app_instance

        self.label = Label(self, text="Welcome to Main Frame", fg="green", font=FONT)
        self.label.grid(row=0, column=1, columnspan=3)

        self.cgpa_calculator = Button(self, text="Calculate", height=2, command=self.open_cgpa_calculator)
        self.cgpa_calculator.grid(row=1, column=1, columnspan=2, rowspan=2, pady=100)

        self.attendance = Button(self, text="Attendance", height=2)
        self.attendance.grid(row=1, column=3, columnspan=2, rowspan=2)

        self.updates = Button(self, text="Updates", height=2)
        self.updates.grid(row=3, column=1, columnspan=2, rowspan=2, pady=20)

        self.exam_schedule = Button(self, text="Exam Schedule", height=2)
        self.exam_schedule.grid(row=3, column=3, columnspan=2, rowspan=2)

    def open_cgpa_calculator(self):
        if self.cal is None:
            self.cal = Toplevel(self)
            CGPACalculatorApp(self.cal)
            self.cal.protocol("WM_DELETE_WINDOW", self.on_cgpa_calculator_close)

    def on_cgpa_calculator_close(self):
        self.cal.destroy()
        self.cal = None
