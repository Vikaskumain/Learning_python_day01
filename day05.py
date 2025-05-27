# today we are going to solve the problem and finding how functions works 
# in python
def sum_val(a,b):
      sum = a+b
      return sum 
result = sum_val(10,20)
print(result)
# this is a simple function that takes two arguments and returns their sum
# now we are going to solve the problem of finding the sum of two numbers
# using the function we created above

def vikas():
      print("hello vikas")
vikas()

# give me the some no of the avrage values 
def avrage(a,b,c,d):
      sum = a+b+c+d
      avrage = sum/4
      print("the avrage of the no is ",avrage)
      return avrage
result = avrage(10,20,30122,30)
# this is a simple function that takes four arguments and returns their avrage
print(result)


# our problem is to find the no is odd ,ol even and take the input from the user 
# def odd_even():
#       num = int(input ("Enter the No : "))
#       if num %2 ==0:
#             print("the no is even")
#       else:
#             print("the no is odd")
# odd_even()

import os
print(os.path.exists(r"C:\Users\vikas kumain\Downloads\PTLOperatorRequest.xlsx"))

import pandas as pd

# Correct path with raw string (important!)
file_path = r"C:\Users\vikas kumain\Downloads\PTLOperatorRequest.xlsx"

# Read Excel file using pandas
try:
    data = pd.read_excel(file_path)
    print(data)
except Exception as e:
    print("An error occurred:", e)

# this is a simple function that takes no arguments and returns the no is odd or even