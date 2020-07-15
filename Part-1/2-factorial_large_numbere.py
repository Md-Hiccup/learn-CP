"""
Factorial of Large number   -   [https://www.geeksforgeeks.org/factorial-large-number/]

Example:
Input
    3
    5
    10
    2

Output
    120
    3628800
    2
"""

#code
import sys

def factorial(n):
    res = [None]*500

    # Initialize
    res[0] = 1
    res_size = 1

    # Factorial of
    # n! = 1 * 2 * 3 * 4 * ... * (n)
    for i in range(2, n+1):
        res_size = multiply(i, res, res_size)

    print("Factorial of give number is : ", end="")

    i = res_size - 1
    while i>=0:
        print(res[i], end='')
        i -= 1
    # while i >= 0:
        # sys.stdout.write(str(res[i]))
        # sys.stdout.flush()
        # i -= 1
    print()


def multiply(x, res, res_size):
    # Initialize carry
    carry = 0

    # One by one multiply n with individual digits of res[]
    i = 0
    for i in range(res_size):
        prod = res[i] * x + carry
        # Store last digit of prod in res[]
        res[i] = prod % 10
        # Put rest in carry
        carry = prod // 10

    # Put carry in res and increase the res_size
    if carry:
        res[res_size] = carry % 10
        # Make sure float division is used to avoid floating value
        carry = carry // 10
        res_size = res_size + 1

    return res_size

t = int(input())
for _ in range(t):
    factorial(int(input()))
