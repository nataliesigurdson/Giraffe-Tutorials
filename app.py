# Variables and data types
# character_name = "Tom"
#character_age = 50

#print("There was once a man named " + character_name +",")
#print("he was " + character_age +" years old.")

#character_name = "Mike"
#print("He really liked the name " + character_name +",")
#print("but didn't like being " + character_age +".")


# Working with strings
#print("Giraffe\nAcademy")
#print("Giraffe\"Academy")
#print("Giraffe\Academy")

# phrase = "Giraffe Academy"
# print(phrase + " is cool")
# print(phrase.lower())  # makes all letters lowercase
# print(phrase.upper())  # makes all letters uppercase
# print(phrase.isupper())  # determines if the phrase is all uppercase
# print(phrase.upper().isupper())  # converts the phrase to uppercase and then determines if it is uppercase
# print(len(phrase))  # determines number of characters (length) of the string
# print(phrase[0])  # grabs the first (0) character in the string
# print(phrase.index("G"))  # returns the index of "G" in the string
# print(phrase.index("Acad"))  # returns the index of where "Acad" begins in the string
# print(phrase.replace("Giraffe", "Elephant"))  # replaced first string in quotes with second string in quotes


# Working with numbers
# print(-2.34)  # prints number
# print(3 - 2.5)  # returns difference of two numbers
# print(3 * (4 + 5))  # uses parenthesis to specify order of operations
# print(10 % 3)  # returns remainder of 10 divided by 3

# my_num = -5
# print(str(my_num) + " my favorite number")  # converts number to a string
# print(abs(my_num))  # returns absolute value of number
# print(pow(3, 2))  # raises 3 to the 2nd power (3^2)
# print(max(4, 6, 7))  # returns the highest number
# print(min(4, 6))  # returns smallest number
# print(round(3.7))  # rounds number

# from math import *
# print(floor(3.7))  # returns number rounded down to whole number
# print(ceil(3.1))  # returns number rounded up tp whole number
# print(sqrt(36))  # returns square root


# Getting input from users
# name = input("Enter your name: ")
# age = input("Enter your age: ")  # gets info from user (name and age)
# print("Hello " + name + "! You are " + age)  # uses that info to output a hello and the users name and age


# num1 = input("Enter a number: ")  # allows user to enter an input
# num2 = input("Enter another number: ")
# result = int(num1) + int(num2)  # converts num1 and num2 to integers
# result = float(num1) + float(num2)  # converts num1 and num2 to floats or able to type in decimal numbers
# print(result)

# MadLibs Game
# color = input("Enter a color: ")
# plural_noun = input("Enter a Plural Noun: ")
# celebrity = input("Enter a celebrity: ")
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)


# Lists
# friends = ["Rhea", "Joseph", "Pratik"]
# print(friends[0])  # prints the first (0) index in friends- Rhea
# print(friends[-1])  # prints the first index from the back of the list- Pratik

# friends = ["Rhea", "Joseph", "Pratik", "Akshaya", "Jassiel"]
# print(friends[1:])  # prints all names from the second index (1) and after- Joseph, Pratik, Akshaya, Jassiel
# print(friends[1:3])  # prints all elements from 1 until, but not including 3

# friends = ["Rhea", "Joseph", "Pratik", "Akshaya", "Jassiel"]
# friends[1] = "Gabi"  # modifies index position 1 from Pratik to Gabi
# print(friends[1])


# List Functions
lucky_numbers = [42, 8, 15, 16, 23]
# friends = ["Rhea", "Joseph", "Pratik", "Akshaya", "Jassiel"]
# friends.extend(lucky_numbers)  # prints friends list and then extends the list to print Lucky_numbers list (adds
# two lists togther
# friends.append("Carlos") # adds and item to the end of the list
# friends.insert(1, "Josh")  # inserts Josh in index 1 position and shifts following elements back one index
# friends.remove("Pratik")  # removes the element Pratik
# friends.clear()  # clears all index
# friends.pop() # removes last element from the list
# print(friends)
# print(friends.index("Akshaya")) # prints index of Akshaya- 3

friends = ["Rhea", "Joseph", "Pratik", "Pratik", "Akshaya", "Jassiel"]
# print(friends.count("Pratik"))  # prints the number of times Pratik occurs in the list- 2

# friends.sort() # prints list in alphabetical order
# print(friends)

# lucky_numbers.sort()  # prints list in numerical order
# lucky_numbers.reverse()  # prints list in reversed order
# print(lucky_numbers)

# friends2 = friends.copy()  # copies the list
# print(friends2)


# Tuples- cannot be modified
# coordinates = (4, 5)  # creates a tuple with the coordinates 4 and 5 inside it
# coordinates[1] = 10  # prints an error because tuples cannot be modified
# print(coordinates[0])  # prints the index 0- 4
# coordinates = [(4, 5), (6, 7), (80, 34)]  # tuples inside a list


# Functions
# def say_hi():  # function definition
#     print("Hello User")
# print("Top")
# say_hi()  # calling the function
# print("Bottom")

# def say_hi(name, age):  # function definition
#     print("Hello " + name + ", you are " + str(age))
# say_hi("Cooper", 18)
# say_hi("Gabi", 17)


# Return Statement
# def cube(num):
#    return num*num*num

# result = cube(4)
# print(result)


# If statements
# is_male = False
# is_tall = False
# if is_male or is_tall:
#    print("You are a male or tall or both")
# else:
#     print("You are neither a male nor tall")
# if is_male and is_tall:
#     print("You are a tall male")
# else:
#     print("You are either not a male or not tall or both")
# if is_male and is_tall:
#    print("You are a tall male")
# elif is_male and not(is_tall):
#   print("You are a short male")
# elif not(is_male) and (is_tall):
#    print("You are not a male but are tall")
# else:
#    print("You are not a male and not tall")


# If statements and comparisons
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:  # other comparison operators: == equal to, != not equal to
#         return num1
#         return num2
#     else:
#         return num3
# print(max_num(300, 40, 5))


# Building a better calculator
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")


# Dictionaries
# monthConversions = {
#     0: "January",
#     10: "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
# }

# print(monthConversions["Mar"])
# print(monthConversions.get("Mar"))  # these do the same thing
# print(monthConversions.get("Dec", "Not a valid Key"))


# While loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1  # i = i + 1

# print("done with loop")


# Building a guessing game
# secret_word = "Artemis"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print("Out of guesses. Game Over.")
# else:
#    print("You win!")


# For loop
# for index in range(10):  # prints numbers between 0 and 10, not including 10
#    print(index)

# for index in range(5):
#     if index == 0:
#         print("first Iteration")
#     else:
#         print("Not first")


# Exponent function
# def raise_to_power(base_num, pow_num):
#    result = 1
#    for index in range(pow_num):
#        result = result * base_num
#    return result
# print(raise_to_power(3, 17))


# 2D Lists and nested loops
# number_grid = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
#    [0]
# ]
# print(number_grid[2][1])  # prints 3rd row and 2nd column- 8

# for row in number_grid:
#     for col in row:
#         print(col)


# Build a translator
# def translate(phrase):    translation = ""
#   for letter in phrase:
#       if letter.lower() in "aeiou":
#            if letter.isupper():
#                translation = translation + "G"
#            else:
#                translation = translation + "g"
#        else:
#            translation = translation + letter
#    return translation
#
# print(translate(input("Enter a phrase: ")))


# Try except
# try:  # can handle an error
#     answer = 10/0
#     number = int(input("enter a number "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)  # print the error
# except ValueError:
#     print("invalid input")


# Reading files
# name_of_file = open("name_of_file.txt", "r")  # read file
# name_of_file = open("name_of_file.txt", "w")  # write file- add new info or change existing info- writes over file
# name_of_file = open("name_of_file.txt", "a")  # append file- only add new info
# name_of_file = open("name_of_file.txt", "r+")  # read and write file

# print(name_of_file.read())  # return file
# print(name_of_file.readlines()[1])

# name_of_file.write("\Kelly")
# name_of_file.close()


# Modules- look up list of python modules to find a list of already made modules
# import useful_tools  # gets info from another file so you can use the functions in it
# print(useful_tools.roll_dice(10))  # uses the roll dice function from the useful_tools files

# external libraries / lib to find external modules


