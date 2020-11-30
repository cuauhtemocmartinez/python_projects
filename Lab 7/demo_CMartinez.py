###########################################################################
# Program Header
# Course: CIS 117 Python Programming
# Name: Cuauhtemoc Alex Martinez
# Description: Lab 7
# Application: Creating an e-mail Message Class
# Topics: Objects and Classes
# Development Environment: Windows 10
# Version: Python 3.8.2
# Solution File: CMartinezLab6
# Due date: 03/17/20
###########################################################################

# Program Source Statements

import CMartinezLab7 # import Message

def main():

    email = CMartinezLab7.Message('Alex', 'Terri')#Create the message 
    email.add_body('What do you think the Cat is doing?') #with variables

    email.to_string() #runs to_string function to print string

if __name__ == '__main__':
    main()  # call main function

import datetime  # datetime

d = datetime.date.today()
print(d)

# Program Output

"""
From: Alex 

To: Terri 

Message: 

['What do you think the Cat is doing?']

2020-03-17

"""
