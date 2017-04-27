"""
You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry.
 The marks can be floating values. The user enters some integer  followed by the names and marks for  students.
 You are required to save the record in a dictionary data type. The user then enters a student's name.
Output the average percentage marks obtained by that student, correct to two decimal places.

Input: 3
       Tim 10 12 31
       Jim 23 32 40
       Rim 31 41 25
       Tim
"""
from decimal import Decimal as D
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg_list = student_marks[query_name]

    avg = sum(avg_list)
    avg = D(avg/3)
    print(round(avg,2))