##Algorithm
1. Start.
2. Declare basic pay, overtime, and incentive.
3. Calculate HRA as 20% of basic pay.
4. Calculate other allowance as 10% of basic pay.
5. Add all amounts to calculate gross salary.
6. Calculate deductions using the given salary bands.
7. Subtract deductions from gross salary.
8. Display the salary statement
9. Stop

## Flowchart

#              ( START )
#                  |
#        / Input basic pay, OT, incentive /
#                  |
#          [ Calculate HRA ]
#                  |
#       [ Calculate other allowance ]
#                  |
#          [ Calculate gross salary ]
#                  |
#          < Gross <= Rs.20000? >
#              /          \
#            Yes           No
#             |             |
#    [ Deduction = 0 ]  < Gross <= Rs.40000? >
#                         /           \
#                       Yes            No
#                        |              |
#                [ Deduct 5% ] [ Deduct 5% and 10% ]
#                        |              |
#                        +-------+------+
#                                |
#                      [ Calculate net salary ]
#                                |
#                      / Display salary statement /
#                                |
#                             ( STOP )

##Python code

basic = 30000
overtime = 2500
incentive = 1500

hra = basic * 0.20
other_allowance = basic * 0.10

gross = basic + hra + other_allowance + overtime + incentive

if gross <= 20000:
    deduction = 0
elif gross <= 40000:
    deduction = (gross - 20000) * 0.05
else:
    deduction = 20000 * 0.05 + (gross - 40000) * 0.10

net_salary = gross - deduction

print("SALARY STATEMENT")
print("Basic pay: Rs.", basic)
print("HRA: Rs.", hra)
print("Other allowance: Rs.", other_allowance)
print("Overtime: Rs.", overtime)
print("Incentive: Rs.", incentive)
print("Gross salary: Rs.", gross)
print("Deduction: Rs.", round(deduction, 2))
print("Net salary: Rs.", round(net_salary, 2))

##Output

SALARY STATEMENT
Basic pay: Rs. 30000
HRA: Rs. 6000.0
Other allowance: Rs. 3000.0
Overtime: Rs. 2500
Incentive: Rs. 1500
Gross salary: Rs. 43000.0
Deduction: Rs. 1300.0
Net salary: Rs. 41700.0