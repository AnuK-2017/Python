"""
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print
the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input: 3
       Tim
       20
       Jim
       40
       Rim
       50
"""

if __name__ == '__main__':
    # Method 1:
    # students = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #
    #     students.append([name, score])
    #
    # stu = sorted(set([score for name, score in students]))[1]
    #
    # print("\n".join(name for name, score in sorted(students) if score == stu))

    # Method 2:
    students = [[input(), float(input())] for _ in range(int(input()))]
    print(students)

    stu = sorted(set([marks for name, marks in students]))[1]

    print('\n'.join(a for a,b in sorted(students) if b==stu))