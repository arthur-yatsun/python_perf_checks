from utils import measure_time_with_iterations


test_dict = {i: i+1 for i in range(10_000)}


@measure_time_with_iterations(100_000)
def test_1():
    for key in test_dict:
        pass


@measure_time_with_iterations(100_000)
def test_2():
    for key in test_dict.keys():
        pass


if __name__ == '__main__':
    test_1()
    test_2()

