import csv
from tkinter import *


class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Enter Name')
        self.label_first = Label(self.frame_name, text='First:')
        self.entry_first = Entry(self.frame_name)
        self.label_last = Label(self.frame_name, text='Last:')
        self.entry_last = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='left')
        self.label_first.pack(padx=10, side='left')
        self.entry_first.pack(padx=1, side='left')
        self.label_last.pack(padx=5, side='left')
        self.entry_last.pack(padx=1, side='left')
        self.frame_name.pack(anchor='w', pady=10)  # anchor='w' helps to change the frame position from center to west.

        self.frame_contact = Frame(self.window)
        self.label_contact = Label(self.frame_contact, text='Contact Info')
        self.label_email = Label(self.frame_contact, text='Email:')
        self.entry_email = Entry(self.frame_contact)
        self.label_phone = Label(self.frame_contact, text='Phone:')
        self.entry_phone = Entry(self.frame_contact)
        self.label_contact.pack(padx=5, side='left')
        self.label_email.pack(padx=10, side='left')
        self.entry_email.pack(padx=1, side='left')
        self.label_phone.pack(padx=5, side='left')
        self.entry_phone.pack(padx=1, side='left')
        self.frame_contact.pack(anchor='w', pady=10)

        self.frame_status = Frame(self.window)
        self.radio_var = IntVar()
        self.radio_var.set(0)
        self.label_status = Label(self.frame_status, text='Status')
        self.radio_student = Radiobutton(self.frame_status, text='Student', variable=self.radio_var, value=1)
        self.radio_staff = Radiobutton(self.frame_status, text='Staff', variable=self.radio_var, value=2)
        self.radio_both = Radiobutton(self.frame_status, text='Both', variable=self.radio_var, value=3)
        self.label_status.pack(padx=5, side='left')
        self.radio_student.pack(padx=5, side='left')
        self.radio_staff.pack(padx=5, side='left')
        self.radio_both.pack(padx=5, side='left')
        self.frame_status.pack(anchor='w', pady=10)

        self.frame_buttons = Frame(self.window)
        self.button_enter = Button(self.frame_buttons, text='SUBMIT ENTRY', command=self.clicked_submit)
        self.button_enter.pack()
        self.button_clear = Button(self.frame_buttons, text='CLEAR ENTRY', command=self.clear)
        self.button_clear.pack()
        self.frame_buttons.pack(anchor='n')

    def clicked_submit(self):
        first_name = self.entry_first.get()
        last_name = self.entry_last.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()

        status = 'Unselected'
        radio = self.radio_var.get()

        if radio == 1:
            status = 'Student'
        elif radio == 2:
            status = 'Staff'
        elif radio == 3:
            status = 'Both'

        self.clear()

        with open('records.csv', 'a', newline='') as csvfile:
            content = csv.writer(csvfile, delimiter=',')
            content.writerow([last_name, first_name, email, phone, status])

    def clear(self):
        self.entry_first.delete(0, END)
        self.entry_last.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_phone.delete(0, END)
        self.radio_var.set(0)
