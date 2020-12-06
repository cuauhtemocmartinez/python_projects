###########################################################################
# Program Header
# Course: CIS 117 Python Programming
# Name: Cuauhtemoc Alex Martinez
# Description: Lab 8
# Application: Creating a Kilometer to Miles Converter
# Topics: GUI Programming
# Development Environment: Windows 10
# Version: Python 3.8.2
# Solution File: CMartinezLab8
# Due date: 03/24/20
###########################################################################

# Program Source Statements

from tkinter import *
from tkinter.messagebox import showinfo, showerror


class window:
    '''an application that converts Kilometers to Miles'''

    def __init__(self, root): # Frame
        frame = LabelFrame(root, text='Please input a number into the' \
                          ' field below', padx=5, pady=5)
        frame.pack(padx=10, pady=10) # Frame padding
        root.title("Kilometers to Miles Converter") # Frame title

        # entry
        self.ent = Entry(frame, width=48, borderwidth=5)
        self.ent.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # create button labeled 'Convert' and event handler new_win()
        self.button1 = Button(frame, text='Convert', command=self.new_win)
        # button click triggers convert_num

        # create button labeled 'Quit' and button to close GUI
        self.button2 = Button(frame, text='Quit', command=frame.quit)
        
        # create location of buttons
        self.button1.grid(row=1, column=0)
        self.button2.grid(row=1, column=2, pady=5)
    
    def new_win(self):
        '''displays conversion or error in new window'''

        try:
            kilometers = float(self.ent.get())
            # Taking kilometers input from field
            conv_fac = 0.621371  # conversion factor
            miles = kilometers * conv_fac  # calculate miles
            showinfo(message = "{} km equals {} miles.".format(str(format\
            (float(kilometers), ",.1f")), str(format(float(miles), ",.1f"))))
            # open up second window with result
            self.ent.delete(0, END)  # clears entry
        except ValueError:  # May raise a ValueError exception.
           showerror(message = "Error: Please input a number")
           # Message for showerror
           self.ent.delete(0, END)  # clears entry

        
root = Tk()
exec = window(root) # executes
root.mainloop()

# Program Output

"""
See Screenshot -> CMartinezLab8demo.png
"""