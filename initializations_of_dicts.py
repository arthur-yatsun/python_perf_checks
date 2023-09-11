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


if __name__ == '__main__':
    empty_dict_1()
    empty_dict_2()

