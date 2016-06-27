import math

def compute_primes(max):
    primes = [2]
    for p in range(3, max, 2):
        is_prime = True
        for divisor in primes:
            if divisor > math.sqrt(p):
                break
            if p % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(p)