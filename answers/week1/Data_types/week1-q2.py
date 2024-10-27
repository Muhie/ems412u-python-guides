# Yash Vaghela
# 27/10/2024
'''Explanation: The program asks for 2 inputs, the bill amount,
 and the percent of tip you would like to give, then it will calculate the tip amount, 
 finally outputting the tip amount and type of the variable.'''

bill = float(input("Please enter your bill amount: £"))     # takes the bill amount as a float input

tip_percent = float(input("Enter what percent of the total bill you would like to tip: "))      # takes the percent you would like to tip as a float input

if tip_percent < 0:     # checks the percent entered in the previous step is valid
    print("Please enter a valid percent")
else:
    tip_amount = bill * tip_percent / 100       # calculates the tip amount be given
    print(f"You need to tip £{round(tip_amount, 2)}")       # prints out the tip amount and rounds to 2 d.p.
    print(type(tip_amount))     # prints the type of the tip_amount variable