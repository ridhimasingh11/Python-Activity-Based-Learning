##Algorithm

1. Start
2. Read the transactions.
3. Read each transaction type and amount.
4. Reject transactions with an amount less than or equal to zero.
5. For deposits, add the amount to the balance.
6. For withdrawals, check that the amount does not exceed ₹2,000 or the available balance.
7. Update the balance and count accepted or rejected transactions.
8. Display the final balance and transaction summary.
9. Stop.

##Flowchart

#              ( START )
#                  |
#         [ Set opening balance = 5000 ]
#                  |
#          / Read transaction list /
#                  |
#           [ Process transaction ]
#                  |
#           < Amount > 0? >
#              /         \
#            No           Yes
#             |            |
#       [ Reject ]   < Deposit or withdrawal? >
#                        /              \
#                    Deposit          Withdrawal
#                       |                 |
#                [ Add to balance ] < Amount <= 2000
#                                     and balance? >
#                                      /       \
#                                    Yes        No
#                                     |          |
#                              [ Subtract ] [ Reject ]
#                                     |          |
#                                     +-----+----+
#                                           |
#                                  < More transactions? >
#                                      /          \
#                                    Yes           No
#                                     |             |
#                              [ Process next ] [ Display summary ]
#                                     |             |
#                                     +--> ( LOOP ) |
#                                                   |
#                                                ( STOP )

##Python code

balance = 5000

transactions = [
    ("DEPOSIT", 1000),
    ("WITHDRAWAL", 1200),
    ("WITHDRAWAL", 2500),
    ("DEPOSIT", -100),
    ("WITHDRAWAL", 700)
]

accepted = 0
rejected = 0

for kind, amount in transactions:
    if amount <= 0:
        print("Rejected:", kind, amount, "- invalid amount")
        rejected += 1

    elif kind == "DEPOSIT":
        balance += amount
        print("Accepted deposit:", amount, "Balance:", balance)
        accepted += 1

    elif kind == "WITHDRAWAL":
        if amount > 2000 or amount > balance:
            print("Rejected withdrawal:", amount)
            rejected += 1
        else:
            balance -= amount
            print("Accepted withdrawal:", amount, "Balance:", balance)
            accepted += 1

    else:
        print("Rejected: unknown transaction type")
        rejected += 1

print("Final balance:", balance)
print("Accepted transactions:", accepted)
print("Rejected transactions:", rejected)

##Output

Accepted deposit: 1000 Balance: 6000
Accepted withdrawal: 1200 Balance: 4800
Rejected withdrawal: 2500
Rejected: DEPOSIT -100 - invalid amount
Accepted withdrawal: 700 Balance: 4100
Final balance: 4100
Accepted transactions: 3
Rejected transactions: 2