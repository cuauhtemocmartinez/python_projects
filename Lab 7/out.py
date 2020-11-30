###########################################################################
# Program Header
# Course: CIS 117 Python Programming
# Name: Cuauhtemoc Alex Martinez
# Description: Lab 7
# Application: Creating an e-mail Message Class
# Topics: Objects and Classes
# Development Environment: Windows 10
# Version: Python 3.8.2
# Solution File: CMartinezLab7
# Due date: 03/17/20
###########################################################################

# Program Source Statements

class Message:
    
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        
    def add_body(self, body):
        self.body = []
        self.body.append(body)
        






