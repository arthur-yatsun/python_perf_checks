import random
import string
import time
import timeit

from utils import measure_time_with_iterations


@measure_time_with_iterations()
def empty_dict_1():
    a = dict()


@measure_time_with_iterations()
def empty_dict_2():
    b = {}


@measure_time_with_iterations(iterations=1_000_000)
def dict_1():
    a = dict(a=1, b=2, c=3)


@measure_time_with_iterations(iterations=1_000_000)
def dict_2():
    b = {"a": 1, "b": 2, "c": 3}


if __name__ == '__main__':
    empty_dict_1()
    empty_dict_2()

    dict_1()
    dict_2()
