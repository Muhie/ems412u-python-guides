# Yash Vaghela
# 10/08/2024
""" Explanation of the program: 
Write a Python program to get the length and the angle of a complex number.
"""

# Method 1
import numpy as np
a = complex(2, 3)  # a = 2 + 3j
length = abs(a)
print(length) # 3.605551275463989
angle = np.arctan2(a.imag, a.real)
print(str(angle) + " radian", np.degrees(angle), "degrees") # 0.982793723247329 radians 56.309932474020215 degrees)

# Method 2:
import numpy as np
a = input("Enter the real part of the complex number: ")    # Takes input from the user as a string.
b = input("Enter the imaginary part of the complex number: ")   # Takes input from the user as a string.
print("The complex number is: ", a, "+", b, "j")    # Prints the complex number.
print("The length of the complex number is: ", abs(complex(float(a), float(b))))   # Prints the length of the complex number by finding the absolute value of the complex number.
print("The angle of the complex number is: ", np.arctan2(float(b), float(a)), "radians")    # Prints the angle of the complex number by finding the arctan of the imaginary part divided by the real part.