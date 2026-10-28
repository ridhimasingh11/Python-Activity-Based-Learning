##Algorithm

1. Start 
2. store the number of meals prepared and served each day.
3. Check that prepared meals are greater than zero and served meals are valid.
4. Calculate leftovers by subtracting served meals from prepared meals.
5. Calculate wastage percentage using leftovers divided by prepared meals, multiplied by 100.
6. If wastage exceeds 10%, display an alert.
7. Add the daily totals to calculate overall wastage.
8. Display daily results and overall wastage.
9. Stop.

## Flowchart

#              ( START )
#                  |
#         [ Initialize totals and limit ]
#                  |
#           / Read daily meal data /
#                  |
#          < Prepared > 0 and
#          0 <= Served <= Prepared? >
#                /             \
#              Yes              No
#               |                |
#       [ Calculate leftovers ] [ Display invalid data ]
#               |                |
#       [ Calculate waste % ]    |
#               |                |
#          < Waste > 10%? >       |
#             /         \        |
#           Yes          No      |
#            |            |      |
#      [ Show alert ] [ Within limit ]
#            |            |      |
#            +------+-----+------+
#                   |
#          [ Update overall totals ]
#                   |
#             < More days? >
#                /       \
#              Yes        No
#               |          |
#         [ Process next ] [ Calculate overall waste % ]
#               |          |
#               +--> LOOP  |
#                          |
#                  / Display summary /
#                          |
#                       ( STOP )

##Python code

daily_data = [
    ("Monday", 200, 185),
    ("Tuesday", 220, 198),
    ("Wednesday", 180, 150),
    ("Thursday", 210, 205)
]

limit = 10
total_prepared = 0
total_leftover = 0

for day, prepared, served in daily_data:
    if prepared <= 0 or served < 0 or served > prepared:
        print(day, "- Invalid data")
        continue

    leftover = prepared - served
    waste_percent = leftover / prepared * 100

    total_prepared += prepared
    total_leftover += leftover

    print(day, "Prepared:", prepared,
          "Served:", served,
          "Leftover:", leftover,
          "Waste:", round(waste_percent, 2), "%")

    if waste_percent > limit:
        print(" ALERT: Wastage exceeds", limit, "%")

overall = total_leftover / total_prepared * 100

print("Total prepared:", total_prepared)
print("Total leftover:", total_leftover)
print("Overall wastage:", round(overall, 2), "%")

##Output

Monday Prepared: 200 Served: 185 Leftover: 15 Waste: 7.5 %
Tuesday Prepared: 220 Served: 198 Leftover: 22 Waste: 10.0 %
Wednesday Prepared: 180 Served: 150 Leftover: 30 Waste: 16.67 %
 ALERT: Wastage exceeds 10 %
Thursday Prepared: 210 Served: 205 Leftover: 5 Waste: 2.38 %
Total prepared: 810
Total leftover: 72
Overall wastage: 8.89 %