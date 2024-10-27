# Muhie Al Haimus
# 7/08/2024
""" Explanation of the program: Write a Program using a for loop that counts from 1-100 that prints out if
the variable increasing after iteration is a multiple of five. Hint: use the modulus
operator."""


# create a for loop that counts from 1 to 100

for i in range(1, 101): # A standard for loop is i = 0, i < 100, (i = i + 1) so this would only print to 99 so that's why you need to add 1 to 100
  # check if the number is a multiple of 5
  if i % 5 == 0:
    print(f"{i} is a multiple of 5! ")
  else:
    print(f"{i} is not a multiple of 5! ")  