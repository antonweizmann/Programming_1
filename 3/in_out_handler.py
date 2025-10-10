import sys

def my_input(expected_type: int):
    out = None
    while True:
        try:
            if expected_type == 0:
                out = int(input())
            elif expected_type == 1:
                out = input()
            else:
                print("Error: no known expected type specified", file=sys.stderr)
            break
        except ValueError:
            if expected_type == 0:
                print("Error: expected input is an integer")
    return out