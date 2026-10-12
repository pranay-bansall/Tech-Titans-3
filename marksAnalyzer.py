# Student Marks Analyzer
# Write a program that accepts the marks obtained by a student in five subjects.
# The program should determine the highest marks, lowest marks, and average marks obtained by the student, and display all three results.

# Variables to Store Highest, Lowest and Average Marks
highestMarks = 0 #semi column is removed from the end of the line as it is not required in Python   
lowestMarks = 100 #semi column is removed from the end of the line as it is not required in Python   


# Taking Marks for Five Subjects as Input
subject1 = int(input("Enter Marks for Subject 1: "))#semi column is removed from the end of the line as it is not required in Python   
subject2 = int(input("Enter Marks for Subject 2: "))#semi column is removed from the end of the line as it is not required in Python   
subject3 = int(input("Enter Marks for Subject 3: "))#semi column is removed from the end of the line as it is not required in Python   
subject4 = int(input("Enter Marks for Subject 4: "))#semi column is removed from the end of the line as it is not required in Python   
subject5 = int(input("Enter Marks for Subject 5: "))#semi column is removed from the end of the line as it is not required in Python   


# Finding the Lowest Marks
if subject1 > subject2 and subject1 > subject3 and  subject1 > subject4 and subject1 > subject5:
    lowestMarks = subject1 #semi column is removed from the end of the line as it is not required in Python   

elif subject2 > subject3 and  subject2 > subject4 and subject2 > subject5:
    lowestMarks = subject2 #semi column is removed from the end of the line as it is not required in Python   

elif  subject3 > subject4 and subject3 > subject5:
    lowestMarks = subject3 #semi column is removed from the end of the line as it is not required in Python   

elif lowestMarks < subject4:
    lowestMarks = subject4 #semi column is removed from the end of the line as it is not required in Python   

elif lowestMarks < subject5:
    lowestMarks = subject5 #semi column is removed from the end of the line as it is not required in Python   



# Calculating the Average Marks
avg = subject1 + subject2 + subject3 + subject4 + subject5 / 5

# Displaying the Results
print(f"Highest: {highestMarks}")
print(f"Lowest: {lowestMarks}")
print(f"Average: {avg}")