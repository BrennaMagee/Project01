import csv
from tkinter import *
from tkinter.ttk import Combobox


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

        self.label_status = Label(self.user_info_frame, text='Status')
        self.label_status.grid(row=2, column=2)
        self.combobox_status = Combobox(self.user_info_frame, values=["Full-time", "Part-time", "Student",
                                                                      "Unemployed", "Prefer not to answer"])
        self.combobox_status.grid(row=3, column=2)

        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=5, pady=5)

        # Terms and conditions frame
        self.terms_frame = LabelFrame(self.frame)
        self.terms_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

        self.check_terms = Checkbutton(self.terms_frame, text="I have read and agree to the terms"
                                                              " and conditions.")
        self.check_terms.grid(row=0, column=0, sticky='w')
        self.check_rules = Checkbutton(self.terms_frame, text="I understand I am responsible for"
                                                              " abiding by the contest rules.")
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
        status = self.combobox_status.get()

        self.clear()

        with open('records.csv', 'a', newline='') as csvfile:
            content = csv.writer(csvfile, delimiter=',')
            content.writerow([last_name, first_name, age, email, phone, status])

    def clear(self):
        self.entry_first.delete(0, END)
        self.entry_last.delete(0, END)
        self.spinbox_age.delete(0, END)
        self.spinbox_age.insert(0, '18')
        self.entry_email.delete(0, END)
        self.entry_phone.delete(0, END)
        self.combobox_status.delete(0, END)
