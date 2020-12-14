#################################################################
# Program Header
# Course: CIS 117 Python Programming
# Name: Cuauhtemoc Alex Martinez
# Description: Lab 2
# Application: Print Expressions
# Topics: Arithmetic, Data Types, User Input, Importing Modules
# Development Environment: Windows 10
# Version: Python 3.7.4
# Solution File: CMartinezLab2
# Date: 02/4/20
#################################################################

#Program Source Statements

num_let = input("Enter your family name: ")
total = len(num_let)
print("num_let is: ", + total)

my_id = input("Enter your Student ID: ")
n = my_id
numlist = [n[0], n[1], n[2], n[3], n[4], n[5], n[6], n[7]]
addList = (int(n[0]) + int(n[1]) + int(n[2]) + int(n[3]) + int(n[4]) + int(n[5])
    + int(n[6]) + int(n[7]))

print("my_id is: ", + round(addList, 2)) 

print("expression1: ", + addList / 2)

print("expression2: ", + addList % 2)

min = 2
exper3 = 8 if total == min else sum(range(2, total + 1))
print("expression3: ", + exper3)

print("expression4: ", + addList + total)

both = (total - addList)
print("expression5: ", + abs(both))      

print("expression6: ", + round((addList) / (total + 1100), 2))

print("expression7: ", + (total % total) and (addList * addList))

print("expression8: ", + 1 or (addList / 0))

print("expression9: ", + round(3.15, 1))

import datetime
d = datetime.date.today()
print(d)

# Program Output

"""
Enter your family name: Martinez
num_let is:  8
Enter your Student ID: 01010673
my_id is:  18
expression1:  9.0
expression2:  0
expression3:  35
expression4:  26
expression5:  10
expression6:  0.02
expression7:  0
expression8:  1
expression9:  3.1
2020-02-04
"""
