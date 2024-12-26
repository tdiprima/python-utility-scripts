# This program creates a pool of worker processes which prints '1', raises an exception, and attempts to
# calculate the square of a series of numbers from 0 to 999 in a parallel manner.
from multiprocessing import Pool


def go(x1):
    print(f"Processing {x1}")
    # Simulate a task that takes a long time (commented out for simplicity)
    # task_that_takes_a_long_time()
    if x1 == 5:  # Example condition to simulate failure
        raise Exception("Can't go anywhere.")
    print(f"Finished {x1}")
    return x1 ** 2


if __name__ == "__main__":
    p = Pool()  # Create a pool of worker processes
    results = []

    # Submit tasks to the pool
    for x in range(10):  # Reduced range for simplicity
        results.append(p.apply_async(go, [x]))

    p.close()  # Close the pool to stop accepting new tasks
    p.join()  # Wait for all worker processes to finish

    # Collect results and handle exceptions
    for r in results:
        try:
            print(r.get())  # Retrieve the result
        except Exception as e:
            print(f"Error occurred: {e}")
