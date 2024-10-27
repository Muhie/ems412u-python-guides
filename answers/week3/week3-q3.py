#Yash Vaghela
#11/08/2024
""" Explanation of Program:
Write a program, to take a number from the user and display its
factorial e.g.
Factorial of 2 = 2 x 1 = 2
Factorial of 3 = 3 x 2 x 1 = 6
Factorial of 4 = 4 x 3 x 2 x 1 = 24
The program should comprise of three functions: get number - function that
gets and returns the number from the user. factorial - function that passes a
number (previously entered) as a parameter and returns one value which is the
2
factorial of this number. main - the main function that calls get number and
factorial and displays the result.

"""


def getnumber():  #defines the getnumber function, where the user will input a number.
  correct_input = False
  while correct_input == False:
    number = int(input("Enter a positive number: "))
    if number > 0:
      correct_input = True 
    else:
      print("Invalid input, please input a positive integer")
    
  return number  #returns the number to the main program

def factorial():  #defines the factorial function, where the factorial of the number will be calculated.
  number = getnumber()  #calls the getnumber function to get the number from the user.
  factorial = 1
  for i in range(1, number + 1):  #for loop that will calculate the factorial of the number.
      factorial *= i
  return factorial

def main():  #defines the main function, where the factorial of the number will be printed.
  print(factorial())

main()  #calls the main function to run the program.