import csv
from tkinter import *


class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Name')
        self.entry_name = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=10)  # anchor='w' helps to change the frame position from center to west.

        self.frame_age = Frame(self.window)
        self.label_age = Label(self.frame_age, text='Age')
        self.entry_age = Entry(self.frame_age)
        self.label_age.pack(padx=5, side='left')
        self.entry_age.pack(padx=10, side='left')
        self.frame_age.pack(anchor='w', pady=10)

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

        self.frame_button = Frame(self.window)
        self.button_save = Button(self.frame_button, text='SAVE', command=self.clicked)
        self.button_save.pack()
        self.frame_button.pack(anchor='n')

    def clicked(self):
        name = self.entry_name.get()
        age = int(self.entry_age.get()) * 2
        status = 'Unselected'
        radio = self.radio_var.get()

        if radio == 1:
            status = 'Student'
        elif radio == 2:
            status = 'Staff'
        elif radio == 3:
            status = 'Both'

        with open('records.csv', 'a', newline='') as csvfile:
            content = csv.writer(csvfile, delimiter=',')
            content.writerow([name, age, status])

        self.entry_name.delete(0, END)
        self.entry_age.delete(0, END)
        self.radio_var.set(0)
