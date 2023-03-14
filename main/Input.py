# import sys


# def mul(a, b):
#     x = a*b
#     return x

# a = int(sys.argv[1])
# b = int(sys.argv[2])
# # c = sys.argv[3]

# print(f'Multiply to {a} and {b} = {mul(a, b)}')
# # print("!! Hello", c, "!!")

import sys
print("Inputs:")
one = sys.stdin.readline()
two = sys.stdin.readline()
print("Output:")
three = int(one) + int(two)
four = str(three)
sys.stdout.write(four)