from utils.primes import compute_primes
from random import randint

MAX_VAL = 10000
product = randint(2, MAX_VAL)
primes = compute_primes(MAX_VAL)
prime_divisors = []
print('The prime divisors of %d are:' % product)
# You now have a list of all prime numbers below 10,000. It is called "primes"
# Find all of the prime divisors of "product", and add them to the list prime_divisors.
# Finally, output the equation that uses these prime divisors and equals "product"