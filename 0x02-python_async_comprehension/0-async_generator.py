#!/usr/bin/env python3
""" A coroutine that takes no args and loop 10 times
, waiting 1 sec then yield random between 0 and 10"""


import asyncio
import random


async def async_generator():
    """ async gen function """
    for _ in range(10):
        y = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield y
