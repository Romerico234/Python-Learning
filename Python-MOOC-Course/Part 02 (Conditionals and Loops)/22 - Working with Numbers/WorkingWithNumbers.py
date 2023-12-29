count = 0
total = 0
posNum = 0
negNum = 0

print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num = int(input("Number:"))
    if num == 0:
        break
    count += 1
    total += num
    if num >= 0:
        posNum += 1
    else:
        negNum += 1

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {total}")
print("The mean of the numbers is",(float(total/count)))
print(f"Positive numbers {posNum}")
print(f"Negative numbers {negNum}")
