# Yash Vaghela
# 10/08/2024
""" Explanation of the program:
Write a Python program to multiply two complex numbers together. 
"""

# Method 1:
a = complex(2, 3) # 2 + 3j
b = complex(4, 5)  # 4 + 5j
c = a * b
print(c) # (-7+22j)

# Method 2:
a_R = input("Enter the real part of the first complex number: ")    # Takes input from the user as a string.
a_I = input("Enter the imaginary part of the first complex number: ") # Takes input from the user as a string.
b_R = input("Enter the real part of the second complex number: ")
b_I = input("Enter the imaginary part of the second complex number: ")
a = complex(float(a_R), float(a_I))    # Converts the input string into the first complex number.
print("The first complex number is: ", a)    # Prints the complex number.
b = complex(float(b_R), float(b_I))
print("The second complex number is: ", b)
multiply = complex(float(a_R), float(a_I)) * complex(float(b_R), float(b_I))    # Multiplies the two complex numbers.
print("The product of the two complex numbers is: ", multiply)    # Prints the product of the two complex numbers.