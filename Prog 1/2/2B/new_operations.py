num1 = int(input("What's the first number\n"))
num2 = int(input("What's the second number\n"))
power = 0
if num1 < num2:
    temp = num1
    num1 = num2
    num2 = temp

floor = str(num1 // num2)
mod = str(num1 % num2)

print(str(num1) + "//" + str(num2) + " is:\n" + floor)
print(str(num1) + "%" + str(num2) + " is:\n" + mod)
if num2 < 5:
    power = str(num1 ** num2)
    print(str(num1) + "**" + str(num2) + " is:\n" + power)

