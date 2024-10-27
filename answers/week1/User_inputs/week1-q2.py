 # Muhie Al Haimus
# 7/08/2024
"""  Explanation of the program: A program to read in two numbers and print their sum and average.
Run your program with the numbers 12 and 15 to show that it works. """

num_1 = int(input("Enter the first number: ")) 
# notice the change of variable type the input is of type string and then we convert it to a type integer see what happens if you remove the int() method

num_2 = int(input("Enter the second number: "))

sum = num_1 + num_2

average = sum/2

print(f"The sum of {num_1} and {num_2} is {sum} and the average is {average}")