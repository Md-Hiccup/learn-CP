""" 
Binary Exponentiation   -   [https://cp-algorithms.com/algebra/binary-exp.html]

Binary exponentiation (also known as exponentiation by squaring) is a trick which allows to calculate an using only O(logn) multiplications (instead of O(n) multiplications required by the naive approach).

Example:
    3^1 = 3
    3^2 = (3^1)2 = 3^2 = 9
    3^4 = (3^2)2 = 9^2 = 81
    3^8 = (3^4)2 = 81^2 = 6561
"""


def bin_exp(a, n):
    res = 1
    while(n):
        if (n%2):           #  ( n&1 ):
            res = res * a 
        
        a = a * a
        n = n // 2          #   n >>= 1 
    
    return res


a = 2
n = 5
res = bin_exp(a, n)

print(f'Value: {res}')

