import tkinter as tk

marks_dict = {
    's': 10,
    'a': 9,
    'b': 8,
    'c': 7,
    'd': 6,
    'e': 5
}


class CGPACalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CGPA Calculator")

        self.main_grades = []
        self.lab_grades = []

        # Main subjects input frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=10)

        tk.Label(self.main_frame, text="Enter main subject grades:").pack()
        self.main_subjects_entry = tk.Entry(self.main_frame)
        self.main_subjects_entry.pack()

        # Lab subjects input frame
        self.lab_frame = tk.Frame(root)
        self.lab_frame.pack(pady=10)

        tk.Label(self.lab_frame, text="Enter lab grades:").pack()
        self.lab_subjects_entry = tk.Entry(self.lab_frame)
        self.lab_subjects_entry.pack()

        # Calculate button
        self.calculate_button = tk.Button(root, text="Calculate CGPA", command=self.calculate_cgpa)
        self.calculate_button.pack(pady=10)

        # Result label
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def calculate_cgpa(self):
        main_grades = self.main_subjects_entry.get().split()
        lab_grades = self.lab_subjects_entry.get().split()

        final_marks = []
        final_lab_marks = []

        for marks in main_grades:
            if marks in marks_dict:
                mark = marks_dict[marks] * 4
                final_marks.append(mark)

        for marks in lab_grades:
            if marks in marks_dict:
                mark = marks_dict[marks] * 2
                final_lab_marks.append(mark)

        total_main_marks = sum(final_marks)
        total_lab_marks = sum(final_lab_marks)

        final_cgpa = round((total_main_marks + total_lab_marks) / (4 * len(main_grades) + 2 * len(lab_grades)), 1)

        self.result_label.config(text=f"Your CGPA is: {final_cgpa}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CGPACalculatorApp(root)
    root.mainloop()
