# Generates a sequence of numbers from 0 to 19, then randomly selects and prints 5 numbers from the sequence.
# choose a random element from a list
from random import choice
from random import seed

# seed random number generator
seed(1)

# prepare a sequence
sequence = [i for i in range(20)]
print(sequence)

# make choices from the sequence
for _ in range(5):
    selection = choice(sequence)
    print(selection)
