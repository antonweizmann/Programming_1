def is_even(n):
    if n % 2 == 0:
        return True
    else :
        return False

def find_max(to_search):
    highest = to_search[0]
    for n in to_search:
        if highest < n:
            highest = n
    return highest

def calculator(num1, num2, operation):
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
    return 0