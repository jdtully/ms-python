from taxes import taxes
price = input("How Much is the item?  ")

try:
    price = float(price)
except ValueError:
    print("I figured out how to trap for that :P")
else:
    if price < 1.00:
        final_price = price
    else:
        county = input("What county are you in?  ")
        county = county.lower()
        try:
            tax = taxes[county]
        except KeyError:
            print("Thats not a county in my State")

        final_price = price + (price * tax)
    you_pay = '${:.2f}'.format(final_price)
    print(you_pay)
