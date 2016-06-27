# https://xkcd.com/710/
from random import randint
initial_value = randint(1, 1000)

# The Collatz Conjecture states that if you pick a number and do the following:
# -If even, divide by 2.
# -If odd, multiply by 3 and add 1
# And then repeat this iteratively, eventually it will reach 1

# Write a program to show that the collatz conjecture is true
# for the random integer initial_value