'''
A teacher has to distribute grades for students based ont their 
aggregate scores out of 100.

    The teacher has to distribute the grades in the following manner:
        - If the student's score is less than or equal to 40, grade is F
        - If the student's score is greater than 40 and less than or equal to
          50, grade is D
        - If the student's score is greater than 50 and less than or equal to
          60, grade is C
        - If the student's score is greater than 60 and less than or equal to
          70, grade is B
        - If the student's score is greater than 70 and less than or equal to
          80, grade is A
        - If the student's score is greater than 80, grade is A+
'''

student_score = int(input("Enter the student's score: "))

if (student_score <= 40):
    print("Grade is F")
elif (student_score > 40 and student_score <= 50):
    print("Grade is D")
elif (student_score > 50 and student_score <= 60):
    print("Grade is C")
elif (student_score > 60 and student_score <= 70):
    print("Grade is B")
elif (student_score > 70 and student_score <= 80):
    print("Grade is A")
elif (student_score > 80):
    print("Grade is A+")