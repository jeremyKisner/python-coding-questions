#!/bin/python3
#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for index in range(len(grades)):
        print(grades[index])
        if grades[index] < 38:
            print("skipping unscalable, failing grade")
        elif grades[index] % 5 == 3:
            grades[index] += 2
        elif grades[index] % 5 == 4:
            grades[index] += 1
    return grades

if __name__ == '__main__':
    grades = [37, 38]
    result = gradingStudents(grades)
    print(result)
