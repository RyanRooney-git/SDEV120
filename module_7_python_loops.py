
# This program is inteded to print even and odd numbers from
# 1 to 15.

# Creating a list of numbers from 1 to 15
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# creating the for loop to iterate over the numbers list and print
# even and odd numbers accordingly
for number in numbers:
    if (number % 2 == 0):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
