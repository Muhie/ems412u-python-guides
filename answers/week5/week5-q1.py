#Yash Vaghela
#20/08/2024
'''Explanation: First, 
import numpy to allow the use of matrices. Then 
create a function and within it define the matrix 
size and initialise it with all zeros. Then create a for
 loop that will iterate through the rows and columns of the
   matrix, allowing user input. Finally, print the matrix'''

import numpy as np


def matrix():  # function to create a 3x2 matrix and fill it with user input
  matrix = np.zeros((3, 2))
  for i in range(3):  # loop to iterate through the matrix rows
    for j in range(2):  # loop to iterate through the matrix columns
      try:  # try is used to catch any errors (**try except is ok here just**)
        matrix[i][j] = float(
            input(f"Enter a value for the matrix element {i+1, j+1}: "))
      except ValueError:  # if the input is not a float, it will print the message and the matrix
        print("Please enter a float value")
  print(matrix)

matrix()


