file_name = input('Please enter the file name: ')
def main():
    

    while (file_name != 'valid.dat') and (file_name != 'bad1.dat') and \
            (file_name != 'bad2.dat') and (file_name != 'bad3.dat') and \
            (file_name != 'bad4.dat'):
        # Test the input - looking for correct input
        print('Error: File not found.''\n')
        # Error displayed if no valid input
        file_name = input('Please enter the file name: ''\n')
        # ask for the input again

        get_input = file_name

        if get_input in str('valid.dat'):  # if loop to connect to 
            contents = open('good.dat', 'r') # correct .dat file
        elif get_input in str('bad1.dat'):
            contents = open('bad1.dat')
        elif get_input in str('bad2.dat'):
            contents = open('bad2.dat')
        elif get_input in str('bad3.dat'):
            contents = open('bad3.dat')
        elif get_input in str('bad4.dat'):
            contents = open('bad4.dat')

        numbers = []
    try:
  
          for n in contents:
              numbers.append(int(n))
              print(numbers)
              print('The sum is: ',(sum(numbers)))
      
##        for i, num in enumerate(numbers, 1):
##            print(i, num)
##            if i == 11:
##                return True

    except ValueError:
          print("Error: file contents invalid.")
##    finally:
##        print("Test Error")

        



if __name__ == '__main__':
    main() # call main function
