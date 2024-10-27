# Ilanthiraiyan Sivagnanamoorthy
# 7/08/2024

""" Explanation of the program: 
Using a function create a Fahrenheit to Centigrade converter and call this function three times to show that you don’t have to copy and paste the code blocks or re-run the code. Temperatures can be converted from Fahrenheit to Centigrade using the following formula, where F is the temperature in Fahrenheit and C the temperature in Centigrade: C = 5(F − 32)/9. 

Write a function to input a Fahrenheit temperature and output the equivalent temperature in Centigrade.
Extension: modify the output to display the temperature to two decimal places. (hint: use google if needed!)"""

"Problem Solution"

# 1. Define the function to convert Fahrenheit to Centigrade:
def fahrenheit_to_centigrade(fahrenheit):
  # 2. Compute the equivalent temperature in centigrade using the formula:
  centigrade = 5 * (fahrenheit - 32)/9
  # 3. Take the variable "centigrade", round it to 2 dp using the round function:
  centigrade = round(centigrade, 2)
  # 4. Return the rounded value (stored in the variable "centigrade") 
  return centigrade

# 5. Evoke the function 3 times:

# This function call returns 65.56 but does not output anything:
fahrenheit_to_centigrade(150) 

# This call outputs 6.11 (the returned value is immediately printed out):
print(fahrenheit_to_centigrade(43)) 

# This call stores the returned value (31.67) in the variable "answer_to_89" and prints it on the subsequent line:
answer_to_89 = fahrenheit_to_centigrade(89) 
print(answer_to_89)

"""Note: The body of the function that we have defined could well be shortened to a single line, but we have chosen to keep it as it is for the sake of clarity. But can you rewrite lines 15, 17 and 19 as a single line?""" 











