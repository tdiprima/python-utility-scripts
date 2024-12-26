# Generates a random lowercase string of length 63 consisting of upper case letters and digits.
# https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
import random
import string


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# result = id_generator()
result = id_generator(63)
# result = id_generator(3, "6793YUIO")
print(result.lower())

# https://www.w3schools.com/python/python_for_loops.asp
# for x1 in range(12):
#     print('touch', id_generator() + '.css')
