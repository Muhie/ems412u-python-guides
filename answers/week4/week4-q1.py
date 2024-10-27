# Yash Vaghela
# 10/08/2024
""" Explanation of the program: 
Sum to N using a function called sum to n return the value of 15r^3+2r^2+3
"""

sum = 0
'''Takes values from a range of 5 to 21, since the range is exclusive of the last value, and iterates through each value of the sum.'''
for i in range(5, 21):
    sum += 15*(i**3) + 2*(i**2) + 3
print(sum)
'''Then, only the last value of the sum is printed, since the print statement is outside of the for loop.'''