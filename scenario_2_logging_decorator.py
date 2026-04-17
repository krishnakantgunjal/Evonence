import time

def log_execution_time(func):
    def wrapper(n):
        start = time.time()
        result = func(n)
        end = time.time()
        print("Execution time:", end - start)
        return result
    return wrapper

@log_execution_time
def calculate_sum(n):
    return sum(range(1, n + 1))

print(calculate_sum(1000000))
