import random


def get_random_int(min_val, max_val):
    return random.randint(min_val, max_val)


min_val = 1
max_val = 53

for i in range(5):
    print(get_random_int(min_val, max_val))
