#!/usr/bin/python3
if __name__ == "__main__":
    from sys import a_gv, exit
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = argv[2]
        a = int(argv[1])
        b = int(argv[3])
        if operator == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            exit(0)
        elif operator == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
            exit(0)
        elif operator == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
            exit(0)
        elif operator == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
