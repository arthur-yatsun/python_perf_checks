import time
from concurrent.futures import ThreadPoolExecutor

import requests


def send_request(request_id: int):
    start = time.perf_counter()
    response = requests.get("http://example.com")
    end = time.perf_counter()

    print(request_id, end - start, response)


def start(workers: int, requests_number = 10):
    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=workers) as executor:
        print("Executor id:", id(executor))
        for i in range(1, requests_number + 1):
            executor.submit(send_request, i)

    end = time.perf_counter()
    print(f"\nTotal execution time {end - start}")


if __name__ == '__main__':
    print("10 workers, 10 iterations")
    print("-" * 15)
    start(10)

    print("7 workers, 10 iterations")
    print("-" * 15)
    start(7)

    print("5 workers, 10 iterations")
    print("-" * 15)
    start(5)

    time.sleep(3)

    print("10 workers, 100 iterations")
    print("-" * 15)
    start(10, 100)


