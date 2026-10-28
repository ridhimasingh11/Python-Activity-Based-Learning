##Algorithm

1. Start 
2. Read monthly unit consumption.
3. Check which electricity slab applies.
4. Calculate the energy charge.
5. Add ₹50 as the fixed charge.
6. Apply a 5% rebate if consumption is at most 100 units.
7. Compare the bill with the previous month.
8. If the increase exceeds 30%, display an alert.
9. Display each bill and stop.

##Flowchart

#              ( START )
#                  |
#          / Read monthly units /
#                  |
#          < Units <= 100? >
#             /         \
#           Yes          No
#            |            |
#    [ Charge at Rs.2 ]   < Units <= 200? >
#                         /          \
#                       Yes           No
#                        |             |
#               [ Calculate slab ] [ Calculate slab ]
#                        |             |
#                        +------+------+
#                               |
#                    [ Add fixed charge ]
#                               |
#                      < Units <= 100? >
#                         /        \
#                       Yes         No
#                        |           |
#                 [ Apply rebate ] [ No rebate ]
#                        |           |
#                        +-----+-----+
#                              |
#                    < First month? >
#                       /         \
#                     Yes          No
#                      |            |
#                [ Skip check ] [ Compare bills ]
#                                   |
#                         < Increase > 30%? >
#                            /          \
#                          Yes           No
#                           |             |
#                    [ Flag increase ] [ No alert ]
#                           |             |
#                           +------+------+
#                                  |
#                          / Display bill /
#                                  |
#                               ( STOP )

##Python code

monthly_units = [80, 120, 250]
previous_bill = None

for month, units in enumerate(monthly_units, start=1):
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5

    bill = energy + 50
    rebate = 0

    if units <= 100:
        rebate = bill * 0.05
        bill = bill - rebate

    print("Month", month, "| Units:", units,
          "| Energy charge:", energy,
          "| Rebate:", round(rebate, 2),
          "| Bill:", round(bill, 2))

    if previous_bill is not None:
        increase = (bill - previous_bill) / previous_bill * 100
        if increase > 30:
            print(" Unusual increase:", round(increase, 2), "%")

    previous_bill = bill

##Output

Month 1 | Units: 80 | Energy charge: 160 | Rebate: 10.5 | Bill: 199.5
Month 2 | Units: 120 | Energy charge: 260 | Rebate: 0 | Bill: 310
Unusual increase: 55.39 %
Month 3 | Units: 250 | Energy charge: 650 | Rebate: 0 | Bill: 700
Unusual increase: 125.81 %