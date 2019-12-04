# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(number):
    if number % 2 == 0:
        print('true')
        return True
    else:
        print('false')
        return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
# print(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

if num % 2 == 0:
    print("Even!")
else:
    print('Odd')