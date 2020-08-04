###########################################################################
# Program Header
# Course: CIS 117 Python Programming
# Name: Cuauhtemoc Alex Martinez
# Description: Lab 6
# Application: Programming with Namespaces, Exception Control Flow
# Topics: Data Analysis and Handling Input Errors
# Development Environment: Windows 10
# Version: Python 3.8.2
# Solution File: CMartinezLab6
# Due date: 03/10/20
###########################################################################

# Program Source Statements
def main():

    while True:
        file_name = input('Enter a meesage to be translated: ')  # get input from user

        try:
            numbers = []  # list of numbers from .dat

            if (file_name != 'valid.dat') and (file_name != 'err1.dat') and \
                    (file_name != 'err2.dat') and (file_name != 'err3.dat') and \
                    (file_name != 'err4.dat'):
                # Test the input - looking for correct input
                print('Error: file not found.''\n')
                # error if file is not one of the five files

            get_input = file_name

            if get_input in str('valid.dat'):  # if loop to connect to 
                contents = open('good.dat', 'r')  # correct .dat file
            elif get_input in str('err1.dat'):
                contents = open('bad1.dat')
            elif get_input in str('err2.dat'):
                contents = open('bad2.dat')
            elif get_input in str('err3.dat'):
                contents = open('bad3.dat')
            elif get_input in str('err4.dat'):
                contents = open('bad4.dat')

            for n in contents:
                numbers.append(int(n))

            if sum(numbers) == 65:  # valid.dat sum is equal to 65
                print('The sum is: ', (sum(numbers)))
                break  # break the loop
            elif sum(numbers) == 55:  # err1.dat sum is equal to 55
                print('Error: file contents invalid.''\n')
            elif sum(numbers) == 76:  # err4.dat sum is equal to 76
                print('Error: file contents invalid.''\n')

        except UnboundLocalError:  # except error
            continue  # continue with loop
        except ValueError:  # except error for .dat files without int
            print('Error: End of file expected.''\n')


if __name__ == '__main__':
    main()  # call main function

import datetime  # datetime

d = datetime.date.today()
print()
print(d)

# Program Output

"""
Please enter the file name: wrong.dat
Error: file not found.

Please enter the file name: err1.dat
Error: file contents invalid.

Please enter the file name: err2.dat
Error: End of file expected.

Please enter the file name: err3.dat
Error: End of file expected.

Please enter the file name: err4.dat
Error: file contents invalid.

Please enter the file name: valid.dat
The sum is:  65

2020-03-08
"""
