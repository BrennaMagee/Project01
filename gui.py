import csv
from tkinter import *
from tkinter import messagebox


class GUI:
    def __init__(self, window):
        self.window = window
        self.frame = Frame(window)
        self.frame.pack()

        # User Information frame
        self.user_info_frame = LabelFrame(self.frame, text='User Information')
        self.user_info_frame.grid(row=0, column=0)

        self.label_first = Label(self.user_info_frame, text='First:')
        self.label_first.grid(row=0, column=0)
        self.entry_first = Entry(self.user_info_frame)
        self.entry_first.grid(row=1, column=0)

        self.label_last = Label(self.user_info_frame, text='Last:')
        self.label_last.grid(row=0, column=1)
        self.entry_last = Entry(self.user_info_frame)
        self.entry_last.grid(row=1, column=1)

        self.label_age = Label(self.user_info_frame, text="Age")
        self.label_age.grid(row=0, column=2)
        self.spinbox_age = Spinbox(self.user_info_frame, from_=18, to=100)
        self.spinbox_age.grid(row=1, column=2)

        self.label_email = Label(self.user_info_frame, text='Email:')
        self.label_email.grid(row=2, column=0)
        self.entry_email = Entry(self.user_info_frame)
        self.entry_email.grid(row=3, column=0)

        self.label_phone = Label(self.user_info_frame, text='Phone:')
        self.label_phone.grid(row=2, column=1)
        self.entry_phone = Entry(self.user_info_frame)
        self.entry_phone.grid(row=3, column=1)

        self.label_id = Label(self.user_info_frame, text='Student ID')
        self.label_id.grid(row=2, column=2)
        self.entry_id = Entry(self.user_info_frame)
        self.entry_id.grid(row=3, column=2)

        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=5, pady=5)

        # Terms and conditions and Contest rules frame
        self.terms_frame = LabelFrame(self.frame)
        self.terms_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

        self.check_terms_status = BooleanVar()
        self.check_terms = Checkbutton(self.terms_frame,
                                       text="I have read and agree to the terms"
                                            " and conditions.",
                                       variable=self.check_terms_status,
                                       onvalue=1, offvalue=0)
        self.check_terms.grid(row=0, column=0, sticky='w')
        self.check_rules_status = BooleanVar()
        self.check_rules = Checkbutton(self.terms_frame,
                                       text="I understand I am responsible for"
                                            " abiding by the contest rules.",
                                       variable=self.check_rules_status,
                                       onvalue=1, offvalue=0)
        self.check_rules.grid(row=1, column=0, sticky='w')

        for widget in self.terms_frame.winfo_children():
            widget.grid_configure(padx=35, pady=5)

        # Buttons
        self.button_submit = Button(self.frame, text='SUBMIT ENTRY', command=self.clicked_submit)
        self.button_submit.grid(row=2, column=0, sticky="news", padx=20, pady=5)

        self.button_clear = Button(self.frame, text='CLEAR ENTRY', command=self.clear)
        self.button_clear.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    def clicked_submit(self):
        first_name = self.entry_first.get()
        last_name = self.entry_last.get()
        age = self.spinbox_age.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        student_id = self.entry_id.get()
        terms_status = self.check_terms_status.get()
        rules_status = self.check_rules_status.get()

        if terms_status and rules_status:
            self.clear()
            with open('contestants.csv', 'a', newline='') as csvfile:
                content = csv.writer(csvfile, delimiter=',')
                content.writerow([student_id, last_name, first_name, age, email, phone])
        elif not terms_status or not rules_status:
            messagebox.showerror("Checkbox Error", "Users must agree to the Terms and conditions as well as "
                                                   "the contest rules before am entry can be submitted.")

    def clear(self):
        self.entry_first.delete(0, END)
        self.entry_last.delete(0, END)
        self.spinbox_age.delete(0, END)
        self.spinbox_age.insert(0, '18')
        self.entry_email.delete(0, END)
        self.entry_phone.delete(0, END)
        self.entry_id.delete(0, END)
        self.check_terms.deselect()
        self.check_rules.deselect()
