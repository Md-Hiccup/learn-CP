"""
Modular Exponentiation (Fast Exponentiation) -   [https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/]

Examples :

Given three numbers x, y and p, compute (x^y) % p.

Input:  x = 2, y = 3, p = 5
Output: 3
Explanation: 2^3 % 5 = 8 % 5 = 3.

Input:  x = 2, y = 5, p = 13
Output: 6
Explanation: 2^5 % 13 = 32 % 13 = 6.

"""

def mod_exp(a, n, m):
    res = 1

    # Update x if it is more than or equal to p
    # a = a % m
    
    while(n):
        if n%2:              #  ( n&1 ):
            res = (res * a) % m

        a = (a * a) % m
        n = n // 2          #   n >>= 1 
    
    return res


a = 7
n = 3
m = 5
res = mod_exp(a, n, m)

print(f'Result: {res}')
