# Shopping Cart Total
# Write a program that calculates the total price of a product based on the product selected and the quantity entered by the user. The program should support the 
# four available products and display the total amount that needs to be paid



headPhone = 999  #semi column is removed from the end of the line as it is not required in Python   
smartWatch = 1599 #semi column is removed from the end of the line as it is not required in Python  
PS5 = 1299 #semi column is removed from the end of the line as it is not required in Python
iPad = 599 #semi column is removed from the end of the line as it is not required in Python


productName = input("Enter Product Name: ")
quantity = int(input("Enter the Quantity of the Product: "))  #int data type is used to convert the input string into an integer for quantity


if productName == "headPhone":
    totalPrice = headPhone * quantity

elif productName == "smartWatch":
    totalPrice = smartWatch * quantity

elif productName == "PS5":
    totalPrice = PS5 * quantity

elif productName == "iPad":
    totalPrice = iPad * quantity


print(f"Total Amount To Be Paid: {totalPrice}")