import asyncio
import cProfile
import pstats

import requests
import httpx

from io_bound_threading import start


def test_func():
    for i in range(10):
        requests.get("https://example.com")


async def async_test_func():
    async with httpx.AsyncClient() as client:
        tasks = (client.get("https://example.com") for i in range(10))
        responses = await asyncio.gather(*tasks)
        print(responses)
            # response = await client.get("https://example.com")
            # print(response)


def main():
    # with cProfile.Profile() as profiler:
    #     test_func()
    #
    # stats = pstats.Stats(profiler)
    # stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    #
    # stats.dump_stats("stats.prof")

    with cProfile.Profile() as profiler:
        asyncio.run(async_test_func())

    stats = pstats.Stats(profiler)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

    stats.dump_stats("stats.prof")


if __name__ == '__main__':
    main()
    # snakeviz <filename>
