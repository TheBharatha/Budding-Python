import math
import os
import sys

def gradingStudents(grades):
    scores = grades
    meeting = list()
    for i in range(len(grades)):
        if scores[i] < 38:
            meeting.append(scores[i])
        else:
            upgrade = 5-(scores[i] % 5)
            if not upgrade == 5 and upgrade < 3:
                scores[i] = scores[i] + upgrade
                meeting.append(scores[i])
            else:
                meeting.append(scores[i])
    return(meeting)

if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    print('\n'.join(map(str, result)))
    print('\n')
