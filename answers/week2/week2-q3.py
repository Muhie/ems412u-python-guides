#Yash Vaghela
#11/08/2024
""" Explanation of Program Write a program that uses a while loop to ask the user to type in 'ducky'
and run the loop endlessly until the user types it in. Show it working with the
words: cup, teapot, cake, and ducky entered in sequence. """ 

enter = "" #Create an empty variable
while enter != "ducky": #While variable is not equal to "ducky", loop will continue
  enter = input("Enter 'ducky': ")
print("You entered 'ducky'.")
# ^ When ducky is entered, the loop will break and this statement will be printed
