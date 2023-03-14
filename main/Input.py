import sys


def mul(a, b):
    x = a*b
    return x

a = int(sys.argv[1])
b = int(sys.argv[2])
# c = sys.argv[3]

print(f'Multiply to {a} and {b} = {mul(a, b)}')
# print("!! Hello", c, "!!")