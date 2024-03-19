#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""

    tsk = [wait_random(max_delay) for _ in range(n)]

    delay = asyncio.as_completed(tsk)
    # delays.append(await asyncio.gather(i) for i in tsk)
    delay = [await result for result in delay]
    return delay
