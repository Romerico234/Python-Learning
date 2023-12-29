limit = int(input("Upper limit: "))
numbers = "1"
num = 1
total = 1

while total < limit:
    num += 1
    total += num
    numbers += f" + {num}"

print(f"The consecutive sum: {numbers} = {total}")

