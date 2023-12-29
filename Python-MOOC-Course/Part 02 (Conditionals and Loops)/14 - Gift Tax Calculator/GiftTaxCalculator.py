gift_value = int(input("Value of gift: "))

if gift_value >= 1000000:
    tax = 142100 + (gift_value - 1000000) * 0.17
elif gift_value >= 200000:
    tax = 22100 + (gift_value - 200000) * 0.15
elif gift_value >= 55000:
    tax = 4700 + (gift_value - 55000) * 0.12
elif gift_value >= 25000:
    tax = 1700 + (gift_value - 25000) * 0.10
elif gift_value >= 5000:
    tax = 100 + (gift_value - 5000) * 0.08
else:
    tax = 0

if tax != 0:
    print(f"Amount of tax: {tax} euros")
else:
    print("No tax!")
