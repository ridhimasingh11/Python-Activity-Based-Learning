##Algorithm
1. Start 
2. Read student names and marks for two assessments.
3. Calculate the first assessment average.
4. Calculate the second assessment average.
5. Find the difference between the averages.
6. Identify second-assessment subject marks below 40.
7. Classify performance as High, Moderate, or Needs Support.
8. Display the results for each student.
9. Stop.

## Flowchart

#              ( START )
#                  |
#        / Input student marks /
#                  |
#          [ Calculate first average ]
#                  |
#         [ Calculate second average ]
#                  |
#          [ Calculate improvement ]
#                  |
#        [ Identify weak subjects ]
#                  |
#         < Average >= 75? >
#              /          \
#            Yes           No
#             |             |
#       [ Category High ] < Average >= 50? >
#                            /         \
#                          Yes          No
#                           |            |
#                    [ Moderate ] [ Needs Support ]
#                           |            |
#                           +------+-----+
#                                  |
#                       / Display report /
#                                  |
#                               ( STOP )

##Python code

students = [
    ("Asha", [65, 70, 72], [78, 80, 75]),
    ("Bharat", [55, 48, 60], [52, 39, 58]),
    ("Charan", [35, 42, 38], [45, 48, 40])
]

for name, first, second in students:
    old_avg = sum(first) / len(first)
    new_avg = sum(second) / len(second)

    change = new_avg - old_avg
    weak = []

    for i in range(len(second)):
        if second[i] < 40:
            weak.append(i + 1)

    if new_avg >= 75:
        category = "High"
    elif new_avg >= 50:
        category = "Moderate"
    else:
        category = "Needs Support"

    print(name, "| First avg:", round(old_avg, 2),
          "| Second avg:", round(new_avg, 2),
          "| Change:", round(change, 2),
          "| Weak subject numbers:", weak,
          "| Category:", category)

##Output

Asha | First avg: 69.0 | Second avg: 77.67 | Change: 8.67 | Weak subject numbers: [] | Category: High
Bharat | First avg: 54.33 | Second avg: 49.67 | Change: -4.67 | Weak subject numbers: [2] | Category: Needs Support
Charan | First avg: 38.33 | Second avg: 44.33 | Change: 6.0 | Weak subject numbers: [] | Category: Needs Support