# #                 PYTHON FOR BEGINNERS - LEARN PYTHON IN 1 HOUR BY MOSH
# # AGE CALCULATOR
# birth_year = input("Enter your birth year: ")
# age = 2021 - int(birth_year)
# print(age)

# int() # Converts to a whole number ie; 10,12,15,22
# float() # Converts to whole or decimal number if isn't a whole number ie; 10.1, 12.3, 15.50
# bool() # 
# str()


# # Basic CALCULATOR adding two whole numbers
# first = input("First: ")
# second = input("Second: ")
# sum = int(first) + int(second)
# print(sum)

# #  Basic CALCULATOR adding decimals along with a str concatenation on ln 22
# first = float(input("First: "))
# second = float(input("Second: "))
# sum = first + second
# print("Sum: " + str(sum))


# course = 'Python for Beginners'
# print(course.replace('for', '4')) #Replacing strings within a variable with Replace method

# x = 10
# x = x + 3
# x += 3 # This is the same as the code above


# # LOGICAL OPERATORS
# price = 25
# print(price > 10 and price < 30) # TRUE
# # If both of these expressions above return TRUE then result of entire expression will be TRUE 

# price = 5
# print(price > 10 or price < 30) # TRUE 
# # First expression will be analyzied to see if price is greater than 5 if False
# # Second expression will be analyzed as well to see if less than 30 and if it is will return TRUE
# # So only 1 of both expressions needs to TRUE or FALSE

# price = 5
# print(not price > 10) # TRUE
# # Expression is checked to see if price is not greater than 10 == True

# # and (both)
# # or (at least one)
# # not ()

# # IF STATEMENTS
# temperature = 1
# if temperature > 30:
#   print("It's a hot day")
#   print("Drink plenty of water")
# elif temperature > 20: # (20, 30]
#   print("It's a nice day")
# elif temperature > 10: # (10, 20]
#   print("It's a bit cold")
# else:
#   print("It's cold")
# print("Done")



# # EXCERCISE CREATE A LBs/KGs CONVERTER
# weight = int(input("Weight: "))
# unit = input("(K)g or (L)bs: ")
# if unit.upper == "K":
#   converted = weight / 0.45
#   print("Weight in Lbs: " + str(converted))
# else:
#   converted = weight * 0.45
#   print("Weight in Kgs: " + str(converted))

# # WHILE LOOP
# i = 1
# while i <= 5:
#   print(i) 
#   i = i + 1


# # LIST METHODS 
# names = ["John", "Bob", "Mosh", "Sam", "Mary"]
# names[0] = "Jon" # This will rename John to Jon 
# print(names[0:3]) # This will show variables in list up to Mosh 

# numbers = [1, 2, 3, 4, 5]
# numbers.insert(0, -1) 
# numbers.remove(3) # Removes 3 from the list
# numbers.clear() # Clears the list
# print(len(numbers)) # this will print 5 because we have 5 numbers in the list


# # FOR LOOPS
# numbers = [1, 2, 3, 4, 5]
# for item in numbers:
#   print(item)

# i = 0
# while i < len(numbers):
#   print(numbers[i])
#   i = i + 1

# # RANGE FUNCTION
# numbers = range(5, 10) # This will list the numbers excluding the numbers printed inside the range function IE; 6,7,8,9
# numbers = range(5, 10, 2) # This will do the same as above except we jump every 2 numbers IE; 5, 7, 9
# for number in numbers:
#   print(number)


# TUPLES
# numbers = (1, 2, 3)