###########################################################################
# Program Header
# Course: CIS 117 Python Programming
# Name: Cuauhtemoc Alex Martinez
# Description: Lab 3
# Application: Your Supermarket Coupons – The Grocery Bill
# Topics: Programming with Numbers and Strings, Execution Control,
# Iterator Structures and User Defined Functions
# Development Environment: Windows 10
# Version: Python 3.7.4
# Solution File: CMartinezLab3
# Date: 02/11/20
###########################################################################

#Program Source Statements

def get_input(): # Read input from the user
    cost = input("Please enter the cost of your groceries: ") # get_input
    print("Enter cost >= 0: " + cost)
    return (float(cost)) # returns a float 

NUM_RUNS = 5 # named constant
  
def main():  # main fuction definition  
    cost = get_input()  # call get_input function
    for i in range(NUM_RUNS): # number of runs which equals 5 (above)

        entry1 = (input("Enter cost >= 0: "))
        if  float(entry1) < 0:
            print("Please enter a positive number.")
            # Positive number response only

        elif 0 <= float(entry1) < 10:
            print("Sorry, no discount for your $" + str(format(float(entry1),\
            ",.2f")) + " purchase. (0% of your purchase)")
            # Enter cost >= 0:  Less than $10 = No coupon

        elif 10 <= float(entry1) < 60:
            print("You win a discount coupon of $" + str(format(float(entry1)\
            * .08, ",.2f")) + " purchase. (8% of your purchase)")
            # Enter cost >= 0:  From $10 to less than $60 = 8% discount

        elif 60 <= float(entry1) < 150:
            print("You win a discount coupon of $" + str(format(float(entry1)\
            * .10, ",.2f")) + " purchase. (10% of your purchase)")
            # Enter cost >= 0:  From $60 to less than $150 =10% discount

        elif 150 <= float(entry1) < 210:
            print("You win a discount coupon of $" + str(format(float(entry1)\
            * .12, ",.2f")) + " purchase. (12% of your purchase)")
            # Enter cost >= 0:  From $150 to less than $210 = 12% discount

        elif float(entry1) >= 211:
            print("You win a discount coupon of $" + str(format(float(entry1)\
            * .14, ",.2f")) + " purchase. (14% of your purchase)")
            # Enter cost >= 0:  From $210 or more = 14% discount        
        
if __name__ == '__main__': 
    main() # call main function
          
import datetime
d = datetime.date.today()
print(d)

# Program Output

"""
Please enter the cost of your groceries: 25.36
Enter cost >= 0: 25.36
Enter cost >= 0: -.23
Please enter a positive number.
Enter cost >= 0: 1.25
Sorry, no discount for your $1.25 purchase. (0% of your purchase)
Enter cost >= 0: 25.14
You win a discount coupon of $2.01 purchase. (8% of your purchase)
Enter cost >= 0: 75.85
You win a discount coupon of $7.58 purchase. (10% of your purchase)
Enter cost >= 0: 200.00
You win a discount coupon of $24.00 purchase. (12% of your purchase)
2020-02-11
"""
