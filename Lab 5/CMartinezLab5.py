###########################################################################
# Application: Creating a Dictionary of Identifiers 
# Topics: Execution Control Structures, File Encoding, Using Containers
# Development Environment: Windows 10
# Version: Python 3.7.4
# Solution File: CMartinezLab5
###########################################################################

#Program Source Statements

def get_input():  #get input from user
    file_name = input('Enter the name of an input file: ')  # file_name

    while file_name != 't5.dat':   # Test the input - looking for bad input
        print('Oops... An error occured - Try again')
        # ask for the imput again
        file_name = input('Enter the name of an input file: ')  # file_name

get_input()
     
def main():  # prints frequency of each word in contents 
    counters = {}            # dictionary of counters

    file_in = open('t5.dat', 'r', encoding = 'utf-8') # open t5.dat file
    contents = file_in.readlines() # read each line in t5.dat
    file_in.close() 
    clean_data = [] # create a new list named clean_data

    for line in contents:  # for loop to strip '\n' 
        val = line.strip()
        clean_data.append(val) # insert new clean list to clean_data

    for i, word in enumerate(clean_data, 1): # create counters for location 
        if word in counters: 
            counters[word].append(i)
        else:                
            counters[word] = [i]

    for word in counters:    # word and word location combined
        if counters[word] == 1:
            print('{}: {}'.format(word, counters[word]))
        else:
            print('{}: {}'.format(word, counters[word]))

    file_in = open('t5.dat', 'r', encoding = 'utf-8') # open t5.dat file
    contents = file_in.read() # read t5.dat
    file_in.close() 

    print('\n''Scanning t5.dat document...''\n''\n''Scanning complete!''\n')
            # to show user that the document is being scanned (for funzies)
    a_str = contents # identify invalid characters in document
    for a_char in a_str:
        if a_char == '&': # characters identified and shown in print
            print("Invalid character found -> & <- This is not a number, "\
                  "letter or underscore")
        elif a_char == '*':
            print("Invalid character found -> * <- This is not a number, "\
                  "letter or underscore")
        elif a_char == '@':
            print("Invalid character found -> @ <- This is not a number, "\
                  "letter or underscore")
        elif a_char == '.':
            print("Invalid character found -> . <- This is not a number, "\
                  "letter or underscore")
        elif a_char == '!':
            print("Invalid character found -> ! <- This is not a number, "\
                  "letter or underscore")
        elif a_char == '$':
            print("Invalid character found -> $ <- This is not a number, "\
                  "letter or underscore")

if __name__ == '__main__':
    main() # call main function

import datetime # datetime
d = datetime.date.today()
print(d)

# Program Output

"""
Enter the name of an input file: t5.dat
apple: [1, 11]
1: [2, 3]
ball: [4, 19]
art: [5]
dog: [6]
&: [7]
pen: [8, 21]
rat: [9]
4: [10]
1@.: [12]
carrot: [13]
!: [14]
orange: [15]
ant: [16, 17, 18]
stick: [20]
_: [22]
$a: [23]
***: [24]
goodbye: [25]

Scanning t5.dat document...

Scanning complete!

Invalid character found -> & <- This is not a number, letter or underscore
Invalid character found -> @ <- This is not a number, letter or underscore
Invalid character found -> . <- This is not a number, letter or underscore
Invalid character found -> ! <- This is not a number, letter or underscore
Invalid character found -> $ <- This is not a number, letter or underscore
Invalid character found -> * <- This is not a number, letter or underscore
Invalid character found -> * <- This is not a number, letter or underscore
Invalid character found -> * <- This is not a number, letter or underscore
2020-03-02

"""





















