##Algorithm

1. Start
2. Read product details.
3. Calculate the total for each product using price × quantity.
4. Add the product totals to get the subtotal.
5. If the subtotal is at least ₹2,000, apply a 10% discount capped at ₹300.
6. Distribute the discount proportionally across products.
7. Apply 5% tax to food and 12% tax to other products.
8. Add discounted prices and taxes to calculate the final bill.
9. Display the invoice
10.Stop

## Flowchart

#              ( START )
#                  |
#            / Input products /
#                  |
#            [ Calculate line totals ]
#                  |
#            [ Calculate subtotal ]
#                  |
#            < Subtotal >= Rs.2000? >
#                 /           \
#               Yes            No
#                |              |
#        [ Calculate 10% ] [ Discount = 0 ]
#        [ discount, max 300 ] |
#                |              |
#                +-------+------+
#                        |
#             [ Allocate discount per item ]
#                        |
#              [ Calculate discounted price ]
#                        |
#                 < Category = food? >
#                    /          \
#                  Yes           No
#                   |             |
#             [ Apply 5% tax ] [ Apply 12% tax ]
#                   |             |
#                   +------+------+
#                          |
#                 [ Calculate grand total ]
#                          |
#                  / Display invoice /
#                          |
#                       ( STOP )

##Python code

products = [
    ("Bread", "food", 50, 4),
    ("Headphones", "other", 1200, 2),
    ("Juice", "food", 100, 3)
]

lines = []
subtotal = 0

for name, category, price, quantity in products:
    line_total = price * quantity
    lines.append((name, category, line_total))
    subtotal += line_total

if subtotal >= 2000:
    discount = min(subtotal * 0.10, 300)
else:
    discount = 0

grand_total = 0

print("ITEM | LINE | DISCOUNTED | TAX")

for name, category, line_total in lines:
    share = discount * line_total / subtotal
    discounted = line_total - share

    if category == "food":
        tax_rate = 0.05
    else:
        tax_rate = 0.12

    tax = discounted * tax_rate
    grand_total += discounted + tax

    print(name, "|", round(line_total, 2), "|",
          round(discounted, 2), "|", round(tax, 2))

print("Subtotal:", round(subtotal, 2))
print("Discount:", round(discount, 2))
print("Grand total:", round(grand_total, 2))

##Output

ITEM | LINE | DISCOUNTED | TAX
Bread | 200 | 180.0 | 9.0
Headphones | 2400 | 2160.0 | 259.2
Juice | 300 | 270.0 | 13.5
Subtotal: 2900
Discount: 290.0
Grand total: 2891.7