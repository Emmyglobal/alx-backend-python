#!/usr/bin/env python3
"""A new function that is identical to wait_n"""


from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times"""

    tsk = [task_wait_random(max_delay) for _ in range(n)]

    delay = asyncio.as_completed(tsk)
    # delays.append(await asyncio.gather(i) for i in tsk)
    delay = [await result for result in delay]
    return delay
