#!/usr/bin/env python3
""" A Function that takes an int max_delay and returns a asyncio.Task
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """create Task"""
    tsk = asyncio.create_task(wait_random(max_delay))
    return tsk
