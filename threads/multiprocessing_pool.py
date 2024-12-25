# Uses multiprocessing to calculate the square of each number in a list and then prints out the results.
# https://docs.python.org/2/library/multiprocessing.html
from multiprocessing import Pool


def f(n):
    return n * n


if __name__ == "__main__":
    p = Pool(processes=3)
    result = p.map(f, [1, 2, 3, 4, 5])
    for pp in result:
        print(pp)
