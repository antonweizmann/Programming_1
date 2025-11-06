def mysum(num1, num2):
    result = num1 + num2
    print("The result is: " + str(result))
def mysubtract(num1, num2):
    result = num1 - num2
    print("The result is: " + str(result))
def mymultiply(num1, num2):
    result = num1 * num2
    print("The result is: " + str(result))
def mydivide(num1, num2):
    result = num1 / num2
    print("The result is: " + str(result))

def myinput(msg):
    while True:
        try:
            out = int(input(msg))
            break
        except ValueError:
            print("Invalid Input!")
    return out

def calculator():
    operation = input("Choose one operation [sum, subtraction, multiplication, division]:\n")
    num1 = int(myinput("Type the first number\n"))
    num2 = int(myinput("Type the second number\n"))
    match operation:
        case "sum":
            mysum(num1, num2)
        case "subtraction":
            mysubtract(num1, num2)
        case "multiplication":
            mymultiply(num1, num2)
        case "division":
            if num2 == 0:
                print("Division by zero is not possible!")
            else:
                mydivide(num1, num2)
        case _:
            print("Unknown operation")


calculator()