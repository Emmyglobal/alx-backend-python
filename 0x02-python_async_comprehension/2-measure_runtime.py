#!/usr/bin/env python3
""" Run time for parallel comprehensions """


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """ Measuring run time of async comp """
    start = time.time()
    comp = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*comp)
    end = time.time()
    total = end - start
    return total
