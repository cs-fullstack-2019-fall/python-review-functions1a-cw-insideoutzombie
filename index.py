### Problem 1
# Create a ```printNumbers``` function to print integers from -25 to 20 to the console (print in the function)
# def printNumbers():
#     for x in range(-25, 21, 1):
#         print(x)
#
# printNumbers()

# ### Problem 2
# Create a function called checkPassword. Send two string variables to the
# checkPassword function to check if the strings are equal.
# Return true if they are equal and false if they are not equal. Print the function's return value.
# def checkPassword():
#     userInput1 = input("Enter first word ")
#     userInput2 = input("Enter second word ")
#     if userInput1 != userInput2:
#         print("false")
#     else:
#         print("True")
#
# checkPassword()
# ### Problem 3
# Write a function that determines if a number passed to it is odd or even.
# Pass a number of your choosing (using input a good idea) and then using the result
# from the function, print if the number was even or not.
# examples:
# ```
# The number 12 is an even number!
#
# The number 5 is an odd number!
# userNum = int(input("Enter a num to see if its odd or even "))


# def problem3():
#     userNum = int(input("Enter a num to see if its odd or even "))
#
#     return (userNum / 2)
#
#     number_to_check = userNum / 2
#     if number_to_check > 100:
#         return (f'The number {number_to_check} is Even!')
#     elif number_to_check < 100:
#         return (f'The number {number_to_check} is Odd!')
#
# problem3()
# ### Problem 4
# * Create a function for the challenge that you call from your ```main```
# * Create a *second* function that takes NO parameters
# * Create a *third* function that takes a single greeting parameter (ex. ```Howdy```)
# and returns a string using the passed in greeting and 'World' (ex. ```Howdy World!```)
# * From your *first* function, call the function(s) and print out the final result returned
# def first():
#     second()
#     third()
#
# def second(user1):
#     userInput = input("Enter here ")
#
#
# def third(greeting):
#     greeting = user1 + "World"
#
# first()

# ### Problem 5:
# ##### We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
def infinite():
    userInput5 = input("Enter something or hit 'q' to quit ")
    while userInput5 != 'q':
        userInput5 = input("Input another string ")
        print(userInput5)

infinite()


# ### Challenge
# Create a function that accepts 2 numbers. When the function is called return the sum,
# difference, product, and quotient as 4 separate return values.
#
# Print the 4 results that are returned using f-strings.
#
# Example: If 2 and 6 are passed into the function, output should be similar to the following:
#
# ```
# The sum of 2 + 6 is 8
# The difference of 2 - 6 is  -4
# The product of 2 * 6 is 12
# The quotient of 2 / 6 is .333
# ```
#
a = int(input("enter first number: "))
b = int(input("enter second number: "))

def addNum():
    sum = a + b
    print(f'The sum of {a} + {b} is {sum}')

def subNum():
    sum = a - b
    print(f'The difference of {a} - {b} is {sum}')

def divNum():
    sum = a / b
    print(f'The product of {a} + {b} is {sum}')

def mulNum():
    sum = a * b
    print(f'The quotient of {a} + {b} is {sum}')

def main():
    addNum()
    subNum()
    divNum()
    mulNum()


main()
