from multiprocessing import Pool


def go(x):
    print(1)
    # task_that_takes_a_long_time()
    raise Exception("Can't go anywhere.")
    print(2)
    return x ** 2


p = Pool()
results = []
for x in range(1000):
    results.append(p.apply_async(go, [x]))

p.close()

for r in results:
    r.get()
