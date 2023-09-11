from utils import measure_time_with_iterations, measure_time


class WithoutSlots:
    def __init__(self, a, b, c, d, e, f, g, h):
        self.a, self.b = a, b
        self.c, self.d = c, d
        self.e, self.f = e, f
        self.g, self.h = g, h


class SlotsPerf(WithoutSlots):
    __slots__ = "a", "b", "c", "d", "e", "f", "g", "h"


@measure_time_with_iterations(10_000)
def test1():

    data_classes = []
    for i in range(10_000):
        data_classes.append(SlotsPerf(1, 2, 3, 4, 5, 6, 7, 8))

    for i in data_classes:
        var = i.a, i.b


@measure_time_with_iterations(10_000)
def test2():
    data_classes = []
    for i in range(10_000):
        data_classes.append(WithoutSlots(1, 2, 3, 4, 5, 6, 7, 8))

    for i in data_classes:
        var = i.a, i.b


@measure_time_with_iterations(100)
@measure_time
def test3():
    for i in range(30):
        SlotsPerf(1, 2, 3, 4, 5, 6, 7, 8)


@measure_time_with_iterations(100)
@measure_time
def test4():
    for i in range(30):
        WithoutSlots(1, 2, 3, 4, 5, 6, 7, 8)


if __name__ == '__main__':
    # test1()
    # test2()

    test3()
    test4()
