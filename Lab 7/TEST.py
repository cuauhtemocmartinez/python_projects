CreditCardNum = input("Input a credit card number(no spaces/hyphens): ")

#The if statements
if len(str(CreditCardNum)) <= 50:
    print("Valid")
elif len(str(CreditCardNum)) > 50:
    if str(CreditCardNum[0]) == '4':
        print("The Card is a Visa")
    elif str(CreditCardNum[0]) == '5':
        print("The Card is a Master Card")
    elif str(CreditCardNum[0]) == '6':
        print("The Card is a Discover Card.")
    else:
        print("The brand could not be determined.")


if not wish_list.set_sender(chr(7)):
    print('Correctly rejected sender nonprintable err')
