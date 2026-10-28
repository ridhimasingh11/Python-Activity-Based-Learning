##Algorithm

1. Start.
2. Read student details.
3. Check all scholarship conditions.
4. Add eligible students to a list.
5. Sort eligible students by marks from highest to lowest.
6. Display their ranks.
7. Stop.

## Flowchart

             ( START )
                |
       / Input applicant data /
                |
       [ Calculate percentage ]
                |
    < All eligibility conditions? >
          /             \
       Yes              No
        |                |
    [ Mark eligible ]  [ Not eligible ]
        |                |
        +-------+--------+
                |
   [ Rank eligible applicants ]
                |
          [ Select top 2 ]
                |
        / Display recipients /
                |
             ( STOP )

##Python code

students = [
    ("Anu", 88, [85, 82, 90], 90, 150000),
    ("Ravi", 88, [80, 75, 84], 85, 180000),
    ("Maya", 78, [80, 75, 80], 90, 100000),
    ("Kiran", 92, [95, 90, 91], 80, 300000),
]

eligible = []

for name, marks, subjects, attendance, income in students:
    if (marks >= 80 and min(subjects) >= 60
            and attendance >= 75 and income <= 200000):
        eligible.append((name, marks, attendance))

eligible.sort(key=lambda s: (-s[1], -s[2]))

print("Eligible Students:")
for rank, student in enumerate(eligible, start=1):
    print(rank, student[0], student[1])

##Output

Eligible Students:
1 Anu 88
2 Ravi 88