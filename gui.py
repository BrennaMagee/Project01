import csv
import re
from tkinter import *
from tkinter import messagebox
from random import randrange

messagebox.showinfo("Contest Info", f"Students may enter as many times as they please.\n"
                                    f"Proper contact info is encouraged so winners can receive their prize.\n"
                                    f"Student ID numbers will be used to identify how many entries "
                                    f"were made by each student.\n")


class GUI:
    """
    Class that contains graphical user interface code and other functional aspects of the program
    """
    def __init__(self, window) -> None:
        """
        Constructor to create initial GUI and allow user interaction.
        """
        self.window = window
        self.frame = Frame(window)
        self.frame.pack()

        # User Information frame
        self.user_info_frame = LabelFrame(self.frame, text='User Information')
        self.user_info_frame.grid(row=0, column=0)

        # Label and entry box for user's first name
        self.label_first = Label(self.user_info_frame, text='First:')
        self.label_first.grid(row=0, column=0)
        self.entry_first = Entry(self.user_info_frame)
        self.entry_first.grid(row=1, column=0)

        # Label and entry box for user's last name
        self.label_last = Label(self.user_info_frame, text='Last:')
        self.label_last.grid(row=0, column=1)
        self.entry_last = Entry(self.user_info_frame)
        self.entry_last.grid(row=1, column=1)

        # Label and spinbox for user's age
        self.label_age = Label(self.user_info_frame, text="Age")
        self.label_age.grid(row=0, column=2)
        self.spinbox_age = Spinbox(self.user_info_frame, from_=18, to=100)
        self.spinbox_age.grid(row=1, column=2)

        # Label and entry box for user's email
        self.label_email = Label(self.user_info_frame, text='Email:')
        self.label_email.grid(row=2, column=0)
        self.entry_email = Entry(self.user_info_frame)
        self.entry_email.grid(row=3, column=0)

        # Label and entry box for user's phone number
        self.label_phone = Label(self.user_info_frame, text='Phone:')
        self.label_phone.grid(row=2, column=1)
        self.entry_phone = Entry(self.user_info_frame)
        self.entry_phone.grid(row=3, column=1)

        # Label and entry box for user's student ID number
        self.label_id = Label(self.user_info_frame, text='Student ID')
        self.label_id.grid(row=2, column=2)
        self.entry_id = Entry(self.user_info_frame)
        self.entry_id.grid(row=3, column=2)

        # Configuration of widget grid
        # Helps make the layout of all the widgets even and pleasing to the eye
        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=5, pady=5)

        # Terms and conditions and Contest rules frame
        self.terms_frame = LabelFrame(self.frame)
        self.terms_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

        # Below are the boolean variables used to recognize the state of the checkboxes
        # and the checkbox code
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

        # Buttons at bottom of GUI
        self.button_submit = Button(self.frame, text='SUBMIT ENTRY', command=self.clicked_submit)
        self.button_submit.grid(row=2, column=0, sticky="news", padx=20, pady=5)

        self.button_clear = Button(self.frame, text='CLEAR ENTRY', command=self.clear)
        self.button_clear.grid(row=3, column=0, sticky="news", padx=20, pady=5)

        self.button_winner = Button(self.frame, text='WINNER SELECTION', command=self.selection)
        self.button_winner.grid(row=4, column=0, sticky="news", padx=20, pady=5)

        # The two with open statements below overwrite the contents of the files
        # if previously filled by an earlier run.
        with open('contestants.csv', 'w', newline='') as csvfile:
            content = csv.writer(csvfile, delimiter=',')
            content.writerow("0")

        with open('entry_count.csv', 'w', newline='') as csvfile:
            content = csv.writer(csvfile, delimiter=',')

    def clicked_submit(self) -> None:
        """
        Method to pull information from the form, validate it, then write it to the contestants file.
        """
        first_name: str = self.entry_first.get()
        last_name: str = self.entry_last.get()
        age: str = self.spinbox_age.get()
        email: str = self.entry_email.get()
        phone: str = self.entry_phone.get()
        student_id: str = self.entry_id.get()
        terms_status: bool = self.check_terms_status.get()
        rules_status: bool = self.check_rules_status.get()

        # Regular expressions used to check the validity of input
        email_check = re.compile(r'^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        phone_check = re.compile(r'^([0-9]{3})-([0-9]{3})-([0-9]{4})$')
        id_check = re.compile(r'^([0-9]{8})$')

        # If/elif statement to verify each input necessary and alert of invalid input.
        if not first_name.isalpha():
            messagebox.showwarning("Invalid First Name", "Names should only contain alphabetic characters.")
        elif not last_name.isalpha():
            messagebox.showwarning("Invalid Last Name", "Names should only contain alphabetic characters.")
        elif not email_check.search(email):
            messagebox.showwarning("Invalid Email", "The email entry is either missing an '@' or a period. Please "
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

    def clear(self) -> None:
        """
        Method to clear all information typed in the form, and reset to default values.
        """
        self.entry_first.delete(0, END)
        self.entry_last.delete(0, END)
        self.spinbox_age.delete(0, END)
        self.spinbox_age.insert(0, '18')
        self.entry_email.delete(0, END)
        self.entry_phone.delete(0, END)
        self.entry_id.delete(0, END)
        self.check_terms.deselect()
        self.check_rules.deselect()

    def selection(self) -> None:
        """
        Method to select the winner of the contest and output the notification box alerting everyone who won.
        """
        row_count: int = 0
        id_list: list = []
        entry_totals: dict = {}

        # Reads file of contestant information
        with open('contestants.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skips the zero placed in the first line.
            reader_list: list = list(reader)

            for index in reader_list:
                row_count += 1  # counts number of rows so the proper range
                # can be used when generating random numbers for winner selection.
                student_id: int = index[0]
                id_list.append(student_id)  # Places all IDs into a list.
            for the_id in id_list:  # Counts the number of entries per ID and pairs them in a dictionary.
                entry_totals[the_id] = entry_totals.get(the_id, 0) + 1

            winner = reader_list[randrange(row_count)]  # Selects the winning index
            winner_name: str = f"{winner[2]} {winner[1]}"
            winner_id: int = winner[0]
            winner_num_entries: int = entry_totals.get(winner_id)

        # Writes the student ID and number of entries per ID so users can see how many entries each user had.
        with open('entry_count.csv', 'w', newline='') as csvfile:
            content = csv.writer(csvfile, delimiter=',')
            for key, value in entry_totals.items():
                content.writerow([key, value])

        messagebox.showinfo("WINNER SELECTED", f"The winner is {winner_name} ({winner_id}) with "
                                               f"{winner_num_entries} entries!")
