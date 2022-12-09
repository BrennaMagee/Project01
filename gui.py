import csv
import re
from tkinter import *
from tkinter import messagebox

messagebox.showinfo("Contest Info", f"Students may enter as many times as they please.\n"
                                    f"Proper contact info is encouraged so winners can receive their prize.\n"
                                    f"Student ID numbers will be used to identify how many entries "
                                    f"were made by each student.\n")


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
        self.button_clear.grid(row=3, column=0, sticky="news", padx=20, pady=5)

        self.button_winner = Button(self.frame, text='SEE WHO WINS', command=self.selection)
        self.button_winner.grid(row=4, column=0, sticky="news", padx=20, pady=5)

        with open('contestants.csv', 'w', newline='') as csvfile:
            content = csv.writer(csvfile, delimiter=',')
            content.writerow("0")

        self.id_list = []
        self.entry_totals = {}

    def clicked_submit(self):
        first_name = self.entry_first.get()
        last_name = self.entry_last.get()
        age = self.spinbox_age.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        student_id = self.entry_id.get()
        terms_status = self.check_terms_status.get()
        rules_status = self.check_rules_status.get()

        email_check = re.compile(r'^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        phone_check = re.compile(r'^([0-9]{3})-([0-9]{3})-([0-9]{4})$')
        id_check = re.compile(r'^([0-9]{8})$')

        if not first_name.isalpha():
            messagebox.showwarning("Invalid First Name", "Names should only contain alphabetic characters.")
        elif not last_name.isalpha():
            messagebox.showwarning("Invalid Last Name", "Names should only contain alphabetic characters.")
        elif not email_check.search(email):
            messagebox.showwarning("Invalid Email", "The email entry does not contain an '@' symbol. Please "
                                                    "enter a valid email")
        elif not phone_check.search(phone):
            messagebox.showwarning("Invalid Phone Number", "Phone number entries should follow "
                                                           "the format XXX-XXX-XXXX.")
        elif not id_check.search(student_id):
            messagebox.showwarning("Invalid Student ID", "A student ID is a unique 8 number sequence used "
                                                         "to verify a student's identity. Please enter your ID.")
        elif not terms_status or not rules_status:
            messagebox.showwarning("Checkbox Warning", "Users must agree to the Terms and conditions as well as "
                                                       "the contest rules before am entry can be submitted.")
        else:
            self.clear()
            with open('contestants.csv', 'a', newline='') as csvfile:
                content = csv.writer(csvfile, delimiter=',')
                content.writerow([student_id, last_name, first_name, age, email, phone])

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

    def selection(self):
        with open('contestants.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for line in reader:
                student_id = line[0]
                self.id_list.append(student_id)
            for the_id in self.id_list:
                self.entry_totals[the_id] = self.entry_totals.get(the_id, 0) + 1

        with open('entry_count.csv', 'w', newline='') as csvfile:
            content = csv.writer(csvfile, delimiter=',')
            for key, value in self.entry_totals.items():
                content.writerow([key, value])

        # messagebox.showinfo("WINNER SELECTED", f"The winner is {first_name} {last_name} with {num_entries}!")
