 # Muhie Al Haimus
# 7/08/2024
""" Explanation of the program: A program that asks the user to input their age. If the age is 15 or less,
display the message “You are entitled to purchase a child's ticket”. Otherwise,
display “You must buy and adult ticket!” Show that the program works correctly
with the inputs of 14, 15 and 16."""

age = int(input("Enter your age: "))

if age <= 15 and age >= 0: # check for age less than or equal to 15 and making sure that the input is greater than 0
  print("You are entitled to purchase a child's ticket! ")
elif age >= 16: # check for age greater than or equal to 16
  print("You must buy an adult ticket! ")
elif age < 0: # this catches negative numbers
  print("Invalid age")



