import sys

def n_prime_nums(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

n = sys.argv[1]
try :
    n = int(n)
    if n < 1:
        print("Please enter a number greater than 0.")
    else:
        print(n_prime_nums(n))
except ValueError:
    print("Please enter a valid number.")