# Yash Vaghela
# 22/08/2024
'''Explanation: The program asks for 2 inputs, the bill amount, and the
 tendered amount, then depending on the conditions given it will output 
 one of 2 messages as shown below.'''
def change_due():
    bill_amount = float(input("Enter the bill amount £")) # float inputs are used to allow decimal inputs
    tendered_amount = float(input("Enter the tendered amount £"))
    if tendered_amount < bill_amount:    #checks whether the tendered amount is less than the bill amount
        print("You have not given enough money\n")
        print(f"You still owe £{bill_amount - tendered_amount}")
    else:    #prints the change due if the tendered amount is greater than the bill amount
        print(f"Change due £{tendered_amount - bill_amount}")

change_due()