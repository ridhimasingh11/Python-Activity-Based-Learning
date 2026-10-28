##Algorithm

1. Start
2. Read student names, subjects, and marks in a nested list.
3. Calculate each student's total and average.
4. Calculate each subject's average across all students.
5. Find the student with the highest total.
6. Check whether any subject average is below 60.
7. Display the student results, subject averages, and top performer.
8. Stop.

## Flowchart

#              ( START )
#                  |
#         / Input names and marks /
#                  |
#          [ Initialize totals ]
#                  |
#           [ Calculate student total ]
#                  |
#           [ Calculate student average ]
#                  |
#            < More students? >
#               /          \
#             Yes           No
#              |             |
#        [ Process next ] [ Calculate subject averages ]
#              |             |
#              +---> LOOP    |
#                            |
#                   [ Find top performer ]
#                            |
#                    [ Check subject averages ]
#                            |
#                    < Average < 60? >
#                       /         \
#                     Yes          No
#                      |            |
#               [ Flag subject ] [ No flag ]
#                      |            |
#                      +------+-----+
#                             |
#                    / Display summary /
#                             |
#                          ( STOP )

##Python code

names = ["Asha", "Bharat", "Charan"]

subjects = ["Python", "Mathematics", "Physics"]

marks = [
    [85, 78, 90],
    [65, 58, 62],
    [92, 88, 95]
]

totals = []

for i in range(len(marks)):
    total = sum(marks[i])
    totals.append(total)

    average = total / len(subjects)

    print(names[i], "Total:", total,
          "Average:", round(average, 2))

subject_averages = []

for col in range(len(subjects)):
    total = 0

    for row in range(len(marks)):
        total += marks[row][col]

    average = total / len(marks)
    subject_averages.append(average)

    print(subjects[col], "Average:", round(average, 2))

top_index = totals.index(max(totals))

print("Top performer:", names[top_index],
      "Total:", totals[top_index])

for i in range(len(subjects)):
    if subject_averages[i] < 60:
        print("Low-performing subject:", subjects[i])

##Output

Asha Total: 253 Average: 84.33
Bharat Total: 185 Average: 61.67
Charan Total: 275 Average: 91.67
Python Average: 80.67
Mathematics Average: 74.67
Physics Average: 82.33
Top performer: Charan Total: 275