import time
from functools import wraps
from timeit import timeit


def measure_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()
        print(f"{func.__name__} - {end - start}")

        return result
    return wrapper


def measure_time_with_iterations(iterations: int = 10_000):

    def measure_time(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = timeit(lambda: func(*args, **kwargs), number=iterations)
            print(f"{func.__name__} - {result}")
        return wrapper

    return measure_time
