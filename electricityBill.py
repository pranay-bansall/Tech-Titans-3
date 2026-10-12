# Electricity Bill Calculator
# Write a program that calculates the electricity bill based on units consumed using different rates for different slabs.
# 100 and below = 3
# 100-200 = 5
# 200-300 = 7
# 300 above = 10
# Taking Units Consumed as Input
units = int(input("Enter Units Consumed: ")) # int data type is used to convert the input string into an integer for units consumed


# Calculating Bill Based on Slabs
if units <= 100:
    totalBill = units * 3 # debug semi column is removed from the end of the line as it is not required in Python and equal to sign changed to less than or equal to sign

elif units <= 200:
    totalBill = 100*3 + (units-100)*5 # debug semi column is removed from the end of the line as it is not required in Python

elif units <= 300:
    totalBill = 100*3 + 100*5 + (units-200)*7 #debug semi column is removed from the end of the line as it is not required in Python

else:
    totalBill = 100*3 + 100*5 + 100*7 + (units-300)*10 #debug semi column is removed from the end of the line as it is not required in Python

# Displaying the Final Bill
print(f"Total Electricity Bill: {totalBill}")