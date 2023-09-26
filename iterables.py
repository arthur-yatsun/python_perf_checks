import random
from collections import deque


from utils import measure_time


def gen_iter(iterations: int = 10):
    print(f"gen_list {iterations}", end=" ")
    for i in range(iterations):
        a = i * random.randrange(0, 100)
        yield a


def list_iter(iterations: int = 10):
    print(f"list_iter {iterations}", end=" ")

    result = []
    for i in range(iterations):
        a = i * random.randrange(0, 100)
        result.append(a)

    return result


def deque_iter(iterations):
    print(f"deque_iter {iterations}", end=" ")

    result = deque()
    for i in range(iterations):
        a = i * random.randrange(0, 100)
        result.append(a)

    return result


def set_iter(iterations):
    print(f"set_iter {iterations}", end=" ")

    result = set()
    for i in range(iterations):
        a = i * random.randrange(0, 10000000)
        result.add(a)

    return result


@measure_time
def measure_get(iterations, func):
    for i in func(iterations):
        i += 1


@measure_time
def measure_pop(iterations, func):
    iterable = func(iterations)
    for i in range(len(iterable) // 2):
        iterable.pop()
        iterable.append(1)


@measure_time
def measure_in(iterations, func):
    iterable = func(iterations)
    for i in range(1000):
        a = i in iterable


@measure_time
def measure_in_all_sets(iterations, func):
    """LETS GOOOOOO"""

    iterable = func(iterations)
    iterable = set(iterable)
    for i in range(1000):
        a = i in iterable


if __name__ == '__main__':

    iterations = 10
    for i in range(1, 6):
        iterations *= 10

        # measure_get(iterations, gen_iter)
        # measure_get(iterations, list_iter)
        # measure_get(iterations, deque_iter)

        # measure_pop(iterations, list_iter)
        # measure_pop(iterations, deque_iter)

        measure_in(iterations, list_iter)
        # measure_in(iterations, deque_iter)
        # measure_in(iterations, set_iter)

        measure_in_all_sets(iterations, list_iter)
        # measure_in_all_sets(iterations, deque_iter)
        # measure_in_all_sets(iterations, set_iter)

        print()

