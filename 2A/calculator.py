def mysum(num1, num2):
    result = int(num1) + int(num2)
    return result
def mysubtract(num1, num2):
    result = int(num1) - int(num2)
    return result
def mymultiply(num1, num2):
    result = int(num1) * int(num2)
    return result
def mydivide(num1, num2):
    result = int(num1) / int(num2)
    return result

def calculator():
    opperation = input("Choose the operation:\n- sum [b]\n- subtraction [2]\n- multiplication [3]\n- division [4]\n")
    num1 = int(input("What's the first number\n"))
    num2 = int(input("What's the second number\n"))
    match opperation:
        case 1:
            mysum(num1, num2)
        case 2:
            mysubtract(num1, num2)
        case 3:
            mymultiply(num1, num2)
        case 4:
            mydivide(num1, num2)