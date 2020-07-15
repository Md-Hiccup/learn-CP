""" 
Modular Arithmetic  -   
[http://theoryofprogramming.com/2014/12/24/modular-arithmetic-properties/]
[https://www.geeksforgeeks.org/modular-arithmetic/?ref=rp]


Principle:

    1.  Modular Addition

        -   (a + b) mod m = ((a mod m) + (b mod m)) mod m

        Example:
            (15 + 17) % 7
            = ((15 % 7) + (17 % 7)) % 7
            = (1 + 3) % 7
            = 4 % 7
            = 4
    
    2.  Modular Multiplication
    
        -   (a x b) mod m = ((a mod m) x (b mod m)) mod m

        Example:
            (12 x 13) % 5
            = ((12 % 5) x (13 % 5)) % 5
            = (2 x 3) % 5
            = 6 % 5
            = 1

    3.  Modular Division
        
        [ (a / b) mod m is not equal to ((a mod m) / (b mod m)) mod m. ]
    
        -   (a / b) mod m = (a x (inverse of b if exists)) mod m
    


    4.  Modulo Inverse
        -   The modular inverse of a mod m exists only if a and m are relatively prime i.e. gcd(a, m) = 1.
        Hence, for finding inverse of a under modulo m,
        if (a x b) mod m = 1 then b is modular inverse of a.
        
        Example:
            a = 5, m = 7
            (5 x 3) % 7 = 1     ,   hence, 3 is modulo inverse of 5 under 7.
    
        Fermet's Little Theorem:
            -   a^(m-1) = 1 mod m       (where, m is Prime)
            
            Divide by a
            -   a^(m-2) = 1 mod m

            -   a^(-1) = a^(m-2) mod m      ( X = a^(-1) )

    5.  Modular Exponentiation
        -   Finding a^b mod m is the modular exponentiation

        Example:
            a = 5, b = 2, m = 7
            (5 ^ 2) % 7 = 25 % 7 = 4
"""