'''
Accept n number of student's marks and display the aggregate marks of the class.
'''

n = int(input("Enter the number of students: "))

total_marks = 0

for i in range(n):
    marks = int(input("Enter marks of student " + str((i+1)) + ": "))
    total_marks += marks

avg_marks = total_marks / n

print("The average marks of the class is:", avg_marks)