# maxN = 100000     ## For Basic of Sieve
maxN = 90000000

isPrime = [1]*(maxN + 1)
primeList = []

def sieve():
    isPrime[0] = isPrime[1] = 0

    i = 2
    while (i * i < maxN):
        if isPrime[i]:
            j = i*i
            while (j <= maxN):
                print(j, i)
                isPrime[j] = 0
                j += i
        i += 1

def kthPrime():
    # isPrime = [1] * (maxN + 1)
    isPrime[0] = isPrime[1] = False

    i = 2
    while (i * i <= maxN):
        if isPrime[i]:
            j = i * i
            while (j <= maxN):
                isPrime[j] = False
                j += i
        i += 1

    k=2
    while (k <= maxN):
        if isPrime[k]:
            primeList.append(k)
        k += 1

    return primeList


if __name__ == "__main__":
    # ### Basic of Sieve of Eratosthenes
    # sieve()
    # print(isPrime[0:100])
    t = int(input())

    for _ in range(t):
        # ### Find Kth of Prime - [https://www.spoj.com/problems/TDKPRIME/]
        pl= kthPrime()
        n = int(input())
        print(primeList[n-1])

