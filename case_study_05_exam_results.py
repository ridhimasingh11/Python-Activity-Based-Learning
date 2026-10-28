##Algorithm

1. Start 
2. Reads marks in four subjects.
3. Make a copy of the original marks.
4. Identify subjects with marks below 40.
5. If exactly one subject has marks between 35 and 39, calculate the grace marks required.
6. Apply grace marks only if the required amount is at most 5.
7. Check whether all final marks are at least 40.
8. Display original marks, final marks, grace marks used, and result.
9. Stop.

##Flowchart

#              ( START )
#                  |
#             / Input marks /
#                  |
#          [ Find failed subjects ]
#                  |
#          < Exactly one failed subject? >
#                /            \
#              Yes             No
#               |               |
#       < Marks between 35-39? > |
#           /           \        |
#         Yes            No      |
#          |              |      |
#    [ Calculate grace ]  |      |
#          |              |      |
#     < Grace <= 5? >     |      |
#       /         \       |      |
#     Yes          No     |      |
#      |            |     |      |
# [ Add grace ] [ No grace ]     |
#      |            |            |
#      +------------+------------+
#                   |
#           < All marks >= 40? >
#                /         \
#              Yes          No
#               |            |
#          [ Result PASS ] [ Result FAIL ]
#               |            |
#               +------+-----+
#                      |
#             / Display final marks /
#                      |
#                   ( STOP )

##Python code

marks = [78, 36, 65, 82]
original = marks.copy()

failed = []

for i in range(len(marks)):
    if marks[i] < 40:
        failed.append(i)

grace_used = 0

if len(failed) == 1:
    i = failed[0]
    needed = 40 - marks[i]

    if 35 <= marks[i] <= 39 and needed <= 5:
        marks[i] = marks[i] + needed
        grace_used = needed

passed = True

for mark in marks:
    if mark < 40:
        passed = False

print("Original marks:", original)
print("Final marks:", marks)
print("Grace marks used:", grace_used)

if passed:
    print("Result: PASS")
else:
    print("Result: FAIL")

##Output

Original marks: [78, 36, 65, 82]
Final marks: [78, 40, 65, 82]
Grace marks used: 4
Result: PASS