import random
number = random.randint(1,10)
for i in range(0,5):
    while True:
        try:
            player = int(input("Guess the number from 1 to 10. "))
            break
        except:
            print("You have entered a letter or word. Please enter a number from 1 to 10")
    if player == number:
        print("We have a Winner!!!")
        print(f"You guessed the number! It's {number}")
        break
    elif player > 10:
        print("Your number is greater than 10. Please choose a number from 1 to 10.")
    elif player < 1:
                print("Your number is less than 1. Please choose a number from 1 to 10.")
if player != number:
        print(f"Your guess is incorrect the number is {number}")
 