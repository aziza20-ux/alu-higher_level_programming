#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import sub, div, add, mul
    from sys import argv
    length = len(argv) - 1
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ops = argv[2]
    if not (ops == '+' or ops == '-' or ops == '*' or ops == '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if (ops == '+'):
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif (ops == '-'):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif (ops == '*'):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
