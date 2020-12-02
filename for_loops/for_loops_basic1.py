# Basic - Print all integers from 0 to 150.
print("\nPrint all integers from 0 to 150")
for x in range(151):
    
    print(x)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
print("\nPrint all the multiples of 5 from 5 to 1,000")
for y in range(5, 1005, 5):
    print(y)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
print("\nPrint integers 1 to 100. If divisible by 5, print Coding instead. If divisible by 10, print Coding Dojo.")
for i in range(1, 101, 1):
    if i % 5 == 0 and not i % 10 == 0:
        print("Coding")
    elif i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
print("\nAdd odd integers from 0 to 500,000, and print the final sum")
sum = 0
for j in range(500000):
    if j % 2 == 0:
        pass
    else:
        sum = sum + j
print("The sum equals", sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
print("\nPrint positive numbers starting at 2018, counting down by fours")
for k in range(2018, 0, -4):
    print(k)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
print("\nSet three variables: lowNum, highNum, mult")
def flexible_counter(low_num, high_num, mult):
  for m in range(low_num, high_num + 1):
    if m % mult == 0:
      print(m)

flexible_counter(2, 9, 3)

