def mysum(num1, num2):
    result = num1 + num2
    print("The result is:\n" + str(result))
def mysubtract(num1, num2):
    result = num1 - num2
    print("The result is:\n" + str(result))
def mymultiply(num1, num2):
    result = num1 * num2
    print("The result is:\n" + str(result))
def mydivide(num1, num2):
    result = num1 / num2
    print("The result is:\n" + str(result))

def myinput(msg):
    while True:
        try:
            out = int(input(msg))
            break
        except ValueError:
            print("Invalid Input!")
    return out

def calculator():
    operation = int(myinput("Choose the operation:\n- sum [1]\n- subtraction [2]\n- multiplication [3]\n- division [4]\n"))
    num1 = int(myinput("What's the first number\n"))
    num2 = int(myinput("What's the second number\n"))
    match operation:
        case 1:
            mysum(num1, num2)
        case 2:
            mysubtract(num1, num2)
        case 3:
            mymultiply(num1, num2)
        case 4:
            if num2 == 0:
                print("Division by zero is not possible!")
            else:
                mydivide(num1, num2)
        case _:
            print("Unknown operation")

calculator()
